def reverse(input, output):
    with open(input, 'rb') as inp, open(output, 'wb') as out:
        out.write(inp.read()[::-1])

reverse("in.dat", "out.dat")