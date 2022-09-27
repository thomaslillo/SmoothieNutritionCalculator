import streamlit as st
import pandas
import requests
# import snowflake.connector

# bring in the data - alt source
# my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# my_fruit_list = my_fruit_list.set_index('Fruit')

def get_all_fruit():    
  fruit_table = pandas.read_csv("./data/fruitweights.csv")  
  return fruit_table

def smoothie_nutri_total(df, col_name, multiples):  
  total = 0
  for fruit in multiples:
    stats = df.loc[[fruit[0]]]
    weight_multiple = float(stats['Weight']) / 100    
    total += (float(stats[col_name]) * weight_multiple) * fruit[1]
  total = round(total, 2)
  return str(total)

def selected_fruit_slider(fruit_name):
  prompt = "Number of " + fruit_name + " in the smoothie: "
  num = st.slider(prompt, 0, 20, 2)
  return [fruit_name, num]

def App():  
  st.header('Build your own smoothie below!')
  st.text('Figure out how healthy your smoothies with this easy tool.')
  
  # API request for fruits
  fruits_df = get_all_fruit()
  fruits_df = fruits_df[~fruits_df['Calories'].isnull()]
  
  # clean the table
  all_fruits = fruits_df.set_index('Fruit')
      
  # list the selected fruits
  fruits_selected = st.multiselect("Pick Fruits:", list(all_fruits.index))  
  
  # get fruit multiples
  fruit_counts = []  
  for fruit in fruits_selected:
    fruit_counts.append(selected_fruit_slider(str(fruit)))          

  # get the smoothie stats
  st.header("Your Smoothie's Stats")
  
  total_cals = smoothie_nutri_total(all_fruits, 'Calories', fruit_counts)
  total_sugar = smoothie_nutri_total(all_fruits, 'Sugar', fruit_counts)
  total_carbs = smoothie_nutri_total(all_fruits, 'Carbohydrates', fruit_counts)
  total_protine = smoothie_nutri_total(all_fruits, 'Protein', fruit_counts)
  total_fat = smoothie_nutri_total(all_fruits, 'Fat', fruit_counts)
  
  # display the stats    
  cals, sugar = st.columns(2)
  carbs, protine = st.columns(2)
  fat, other = st.columns(2)
  
  # row 1
  cals.metric(label="Smoothie Calories", value=total_cals, delta="1.2 °F")      
  sugar.metric(label="Smoothie Sugar", value=total_sugar, delta="1.2 °F")        
  # row 2
  carbs.metric(label="Smoothie Carbohydrates", value=total_carbs, delta="1.2 °F")    
  protine.metric(label="Smoothie Protein", value=total_protine, delta="1.2 °F")
  # row 3
  fat.metric(label="Smoothie Fat", value=total_fat, delta="1.2 °F")  
  
  # the all fruits reference table  
  st.header('All Fruits Reference')
  st.dataframe(all_fruits)
    
# run the app
App()
