from requests import get
from time import sleep
import pandas as pd

url = "https://swapi.dev/api/people/"
all_data = []
for i in range(5):
  index = i + 1
  new_url = url + str(index)
  resp = get(new_url).json()
  name = resp["name"]
  height = resp["height"]
  mass = resp["mass"]
  gender = resp["gender"]
  ## 200 = ok
  # print(response.status_code)
  # print(response.json())
  sleep(2)
df = pd.DataFrame(all_data)
print(df)
# df.to_csv("star_wars_people.csv", index=False)