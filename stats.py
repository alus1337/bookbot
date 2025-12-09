def words_in_string(string):
    return len(string.split())

def character_count(string):
    string = string.lower()
    char_dict = {}

    for i in range(len(string) - 1):
        if string[i] in char_dict:
            char_dict[string[i]] += 1
        else:
            char_dict[string[i]] = 1
    
    return char_dict

def sort_on(dict):
    return dict["num"]
    
def char_to_dict(char_dict):
    dict_list = []

    for i in char_dict:
        dict_list.append({"char": i, "num": char_dict[i]})

    dict_list.sort(reverse=True, key=sort_on)
    return dict_list