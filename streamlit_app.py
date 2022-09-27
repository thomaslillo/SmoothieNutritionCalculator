import streamlit as st
import pandas
import requests
# import snowflake.connector

# bring in the data - alt source
# my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# my_fruit_list = my_fruit_list.set_index('Fruit')

def get_all_fruit():    
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/all")  
  #st.text(fruityvice_response.json())    
  if (fruityvice_response.ok):  
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())   
  return fruityvice_normalized

def sum_values(df, col_name):
  value = 1
  return value

def App():  
  st.header('Build your own smoothie below!')
  st.text('Figure out how healthy your smoothies are.')
  
  fruits_df = get_all_fruit()    
  # clean the table
  all_fruits = (fruits_df.set_index('name')).drop(['id','order','family','genus'], axis=1)  
  
  # list the selected fruits
  fruits_selected = st.multiselect("Pick Fruits:", list(all_fruits.index))
  smoothie = all_fruits.loc[fruits_selected]
  st.header('Your Selected Fruits')
  st.table(smoothie)
      
  # the stats
  col1, col2, col3 = st.columns(3)
  col1.metric(label="Total Calories", value="70 °F", delta="1.2 °F")
  col2.metric(label="Total Fat (G)", value="70 °F", delta="1.2 °F")
  col3.metric(label="Total Protine (G)", value="70 °F", delta="1.2 °F")  
  
  st.header('All Fruits Chart')
  st.dataframe(all_fruits)
    
# run the app
App()
