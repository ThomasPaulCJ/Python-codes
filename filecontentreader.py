import string
def count_characters(text):
    num_words=len(text.split())
    num_sentences=text.count('.')+text.count('?')+text.count('!')
    num_upper=sum(1 for c in text if c.isupper())
    num_lower=sum(1 for c in text if c.islower())
    num_digits=sum(1 for c in text if c.isdigit())  
    num_specials=sum(1 for c in text if c in string.punctuation)

    return num_words,num_sentences,num_upper,num_lower,num_digits,num_specials

def main():
    filename=input("Enter the filename: ")

    try:
        with open(filename,'r') as file:
            text=file.read()
            num_words,num_sentences,num_upper,num_lower,num_digits,num_specials=count_characters(text)
            print(f"Number of words : {num_words}")
            print(f"Number of sentences : {num_sentences}")
            print(f"Number of uppercase characters : {num_upper}")
            print(f"Number of lowercase characters : {num_lower}")
            print(f"Number of digits : {num_digits}")
            print(f"Number of special characters : {num_specials}")

    except FileNotFoundError:
        print(f"File {filename} not found") 
        
if __name__ == "__main__":
    main()