def get_all_fruit():    
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/all")  
  #st.text(fruityvice_response.json())
  
  if (fruityvice_response.code = 200):    
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  else:
    fruityvice_normalized = "issues"
  
  return fruityvice_normalized
