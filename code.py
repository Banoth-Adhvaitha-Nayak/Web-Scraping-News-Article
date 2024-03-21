
import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import time
import schedule
# df = pd.DataFrame(columns = ["Headline", "Date", "Info"])
# df.to_csv("news_every_hour.csv")
def add_headline(Headline: str, Date: str, Info: str)-> None:
    new_data = pd.DataFrame({
        "Headline": [Headline],
        "Date": [Date],
        "Info": [Info]
        })
    print("CSV creation")
    new_data.to_csv("news_every_hour.csv", mode='a', header=False, index=False)
    print(f"News appended on {datetime.datetime.today()}")
def main()-> None:
    try:
        response = requests.get("https://indianexpress.com/section/india/").text
        soup = BeautifulSoup(response, "html.parser")
        print("found container")
        container_div = soup.find("div", class_ = "nation")
        print("found article")
        articles = container_div.find_all("div", class_ = "articles")
        df = pd.read_csv("news_every_hour.csv")
        print("CSV found")
        for article in articles:
            print("parcing articles")
            Headline = article.h2.text
            Date = article.find("div", class_ = "date").text
            Info = article.find("p").text
            if ((df['Headline'] == Headline) | (df["Info"] == Info)).any():
                print("Already present skipped")
                continue
            else:
                print("Sending to data-frame function")
                add_headline(Headline= Headline, Date=Date, Info=Info)
    except Exception as e:
        print(f"link not  working: tried at {datetime.datetime.now()} got: {e}")
#schedule.every(1).minutes.do(main)
print(f"Started at: {datetime.datetime.now()}")
# while True:
#     schedule.run_pending()
#     time.sleep(1)
    
main()
