import streamlit
import pandas

streamlit.header('Smoothie Nutrition')
streamlit.text('Figure out how healthy your smoothies are.')

streamlit.header('Build your own smoothie below!')

# bring in the data
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

# my_fruit_list = my_fruit_list.set_index('Fruit')

# list the fruits
fruits_selected = streamlit.multiselect("Pick Fruits:", list(my_fruit_list.Fruit))

streamlit.header('Your Selected Fruits')
display_selected_fruits = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(display_selected_fruits)

streamlit.header('All Fruits')

streamlit.dataframe(my_fruit_list)
