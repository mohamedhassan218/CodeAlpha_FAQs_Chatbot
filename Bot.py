"""
    A simple retrieval-based chatbot using TF-IDF and cosine similarity.
    
    @author  Mohamed Hassan

    @since   2024-5-6
"""

import numpy as np
import string
import random
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re


class Bot:
    """
    A class representing a retrieval-based chatbot.
    """

    def __init__(self, file_path):
        """
        Initializes the chatbot with data from a file.

        @param file_path: Path to the file containing data for the chatbot.
        """
        self.raw_data = self.load_data(file_path)
        self.raw_data = self.raw_data.lower()
        self.sentence_tokens = nltk.sent_tokenize(self.raw_data)
        self.word_tokens = nltk.word_tokenize(self.raw_data)
        self.lemmer = nltk.stem.WordNetLemmatizer()
        self.remove_punc_dict = dict((ord(punct), None) for punct in string.punctuation)
        self.greet_inputs = ("Hello", "Hi", "Whatssup!", "How are you??")
        self.greet_responses = ("Hi", "Hey!", "Hey there", "Hola")
        self.prepare_nltk()

    def load_data(self, file_path):
        """
        Loads data from a file.

        @param file_path: Path to the file.
        @return: String containing the data from the file.
        """
        with open(file_path, "r", errors="ignore") as file:
            return file.read()

    def prepare_nltk(self):
        """
        Prepares NLTK by downloading necessary resources.
        """
        nltk.download("punkt")
        nltk.download("wordnet")
        nltk.download("omw-1.4")

    def LemTokens(self, tokens):
        """
        Lemmatizes tokens.

        @param tokens: List of tokens to lemmatize.
        @return: List of lemmatized tokens.
        """
        return [self.lemmer.lemmatize(token) for token in tokens]

    def LemNormalize(self, text):
        """
        Normalizes text by lemmatizing and removing punctuation.

        @param text: Text to normalize.
        @return: Normalized text.
        """
        return self.LemTokens(
            nltk.word_tokenize(text.lower().translate(self.remove_punc_dict))
        )

    def remove_square_brackets_and_numbers(self, input_str):
        """
        Removes square brackets and numbers from input string.

        @param input_str: Input string.
        @return: String with square brackets and numbers removed.
        """
        return re.sub(r"\[\d+\]", "", input_str).strip()

    def greet(self, sentence):
        """
        Responds with a greeting if the input sentence is a greeting.

        @param sentence: Input sentence.
        @return: Random greeting response if input is a greeting, otherwise None.
        """
        for word in sentence.split():
            if word.lower() in self.greet_inputs:
                return random.choice(self.greet_responses)

    def response(self, user_question):
        """
        Generates a response to the user question using TF-IDF and cosine similarity.

        @param user_question: User question.
        @return: Bot response.
        """
        bot_response = ""
        TfidVec = TfidfVectorizer(tokenizer=self.LemNormalize, stop_words="english")
        tfidf = TfidVec.fit_transform(self.sentence_tokens)
        values = cosine_similarity(tfidf[-1], tfidf)
        indx = values.argsort()[0][-2]
        flat = values.flatten()
        flat.sort()
        req_tfidf = flat[-2]
        if req_tfidf == 0:
            bot_response = bot_response + "Sorry, unable to understand you!"
            bot_response = self.remove_square_brackets_and_numbers(bot_response)
            return bot_response
        else:
            bot_response = bot_response + self.sentence_tokens[indx]
            bot_response = self.remove_square_brackets_and_numbers(bot_response)
            return bot_response
