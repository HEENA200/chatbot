

def chatbot():
    print("🤖 Chatbot: Hello! I am a simple chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()  

        if "hello" in user_input or "hi" in user_input:
            print("🤖 Chatbot: Hello! How can I help you today?")
        
        elif "how are you" in user_input:
            print("🤖 Chatbot: I'm just a program, but I'm doing great! How about you?")
        
        elif "your name" in user_input:
            print("🤖 Chatbot: I am a simple rule-based chatbot created with Python.")
        
        elif "bye" in user_input:
            print("🤖 Chatbot: Goodbye! Have a great day!")
            break
        
        elif "time" in user_input:
            from datetime import datetime
            print("🤖 Chatbot: Current time is:", datetime.now().strftime("%H:%M:%S"))
        
        elif "date" in user_input:
            from datetime import datetime
            print("🤖 Chatbot: Today's date is:", datetime.now().strftime("%Y-%m-%d"))
        
        else:
            print("🤖 Chatbot: Sorry, I don’t understand that. Can you rephrase?")

# Run the chatbot
chatbot()
# Simple Rule-Based Chatbot using if-else

def chatbot():
    print("🤖 Chatbot: Hello! I am a simple chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()  # convert input to lowercase for matching

        if "hello" in user_input or "hi" in user_input:
            print("🤖 Chatbot: Hello! How can I help you today?")
        
        elif "how are you" in user_input:
            print("🤖 Chatbot: I'm just a program, but I'm doing great! How about you?")
        
        elif "your name" in user_input:
            print("🤖 Chatbot: I am a simple rule-based chatbot created with Python.")
        
        elif "bye" in user_input:
            print("🤖 Chatbot: Goodbye! Have a great day!")
            break
        
        elif "time" in user_input:
            from datetime import datetime
            print("🤖 Chatbot: Current time is:", datetime.now().strftime("%H:%M:%S"))
        
        elif "date" in user_input:
            from datetime import datetime
            print("🤖 Chatbot: Today's date is:", datetime.now().strftime("%Y-%m-%d"))
        
        else:
            print("🤖 Chatbot: Sorry, I don’t understand that. Can you rephrase?")

# Run the chatbot
chatbot()
