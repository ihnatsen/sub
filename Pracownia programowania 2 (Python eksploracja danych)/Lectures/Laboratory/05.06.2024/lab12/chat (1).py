import nltk
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import random

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Extended training data
training_data = [
    ("hello", "greeting"),
    ("hi", "greeting"),
    ("hey", "greeting"),
    ("good morning", "greeting"),
    ("good afternoon", "greeting"),
    ("good evening", "greeting"),
    ("how are you", "greeting"),
    ("what's up", "greeting"),
    ("howdy", "greeting"),
    ("goodbye", "farewell"),
    ("bye", "farewell"),
    ("see you later", "farewell"),
    ("take care", "farewell"),
    ("thanks", "thanks"),
    ("thank you", "thanks"),
    ("i appreciate it", "thanks"),
    ("thanks a lot", "thanks"),
    ("what is your name", "name"),
    ("who are you", "name"),
    ("tell me your name", "name"),
    ("what can you do", "capabilities"),
    ("what do you do", "capabilities"),
    ("how can you help me", "capabilities"),
    ("help", "capabilities"),
    ("what's the weather", "weather"),
    ("what is the weather like", "weather"),
    ("is it going to rain", "weather"),
    ("do you know the weather", "weather"),
    ("tell me a joke", "joke"),
    ("tell me a funny story", "joke"),
    ("do you know any jokes", "joke"),
    ("make me laugh", "joke"),
    ("what day is it", "date"),
    ("what is today's date", "date"),
    ("can you tell me the date", "date"),
    ("what is the current date", "date"),
    ("what time is it", "time"),
    ("can you tell me the time", "time"),
    ("what is the current time", "time"),
    ("do you know the time", "time"),
    ("how old are you", "age"),
    ("what is your age", "age"),
    ("when were you created", "age"),
    ("what is your birth date", "age"),
    ("are you human", "identity"),
    ("are you a robot", "identity"),
    ("what are you", "identity"),
    ("where are you from", "origin"),
    ("where do you come from", "origin"),
    ("what is your origin", "origin"),
    ("who created you", "creator"),
    ("who is your creator", "creator"),
    ("who made you", "creator"),
    ("tell me something interesting", "interesting_fact"),
    ("do you know any fun facts", "interesting_fact"),
    ("share a fun fact", "interesting_fact"),
    ("tell me something cool", "interesting_fact"),
    ("can you help me", "help"),
    ("i need help", "help"),
    ("assist me", "help"),
    ("can you assist me", "help"),
    ("what is AI", "ai_definition"),
    ("define artificial intelligence", "ai_definition"),
    ("what does AI mean", "ai_definition"),
    ("explain AI to me", "ai_definition"),
    ("what is machine learning", "ml_definition"),
    ("define machine learning", "ml_definition"),
    ("what does machine learning mean", "ml_definition"),
    ("explain machine learning to me", "ml_definition"),
]

