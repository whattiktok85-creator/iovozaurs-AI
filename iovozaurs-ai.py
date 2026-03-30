import os
import json
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from groq import Groq
import time

def load_config():
    config_file = 'api_keys_iovozaurs_ai.json'
    
    if not os.path.exists(config_file):
        print("\n[iovozaur-AI] ERROR: api_config.json not found.")
        print("[iovozaur-AI] SETUP WIZARD STARTED...")
        
        token = input(">>> Enter Telegram Bot Token: ").strip()
        key = input(">>> Enter Groq API Key: ").strip()
        
        data = {
            "bot_token": token,
            "groq_key": key
        }
        
        with open(config_file, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"[iovozaur-AI] SUCCESS: {config_file} created in project folder!\n")
    
    with open(config_file, 'r') as f:
        return json.load(f)

config = load_config()
bot = Bot(token=config['bot_token'])
dp = Dispatcher()
client = Groq(api_key=config['groq_key'])

async def get_ai_response(user_input):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "Ты - iovozaur-AI. Ты говоришь на всех языках которых тебя попросят написать ( Ты пишешь hello! а потом какой язык на этом языке говорить) базовый язык Англиский. "},
                {"role": "user", "content": user_input}
            ],
            model="llama-3.3-70b-versatile",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"[SYSTEM ERROR]: {str(e)}"

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("iovozaur-AI Status: ONLINE 🟢\nCreated by iovozaur-team.\nReady for input.")

@dp.message()
async def msg_handler(message: types.Message):
    await bot.send_chat_action(message.chat.id, "typing")
    response = await get_ai_response(message.text)
    await message.reply(f"{response}\n\n[Free Software by iovozaur]")

async def main():
    print("-------------------------------------")
    print("iovozaur-AI Project v1.0")
    print("Config: api_config.json")
    print("Status: RUNNING")
    print("Press CTRL+C to Shutdown")
    print("The beta version Changes in the code are possible.) print("-------------------------------------")
    
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("\n[iovozaur-AI] SHUTDOWN: Offline.")
