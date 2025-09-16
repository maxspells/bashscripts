def foo(string):
    index = 0
    top_length = 0
    currest_best = []
    while index <= len(string) - 1:
        letterlist = []
        current_string = string[index:]
        for letter in current_string:
            if letter not in letterlist:
                letterlist.append(letter)
        if len(letterlist) > top_length:
            top_length = len(letterlist)
            current_best = letterlist
            index +=1
            letterlist.pop(0)
    print(f"Current best match = {current_best} length = {top_length}")
