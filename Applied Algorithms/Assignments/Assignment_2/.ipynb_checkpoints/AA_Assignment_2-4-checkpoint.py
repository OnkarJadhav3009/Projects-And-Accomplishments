def return_resultant_string(s, p):
    # While the substring p is in s, loop
    if len(p) == 0:
        return s

    while p in s:
        # Get where the string is present and then concatenate the left and right parts of the string together
        for i in range(0, len(s)):
            if s[i:i+len(p)] == p:
                s = s[:i] + s[i+len(p):]
                break
    return s


print(return_resultant_string("aababccbc", "abc"))
