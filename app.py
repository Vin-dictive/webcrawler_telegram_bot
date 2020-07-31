import pymongo

myclient = pymongo.MongoClient("<mongo server address>")
mydb = myclient["<database>"]
mycol = mydb["<collections>"]

x = mycol.find_one()

def update_db(title,url):
    print(title,"=",url)
    if mycol.find({"url":url}).count() == 0 :
        print("Url Doesnt Exist")
        data = title+"\n"+url
        send_message(bot,data)
    mycol.update({"title":title},{"$set":{"title":title,"url":url}},upsert=True)    
    
import bs4, requests

def crawler():
    url = '<webpage to scan>'
    getPage = requests.get(url)
    getPage.raise_for_status()
    menu = bs4.BeautifulSoup(getPage.text, 'html.parser')
    #Inside the for loop define the type of Information and tags u wanna capture from the page
    for anchor in menu.findAll('a', href=True , class_="btn btn-light btn-small" , title=True):
        update_db(anchor['title'],anchor['href'])


my_bots_api = '<ur bots api>'
recievers_id = '<id to send message to>'
bot = "https://api.telegram.org/bot"+my_bots_api+"/sendMessage?chat_id="+recievers_id+"&text="

def send_message(bot,data):
    requests.get(bot+data)
    
import schedule
import time

print("Program is being scheduled")
schedule.every(1).minute.do(crawler)


while True:
    schedule.run_pending()
    time.sleep(1)
