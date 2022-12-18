def level(level):
    if level < 1 :
        raise Exception("Invalid level ! ",level)

print(level(0))