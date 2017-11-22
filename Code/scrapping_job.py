import requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get(hidden_link)
soup = BeautifulSoup(r.text,'html.parser')
results = soup.find_all("a", attrs={"class":"mrmob5 hidden-xs"})
records = []
for result in results:
    job_title = result.contents[0]
    if 'Python' in job_title:
        job_link = result['href']
        records.append((job_title,job_link)) 

df = pd.DataFrame(records,columns=None)
df.columns = ['job_title','job_link']

# df.to_csv('Python.csv',index=False)
## AND DONE ##
## link_hidden for web privacy 
