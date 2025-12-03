

def count_vowels(string):

    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    counts = {}

    list_of_vowels = []
    list_of_consonants = []

    # for i in range(len(vowels)):
    #     count = 0
    #     for j in range(len(string)):
    #         if string[j] == vowels[i]:
    #             print(f"The word {string[j]} is a vowel")
    #             list_of_vowels.append(string[j])
    #             count += 1
    #             counts[string[j]] = counts.get(string[j], 0) + 1
    #             break
    #         else:
    #             print(f"The word {string[j]} is a consonant")
    #             list_of_consonants.append(string[j])

    for char in string:
        count = 0
        if char in vowels:
             print(f"The word {char} is a vowel")
             list_of_vowels.append(char)
             count += 1
             counts[char] = counts.get(char, 0) + 1
        else:
            print(f"The word {char} is a consonant")
            list_of_consonants.append(char)



    return counts



alphabet_lower = "abcdefghijklmnopqrstuvwxyz"

print(count_vowels(alphabet_lower))


