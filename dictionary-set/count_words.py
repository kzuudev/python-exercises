# Count how many times each word appears in a paragraph.

def count_words(paragraph):

    counts =  {}
    words = paragraph.split()

    print(words)
    count = 0

    for word in words:
        # print(words)
        if word in counts:
            count += 1
            counts[word] = count
            print(counts[word])
        else:
            count = 1
            counts[word] = count


        # counts[word] = count
        # print(counts[word])

    return counts

paragraph = "Hello hello hello test test kevin"
count_words(paragraph.lower())



