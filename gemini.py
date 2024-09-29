import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
# GOOGLE_API_KEY = 'AIzaSyDctvtsI1RXWE1hEETzSvjncO3Q8Idbe4U'
genai.configure(api_key=GOOGLE_API_KEY)

gemini_pro = genai.GenerativeModel("gemini-pro")
prompt  = "こんにちは"
response = gemini_pro.generate_content(prompt)
print(response.text)
print('終了')