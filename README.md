# ArbGPT: AI-Powered Smart Contract Development Assistant

![ArbGPT Logo](https://docs.arbitrum.io/img/logo.svg)

ArbGPT is an AI-driven assistant designed to help **Arbitrum developers** with smart contract debugging, generation, and interactive documentation retrieval. Leveraging **OpenAI embeddings, MongoDB Atlas, and Streamlit**, it provides an efficient way to analyze and optimize smart contracts written in **C#** for the Arbitrum blockchain.

## 🌟 Key Features

- **🛠️ Smart Contract Debugger**: AI-powered debugging for Arbitrum smart contracts with detailed error analysis.
- **⚡ Smart Contract Generator**: Generate and enhance Arbitrum smart contract code based on user input.
- **📚 AI-Assisted Documentation**: Interact with the Arbitrum documentation through an AI-powered chat interface.
- **🔍 Efficient Vector Search**: Uses **MongoDB Atlas Vector Search** for fast and accurate contract information retrieval.
- **🎨 Intuitive UI**: Built with **Streamlit**, offering an easy-to-use interface for developers.

## 🚀 Demo

Check out the live demo here: **[ArbGPT Live](https://github.com/premshah06/ArbGPT)**

## 🏗️ Project Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/premshah06/ArbGPT.git
cd ArbGPT
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up Environment Variables
Copy the example environment file and update the credentials:
```bash
cp .env.example .env
```
Fill in the **MongoDB connection URI** and **GitHub Token** inside the `.env` file.

### 4️⃣ Create Embeddings and Configure MongoDB Atlas
Run the script to generate embeddings and store them in **MongoDB Atlas**:
```bash
python create-embeddings.py
```

### 5️⃣ Run the Application
```bash
streamlit run Home.py
```

## 🔧 Technologies Used

- **Programming Language**: Python
- **Framework**: Streamlit
- **Database**: MongoDB Atlas (Vector Search)
- **AI Models**: OpenAI Embeddings, LangChain
- **Deployment**: Google Cloud Run (Optional)

## 🌍 Deployment (Google Cloud Run)

1. **Build and push the container**
```bash
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/arbGPT
```
2. **Deploy the application**
```bash
gcloud run deploy --image gcr.io/YOUR_PROJECT_ID/arbGPT --platform managed --allow-unauthenticated
```

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Contributors
- **Prem Shah** - [GitHub](https://github.com/premshah06)

Feel free to contribute! Open an issue or submit a pull request. 🎉

## 📞 Contact
For any questions or support, reach out via **[GitHub Issues](https://github.com/premshah06/ArbGPT/issues)**.

---
✨ *Empowering developers with AI-driven smart contract solutions!* ✨

