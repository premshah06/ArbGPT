import os
import pymongo
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from llama_index.core import Settings, StorageContext, VectorStoreIndex
from langchain_openai import OpenAIEmbeddings
from llama_index.vector_stores.mongodb import MongoDBAtlasVectorSearch

# Load environment variables from a .env file
load_dotenv()

# Retrieve environment variables
# Uncomment when running locally
# MONGODB_CONN_URI = os.getenv('MONGODB_CONN_URI')
# GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

MONGODB_CONN_URI = st.secrets['MONGODB_CONN_URI']
GITHUB_TOKEN = st.secrets['GITHUB_TOKEN']

# Set up Streamlit page configuration
st.set_page_config(
    page_title="Smart Contract Debugger/Generator 🛠️",
    page_icon="https://docs.arbitrum.io/img/logo.svg",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.sidebar.warning("ArbGPT can make mistakes. Double-check important info.")

# MongoDB database and collection configuration
DB_NAME = "arb_knowledgebase"
COLLECTION_NAME = "docs"

# Initialize MongoDB client and collection
client = pymongo.MongoClient(MONGODB_CONN_URI)
collection = client[DB_NAME][COLLECTION_NAME]

# Field name for storing vector embeddings in MongoDB
VECTOR_DATABASE_FIELD_NAME = 'idx_embedding'

# Set up embedding model
embed_model = OpenAIEmbeddings(
    model="text-embedding-3-large",
    base_url="https://models.inference.ai.azure.com",
    api_key=GITHUB_TOKEN
)
Settings.embed_model = embed_model

# Set up LLM model
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.8,
    max_tokens=8192,
    api_key=GITHUB_TOKEN,
    base_url="https://models.inference.ai.azure.com"
)
Settings.llm = llm

# Set up vector store for MongoDB Atlas
vector_store = MongoDBAtlasVectorSearch(
    mongodb_client=client,
    db_name=DB_NAME,
    collection_name=COLLECTION_NAME,
    vector_index_name=VECTOR_DATABASE_FIELD_NAME
)

# Create storage context with the vector store
storage_context = StorageContext.from_defaults(vector_store=vector_store)

# Create a VectorStoreIndex with the vector store
index = VectorStoreIndex.from_vector_store(
    vector_store=vector_store,
    embed_model=embed_model,
    llm=llm
)

# Initialize session state if not already set
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Streamlit UI components
st.title("Smart Contract Debugger/Generator 🛠️")
st.subheader("Analyze and Enhance Your Solidity Smart Contracts")

# Radio button to choose between Debug or Generate
action = st.radio("Select an action:", ["Debug Code", "Generate Code"])

# User input for .cs code
cs_code = st.text_area("Paste your query / code here:", height=300)

# Button actions based on selection
if action == "Debug Code":
    if st.button("Submit Debug Request"):
        if cs_code:
            st.subheader("Debugging Results")

            # Show progress bar while debugging
            with st.spinner("Debugging code..."):
                debug_prompt = f"Debug the following Solidity smart contract .sol code if it contains any errors and provide insights on potential issues:\n\n{cs_code}"
                debug_response = llm.invoke(debug_prompt)

            st.code(debug_response.content, language='python')

elif action == "Generate Code":
    if st.button("Submit Generate Request"):
        if cs_code:
            st.subheader("Code Generation Results")

            # Show progress bar while generating code
            with st.spinner("Generating code..."):
                # Prompt the LLM to generate code
                generate_prompt = f"Generate code for the following Solidity smart contract .sol code and provide improvements or enhancements:\n\n{cs_code}"
                generate_response = llm.invoke(generate_prompt)

            st.code(generate_response.content, language='python')
