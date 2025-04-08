from platform import system

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
information = """
Sultan Khan (Punjabi and Urdu: میاں سلطان خان, 1903 – 25 April 1966; often given the erroneous honorific Mir Sultan Khan or Mir Malik Sultan Khan[1]) was a chess player from British India,[2][3][4] and later a citizen of Pakistan, who was the strongest Asian player of the early 1930s. The son of a Muslim landlord and preacher, Khan travelled with Colonel Nawab Sir Umar Hayat Khan (Sir Umar), to Britain, where he took the chess world by storm. In an international chess career of less than five years (1929–33), he won the British Championship three times in four attempts (1929, 1932, 1933), and had tournament and match results that placed him among the top ten players in the world. Sir Umar then brought him back to his homeland, where he gave up chess and returned to cultivate his ancestral farmlands in the area which became Pakistan. He lived there before dying in his sixties in the city of Sargodha. David Hooper and Kenneth Whyld have called him "perhaps the greatest natural player of modern times".[5] In 2024 FIDE posthumously awarded him the title of Honorary Grandmaster.[6]
"""
if __name__ == "__main__":
    system_prompt = """
    given the information {information} about a person from I want you to create:
    1. a short summary of the information
    2. two interesting facts about the them
    """
    prompt_template = PromptTemplate(
        input_variables=["information"], template=system_prompt
    )

    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)

    chain = prompt_template | llm

    result = chain.invoke(input={"information": information})
    print(result.content)
