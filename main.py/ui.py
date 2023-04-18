import os
from megabots import bot, create_interface

os.environ["OPENAI_API_KEY"] = "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"

qnabot = bot("qna-over-docs", index="./index.pkl")  # Make sure to use the correct index file or directory
demo = create_interface(qnabot)
demo.launch(share=True)
