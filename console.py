import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

print("チャットボットです。何か質問はありますか？（終了するには「終了」と入力してください）")

while True:
  user_input = input("質問内容を入力してください：　")

  if user_input == "終了":
    print("チャットを終了します。またのお越しを！")
    break

  response = chat.send_message(user_input)
  print(response.text)