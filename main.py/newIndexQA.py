import os
from megabots import bot
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ["OPENAI_API_KEY"]
# Create a bot with one line of code. Automatically loads your data from the specified index directory.
qnabot = bot("qna-over-docs", index=r'C:\Users\Ethan\Kingsmen\Photography Transcript Reader, POC\megabots\main.py\ks-db-test')

#qnabot.save_index("index.pkl")
answer = qnabot.ask("What is the Kingsmen Way?")
print(answer)
