try:
    fh = open("testfile","w")
    try:
        fh.write("File for exception handling")
    finally:
        print("FILE AKAN DITUTUP")
        fh.close()
except IOError:
    print("ERROR: CANNOT FIND THE FILE OR DATA")