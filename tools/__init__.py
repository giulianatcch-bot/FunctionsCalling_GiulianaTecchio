import os 
import json
from datetime import datetime
from openai import OpenAI
import chainlit as cl 
from dotenv import load_dotenv
from tools import CourseInfoTool, ScheduleTool, BookingTool  

load_dotenv()

OPENAI_KEY = os.getenv('OPENAI_KEY')     

client = OpenAI(api_key=OPENAI_KEY)

course_tool = CourseInfoTool()
schedule_tool = ScheduleTool()
booking_tool = BookingTool()

TOOLS = [
            {
                "type": "function",
                "function": {
                    "name": "get_course_info",
                    "description": "Ottiene informazioni su un corso specifico",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "course_name": {
                                "type": "string",
                                "description": "Nome del corso"
                            }
                        },
                        "required": ["course_name"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "get_upcoming_classes",
                    "description": "Ottiene le date delle prossime classi in partenza",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "course_name": {
                                "type": "string",
                                "description": "Nome del corso (opzionale)"
                            },
                            "start_date": {
                                "type": "string",
                                "description": "Data di inizio (formato YYYY-MM-DD)"
                            }
                        }
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "book_consultation",
                    "description": "Prenota una video chiamata con un docente",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "date": {
                                "type": "string",
                                "description": "Data desiderata (formato YYYY-MM-DD)"
                            },
                            "time": {
                                "type": "string",
                                "description": "Orario desiderato (formato HH:MM)"
                            },
                            "teacher_id": {
                                "type": "string",
                                "description": "ID del docente (opzionale)"
                            }
                        },
                        "required": ["date", "time"]
                    }
                }
            }
        ]

def handle_tool_call(tool_call) -> str:
    result = None

    function_args = json.loads(tool_call.function.arguments)

    print("*" * 80)
    print("function name: ", tool_call.function.name)
    print("function args: ", function_args)
    print("*" * 80)


    if tool_call.function.name == "get_course_info":
        result = course_tool.get_info(**function_args)
    elif tool_call.function.name == "get_upcoming_classes":
        result = schedule_tool.get_classes(**function_args)
    elif tool_call.function.name == "book_consultation":
        result = booking_tool.book_consultation(**function_args)


    print("result: ", result)
    print("*" * 80)


    return result

def llm(messages):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=TOOLS,
        tool_choice="auto",  
    )
    return completion


@cl.on_chat_start
def on_chat_start():
    today = datetime.today().strftime("%Y-%m-%d")
    cl.user_session.set("messages", [ 
        {
            "role": "developer", 
            "content": f"Sei un assistente specializzato in corsi di cucina. Ricordati che siamo nel 2025, oggi e' il {today}"
        }
    ])
    

@cl.on_message
async def main(message: cl.Message):
   
  
    user_message = message.content

    messages = cl.user_session.get("messages")

    messages.append( {"role": "user", "content": user_message} )

    while True:
       
        completion = llm(messages)

        response_message = completion.choices[0].message
        tool_calls = response_message.tool_calls

        if response_message.refusal:
            break
        
        if response_message.content: 
           
            messages.append( response_message  )
            break    
        
     
        if tool_calls:
          
            messages.append(response_message) 
        
           
            for tool_call in tool_calls:
               
                function_response = handle_tool_call(tool_call)
        
                messages.append(
                    {
                        "tool_call_id": tool_call.id,
                        "role": "tool",
                        "name": tool_call.function.name,
                        "content": function_response,
                    }
                )  

    
    cl.user_session.set("messages", messages)
    
    
    await cl.Message(
        author = "assistant",
        content = messages[-1].content
    ).send()