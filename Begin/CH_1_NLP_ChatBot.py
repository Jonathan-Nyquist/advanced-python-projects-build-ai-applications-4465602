# Importing TextBlob to help the chatbot understand language nuances.
from textblob import TextBlob

# Defining the ChatBot class for interaction.
intents = {
    "hours":{
        "keywords":["hours", "open", "close"],
        "response": "We are open 9 AM to 5 PM, Monday to Friday."
    },
    "return":{
        "keywords": ["refund", "money back", "return"],
        "response": "Hell no, we're keeping your money. Ha ha! Too bad."
    }
}

def get_response(message):
    message = message.lower()
    if any(word in message for word in intents["keywords"]):
        return intents["response"]

    # Analyzing the sentiment of the user's message.
        sentiment = TextBlob(message).sentiment.polarity   
    # Generating the chatbot's response based on sentiment.
        return("That's so great to hear!" if sentiment > 0 else
               "I'm so sorry (not) to hear that. How can I further delay you?" if sentiment < 0 else
               "I see. Continue blathering.")
            
def chat():
    print("Hi, how can I help you today?")
    while(user_message := input("You: ").strip().lower()) not in ['exit', 'quit', 'bye']:
        print(f"\nChatbot: {get_response(user_message)}")
    
    print("Chatbot: Thank you for chatting. I enjoyed wasting your time!")
          


if __name__ == "__main__":
    # Creating the chatbot and starting the chat loop.
    #chatbot = ChatBot()
    #chatbot.start_chat()
    chat()
