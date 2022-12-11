def whos_the_winner(s, p):

    # Function to return the index of first occurrence of p
    def find_p(s, p):
        for i in range(len(s)):
            if i + len(p) > len(s):
                break
            if s[i:i+len(p)] == p:
                return i
        return -1

    if len(p) == 0:
        return "Walter"

    # Check if p is in the string s
    if p in s:
        # Check if the substring p is at the start of at the end of the string s
        # if yes then Veidt wins everytime
        if find_p(s, p) in [0, len(s) - len(p)]:
            return "Veidt"
        else:
            # Else if the left side of the substring p is equal to the right side of substring p then and only then
            # Walter wins
            if len(s[0:find_p(s, p)]) == len(s[find_p(s, p) + len(p): len(s)]):
                return "Walter"
    return "Veidt"


print(whos_the_winner("xyzaaacbcxyzaaacbc", "aaa"))
