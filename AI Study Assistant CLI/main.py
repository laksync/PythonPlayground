# AI Study Assistant CLI
from pypdf import PdfReader
import requests
import json
import os
key = os.getenv("OPENROUTER_API_KEY")
pdf_mode = False
full_text = ""
while True:
    doubt = input("\nEnter study related doubt:\n")
    if doubt == "/exit":
        print("Exiting assistant...")
        break
    elif doubt == "/help":
        print("""
Available Commands:

/help      -> Show commands
/history   -> View chat history
/clear     -> Clear history
/pdf       -> Enter PDF mode
/nopdf     -> Exit PDF mode
/exit      -> Exit assistant
""")
        continue
    elif doubt == "/history":
        try:
            with open("history.txt", "r") as f:
                print(f.read())
        except FileNotFoundError:
            print("No history found.")
        continue
    elif doubt == "/clear":
        with open("history.txt", "w") as f:
            pass
        print("History cleared.")
        continue
    elif doubt == "/pdf":
        path = input("Enter PDF path:\n")
        try:
            pdf = PdfReader(path)
            full_text = ""
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    full_text += text
            pdf_mode = True
            print("\nPDF loaded successfully.")
            print("You are now in PDF mode.")
        except Exception as e:
            print("Could not read PDF.")
            print("Error:", e)
        continue
    elif doubt == "/nopdf":
        pdf_mode = False
        full_text = ""
        print("Exited PDF mode.")
        continue
    if pdf_mode:
        context = full_text[:3000]
        prompt = f"""
Answer using these notes:
{context}
Question:
{doubt}
"""
    else:
        prompt = doubt
    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {key}",
                "Content-Type": "application/json"
            },
            data=json.dumps({
                "model": "openai/gpt-4o-mini",
                "messages": [
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            })
        )
        data = response.json()
        if "choices" in data:
            answer = data["choices"][0]["message"]["content"]
            print("\nAI:\n")
            print(answer)
            with open("history.txt", "a", encoding="utf-8") as f:
                f.write("User: " + doubt + "\n")
                f.write("AI: " + answer + "\n\n")
        else:
            print("\nAPI Error:")
            print(data)
    except Exception as e:
        print("Request failed.")
        print("Error:", e)