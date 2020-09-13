def main():
    #f= open("values.txt","w+")
    f=open("values.txt","a+")
    for i in range(10):
         f.write("appended line %d\r\n" % (i+1))
    f.close()
    #Open the file back and read the contents
    #f=open("values.txt", "r")
    #if f.mode == 'r':
    #   contents =f.read()
    #    print (contents)
    #or, readlines reads the individual line into a list
    #fl =f.readlines()
    #for x in fl:
    #print(x)
if __name__== "__main__":
  main()
