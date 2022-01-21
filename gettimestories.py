from bs4 import BeautifulSoup
import urllib.request
from fastapi import FastAPI
import uvicorn 

app = FastAPI()



@app.get('/getTimeStories')
def get_latest_stories():
    base_url = "https://time.com"
    content = urllib.request.urlopen(base_url).read()
    soup = BeautifulSoup(content, 'html.parser')
    return [{'title':i.get_text(),
    'link':f"{base_url}{i.find('a').get('href')}"
    } 
    for i in soup.find(
        attrs={"class":"homepage-module latest"}
        ).find_all("h2")
        ]


if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)