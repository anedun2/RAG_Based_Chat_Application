#Import libraries
import openai
from llama_index import StorageContext, load_index_from_storage
import config


openai.api_key = config.openai_key

storage_context = StorageContext.from_defaults(persist_dir="index")

index = load_index_from_storage(storage_context)

chat_engine = index.as_chat_engine(verbose=True)

while True:
    prompt = input('Prompt: ')
    response = chat_engine.chat(""+prompt+"")
    # print(response)