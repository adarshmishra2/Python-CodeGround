def main():
    text=input("enter words:")
    longest=0

    for word in text.split(','):
        if len(word)>longest:
            longest=len(word)
            longest_word=word


    print(longest_word,len(longest_word))


main()
