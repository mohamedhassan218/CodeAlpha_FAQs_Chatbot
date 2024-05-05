"""
    Module implementing a simple chatbot capable of engaging in conversations about various topics.

    @author  Mohamed Hassan
    @since   5-5-2024
"""

import re
import random


class Bot:
    """
    A simple chatbot class capable of engaging in conversations on various topics.
    """

    negative_responses = (
        "no",
        "sorry",
        "bad",
        "sad",
        "nope",
        "not really",
        "negative",
        "I don't think so",
        "nah",
        "uh-uh",
    )
    exit_commands = (
        "quit",
        "pause",
        "exit",
        "goodbye",
        "bye",
        "see you later",
        "adios",
        "later",
        "farewell",
    )
    random_questions = (
        "What are you doing here?",
        "How are you?",
        "Where are you from?",
        "What's your favorite color?",
        "Do you have any pets?",
        "What do you like to do for fun?",
        "Have you traveled to any interesting places?",
        "Do you believe in aliens?",
        "What's the meaning of life?",
        "What's your favorite food?",
        "Tell me about your family.",
        "What's the best book you've ever read?",
        "What's your dream job?",
        "What's your opinion on artificial intelligence?",
    )

    def __init__(self):
        """
        Initialize the chatbot.
        """
        self.alienbabble = {
            "describe_planet_intent": r".*\s*your planet.*",
            "answer_why_intent": r"why\sare.*",
            "about_intellipat": r".*\s*intellipaat",
        }

    def greet(self):
        """
        Greet the user and start the conversation.
        """
        self.name = input("What is your name?")
        will_help = input(f"Hi {self.name}, help me to know more about your planet")
        if will_help.lower() in self.negative_responses:
            print("Ok, goodbye!")
            return
        self.chat()

    def make_exit(self, reply):
        """
        Check if the user wants to exit the conversation.

        @param reply: User input.
        @return: Boolean indicating whether to exit the conversation.
        """
        if reply.lower() in self.exit_commands:
            print("Ok, goodbye!")
            return True

    def chat(self):
        """
        Start the conversation loop.
        """
        reply = input(random.choice(self.random_questions)).lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))

    def match_reply(self, reply):
        """
        Match user input to predefined intents and generate appropriate responses.

        @param reply: User input.
        @return: Response based on the matched intent.
        """
        found_match = None
        for key, value in self.alienbabble.items():
            intent = key
            regex_pattern = value
            found_match = re.match(regex_pattern, reply)
            if found_match:
                if intent == "describe_planet_intent":
                    return self.describe_planet_intent()
                elif intent == "answer_why_intent":
                    return self.answer_why_intent()
                elif intent == "about_intellipat":
                    return self.about_intellipat()
        if not found_match:
            return self.no_match_intent()

    def describe_planet_intent(self):
        """
        Generate a response for the 'describe_planet_intent' intent.

        @return: Random response describing the planet.
        """
        responses = [
            "Our planet is called Zorblat. It's a vibrant world with three moons and lush forests.",
            "On our planet, we have vast oceans filled with bioluminescent creatures.",
            "Zorblat is known for its advanced technology and harmonious society.",
            "Our planet's landscape is dotted with crystalline formations and floating islands.",
        ]
        return random.choice(responses)

    def answer_why_intent(self):
        """
        Generate a response for the 'answer_why_intent' intent.

        @return: Random response explaining the purpose of the civilization.
        """
        responses = [
            "We exist to explore the cosmos and learn from other intelligent beings.",
            "The purpose of our civilization is to seek knowledge and foster peace among the stars.",
            "Our mission is to promote understanding and cooperation between different species in the universe.",
            "We are driven by curiosity and the desire to expand our collective consciousness.",
        ]
        return random.choice(responses)

    def about_intellipat(self):
        """
        Generate a response for the 'about_intellipat' intent.

        @return: Random response providing information about Intellipaat.
        """
        responses = [
            "Intellipaat is a leading provider of online courses and certifications in various fields of technology.",
            "Intellipaat offers comprehensive training programs designed to help individuals upskill and advance their careers.",
            "With Intellipaat, you can learn cutting-edge technologies from industry experts at your own pace.",
            "Intellipaat's courses cover a wide range of topics, from programming and data science to cloud computing and cybersecurity.",
        ]
        return random.choice(responses)

    def no_match_intent(self):
        """
        Generate a response for unmatched intents.

        @return: Default response asking the user to rephrase.
        """
        return "I'm sorry, I didn't understand that. Can you please rephrase?"


# Time to try our bot!
if __name__ == "__main__":
    bot = Bot()
    bot.greet()
