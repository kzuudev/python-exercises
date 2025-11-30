

def remove_duplicates(string):

    new_string = ""

    for i in range(len(string)):
       if string[i] not in new_string:
           new_string += string[i]
        # else do nothing and just skip duplicates

    return new_string


word = "kevinjohnburat"


print(remove_duplicates(word))