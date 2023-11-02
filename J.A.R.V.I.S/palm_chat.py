
def palmchat(query):
    import google.generativeai as palm
    from Speak import Speak

    palm.configure(api_key='')#insert the api key from bard..
    reply = palm.chat(context="You are the AI Jarvis from the movie Iron Man.The user is Tony Stark.Give responses in a simple and esay manner.Be smart while replying",
    temperature=0.3 ,messages=query)
    Speak(reply.last)





