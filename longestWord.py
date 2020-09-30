# Daniel Ham
# Longest Word

# Function to find longest word and word count of message
def longestWord(message):

    wordList = message.split(" ")

    longestWord = ""
    wordCount = 0

    for word in wordList:
        if len(word) > len(longestWord):
            longestWord = word
        wordCount += 1

    print("That message had", wordCount, "words.\nThe longest word was:",longestWord)






# Main

# Get input of message from user
string = input("Please enter a message: ")
# Call function to return result
longestWord(string)
