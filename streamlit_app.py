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

def smoothie_nutri_total(df, col_name, multiples):  
  total = 0
  for fruit in multiples:
    st.text(fruit[0])
    stats = all_fruits.loc[fruit[0]]
    total += float(stats[col_name]) * fruit[1]
  return total

def selected_fruit_slider(fruit_name):
  prompt = "Number of " + fruit_name + " (by 100g) in your smoothie: "
  num = st.slider(prompt, 0, 20, 2)
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
  # smoothie = all_fruits.loc[fruits_selected]    
  # st.table(smoothie)
  
  # get fruit multiples
  fruit_counts = []  
  for fruit in fruits_selected:
    fruit_counts.append(selected_fruit_slider(str(fruit)))
          
  st.text(str(fruit_counts))

  # get the smoothie stats
  st.header("Your Smoothie's Stats")
  
  # total_cals = smoothie_nutri_total(all_fruits, 'Calories', fruit_counts)
  # total_carbs = smoothie_nutri_total(all_fruits, 'Carbohydrates', fruit_counts)
  # total_protine = smoothie_nutri_total(all_fruits, 'Protein', fruit_counts)
  # total_fat = smoothie_nutri_total(all_fruits, 'Fat', fruit_counts)
  # total_sugar = smoothie_nutri_total(all_fruits, 'Sugar', fruit_counts)      
  
  # display the stats
  cals, carbs, protine, fat, sugar = st.columns(5)
  
  # cals.metric(label="Calories of the Smoothie (per 100g) in Grams", value=str(total_cals), delta="1.2 °F")  
  # carbs.metric(label="Carbohydrates of the Smoothie (per 100g) in Grams", value=str(total_carbs), delta="1.2 °F")
  # protine.metric(label="Protein of the Smoothie (per 100g) in Grams", value=str(total_protine), delta="1.2 °F")
  # fat.metric(label="Fat of the Smoothie (per 100g) in Grams", value=str(total_fat), delta="1.2 °F")    
  # sugar.metric(label="Sugar of the Smoothie (per 100g) in Grams", value=str(total_sugar), delta="1.2 °F")      
    
  # the all fruits reference table  
  st.header('All Fruits Reference')
  st.dataframe(all_fruits)
    
# run the app
App()
