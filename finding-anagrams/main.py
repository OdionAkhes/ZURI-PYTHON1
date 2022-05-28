def find_anagrams(word, anagram):
    
    # convert both the strings into lowercase
    word = word.lower()
    anagram = anagram.lower()

    # check if length is same
    if(len(word) == len(anagram)):

        # sort the strings
        sorted_word = sorted(word)
        sorted_anagram = sorted(anagram)

        # if sorted strings are same
        if(sorted_word == sorted_anagram):
            # print(word, "and" , anagram , "are anagrams.")
            print(True)
        else:
            # print(word, "and" , anagram , "are not anagrams.")
            print(False)

    else:
        print(word, "and" , anagram , "are not of the same character length so they're not anagrams.")
        
    return True

find_anagrams("hello", "check")
find_anagrams("below", "elbow")
