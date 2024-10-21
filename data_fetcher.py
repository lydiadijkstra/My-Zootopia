import requests


REQUEST_URL = 'https://api.api-ninjas.com/v1/animals?name={animal_name}'
KEY = 'Cg1Tw9jXYOCcDG2gBeHm5w==3EUfQgz75QoslqDO'

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
    response = requests.get(REQUEST_URL.format(animal_name=animal_name), headers={'X-Api-Key': KEY})
    res = response.json()
    if response.status_code != requests.codes.ok:
        print("Error:", response.status_code, response.text)
    return res
