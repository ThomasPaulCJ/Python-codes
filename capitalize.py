def capitalize_words(string):
    words = string.split()
    capitalized_words = []
    
    for word in words:
        if len(word) > 1:
            capitalized_word = word[0].upper() + word[1:-1] + word[-1].upper()
        else:
            capitalized_word = word.upper()
        capitalized_words.append(capitalized_word)
    
    return ' '.join(capitalized_words)

# Example usage
input_string = input("enter a string : ")
output_string = capitalize_words(input_string)
print(output_string)