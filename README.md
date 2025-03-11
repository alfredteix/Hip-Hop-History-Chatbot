# Hip-Hop-History-Chatbot
Overview
This is a command-line chatbot that answers questions about hip-hop history using the Together.ai API. Users can ask about key events, artists, and cultural moments in hip-hop, and the chatbot will generate responses using the Llama-3.3-70B-Instruct-Turbo model.

Features
Interactive chat session where users can ask questions about hip-hop history
Uses a free large language model (LLM) API to generate responses
Runs continuously until the user types "exit"
Lightweight and requires minimal setup
Technologies Used
Python for the chatbot logic
Requests library for API interaction
Together.ai API for AI-generated responses
Setup and Installation
Prerequisites
Python 3 installed
An API key from Together.ai
Installation
Clone this repository:
bash
Copy
Edit
git clone https://github.com/yourusername/hiphop-history-chatbot.git
Navigate to the project folder:
bash
Copy
Edit
cd hiphop-history-chatbot
Install the required Python library:
bash
Copy
Edit
pip install requests
Open chatbot.py and replace the placeholder "your_api_key_here" with your actual API key.
Usage
Run the chatbot:
bash
Copy
Edit
python chatbot.py
Ask questions about hip-hop history.
Type "exit" to quit the chatbot.
Example Interaction
pgsql
Copy
Edit
Ask me anything you want to know about hip hop! Type 'exit' to quit

What would you like to know about hip hop? Who started hip-hop?
DJ Kool Herc is widely considered the father of hip-hop for his contributions in the 1970s.

What would you like to know about hip hop? What was the first rap song?
"Rapper's Delight" by The Sugarhill Gang, released in 1979, is often credited as the first commercially successful rap song.

What would you like to know about hip hop? exit
See you next time
Customization
Change the max_tokens value in chatbot.py to increase or decrease response length.
Modify the "prompt" to fine-tune the chatbot’s responses.
Future Enhancements
Improve accuracy by integrating a curated hip-hop knowledge base
Add a GUI version using Streamlit for a better user experience
Expand support for additional LLM APIs
Contributing
If you’d like to contribute, feel free to fork this repository and submit a pull request.

License
This project is licensed under the MIT License.

