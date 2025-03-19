import streamlit as st
import pandas as pd
import numpy as np

# Program's Heading
# print("\n\t\t\t Unit Coverter")
st.title("Unit Coverter")

options:list=["Meter","Centimeter","Kilometer","Milimeter"] #list of units

# taking 1st input from user of unit
unit_a = st.selectbox("Select 1st Unit to convert from :",options) #taking input
st.write(f"You have choosen:{unit_a.capitalize()}") #showing user's selected input 1

#taking 2nd input from user of unit
unit_b = st.selectbox(f"Select 2nd Unit to convert in :",options) #taking input
st.write(f"\t\t\tYou have choosen:{unit_b.capitalize()}") #showing user's selected input 2
   
try:
   num = st.number_input("Enter a Number :") #taking input
   st.write(f"\t\t\tYou have choosen:{str(num)}{unit_a}") #showing user's selected input 2

   def convert_units(value,first_unit,answered_unit):
      conversion_factors ={
         "Meter":{"Centimeter":100, "Kilometer":0.001, "Milimeter": 1000},
         "Centimeter":{"Meter":0.01, "Kilometer":0.00001, "Milimeter":10},
         "Kilometer":{"Meter":1000, "Centimeter":100000, "Milimeter":1e6},
         "Milimeter":{"Meter":0.001, "Centimeter":0.1, "Kilometer":1e-6}
      }

      if first_unit == answered_unit:  
         return value
      
      return value * conversion_factors.get(first_unit,{}).get(answered_unit,1)

   if st.button("Convert"):
      result = convert_units(num, unit_a, unit_b)
      st.success(f"{num} {unit_a} is equal to {result} {unit_b}")

except Exception as error:
    st.write(f"\n\t\t\t{error}")