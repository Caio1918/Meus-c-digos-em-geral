def Hyperword():
    word = [".",".",".","."]

    for i in range(26):
        word[0] = chr(97 + i)
        print(word)
        for j in range(26):
            word[1] = chr(97 + j)
            print(word)
            for k in range(26):
                word[2] = chr(97 + k)
                print(word)
                for l in range(26):
                    word[3] = chr(97 + l)
                    print(word)
    
    return word

print(Hyperword())