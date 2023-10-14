def func12(lst, reg):
    lst1 = []
    for i in lst:
        if reg == "lower":
            lst1.append(i.lower())
        elif reg == "upper":
            lst1.append(i.upper())
    return lst1

print(func12(["HeLLO", "world",], "upper"))
