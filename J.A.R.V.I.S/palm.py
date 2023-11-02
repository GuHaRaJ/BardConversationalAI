def palmtext(query):    
    import google.generativeai as palm
    from Speak import Speak

    palm.configure(api_key='')#insert the api key from bard..
    models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
    model = models[0].name
    prompt = query
    completion = palm.generate_text(
    model=model,
    prompt=prompt,
    temperature=1.0,
    # The maximum length of the response
    max_output_tokens=60,
    )
    Speak(completion.result)







