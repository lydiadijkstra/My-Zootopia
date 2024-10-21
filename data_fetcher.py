import requests
import os
from dotenv import load_dotenv

# call the function from dotenv where the key is hidden
load_dotenv()

REQUEST_URL = 'https://api.api-ninjas.com/v1/animals?name={animal_name}'
API_KEY = os.getenv('API_KEY') # call the os-function to read the key


def fetch_data(animal_name):
    """
    Retrieve the data with help of the api
    :param animal_name: search-prompt
    :return: list of animals, each animal is a dict:
  {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
  },
    """
    response = requests.get(REQUEST_URL.format(animal_name=animal_name), headers={'X-Api-Key': API_KEY})
    res = response.json()
    if response.status_code != requests.codes.ok:
        print("Error:", response.status_code, response.text)
    return res
