## just provide dictionary access
from UDlexPT import UDlexPT

def lexUI():
    print("Creating the lexicon...")
    lex = UDlexPT()
    print()
    while True:
        word = input("Enter the word your are looking for (empty to exit):\n")
        if (word == ""):
            break
        elif ((word.count(" ")+word.count("-")) == 0):
            ans = lex.sget(word)
            if (ans == []):
                print("this word does not appear in PortiLex")
            else:
                print()
                for a in ans:
                    print("- "+word+" as "+a[1])
                    print("-    lemma:  ", a[0])
                    print("-    morph:  ", a[2])
                    print("------------------------")
        else:
            print("this does not appear to be a single word")

lexUI()
