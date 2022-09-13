import requests
import json
from pprint import pprint
   ## pprint(vars(response))
from bs4 import BeautifulSoup
   
prodheaders = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}

## https://realpython.com/beautiful-soup-web-scraper-python/
## sources cited: https://www.freecodecamp.org/news/create-a-discord-bot-with-python/

SiteExamples = {1: "https://realpython.github.io/fake-jobs/jobs/senior-python-developer-0.html", 2: "https://www.bleepingcomputer.com", 3: "https://realpython.github.io/fake-jobs/"}


def get_site(userInput):
    response = requests.get(SiteExamples.get(userInput), prodheaders)
    print("\nrequests.get() returns a \033[95m %s \033[0m object, in this case an http response" % type(response))
    return(response)


def printobjattributes(dictinput):
    #pprint(vars(input))
    try:
        for key in dictinput:
            print("\n")
            print(key, '->', dictinput[key])
    except:
        print("something went wrong.... printing normally")
        pprint(vars(dictinput))
    
#def getHeaders()
    
    
def main():
    while True:
        userchoice = input("\nPress \n[1] for a confirmed site \n[2] for a target\n[3] for detailed\n")
        userchoice = int(userchoice)
        
        scrapedcontent = get_site(userchoice)
        
        #### Print the attributes and features of this scraped content
        printobjattributes(scrapedcontent)
        
        content = scrapedcontent.content
        headers = scrapedcontent.headers
        text = scrapedcontent.text
#        print("\nheaders is as follows: ", headers)
#        print("\ncontent is as follows: \n", content)
        print("\n")
        for i in headers:
            print("%s key wields ---> \033[95m %s \033[0m" % (i, headers[i]))
#            print(i, '->', headers[i])
        
        print("\n\nPrinting Page Content with HTML\n")
        
        
        print(str(content.decode("utf-8")))
        
#        print("-------------------------------------------------------text")
#        print(text)

        print("\n---------------------------------------------------------------------------------------------------------- \nStarting Beautiful Soup Part\n---------------------------------------------------------------------------------------------------------- \n")
        soup = BeautifulSoup(content, "html.parser")
#        print(soup.prettify())
        
        
#        print(text)
        stuff = soup.find_all("div")
        
        stuff = soup.find_all("div", class_="bc_latest_news")
        print(stuff)
            
            ####now to identify specific content
#        try:
#
#            job_elements = results.find_all("div", class_="container")
#            for job_element in job_elements:
#                print(job_element, end="\n"*2)
#
#            for job_element in job_elements:
#                title_element = job_element.find("h2", class_="title")
#                company_element = job_element.find("h3", class_="company")
#                location_element = job_element.find("p", class_="location")
#                print(title_element.text.strip())
#                print(company_element.text.strip())
#                print(location_element.text.strip())
#                print()
#
#
#
#
#
#        except:
#            print("prettify didn't work")
#            print("\n---------------------------------------------------------------------------------------------------------- \nText\n---------------------------------------------------------------------------------------------------------- \n")
#            print(text)
#
    
      

if __name__ == "__main__":
    main()
