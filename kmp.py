def word_simple(letter, uppercased):     #function to check whether a single letter in a word is uppercase and return the uppercased letter
    if letter == letter.upper() and letter != "-":
        uppercased += letter
    return uppercased

simple_word = ""
long_word = input("The names: ")     #inputting the word
for i in range(len(long_word)):     #loop to filter the word to uppercase letters only
    simple_word = word_simple(long_word[i], simple_word)
print(simple_word)     #output the uppercase letter only
