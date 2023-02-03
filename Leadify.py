import requests
import bs4 as BeautifulSoup
import sys
import random, time
colors = [36, 32, 34, 35, 31, 37]
clear = '\x1b[0m'

logo = '''
-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-

██╗░░░░░ ███████╗ ░█████╗░ ██████╗░ ██╗ ███████╗ ██╗░░░██╗
██║░░░░░ ██╔════╝ ██╔══██╗ ██╔══██╗ ██║ ██╔════╝ ╚██╗░██╔╝
██║░░░░░ █████╗░░ ███████║ ██║░░██║ ██║ █████╗░░ ░╚████╔╝░
██║░░░░░ ██╔══╝░░ ██╔══██║ ██║░░██║ ██║ ██╔══╝░░ ░░╚██╔╝░░
███████╗ ███████╗ ██║░░██║ ██████╔╝ ██║ ██║░░░░░ ░░░██║░░░
╚══════╝ ╚══════╝ ╚═╝░░╚═╝ ╚═════╝░ ╚═╝ ╚═╝░░░░░ ░░░╚═╝░░░

-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-
'''

for N, line in enumerate(logo.split('\n')):
    sys.stdout.write(' \x1b[1;%dm%s%s\n ' % (random.choice(colors), line, clear))
    time.sleep(0.06)

def GetNums(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    products = soup.select('div.info')
    print("Found!!")
    print("-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-")
    for product in products:
        reviews = product.select('div.phone')[0].text
        print(reviews)

        with open('Numbers Scrapped.txt', 'a+') as outFile:
            writer = outFile.writelines("\n" + reviews)


def rmDups():
    linesSeen = set()
    with open("Numbers Scrapped.txt", 'r+') as f:
        d = f.readlines()
        f.seek(0)
        for unique in d:
            if unique not in linesSeen:
                f.write(unique)
                linesSeen.add(unique)
        f.truncate()

usrInput = input("[+] Which profession people to search for : ")
city = input("[+] Enter Target city : ")
print("==> Searching.....")
print("-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-҉҉-")
for i in range(11):
    link = "https://www.yellowpages.com/search?search_terms=" + usrInput + "&geo_location_terms=" + city + "&page=" + str(i)
    extract = GetNums(link)

dupsRmvd = rmDups()
print("Done Extracting! :)")
input("Enter any key to exit!")