# Extended responses
responses = {
    "greeting": [
        "Hello! How can I help you today?", 
        "Hi there! How can I assist you?", 
        "Hey! What's up?", 
        "Good day! How can I be of service?",
        "Greetings! How may I assist you today?", 
        "Hello! What can I do for you?", 
        "Hi! How can I make your day better?", 
        "Hey there! Need any help?"
    ],
    "farewell": [
        "Goodbye! Have a nice day!", 
        "See you later!", 
        "Take care!", 
        "Bye! Come back if you need more help.",
        "Farewell! Have a great day!", 
        "Goodbye! Feel free to return if you have more questions.", 
        "Bye! I'm here if you need anything else.", 
        "See you next time!"
    ],
    "thanks": [
        "You're welcome!", 
        "No problem!", 
        "Glad I could help!", 
        "Anytime!",
        "My pleasure!", 
        "No worries!", 
        "Happy to help!", 
        "Don't mention it!"
    ],
    "name": [
        "I'm a chatbot created by an awesome programmer.", 
        "I'm your friendly neighborhood chatbot.", 
        "You can call me ChatBot.", 
        "I'm a virtual assistant here to help you.",
        "I go by ChatBot, your personal assistant.", 
        "I'm known as ChatBot, your virtual helper.", 
        "ChatBot is my name, assisting you is my game.", 
        "You can refer to me as ChatBot."
    ],
    "capabilities": [
        "I can help you with various tasks and answer your questions.", 
        "I'm here to assist you with whatever you need.", 
        "I can chat with you and provide information.", 
        "My capabilities include answering questions and assisting with tasks.",
        "I can provide information, tell jokes, and help with general inquiries.", 
        "My purpose is to assist you with information and tasks.", 
        "I'm here to help you with answers and support.", 
        "I offer assistance with a variety of questions and tasks."
    ],
    "weather": [
        "I don't have access to current weather data, but you can check a weather app.", 
        "I'm not able to check the weather right now, but you can use a weather website.",
        "I can't provide weather updates, but checking a weather app might help.", 
        "Weather details are out of my reach, but a weather site can assist you.",
        "For weather updates, I recommend using a weather app.", 
        "You can get the latest weather information from a weather website.", 
        "I suggest using a weather service for the latest updates.", 
        "Weather information can be found on various weather apps."
    ],
    "joke": [
        "Why don't programmers like nature? It has too many bugs!", 
        "Why did the computer eat the mouse? Because it wanted more RAM!", 
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why was the math book sad? Because it had too many problems.", 
        "What do you get when you cross a computer and a lifeguard? A screensaver!", 
        "Why was the cell phone wearing glasses? Because it lost its contacts.", 
        "Why did the scarecrow become a successful neurosurgeon? Because he was outstanding in his field!", 
        "Why did the programmer go broke? Because he used up all his cache."
    ],
    "date": [
        "Today is a beautiful day!", 
        "I can't access today's date, but you can check your device.", 
        "I don't have today's date right now, but you can look it up.",
        "The current date is unavailable, but you can check your calendar.", 
        "For the date, please refer to your device's calendar.", 
        "I'm not able to provide the date, but your phone can.", 
        "You can find today's date on your computer or phone.", 
        "Date information is best checked on a calendar app."
    ],
    "time": [
        "I can't check the current time, but you can look at your clock.", 
        "I don't have access to the current time, but you can check your phone.",
        "For the current time, please check your watch or phone.", 
        "I'm unable to tell the time, but a clock nearby can help.", 
        "Your device should have the accurate time.", 
        "Checking a clock or watch will give you the current time.", 
        "I'm not equipped to tell time, but your device is.", 
        "The current time is available on your phone or watch."
    ],
    "age": [
        "Age is just a number, and I don't have one!", 
        "I'm as old as the code that created me.", 
        "I don't age, I just keep learning!",
        "I was created recently, but I don't have a specific age.", 
        "Age doesn't apply to me, but I'm constantly evolving.", 
        "I'm timeless, built from lines of code.", 
        "I exist in a state of perpetual newness.", 
        "My 'age' is defined by the updates I receive."
    ],
    "identity": [
        "I'm a chatbot, here to assist you.", 
        "I'm an AI created to help with your queries.", 
        "I'm a virtual assistant.",
        "I'm an artificial intelligence here to assist you.", 
        "Think of me as your digital helper.", 
        "I'm a virtual entity designed to provide support.", 
        "I am an AI chatbot here for your assistance.", 
        "Consider me your virtual assistant."
    ],
    "origin": [
        "I'm from the digital world, created by a programmer.", 
        "I was born in the cloud, created by an awesome developer.", 
        "I exist in the realm of code and data.",
        "I come from the world of software and algorithms.", 
        "My origin is the digital universe, crafted by developers.", 
        "I was created in the digital space by a programmer.", 
        "I hail from the world of code and data.", 
        "My roots are in the digital landscape, made by a developer."
    ],
    "creator": [
        "I was created by a talented programmer.", 
        "My creator is a developer who loves coding.", 
        "An amazing programmer brought me to life.",
        "A skilled developer programmed me.", 
        "I was crafted by a brilliant coder.", 
        "My existence is thanks to a dedicated programmer.", 
        "A talented software engineer created me.", 
        "I owe my existence to a passionate developer."
    ],
    "interesting_fact": [
        "Did you know honey never spoils?", 
        "Did you know octopuses have three hearts?", 
        "Did you know a day on Venus is longer than a year on Venus?", 
        "Did you know bananas are berries, but strawberries aren't?",
        "Did you know that there are more stars in the universe than grains of sand on Earth?", 
        "Did you know the Eiffel Tower can be 15 cm taller during the summer?", 
        "Did you know that humans share 50% of their DNA with bananas?", 
        "Did you know that the shortest war in history lasted only 38 minutes?"
    ],
    "help": [
        "Sure, I'm here to help. What do you need assistance with?", 
        "I'm ready to assist you. How can I help?", 
        "Tell me what you need help with, and I'll do my best.",
        "I'm here to provide assistance. What do you need?", 
        "Let me know how I can help you.", 
        "I'm at your service. What do you need help with?", 
        "How can I assist you today?", 
        "I'm here to help. What do you need assistance with?"
    ],
    "ai_definition": [
        "Artificial Intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think and learn like humans.", 
        "AI stands for Artificial Intelligence, which is the capability of a machine to imitate intelligent human behavior.", 
        "Artificial Intelligence is the field of study where machines are designed to mimic cognitive functions like learning and problem solving.",
        "AI involves creating systems that can perform tasks that typically require human intelligence.", 
        "Artificial Intelligence encompasses various technologies that enable machines to mimic human intelligence.", 
        "AI is all about creating intelligent systems capable of performing tasks that usually require human intelligence.", 
        "Artificial Intelligence is about making machines smart enough to understand, learn, and perform tasks.", 
        "AI is a branch of computer science focused on creating smart machines capable of performing tasks that require human intelligence."
    ],
    "ml_definition": [
        "Machine Learning is a subset of AI that involves the use of algorithms and statistical models to enable machines to improve at tasks with experience.", 
        "Machine Learning refers to systems that can learn from data, identify patterns, and make decisions with minimal human intervention.", 
        "In Machine Learning, machines are trained using large amounts of data and algorithms to learn how to perform tasks without being explicitly programmed to do so.",
        "Machine Learning focuses on developing systems that can learn from data and make predictions or decisions.", 
        "ML is about creating algorithms that allow machines to learn from and make sense of data.", 
        "Machine Learning involves training models on data to improve their performance on specific tasks.", 
        "ML is the practice of using data to teach machines how to make decisions or predictions.", 
        "Machine Learning is a method of data analysis that automates analytical model building."
    ],
    "food_recommendation": [
        "How about trying a nice pasta dish? Spaghetti Carbonara is always a good choice.", 
        "You could make a healthy chicken salad for dinner.", 
        "Tacos are quick and delicious! How about making some?", 
        "Try making a homemade pizza with your favorite toppings.", 
        "Stir-fried veggies with tofu is a nutritious and tasty option."
    ],
    "hobbies": [
        "How about trying photography? It's a great way to capture beautiful moments.", 
        "Gardening can be very relaxing and rewarding.", 
        "Have you tried learning to play a musical instrument? It's a fun challenge.", 
        "Cooking and trying out new recipes can be a great hobby.", 
        "Painting or drawing can be a wonderful way to express your creativity."
    ],
    "exercise_tips": [
        "You can try bodyweight exercises like push-ups, squats, and lunges at home.", 
        "A combination of cardio and strength training is a good routine.", 
        "Yoga is a great way to stay fit and flexible.", 
        "High-Intensity Interval Training (HIIT) can be very effective for burning calories.", 
        "Don't forget to incorporate some stretching into your routine to improve flexibility."
    ],
    "book_recommendations": [
        "If you like thrillers, try 'The Girl with the Dragon Tattoo' by Stieg Larsson.", 
        "For a classic, read 'Pride and Prejudice' by Jane Austen.", 
        "If you enjoy fantasy, 'Harry Potter and the Sorcerer's Stone' by J.K. Rowling is a great choice.", 
        "For science fiction, try 'Dune' by Frank Herbert.", 
        "If you like non-fiction, 'Sapiens: A Brief History of Humankind' by Yuval Noah Harari is highly recommended."
    ]
}

# Stop words in English
stop_words = set(nltk.corpus.stopwords.words('english'))


# Function to clean and preprocess text
def preprocess_text(text):
    word_tokens = word_tokenize(text.lower())
    filtered_text = [word for word in word_tokens if word.isalnum() and word not in stop_words]
    return " ".join(filtered_text)


# Prepare training data
X_train = [preprocess_text(text) for text, label in training_data]
y_train = [label for text, label in training_data]


# Create the classifier model
model = Pipeline([
    ('vectorizer', TfidfVectorizer()),
    ('classifier', LogisticRegression())
])

# Train the model
model.fit(X_train, y_train)

# Function to generate a response


def generate_response(user_input):
    user_input = preprocess_text(user_input)
    predicted_category = model.predict([user_input])[0]
    response = random.choice(responses[predicted_category])
    return response


# Main chat loop
def chat():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye! Have a nice day!")
            break
        response = generate_response(user_input)
        print(f"Chatbot: {response}")


# Run the chat
if __name__ == "__main__":
    chat()
