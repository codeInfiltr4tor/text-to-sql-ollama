
import json
import subprocess

SYSTEM_PROMPT = """You are a helpful assistant that converts questions into SQL.
Return only JSON: { "sql": "..." } and only SELECT queries.
Schema and question are provided below."""

def text_to_sql(question: str, schema: str) -> str:
    prompt = f"{SYSTEM_PROMPT}\n\nSchema:\n{schema}\n\nQuestion:\n{question}\n"
    result = subprocess.run(
        ["ollama", "run", "mistral"],
        input=prompt.encode(),
        capture_output=True,
    )
    output = result.stdout.decode().strip()
    try:
        return json.loads(output)["sql"]
    except Exception:
        return output


# --------------------------------------------------------------

# # app/llm_utils.py
# import os
# import json
# from huggingface_hub import InferenceClient

# # load from .env (HF_TOKEN, HF_MODEL)
# HF_TOKEN = os.getenv("HF_API_KEY")  # rename if you used HF_API_KEY
# HF_MODEL = os.getenv("HF_MODEL", "meta-llama/Meta-Llama-3-8B-Instruct")  # example default

# SYSTEM_PROMPT = """
# You are a SQL assistant. You convert a natural-language question and a database schema
# into a safe, **read-only** SQLite SQL query. Return JSON exactly like:
# { "sql": "SELECT ..." }.
# Only SELECT statements allowed.
# """

# # instantiate client (with provider auto)
# client = InferenceClient(api_key=HF_TOKEN, provider="auto")

# def text_to_sql(question: str, schema: str) -> str:
#     prompt = f"{SYSTEM_PROMPT}\n\nSchema:\n{schema}\n\nQuestion:\n{question}\n\nReturn only JSON."

#     # call the model
#     resp = client.chat.completions.create(
#         model=HF_MODEL,
#         messages=[
#             {"role": "system", "content": SYSTEM_PROMPT},
#             {"role": "user", "content": f"Schema:\n{schema}\n\nQuestion: {question}"}
#         ],
#         temperature=0.1,
#         max_tokens=256
#     )
#     # resp structure: depends on provider; check resp.choices[0].message.content
#     content = resp.choices[0].message.content.strip()

#     try:
#         j = json.loads(content)
#         return j["sql"]
#     except json.JSONDecodeError:
#         # fallback: assume plain SQL
#         return content




# --------------------------------------------------------


# import os
# import json
# import requests

# HF_API_KEY = os.getenv("HF_API_KEY")
# HF_MODEL = os.getenv("HF_MODEL")

# SYSTEM_PROMPT = """You are a SQL assistant. 
# You take a natural language question and a database schema, 
# and you return a safe, read-only SQL query as JSON like this:
# { "sql": "SELECT ..." }.
# Only SELECT statements are allowed. 
# Do not generate INSERT, UPDATE, DELETE, DROP, or ALTER statements."""

# def text_to_sql(question: str, schema: str) -> str:
#     headers = {
#         "Authorization": f"Bearer {HF_API_KEY}",
#         "Content-Type": "application/json",
#     }

#     prompt = f"{SYSTEM_PROMPT}\n\nSchema:\n{schema}\n\nQuestion:\n{question}\n\nReturn only JSON."

#     payload = {
#         "inputs": prompt,
#         "parameters": {"max_new_tokens": 200, "temperature": 0.2},
#     }

#     url = f"https://api-inference.huggingface.co/models/{HF_MODEL}"
#     response = requests.post(url, headers=headers, json=payload)
#     response.raise_for_status()

#     text_output = response.json()[0]["generated_text"].strip()

#     try:
#         sql_json = json.loads(text_output)
#         return sql_json["sql"]
#     except Exception:
#         # fallback if plain SQL returned
#         return text_output
