import requests
import pandas

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/all")  
#st.text(fruityvice_response.json())    
if (fruityvice_response.ok):  
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())    
