import os
import google.generativeai as palm

palm_api_key = os.environ.get("PALM_API_KEY")
palm.configure(api_key=palm_api_key)

defaults = {
  'model': 'models/chat-bison-001',
  'temperature': 0.25,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
}

context = ""
examples = []
messages = []
messages.append("NEXT REQUEST")
response = palm.chat(
  **defaults,
  context=context,
  examples=examples,
  messages=messages
)

while True:
  messages.append("NEXT REQUEST")
  response = palm.chat(
    **defaults,
    context=context,
    examples=examples,
    messages=messages
  )
  
  print(response.last) # Response of the AI to your most recent request

  # Get input from the user
  user_input = input()

  # Add the user input to the context
  context += user_input