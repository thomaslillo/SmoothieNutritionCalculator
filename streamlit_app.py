import streamlit
import pandas

streamlit.header('Smoothie Nutrition')
streamlit.text('Figure out how healthy your smoothies are.')

streamlit.header('Build your own smoothie below!')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")


# list the fruits
streamlit.multiselect("Pick Fruits:", list(my_fruit_list.fruit))

streamlit.dataframe(my_fruit_list)
