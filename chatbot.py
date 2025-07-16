from transformers import pipeline

# Use a simple text generation model
chatbot = pipeline("text-generation", model="gpt2")

def get_response(user_input):
    response = chatbot(user_input, max_length=50, do_sample=True)[0]['generated_text']
    return response
