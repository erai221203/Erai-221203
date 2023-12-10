for i in range(2, 3):
    for j in range(1, 11):
        if i==j:
            continue
        print(j, "*", i, "=", i*j)
    print()
