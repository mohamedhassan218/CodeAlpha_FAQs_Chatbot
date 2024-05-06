"""
    A simple UI using streamlit to be able to access our bot.
    
    @author  Mohamed Hassan

    @since   2024-5-6
"""

import streamlit as st
from custom_templates import css, bot_template, user_template
from Bot import Bot
import nltk

# Get instance of our bot.
bot = Bot("temp.txt")


def chat(bot, user_response):
    """
    Function to handle the logic to generate responses from our bot.
    """
    flag = True
    while flag:
        if user_response != "bye":
            if user_response == "thank you" or user_response == "thanks":
                flag = False
                return "You're welcome!"
            else:
                if bot.greet(user_response) is not None:
                    return bot.greet(user_response)
                else:
                    bot.sentence_tokens.append(user_response)
                    bot.word_tokens += nltk.word_tokenize(user_response)
                    final_words = list(set(bot.word_tokens))
                    return bot.response(user_response)
        else:
            flag = False
            return "Goodbye"


# Build our UI.
st.set_page_config(page_title="FAQs Chatbot", page_icon="robot.png")
if "chat_history" not in st.session_state:
    st.session_state.chat_history = ["I'm a simple retrieval bot, how can I help U?"]

st.header("FAQs Chatbot")
st.write(css, unsafe_allow_html=True)

# Render all messages.
for i in range(len(st.session_state.chat_history)):
    if i % 2 == 1:
        st.write(
            user_template.replace("{{MSG}}", st.session_state.chat_history[i]),
            unsafe_allow_html=True,
        )
    else:
        st.write(
            bot_template.replace("{{MSG}}", st.session_state.chat_history[i]),
            unsafe_allow_html=True,
        )

user_prompt = st.chat_input("Enter your prompt . . .")
if user_prompt is not None and user_prompt != "":
    # Get response from our bot.
    response = chat(bot, user_prompt)
    st.write(
        user_template.replace("{{MSG}}", user_prompt),
        unsafe_allow_html=True,
    )
    st.write(
        bot_template.replace("{{MSG}}", response),
        unsafe_allow_html=True,
    )
    st.session_state.chat_history.append(user_prompt)
    st.session_state.chat_history.append(response)
