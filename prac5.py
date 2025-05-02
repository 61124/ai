import random
import datetime

def chatbot(user_input,context):
    time = str(datetime.datetime.now())
    responses = {
        "hello":"Hello! how can I help you?",
        "hi":"Hi! Nice to see you!",
        "what is your name":"I am your customer service chatbot",
        "what time is it":time,
        "how are you":"Hey I am doing good. How are you?",
        "i am fine":"Glad to hear that",
        "i am good":"Glad to hear that",
        "help":"Sure! How can I help you?",
        "order status":"I'd be happy to help! May I have your order number?",
        "product inquiry": "Please enter the product ID you're interested in.",
        "how is today's weather":"Pls give me input of the city you live in to know about the weather"
    }
    order_status = [
        "Your order is being packed.",
        "Your order is on the way.",
        "Your order has been delivered.",
        "Your order is delayed due to weather conditions.",
        "Your order is out for delivery today."
    ]
    product_status = [
        "Product is in stock and available for purchase.",
        "This product is currently out of stock.",
        "This product will be restocked soon.",
        "Product is available with a 10% discount today!"
    ]
    weather = {
        "mumbai":"Hot and humid",
        "pune":"Dry and sunny",
        "delhi":"Smoke and dusty"
    }
    user_input = user_input.lower()
    if context == "awaiting order":
        resp = random.choice(order_status)
        return resp,None
    elif context == "awaiting product":
        resp = random.choice(product_status)
        return resp,None
    elif context == "awaiting city":
        if user_input in ["mumbai","pune","delhi"]:
            return weather[user_input],None
        else:
            return "City info not available",None

    if user_input in responses:
        if user_input == "order status":
            cont="awaiting order"
            return responses[user_input],cont
        elif user_input == "product inquiry":
            cont="awaiting product"
            return responses[user_input],cont
        elif user_input == "how is today's weather":
            cont = "awaiting city"
            return responses[user_input],cont
        else:
            return responses[user_input],None
    else:
        return "I am sorry, I cannot understand that. Can you please rephrase",None

print("Customer Service Chatbot")
print("Type bye to exit")
context=None
while True:
    user_input = input("You: ")
    if user_input == "bye":
        print("Bye, have a nice day!")
        break
    response,context=chatbot(user_input,context)
    print("Chatbot:",response)