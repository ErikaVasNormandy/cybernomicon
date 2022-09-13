### This is the most minimal example of a scraper in pure python
#### sources cited: https://www.freecodecamp.org/news/create-a-discord-bot-with-python/

#############################################################################
# 0. Import Libraries for Scraping
#############################################################################
import requests
import json


#############################################################################
# 1. Define Function for Scraping
#############################################################################
def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)
    ############# requests library gets content from a site like zenquotes.io
    ############# [requests object].text is a str object ( type(response.text))
    

#############################################################################
# 2. Run the Function in main():
#############################################################################
def main():
    print(get_quote())
    
    
#############################################################################
# 3. Call Main():
#############################################################################
if __name__ == "__main__":
    main()
