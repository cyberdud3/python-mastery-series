def solve(s):
    for x in s[:].split():
        s = s.replace(x, x.capitalize())
    return s


result = solve("abhijith sudhakar")
print(result)
