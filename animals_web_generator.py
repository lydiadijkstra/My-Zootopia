import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def display_animal_data(animals_data):
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


def main():
    animals_data = load_data('animals_data.json')

    display_animal_data(animals_data)


if __name__ == "__main__":
    main()