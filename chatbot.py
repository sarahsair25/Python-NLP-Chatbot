import nltk
from nltk.chat.util import Chat, reflections

# Download required NLTK data (run once)
nltk.download('punkt')

pairs = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]),
    (r"how are you ?", ["I'm doing well, thanks!", "All good 😊"]),
    (r"what is your name ?", ["I'm a simple chatbot built with Python."]),
    (r"quit", ["Goodbye! Take care 👋"]),
]

def start_chatbot():
    print("🤖 Chatbot: Hello! Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    start_chatbot()
