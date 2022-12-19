try:
    fh = open("testfile","w")
    fh.write("File for exception handling")

except IOError:
    print("Error: cannot find file or read data")

else:
    print("Konten berhasil di-write")
    fh.close()