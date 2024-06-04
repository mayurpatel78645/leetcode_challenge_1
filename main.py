word1 = "abcd"
word2 = "pqrs"


def merge_alternating_words(word1, word2):
    wordx = list(word1)
    wordy = list(word2)
    merged_word = []
    total_length = len(wordx) + len(wordy)
    for _ in range(total_length):
        if len(wordx) > 0:
            merged_word.append(wordx.pop(0))
        if len(wordy) > 0:
            merged_word.append(wordy.pop(0))
    return "".join(merged_word)


print(merge_alternating_words(word1, word2))
