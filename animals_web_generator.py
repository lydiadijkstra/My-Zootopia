import json
import requests


REQUEST_URL = 'https://api.api-ninjas.com/v1/animals?name={animal_name}'
KEY = 'Cg1Tw9jXYOCcDG2gBeHm5w==3EUfQgz75QoslqDO'


# def load_data(file_path):
#     """ Loads a JSON file """
#     with open(file_path, "r", encoding="utf-8") as handle:
#         return json.load(handle)


def load_data(animal_name):
    response = requests.get(REQUEST_URL.format(animal_name=animal_name), headers={'X-Api-Key': KEY})
    res = response.json()
    if response.status_code != requests.codes.ok:
        print("Error:", response.status_code, response.text)
    return res


def read_animal_html(html_file_path):
    """ Loads a html-file """
    with open(html_file_path, "r", encoding="utf-8") as fileobject:
        return fileobject.read()


def prompt_user_for_animal_choice():
    animal_prompt = input("Enter an animal name or type: ")
    return animal_prompt


def create_str_for_html(data):
    """ creates the new text for the html-file """
    output = ''
    for animal_data in data:
        output += serialize_animal(animal_data)
    return output


def serialize_animal(animal_data):
    """ serialize the animal data for usage in html """
    output = ''
    diet = animal_data['characteristics'].get('diet')
    fox_type = animal_data['characteristics'].get('type')
    location = animal_data['locations'][0]

    output += "<li class='cards__item'>"
    output += f"<div class='card__title'> {animal_data['name']}</div>\n"
    output += "<p class='card__text'>"
    if diet:
        output += f"<div><strong>Diet:</strong> {animal_data['characteristics']['diet']}</div>\n"
    if location:
        output += f"<div><strong>Location:</strong> {animal_data['locations'][0]}</div>\n"
    if fox_type:
        output += f"<div><strong>Type:</strong> {animal_data['characteristics']['type']}</div>\n"
    output += '</p>'
    output += '</li>'

    return output


def replace_string_html(html_content, output):
    """ replaces the placeholder text and returns the new string """
    new_html_content = html_content.replace("__REPLACE_ANIMALS_INFO__", output)
    return new_html_content


def dump_data_to_html(new_html_content):
    """ dumps the new string in a new created html-file """
    with open("animals.html", "w", encoding="utf-8") as fileobj:
        fileobj.write(new_html_content)


def main():
    """ the functions are called here """
    #animals_data = load_data('animals_data.json')
    animal_name = prompt_user_for_animal_choice()
    animals_data = load_data(animal_name)
    html_content = read_animal_html('animals_template.html')
    output = create_str_for_html(animals_data)
    new_html_content = replace_string_html(html_content, output)
    dump_data_to_html(new_html_content)


if __name__ == "__main__":
    main()



"""
import requests


REQUEST_URL = 'https://api.api-ninjas.com/v1/animals?name={animal_name}'
KEY = 'Cg1Tw9jXYOCcDG2gBeHm5w==3EUfQgz75QoslqDO'


def retrieve_data(animal_name):
    response = requests.get(REQUEST_URL.format(animal_name=animal_name), headers={'X-Api-Key': KEY})
    res = response.json()
    if response.status_code == requests.codes.ok:
        print(res)
    else:
        print("Error:", response.status_code, response.text)
    return res


def show_data(animal_data):
    for animal_information in animal_data:
        print(f"{animal_information["name"]}, scientific name: {animal_information["taxonomy"]["scientific_name"]}")


def main():
    animal_name = "fox"
    animals_data = retrieve_data(animal_name)
    show_data(animals_data)

if __name__ == "__main__":
    main()


"""