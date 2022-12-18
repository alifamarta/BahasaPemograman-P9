try:
    fh = open("testfile","w")
    fh.write("Hello :)")
finally:
    print("ERROR: CANNOT FIND FILE OR DATA")