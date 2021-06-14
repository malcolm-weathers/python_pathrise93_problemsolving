# Retrieve words from a dictionary that are made up of a subsequence of
# characters in an input string. Given input "ABAT", matching words may
# include "BAT" and "TAB" while non-matching words may be "BART" or "BAR".

# Break a word down into a list of characters and the number of times they
# occur.
def dtfy(word):
    chars = {}
    for char in word:
        if not char in chars:
            chars[char] = 1
        else:
            chars[char] += 1
    return chars

# Do the same for the dictionary. Remove any word containing a character not
# in the sequence or which contains more of a character than contained in the
# sequence (e.g. has five As when the sequence has three).
def match(dct, word):
    chars = dtfy(word)
    ans = []
    for w in dct:
        is_valid = True
        wchars = dtfy(w)
        for char in wchars:
            if not char in chars or wchars[char] > chars[char]:
                is_valid = False
                break
        if is_valid:
            ans.append(w)
    
    return ans

def main():
    dct = ['bat', 'tab', 'bart', 'bar']
    print(match(dct, 'abat'))

if __name__ == '__main__':
    main()
