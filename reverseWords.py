def reverseWords(input):
    wordsList = input.split(" ")
    wordsList = wordsList[-1::-1]
    newWords = " ".join(wordsList)
    return newWords

if __name__ == "__main__":
    input = "Hello Are you OK ?"
    input = reverseWords(input)
    print(input)