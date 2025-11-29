

def count_element(words):

    counts = {}
    count = 0
    # for i in range(len(words)):
    #     if words[i] in counts: # check if the specific elements existing in counts, then increment counts
    #          counts[words[i]] += 1
    #     else:
    #          counts[words[i]] = 1 # else just add it in counts dictionary
    #
    # return counts

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



words = ["apple", "apple", "apple", "orange", "banana"]
count_occurence = count_element(words)
print(count_occurence)

