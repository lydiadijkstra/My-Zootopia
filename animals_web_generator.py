from data_fetcher import fetch_data


def read_animal_html(html_file_path):
    """
    Loads the html-file
    :param html_file_path: animals_template.html
    :return: data from html_file
    """
    with open(html_file_path, "r", encoding="utf-8") as fileobject:
        return fileobject.read()


def prompt_user_for_animal_choice():
    """
    Prompt user for a type or name of an animal
    :return: user choice for animal name or type
    """
    while True:
        animal_prompt = input("Enter an animal name or type: ")
        # If no name or type is entered, try again
        if animal_prompt == "":
            print("No input detected. Please enter an animal name or type!")
            continue
        print("Website was successfully generated to the file animals.html.")
        return animal_prompt


def create_str_for_html(data):
    """
    Creates the new text for the html-file with the animal data
    Redirects to the serialization function
    :param data: animal data from the website
    :return: string for the new html-file
    """
    output = ''
    for animal_data in data:
        output += serialize_animal(animal_data)
    return output


def serialize_animal(animal_data):
    """
    Serialize the animal data for usage in html
    :param animal_data: retrieved data from api
    :return: diet, type and location of the chosen animal
    """
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
    """
    Replaces the placeholder text and returns the new string
    :param html_content: the html-content which will be updated with string
    :param output: string which will be shown on generated website
    :return: new content for generating animal website
    """
    if len(output) >= 1:
        new_html_content = html_content.replace("__REPLACE_ANIMALS_INFO__", output)
    else:
        new_html_content = html_content.replace("__REPLACE_ANIMALS_INFO__", "No animal of this type was found")
    return new_html_content


def dump_data_to_html(new_html_content):
    """
    Dumps the new string in a new created html-file, after this the generated website shows chosen animal data
    :param new_html_content: new content which will be shown
    """
    with open("animals.html", "w", encoding="utf-8") as fileobj:
        fileobj.write(new_html_content)


def main():
    """
    Main function to run the programm, calls the functions to run the website with animal data
    """
    animal_name = prompt_user_for_animal_choice()
    animals_data = fetch_data(animal_name)
    html_content = read_animal_html('animals_template.html')
    output = create_str_for_html(animals_data)
    new_html_content = replace_string_html(html_content, output)
    dump_data_to_html(new_html_content)


if __name__ == "__main__":
    main()
