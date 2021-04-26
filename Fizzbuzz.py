checks = { 3 : "Fizz", 5 : "Buzz"}

times = 100

for i in range(1,times+1):
    output = ""

    for l in checks.keys():
        if (i%l == 0) : output += checks[l]

    if (output == "") : output = i

    print(output)