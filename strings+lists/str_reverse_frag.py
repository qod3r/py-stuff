s = input()
s = s[::-1]

start = s.find("h")
end = s.find("h", start+1)

print(s[start+1:end])