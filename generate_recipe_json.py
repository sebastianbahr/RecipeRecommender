import os
import json

def clean_text(text, type_):
    if type_ == 1:
        if type(text) is not list:
            text = text.replace('\n\n', '')
            text = text.replace('\n', '')
            text = text.replace('\\', '')
            text = text.replace('"', '')
            text = text.lstrip()
            text = text.rstrip()
        else:
            text = text
    elif type_ == 2:
        if type(text) is not list:
            text = text.replace('\n\n', ' ')
            text = text.replace('\n', ' ')
            text = text.replace('\\', ' ')
            text = text.lstrip()
            text = text.rstrip()
        else:
            text = text

    return text


def get_recipe_infos(recipe):
    data = recipe.split("---")[1]
    description = recipe.split("---")[2].replace("  ", " ").replace("   ", " ")
    data_order = [x for x in data.split() if x in ["title:", "date:", "tags:", "author:"]]

    data_dict = {}
    for i in range(1, len(data_order)):
        data_dict[data_order[i-1].replace(":", "")] = clean_text(data.split(data_order[i-1])[1].split(data_order[i])[0], 1)

    data_dict[data_order[i].replace(":", "")] = clean_text(data.split(data_order[i-1])[1].split(data_order[i])[1], 1)
    
    data_dict["tags"] = [x.replace("'", "").lstrip().rstrip() for x in data_dict.get("tags").strip('][').split(',')]
    data_dict

    introduction = clean_text(description.split("## Ingredients")[0], 2)
    ingredients = clean_text(description.split("## Ingredients")[1].split("## Directions")[0], 2)
    if "Originally published" in description:
        directions = clean_text(description.split("## Ingredients")[1].split("## Directions")[1].split("Originally published")[0], 2)
    else:
        directions = clean_text(description.split("## Ingredients")[1].split("## Directions")[1], 2)

    return {"title": data_dict.get("title"),
            "date": data_dict.get("date"),
            "tags": data_dict.get("tags"),
            "introduction": introduction,
            "ingredients": ingredients,
            "direction": directions}


dir = "/Users/sebastian/Documents/public-domain-recipes/"
paths = os.listdir(dir + "content/")
recipes_texts = []

for path in paths:
    if path != "_index.md":
        with open(dir + "content/" + path) as file:
            recipe = file.read()

        recipe_text = get_recipe_infos(recipe)

        for key in list(recipe_text.keys()):
            value = recipe_text.get(key)
            recipe_text[key] = value

        recipe_text['output'] = {'title': recipe_text.get("title"),
                                'ingredients': recipe_text.get("ingredients"),
                                'direction': recipe_text.get('direction')}

        recipes_texts.append(recipe_text)


with open ("/Users/sebastian/Documents/RecipeRecommender/recipes_v1.json", "w", encoding="utf8") as json_file:
    json_file.write(json.dumps(recipes_texts, ensure_ascii=False))