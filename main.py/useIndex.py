import os
from megabots import bot
from dotenv import load_dotenv
load_dotenv()
api_key = os.environ["OPENAI_API_KEY"]
qnabot = bot("qna-over-docs", index=r'C:\Users\Ethan\Kingsmen\Photography Transcript Reader, POC\megabots\main.py\ks-db-test')

answer = qnabot.ask("Can you tell me about iteration planning?")

print(answer)