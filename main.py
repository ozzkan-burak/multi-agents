from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.messages import HumanMessage
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

#llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
general_model = init_chat_model(
  "gemini-2.5-flash",
  model_provider="google_genai",
  temperature=0.5,
  max_tokens=4000
)

#result = general_model.invoke("Merhaba nasılsın, kimsin sen.")
repsonse = general_model.batch(
  [
    [HumanMessage(content="2+2 nedir?")],
    [HumanMessage(content="5*235 nedir?")]
  ]
)

for res in repsonse:
  print(res.content)
