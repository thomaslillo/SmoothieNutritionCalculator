import streamlit as st
import pandas
import requests
# import snowflake.connector

def get_all_fruit():    
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/all")  
  #st.text(fruityvice_response.json())    
  if (fruityvice_response.ok):  
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())   
  return fruityvice_normalized

st.header('Build your own smoothie below!')
st.text('Figure out how healthy your smoothies are.')

if st.button("Start Making My Smoothie"):
  returned = get_all_fruit()  
  st.dataframe(returned)

# bring in the data - alt source
# my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# my_fruit_list = my_fruit_list.set_index('Fruit')

# list the fruits
# fruits_selected = st.multiselect("Pick Fruits:", list(my_fruit_list.index))

st.header('Your Selected Fruits')
# display_selected_fruits = my_fruit_list.loc[fruits_selected]

# st.dataframe(display_selected_fruits)


# display the health information
col1, col2, col3 = st.columns(3)

col1.metric(label="Total Calories", value="70 °F", delta="1.2 °F")
col2.metric(label="Total Fat (G)", value="70 °F", delta="1.2 °F")
col3.metric(label="Total Protine (G)", value="70 °F", delta="1.2 °F")

# all fruits
st.header('All Fruits')

# st.dataframe(my_fruit_list)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/all")
#t.text(fruityvice_response.json())

fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
st.dataframe(fruityvice_normalized)
