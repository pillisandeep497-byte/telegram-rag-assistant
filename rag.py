from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_classic.vectorstores import FAISS

files = [
    "docs/handbook.pdf",
    "docs/leave_policy.pdf",
    "docs/hr_rules.pdf"
]

documents = []

for file in files:
    loader = PyPDFLoader(file)
    documents.extend(loader.load())

splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)

embeddings = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)

vectorstore = FAISS.from_documents(
    chunks,
    embeddings
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k":5}
)