# Combine two dictionaries into one.

def combine_dicts():

    dict1 = {
        "first_name": "John Kevin",
        "last_name": "Dela Cruz"
    }

    dict2 = {
        "gender": "Male",
        "age": 23
    }

    # Using the union operator
    dictionaries_union = dict1 | dict2
    print(dictionaries_union)

    # Using the Unpacking Operator
    dictionaries_unpacking = {**dict1, **dict2}
    print(dictionaries_unpacking)

    return dictionaries_union, dictionaries_unpacking



combine_dicts()