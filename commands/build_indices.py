from llama_index import SimpleDirectoryReader, GPTSimpleVectorIndex
from dotenv import load_dotenv

load_dotenv(override=True)

documents = SimpleDirectoryReader('./data/sources').load_data()

index = GPTSimpleVectorIndex(documents=documents)

index.save_to_disk("./data/indices/qrt-tex-vect.json")
