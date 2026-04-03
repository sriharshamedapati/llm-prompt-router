\# LLM-Powered Prompt Router for Intent Classification



\## 📌 Overview



This project implements an LLM-powered prompt routing system that classifies user intent and routes requests to specialized AI personas.



Instead of using a single large prompt, the system follows a two-step approach:



1\. \*\*Intent Classification\*\* – A lightweight LLM call detects user intent.

2\. \*\*Response Generation\*\* – The request is routed to a specialized expert prompt.



\---



\## 🎯 Supported Intents



\* `code` – Programming and debugging

\* `data` – Data analysis and statistics

\* `writing` – Writing improvement and feedback

\* `career` – Career guidance and advice

\* `unclear` – Ambiguous or unsupported queries



\---



\## 🧠 System Architecture



User Input → Classifier → Intent + Confidence → Router → Expert Persona → Final Response



\---



\## ⚙️ Features



\* Intent classification with confidence score

\* Multiple expert personas

\* Structured JSON output

\* Graceful error handling

\* Confidence threshold fallback

\* Logging in JSONL format

\* Docker container support



\---



\## 📂 Project Structure



```

llm-prompt-router/

│

├── app.py

├── classifier.py

├── router.py

├── prompts.py

├── logger.py

├── test\_messages.py

│

├── route\_log.jsonl

├── requirements.txt

├── Dockerfile

├── docker-compose.yml

├── .env.example

└── README.md

```



\---



\## 🚀 Setup (Local)



\### 1. Clone Repository



```

git clone <your-repo-url>

cd llm-prompt-router

```



\### 2. Create Environment File



Create a `.env` file:



```

GEMINI\_API\_KEY=your\_api\_key\_here

```



\### 3. Install Dependencies



```

pip install -r requirements.txt

```



\### 4. Run Application



```

python app.py

```



\---



\## 🐳 Running with Docker



\### Build and Run



```

docker-compose up --build

```



\---



\## 🧪 Example Usage



\### Input



```

how do i sort a list in python?

```



\### Output



```

Intent: code (confidence: \~0.9)

→ Python solution with explanation

```



\---



\## 📜 Logging



All interactions are logged in:



```

route\_log.jsonl

```



\### Log Format



```

{

&#x20; "intent": "code",

&#x20; "confidence": 0.92,

&#x20; "user\_message": "sort list python",

&#x20; "final\_response": "..."

}

```



\---



\## 🧩 Design Decisions



\* Used Gemini Flash model for fast and cost-efficient classification

\* Implemented confidence threshold to avoid incorrect routing

\* Separated prompts into a dedicated module for maintainability

\* Used JSONL format for scalable logging and analysis



\---



\## 🔮 Future Improvements



\* Add web UI using FastAPI or Flask

\* Support multi-intent routing

\* Add caching for repeated queries

\* Implement manual override (e.g., @code)



\---



\## ⚠️ Note



Do not commit your `.env` file. Use `.env.example` to share required environment variables safely.



