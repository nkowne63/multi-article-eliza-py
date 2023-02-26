from pathlib import Path
from llama_index import SimpleDirectoryReader, GPTSimpleVectorIndex, download_loader, GPTTreeIndex
from dotenv import load_dotenv

load_dotenv(override=True)

documents = SimpleDirectoryReader('./data/xmls').load_data()

# PDFReader = download_loader("PDFReader")

# loader = PDFReader()
# documents = loader.load_data(file=Path('./data/pdfs/qrt.pdf'))

index = GPTTreeIndex(documents)

index.save_to_disk("./data/indices/qrt-xml-tree.json")
