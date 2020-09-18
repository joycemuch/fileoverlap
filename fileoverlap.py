#file overlap program

#method for parsing
def parse():
     import requests
     from bs4 import BeautifulSoup
     url = input("enter the url: ")
     prime = requests.get(url).text
     return( prime)

#writng data into a file
def main():
    prime = parse()
    filename = input("enter the name of the text file you want to save to : ")
    with open(filename  , 'w') as f:
            files = f.write(prime)
    print(files)


#fetching data from a file

def readData(text):
    listNum = []
    with open(text) as r:
        line = r.readline()
        while line:
            listNum.append(int(line))
            line = r.readline()      
    return listNum
        
if __name__=='__main__':
     #method used to download url content and  saving in the files
     main()

     #examples
     primenumbers = readData("prime.txt")
     happynumbers = readData("happy.txt")
    
     overlap =[element for element in primenumbers if element in happynumbers]
     print(overlap)

