import requests

API_KEY = "99bb21507ae4c2fe3ae8a8c4ab11aa572ca93e3fcdf62282793913286d0f864e"  # Replace this with your actual API key
ENDPOINT = "https://api.together.xyz/v1/completions"


def ask_hiphop_question(question):
    """Send a hip-hop question to the Together.ai API and return the response."""
    payload = {
        "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo",  # Free model
        "prompt": f"Answer this question about hip-hop history: {question}",
        "max_tokens": 100  # Limit response length
    }

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(ENDPOINT, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json()["choices"][0]["text"].strip()
    else:
        return f"Error: {response.status_code}, {response.text}"

print(f"Ask me anything you want to know about hip hop! Type 'exit' to quit")

while True:
    user = input(f"What would you like to know about hip hop?") #user asks question to chatbot

    if user.lower() == "exit": #exits application
        print("See you next time")
        break

    response = ask_hiphop_question(user)

    print(response)




