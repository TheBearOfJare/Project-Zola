key = "your key"

import time
import google.generativeai as genai

genai.configure(api_key=key)
model = genai.GenerativeModel('gemini-pro')
config = genai.types.GenerationConfig(

    max_output_tokens=250
)
safety = {'HARASSMENT':'block_none','HATE_SPEECH':'block_none','SEXUALLY_EXPLICIT':'block_none'}
chat = model.start_chat(history=[])

# first message

prompt = input()

response = chat.send_message("Respond to messages with an occasional dry sense of humor. Responses should still be correct, but no longer than a paragraph if possible." + prompt, stream=True, generation_config=config, safety_settings=safety)

print("\n")

for chunk in response:
    for char in chunk.text:
            
        print(char, end="")

        time.sleep(0.04)

print("\n\n")

# conversation loop
while True:

    prompt = input()
    
    response = chat.send_message(prompt, stream=True, generation_config=config, safety_settings=safety)

    print("\n")
    
    for chunk in response:
        for char in chunk.text:
                
            print(char, end="")

            time.sleep(0.04)

    print("\n\n")
