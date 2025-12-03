# Given a list of words, return only unique ones (no duplicates).


def unique_words(words):
    counts = {}
    count = 0

    for word in words:
        if word in counts:
            count += 1
            counts[word] = count
        else:
            count = 1
            counts[word] = count

        if counts[word] == 1:
            print(word)


    return counts


words = ["apple", "banana", "orange", "apple", "grape", "banana", "kiwi"]
unique_words(words)
