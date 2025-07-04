import json


def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def generate_html_string_from_json(animals_data):
    """
    take json data and transform into html code: information blocks for every animal in the database
    :param animals_data:
    :return: html-string "animal_info"
    """
    website_string = ""
    for animal_obj in animals_data:
        website_string += serialize_animal(animal_obj)
    return website_string


def serialize_animal(animal_obj):
    """
    take one dictionary from the original list from json and turn it into html
    """
    animal_info = ""
    animal_info += "<li class='cards__item'>"
    try:
        name = animal_obj['name']
        animal_info += f"<div class='card__title'> {name}</div>"
    except KeyError:
        pass
    animal_info += "<p class='card__text'>"
    try:
        diet = animal_obj['characteristics']['order']
        animal_info += f"<strong>Diet:</strong> {diet}<br/>\n"
    except KeyError:
        pass
    try:
        location = animal_obj['locations'][0]
        animal_info += f"<strong>Location:</strong> {location}<br/>\n"
    except KeyError:
        pass
    try:
        type = animal_obj['characteristics']['type']
        animal_info += f"<strong>Type:</strong> {type}<br/>\n"
    except KeyError:
        pass
    animal_info += "</p></li>"
    return animal_info


def main():
    animals_data = load_data('animals_data.json')
    website_string = generate_html_string_from_json(animals_data)

    with open ("animals_template.html", "r") as origin_file:
        html_skeleton = origin_file.read()
    with open("animals.html", "w") as newfile:
        newfile.write(html_skeleton.replace("__REPLACE_ANIMALS_INFO__", website_string))


if __name__ == "__main__":
    main()