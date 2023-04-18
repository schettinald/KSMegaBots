import os
from megabots import bot, create_interface

# Include your own API Key
os.environ["OPENAI_API_KEY"] = "API KEY"

qnabot = bot("qna-over-docs", index="./index.pkl")  # Make sure to use the correct index file or directory
demo = create_interface(qnabot)
demo.launch(share=True)
