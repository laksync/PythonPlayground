import requests
import json
content=input("How can i help u?\nType Exit to leave\n")
while content!="Exit":
    content=input("How can i help u?\nType Exit to leave\n")
    response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
    "Authorization": f"Bearer key",
    "Content-Type": "application/json"
    },
    data=json.dumps({
        "model":"openai/gpt-4o-mini",
    "messages": [
      {
        "role": "user",
        "content": content
      }
    ]
  })
)
    data = response.json()

    print(data["choices"][0]["message"]["content"])