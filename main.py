import os
import json
from datetime import datetime
from openai import OpenAI
import chainlit as cl
from dotenv import load_dotenv
from tools import ProductInfoTool, StockTool, AppointmentTool

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_KEY'))


product_tool = ProductInfoTool()
stock_tool = StockTool()
appointment_tool = AppointmentTool()


TOOLS = [
    {"type": "function", "function": {"name": "get_product_info", "description": "Ottiene dettagli su un capo eco", "parameters": {"type": "object", "properties": {"product_name": {"type": "string"}}, "required": ["product_name"]}}},
    {"type": "function", "function": {"name": "check_availability", "description": "Verifica disponibilità taglie", "parameters": {"type": "object", "properties": {"product_name": {"type": "string"}, "size": {"type": "string"}}, "required": ["product_name", "size"]}}},
    {"type": "function", "function": {"name": "book_fitting", "description": "Prenota sessione di prova", "parameters": {"type": "object", "properties": {"date": {"type": "string"}, "time": {"type": "string"}}, "required": ["date", "time"]}}}
]

def handle_tool_call(tool_call) -> str:
    args = json.loads(tool_call.function.arguments)
    if tool_call.function.name == "get_product_info": return product_tool.get_info(**args)
    if tool_call.function.name == "check_availability": return stock_tool.check_stock(**args)
    if tool_call.function.name == "book_fitting": return appointment_tool.book_appointment(**args)
    return "Funzione non trovata."

@cl.on_chat_start
def on_chat_start():
    today = datetime.today().strftime("%Y-%m-%d")
    cl.user_session.set("messages", [{"role": "system", "content": f"Sei l'assistente di VerdeModa. Oggi è il {today}."}])

@cl.on_message
async def main(message: cl.Message):
    messages = cl.user_session.get("messages")
    messages.append({"role": "user", "content": message.content})
    
    completion = client.chat.completions.create(model="gpt-4o-mini", messages=messages, tools=TOOLS)
    response_message = completion.choices[0].message
    
    if response_message.tool_calls:
        messages.append(response_message)
        for tool_call in response_message.tool_calls:
            result = handle_tool_call(tool_call)
            messages.append({"role": "tool", "tool_call_id": tool_call.id, "name": tool_call.function.name, "content": result})
        
   
        final_completion = client.chat.completions.create(model="gpt-4o-mini", messages=messages)
        messages.append(final_completion.choices[0].message)
        await cl.Message(content=final_completion.choices[0].message.content).send()
    else:
        await cl.Message(content=response_message.content).send()