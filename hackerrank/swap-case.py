def swap_case(s):
    a = []
    for i in range(len(s)):
        if s[i].isupper():
            a.append(s[i].lower())
        else:
            a.append(s[i].upper())
    s = ''.join(str(i) for i in a)
    return s


result = swap_case("Www.HackerRank.com")
print(result)
