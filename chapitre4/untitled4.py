import pandas as pd
import requests
user_agent_url='https://www.w3schools.com/xml/cd_catalog.xml'
xml_data=requests.get(user_agent_url).content
print(xml_data)