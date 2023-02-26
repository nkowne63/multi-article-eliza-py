# import os
from llama_index import GPTSimpleVectorIndex, GPTTreeIndex
from dotenv import load_dotenv

load_dotenv(override=True)

# query = os.getenv('QUERY_STRING')

query = "what is k resource non generating?"

index = GPTTreeIndex.load_from_disk("./data/indices/qrt-xml-tree.json")

response = index.query(query)
print(response)
