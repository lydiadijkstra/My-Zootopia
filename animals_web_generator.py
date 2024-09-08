import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r", encoding="utf-8") as handle:
    return json.load(handle)


def read_animal_html(html_file_path):
    """ Loads a html-file """
    with open(html_file_path, "r", encoding="utf-8") as fileobject:
        return fileobject.read()


"""
def display_animal_data(animals_data):
    "" displays the animals, the diet, the habitat and the type ""
    for foxes in animals_data:
        fox = foxes.get('name', None).upper()
        diet = foxes['characteristics'].get('diet')
        fox_type = foxes['characteristics'].get('type')
        location = foxes['locations'][0]

        print(f"{fox}")
        if diet:
            print(f"  Diet: {diet}")
        if location:
            print(f"  Location: {location}")
        if fox_type:
            print(f"  Type: {fox_type}")
"""


def create_str_for_html(data):
    """ creates the new text for the html-file """
    output = ''
    for animal_data in data:
        diet = animal_data['characteristics'].get('diet')
        fox_type = animal_data['characteristics'].get('type')
        location = animal_data['locations'][0]

        output += '<li class="cards__item">'
        output += f"Name: {animal_data['name']}<br>\n"
        if diet:
            output += f"Diet: {animal_data['characteristics']['diet']}<br>\n"
        if location:
            output += f"Location: {animal_data['locations'][0]}<br>\n"
        if fox_type:
            output += f"Type: {animal_data['characteristics']['type']}<br>\n"
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
    animals_data = load_data('animals_data.json')
    #display_animal_data(animals_data)
    html_content = read_animal_html('animals_template.html')
    output = create_str_for_html(animals_data)
    new_html_content = replace_string_html(html_content, output)
    dump_data_to_html(new_html_content)


if __name__ == "__main__":
    main()
