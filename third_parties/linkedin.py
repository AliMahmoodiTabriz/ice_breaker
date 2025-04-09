import os
from http.client import responses

import requests
from dotenv import load_dotenv

load_dotenv()


def scrape_linkedin_profile(linkdine_profile_url: str, mock: bool = False):
    """
    scarpe the information from the linkedin profile,
    Manully scrape the information from the linkedin profile
    """
    if mock:
        linkdine_profile_url = "https://gist.githubusercontent.com/AliMahmoodiTabriz/5e7211bf64f98d3e0ca6f4c73b601ec2/raw/29fe63a130173af9e36975bfd95678715ba0dfe5/Ali_Mahmoodi_linkedin_Profile"
        responce = requests.get(linkdine_profile_url, timeout=10)
    else:
        api_endpoint = "https://api.scrapin.io/enrichment/profile"
        params = {
            "linkedInUrl": linkdine_profile_url,
            "apikey": os.getenv("SCRAPIN_API_KEY"),
        }
        responce = requests.get(api_endpoint, params=params, timeout=10)
    result = responce.json().get("person")
    return result


if __name__ == "__main__":
    print(scrape_linkedin_profile("https://www.linkedin.com/in/ali-mahmoodi-tabriz/", mock=True))
