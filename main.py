import os 
import json
from datetime import datetime
from openai import OpenAI
import chainlit as cl 
from dotenv import load_dotenv
from tools import ProductInfoTool, StockTool, AppointmentTool  

load_dotenv()

OPENAI_KEY = os.getenv('OPENAI_KEY')     

client = OpenAI(api_key=OPENAI_KEY)

# Tool rinominati coerentemente con il brand
product_tool = ProductInfoTool()
stock_tool = StockTool()
appointment_tool = AppointmentTool()

TOOLS = [
            {
                "type": "function",
                "function": {
                    "name": "get_product_info",
                    "description": "Ottiene dettagli su un capo d'abbigliamento ecologico (materiali, certificazioni, sostenibilità)",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "product_name": {
                                "type": "string",
                                "description": "Nome del capo o categoria (es. maglione lana bio, jeans riciclati)"
                            }
                        },
                        "required": ["product_name"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "check_availability",
                    "description": "Verifica la disponibilità di taglie o colori per un capo in negozio",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "product_name": {
                                "type": "string",
                                "description": "Nome del capo"
                            },
                            "size": {
                                "type": "string",
                                "description": "Taglia desiderata"
                            }
                        }
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "book_fitting",
                    "description": "Prenota una sessione di prova in negozio o consulenza di stile sostenibile",
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

    if tool_call.function.name == "get_product_info":
        result = product_tool.get_info(**function_args)
    elif tool_call.function.name == "check_availability":
        result = stock_tool.check_stock(**function_args)
    elif tool_call.function.name == "book_fitting":
        result = appointment_tool.book_appointment(**function_args)

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
            "content": f"Sei l'assistente virtuale di VerdeModa Italia, un brand di abbigliamento eco-sostenibile per uomo, donna e bambino. "
                       f"Il tuo obiettivo è guidare i clienti verso scelte consapevoli. "
                       f"Ricordati che siamo nel 2026, oggi è il {today}."
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
            messages.append(response_message)
            break    
        
        if tool_calls:
            messages.append(response_message) 
            for tool_call in tool_calls:
                function_response = handle_tool_call(tool_call)
                messages.append({
                        "tool_call_id": tool_call.id,
                        "role": "tool",
                        "name": tool_call.function.name,
                        "content": function_response,
                    }) 

    cl.user_session.set("messages", messages)
    
    await cl.Message(
        author = "VerdeModa Assistant",
        content = messages[-1].content
    ).send()