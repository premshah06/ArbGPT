import streamlit as st

st.set_page_config(
    page_title="Home Page",
    page_icon="https://docs.arbitrum.io/img/logo.svg",
)

st.write("# Welcome to ArbGPT! 👋")
st.write("Explore the capabilities of ArbGPT to chat with Arb documentation, and debug or generate smart contracts.")

st.write("## Get Started!")
st.write("Choose a section to start exploring, chatting, or working with smart contracts.")

st.image("https://docs.arbitrum.io/img/logo.svg", width=150)

st.write("### 💬 Chat with Arb Docs")
st.write("Have questions about Arbitrum? Chat with our AI assistant to get detailed explanations, summaries, and guidance on various Arb-related topics.")
st.write("[Go to Chat with Arb Docs](/Chat_with_arb_docs)")

st.write("### 🛠️ Smart Contract Debugging & Generation")
st.write("Paste your .sol smart contract code to debug or generate enhanced versions. Our AI will help you identify issues and suggest improvements.")
st.write("[Go to Smart Contract Debugger](/AI_assisted_smart_contract_debugger)")