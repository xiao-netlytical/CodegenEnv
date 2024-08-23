import os
from util import *
from config import *


from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import PDFPlumberLoader
from langchain_community.document_loaders import PyMuPDFLoader

from langchain.text_splitter import CharacterTextSplitter

def run_pdf_loader():
    loaders = []
    for filename in os.listdir("./data"):
            if filename.endswith('.pdf'):
                text_file = os.path.join("./data", filename)
                loader = PDFPlumberLoader(text_file)
                loaders.append(loader)
    return loaders

loaders = run_pdf_loader()

def run_splitter():
    document_chunks = []
    for loader in loaders:
        document = loader.load()
        text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=100)
        chunks = text_splitter.split_documents(document)
        document_chunks.extend(chunks)
    
    return document_chunks


def run_recursive_splitter():
    document_chunks = []
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    docs = []
    for loader in loaders:
        docs.extend(loader.load())    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 2000,
        chunk_overlap = 200
    )
    document_chunks = text_splitter.split_documents(docs)
    return document_chunks

document_chunks = run_splitter()
# document_chunks = run_recursive_splitter()


def test_chunk_number(chunks, test_string):
    print(len(chunks))
    i = 0
    for i, document in enumerate(chunks):
        if test_string in document.page_content:
            print(document.page_content)
            print("\n\n")
            print(document.metadata)

# test_chunk_number(document_chunks)


def chunk_embeding(document_chunks, load=False):
    from langchain_openai import OpenAIEmbeddings
    from langchain_community.vectorstores import FAISS

    embedding = OpenAIEmbeddings(model="text-embedding-3-small")

    if load:
        vectorstore = FAISS.load_local("vectorstore", embedding)
    else:
        vectorstore = FAISS.from_documents(document_chunks, embedding)
        # vectorstore.save_local("vectorstore", "user_document")

    from langchain_community.retrievers import BM25Retriever
    bm25_retriever = BM25Retriever.from_documents(document_chunks)
    
    return vectorstore, bm25_retriever

vectorstore, bm25_retriever = chunk_embeding(document_chunks)

def query_rag(query, context_file, k):
    bm25_retriever.k = k

    # k_results = bm25_retriever.invoke(query)

    # s_results = vectorstore.similarity_search(query, k=k)
    # k_results.extend(s_results)

    faiss_retriever = vectorstore.as_retriever(search_kwargs={"k": k})
    from langchain.retrievers import EnsembleRetriever
    ensemble_retriever = EnsembleRetriever(retrievers=[bm25_retriever, faiss_retriever])
    k_results = ensemble_retriever.invoke(query)

    context = "\n\n".join(["Page_Content:"+doc.page_content for doc in k_results])

    save_current_text_result("./data/"+context_file, context )
    
    return context


def query_llm(query, context_file):

    template_m = """
    Use only the provided Context to answer the request.
    If the Context does not provide relevant information for the Request, respond with "I don't know."
    If the Context is relevant to the Request, answer based strictly on the facts provided.
    Do not reason, extend, or simplify when generating the answer, as the Context is part of technical specifications.

    The following is the Context: 
    {contx}

    """
    data_s = get_previous_text_result("./data/"+context_file)
    data_list = data_s.split('Page_Content:')
    run_task_with_multi_context("QA task", data_list, template_m, "Request:"+query, T_TEXT)


def run_query():
    k = 10
    while True:
        query = input("Query:")
        if query == 'n':
            break
        k = input("Number of context retrieved:")
        context_s = query_rag(query, "context.txt", int(k))

        ready = input("Are you ready to ask LLM:")
        if ready == 'y':
            query_llm(query, "context.txt")

run_query()









