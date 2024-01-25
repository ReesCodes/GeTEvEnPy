# This is a terible Idea

outFile = open("getEven.py","w")
outFile.write("import sys\n")
outFile.write("def getEven(a):\n" +
              "\t return")
for i in range(10000):
    outFile.write(f" \"{'even' if(i%2==0) else 'odd'}\" if (a == {i}) else ")
outFile.write('\"Unknown"\n')
outFile.writelines(["if __name__ == \"__main__\":\n", "\tfor arg in sys.argv[1:]:\n", "\t\tprint(f\"{arg}: is {getEven(int(arg))}\")\n"])
outFile.close()