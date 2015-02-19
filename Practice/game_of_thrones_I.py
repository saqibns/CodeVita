ANSWER = {True : "YES", False : "NO"}
def main():
    string = raw_input()
    print ANSWER[check(string)]

def check(string):
    #If every character has an even length and at most one character has odd
    #length, then an anagrom of that string will be a palindrome

    #Find out all the characters and stuff them into a dictionary
    char_map = dict()
    for char in string:
        char_map[char] = 0

    #Find the frequency of each character
    for char in string:
        char_map[char] += 1

    #Finally see if more than one character has even occurences
    odd_exists = False
    for char in char_map:
        if char_map[char] % 2 == 1:
            if not odd_exists:
                odd_exists = True
            else:
                return False
    return True

##print check("saqibnizamshamsi")
##print check("aaabbbb")
##print check("cdefghmnopqrstuvw")
##print check("cdcdcdcdeeeef")
main()