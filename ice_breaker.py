from platform import system

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

from third_parties.linkedin import scrape_linkedin_profile

load_dotenv()
if __name__ == "__main__":
    system_prompt = """
    given the linkedin information {information} about a person from I want you to create:
    1. a short summary of the information
    2. two interesting facts about the them
    """
    prompt_template = PromptTemplate(
        input_variables=["information"], template=system_prompt
    )

    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)

    chain = prompt_template | llm | StrOutputParser()
    linkedin_data=scrape_linkedin_profile("https://www.linkedin.com/in/ali-mahmoodi-tabriz/", mock=True)
    result = chain.invoke(input={"information": linkedin_data})
    print(result)
