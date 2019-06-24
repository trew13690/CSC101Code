

def main():
    print("This program creates a file of usernames from a ")
    print("fiel of names.")

    infileName= input("What file are the names in?")
    outfileName = input("What file shoud the username go in?")

    infile = open(infileName, "r")
    outfile = open(outfileName, "w")

    for line in infile:
        first, last = line.split()
        uname = (first[0]+ last[:7]).lower()
        print(uname, file=outfile)

    infile.close()
    outfile.close()

    print("Usernames have been written to", outfileName)

main()