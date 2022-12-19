def semordnilap(words):
    # Because the reverse order needs to be a different word by definition, converting the array to a set will remove duplicate strings
    set(words)
    result = []
    for word in words:
        # Need to slice the word in reverse order and check if the new word is in the set
        # Need to take care of the edge case where the reverse word is the same as the original word
        if word[::-1] in words and word[::-1] != word:
            result.append([word, word[::-1]])
            words.remove(word)
    return result