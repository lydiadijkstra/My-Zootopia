My-Zootopia - README
This project, My-Zootopia, is a Python application that fetches animal data from an API based on user input, processes the data, and generates an HTML page displaying the information about the chosen animal.

Features
Fetch Animal Data: The application retrieves data about various animals from an API using a user-provided animal name or type.
Generate Dynamic HTML: Based on the retrieved data, an HTML file is generated to display the animal's characteristics, including diet, type, and location.
User-Friendly Interface: Prompts the user for an animal name or type and handles cases where the input is empty.
API Key Protection: The application uses dotenv to keep API keys secure.
Project Structure
bash
Code kopieren
.idea/
My-Zootopia/
__pycache__/
  └── data_fetcher.cpython-312.pyc
.DS_Store
.env
.gitignore
README.md
animals.html
animals_data.json
animals_template.html
animals_web_generator.py
data_fetcher.py
requirements.txt
Key Files
animals_template.html: HTML template containing a placeholder for animal information.
animals.html: Generated HTML file with specific animal data.
data_fetcher.py: Fetches animal data from the API using an API key stored in .env.
animals_web_generator.py: Contains the main code for handling user prompts, fetching animal data, processing it, and generating the final HTML.
Setup Instructions
Prerequisites
Python 3.x
Virtual Environment (recommended)
API key for API Ninjas (for animal data)
Installation
Clone the repository:

bash
Code kopieren
git clone <repository-url>
cd My-Zootopia
Install dependencies:

bash
Code kopieren
pip install -r requirements.txt
Set up API Key:

Create a .env file in the root directory.
Add your API key to the .env file:
makefile
Code kopieren
API_KEY=your_api_key_here
Running the Application
Run the main script:

bash
Code kopieren
python animals_web_generator.py
Enter an animal name or type when prompted.

View Generated HTML:

After running the script, an animals.html file will be generated in the root directory.
Open animals.html in a browser to view the animal details.
Code Explanation
Main Components
prompt_user_for_animal_choice: Prompts the user for an animal name or type and validates the input.
fetch_data: Retrieves animal data from the API based on the user's input. If the response status code indicates an error, it will display an error message.
read_animal_html: Loads the HTML template file.
create_str_for_html: Processes animal data into HTML format, including animal characteristics like diet, type, and location.
serialize_animal: Formats individual animal data entries into HTML elements.
replace_string_html: Replaces the placeholder in the HTML template with formatted animal data.
dump_data_to_html: Writes the final HTML content into animals.html.
API Key Protection
The .env file stores sensitive information (API Key) to keep it secure. The dotenv library loads this file, ensuring that the API key is never hardcoded in the codebase.

Example
bash
Code kopieren
Enter an animal name or type: fox
Website was successfully generated to the file animals.html.
Opening animals.html will display information about foxes, including diet, type, and location.

License
This project is open-source and licensed under the MIT License.

