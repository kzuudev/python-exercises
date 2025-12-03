

def count_element(words):

    counts = {}

    for i in range(len(words)):
        count = 0  # reset count for each new word
        for j in range(len(words)):
            if words[i] == words[j]:
                count += 1
                print(f"Element at index {i} ({words[i]}) is equal to element at index {j} ({words[j]})")
            else:
                print(f"Element at index {i} ({words[i]}) is not equal to element at index {j} ({words[j]})")

        counts[words[i]] = count


    return counts



words = ["apple", "apple", "apple", "orange", "banana", "grapes"]
count_occurence = count_element(words)
print(count_occurence)

