def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    lower_text = text.lower()
    character_dict = {}
    for character in lower_text:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict

def get_sorted_character_dict(unsorted_dict):
    list = []
    for key, value in unsorted_dict.items():
        list.append({"char": key, 'num': value})
    list.sort(reverse=True, key=lambda x: x['num'])

    return list
