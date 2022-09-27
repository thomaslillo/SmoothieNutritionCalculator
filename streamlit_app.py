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

def selected_fruit_slider(fruit_name):
  prompt = "Number of " + fruit_name + " in your smoothie: "
  num = st.slider(prompt, 0, 25, 5)
  return [fruit_name, num]

def App():  
  st.header('Build your own smoothie below!')
  st.text('Figure out how healthy your smoothies are.')
  
  # API request for fruits
  fruits_df = get_all_fruit()    
  
  # clean the table
  all_fruits = (fruits_df.set_index('name')).drop(['id','order'], axis=1)  
  all_fruits.rename(columns = {'nutritions.carbohydrates':'Carbohydrates', 
                               'nutritions.protein':'Protein', 
                               'nutritions.fat':'Fat', 
                               'nutritions.calories':'Calories', 
                               'nutritions.sugar':'Sugar'}, 
                               inplace = True)
    
  # list the selected fruits
  fruits_selected = st.multiselect("Pick Fruits:", list(all_fruits.index))
  
  # display the smoothie  
  st.header('Your Selected Fruits')
  # smoothie = all_fruits.loc[fruits_selected]    
  # st.table(smoothie)
  
  # get fruit multiples
  fruit_counts = []  
  for fruit in fruits_selected:
    fruit_counts.append(selected_fruit_slider(str(fruit)))
          
  st.text(str(fruit_counts))

  st.header("Your Smoothie's Stats")
  
  # get the smoothie stats
  col1, col2, col3 = st.columns(3)
  col1.metric(label="Total Calories", value="70 °F", delta="1.2 °F")
  col2.metric(label="Total Fat (G)", value="70 °F", delta="1.2 °F")
  col3.metric(label="Total Protine (G)", value="70 °F", delta="1.2 °F")  
  
  st.header('All Fruits Reference Chart')
  st.dataframe(all_fruits)
    
# run the app
App()
