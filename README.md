# 🧠 Text-to-SQL App using FastAPI, SQLite, and Ollama (Mistral)

This project demonstrates how to build a **Text-to-SQL natural language interface** — where users can type a question in plain English (like *"Show me all customers who placed more than 5 orders"*) — and the app automatically converts it into an **SQL query** that runs against a **SQLite database**.

The project is inspired by [KDnuggets’ “Creating a Text-to-SQL App with OpenAI, FastAPI, and SQLite”](https://www.kdnuggets.com/creating-a-text-to-sql-app-with-openai-fastapi-sqlite), but this version uses **Ollama’s free Mistral model**, making it **completely open-source and local**.

---

## 🚀 Features

* 🧾 Converts **natural language questions** into **SQL queries**
* ⚡ Powered by **FastAPI** (backend) and **Ollama Mistral** (AI model)
* 🗃️ Uses **SQLite** for easy data storage
* 🔒 100% **local & privacy-friendly** — no external API calls
* 🧰 Easily extendable for other databases (PostgreSQL, MySQL, etc.)

---

## 🏗️ Tech Stack

| Component         | Technology Used               |
| ----------------- | ----------------------------- |
| Backend Framework | FastAPI                       |
| AI Model          | Ollama – Mistral 7B           |
| Database          | SQLite                        |
| Frontend          | HTML + JavaScript (Fetch API) |
| Language          | Python 3.10+                  |

---

## 📦 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/codeInfiltr4tor/text-to-sql-ollama.git
cd text-to-sql-ollama
```

### 2️⃣ Install Ollama

Ollama is required to run the **Mistral** model locally.

#### For Linux or macOS:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

#### For Windows:

Download and install from the official Ollama page:
👉 [https://ollama.com/download](https://ollama.com/download)

---

### 3️⃣ Pull the Mistral Model

Once installed, pull the **Mistral** model locally:

```bash
ollama pull mistral
```

---

### 4️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # for Linux/Mac
venv\Scripts\activate      # for Windows
```

### 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt` yet, here’s what to include:

```
fastapi
uvicorn
sqlite3
requests
```

---

## 🧩 Database Setup

You can use your own SQLite database, or create one with sample data.

Example (for testing):

```bash
sqlite3 shop.db < shop_data.sql
```

Where `shop_data.sql` contains sample shop tables like:

* `products`
* `customers`
* `orders`
* `suppliers`

---

## ⚙️ Run the FastAPI Server

Start the backend server:

```bash
uvicorn main:app --reload
```

You’ll see output like:

```
INFO:     Uvicorn running on http://127.0.0.1:8000
```

Open this URL in your browser:
👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
(You can test the `/query` endpoint here)

---

## 🧠 How It Works

1. User enters a **natural language question** (e.g. *"Show all products with price above 300"*)
2. FastAPI sends this text to **Ollama Mistral** locally.
3. The model returns a **SQL query** (e.g. `SELECT * FROM products WHERE price > 300;`)
4. The backend executes this query on SQLite.
5. Results are displayed to the user.

---

## 🧪 Example Query Flow

**Input:**

> "List all customers who joined this year."

**Generated SQL:**

```sql
SELECT * FROM customers WHERE join_date >= '2025-01-01';
```

**Output:**

```
[
  {
    "id": 23,
    "name": "Rahul Sharma",
    "email": "rahul@example.com",
    "city": "Mumbai",
    "join_date": "2025-03-14"
  },
  ...
]
```

---

## 🖥️ Frontend (Optional UI)

You can add a simple HTML + JS page to make queries interactively:

```html
<input type="text" id="question" placeholder="Ask something about your data...">
<button onclick="sendQuery()">Run</button>
<pre id="result"></pre>

<script>
async function sendQuery() {
  const q = document.getElementById("question").value;
  const res = await fetch("/query", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ question: q })
  });
  const data = await res.json();
  document.getElementById("result").textContent = JSON.stringify(data, null, 2);
}
</script>
```

---

## 🧰 Folder Structure

```
text-to-sql-ollama/
├── main.py
├── shop_data.sql
├── shop.db
├── requirements.txt
├── README.md
└── static/
    └── index.html  # Optional UI
```

---

## 🧑‍💻 Future Enhancements

* Support for **PostgreSQL/MySQL**
* Add **user authentication**
* Integrate with **LangChain or HuggingFace models**
* Export results as CSV or Excel
* Deploy on **Render / Railway / Deta Space**

---

## 💡 Credits

* Inspired by: [KDnuggets Blog](https://www.kdnuggets.com/creating-a-text-to-sql-app-with-openai-fastapi-sqlite)
* AI Model: [Ollama Mistral](https://ollama.com/library/mistral)
* Author: **CODEINFILTR4TOR**
* GitHub: [github.com/codeInfiltr4tor](https://github.com/codeInfiltr4tor)

---

## 🏁 License

This project is released under the [MIT License](LICENSE).

Feel free to fork, improve, and share it!
