from classifier import classify_intent
from router import route_and_respond
from logger import log_route

def main():

    message = input("User: ")

    result = classify_intent(message)

    response = route_and_respond(message, result)

    intent = result["intent"]
    confidence = result["confidence"]

    log_route(intent, confidence, message, response)

    print("\nAI:", response)

if __name__ == "__main__":
    main()