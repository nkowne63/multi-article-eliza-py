# import os
from llama_index import GPTSimpleVectorIndex
from dotenv import load_dotenv

load_dotenv(override=True)

query = "what is completely resource non-generating?"

index = GPTSimpleVectorIndex.load_from_disk(
    "./data/indices/qrt-tex-vect.json")

response = index.query(query)
print(response)
