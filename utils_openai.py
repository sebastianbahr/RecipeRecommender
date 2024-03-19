def authenticate():
    with open("OpenAI_API_KEY.txt", "r") as f:
        API_KEY = f.read()
    return API_KEY