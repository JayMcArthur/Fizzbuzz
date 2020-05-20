checks = { 3 : "fizz", 5 : "buzz"}
for i in range(1,101):
    output = ""

    for l in checks.keys():
        if (i%l == 0) : output += checks[l]

    if (output == "") : output = i

    print(output)