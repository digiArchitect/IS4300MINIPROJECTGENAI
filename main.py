#These are my imports
import google.generativeai as genai
import os
genai.configure(api_key=os.environ["API_KEY"])

model = genai.GenerativeModel('gemini-pro')
#Define hello_world and have the ai generate a specific sentence
def hello_world():
  response = model.generate_content("In two sentences, give me your best response on how would you say hello to the world?")
  print(response.text)
#Call helloworld
hello_world();