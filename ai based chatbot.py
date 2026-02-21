import datetime

print("🤖 AI Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input in ["hi", "hello", "hey"]:
        print("Bot: Hello! How can I help you?")
        
    elif "your name" in user_input:
        print("Bot: I am a simple AI chatbot created using Python.")
        
    elif "ai" in user_input:
        print("Bot: AI stands for Artificial Intelligence.")
        
    elif "how are you" in user_input:
        print("Bot: I am just code, but I'm doing great!")
        
    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("Bot: Current time is", current_time)
        
    elif "date" in user_input:
        today = datetime.date.today()
        print("Bot: Today's date is", today)
        
    elif "calculate" in user_input:
        try:
            expression = user_input.replace("calculate", "")
            result = eval(expression)
            print("Bot: The result is", result)
        except:
            print("Bot: Please enter a valid math expression.")
        
    elif user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a nice day.")
        break
        
    else:
        print("Bot: Sorry, I don't understand that.")
