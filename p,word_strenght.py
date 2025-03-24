import streamlit as st
import re

# setti
st.set_page_config(page_title="🔐Password Strength checker", layout= "centered")
# Giving Title to the web app
st.title("🔑Password Strength checker")

st.markdown('''
    Welcome to the **Ultimate Password Strength Checker..!** 
    Make sure that Password must contain:
    -  ✅ Length (must be 8 characters long)
    -  ✅ Upper(A-Z) and Lowr(a-z) Alphabets
    -  ✅ Numbers(1-10)
    -  ✅ Special characters(!@#$&/?*)
''')


p_word = st.text_input("Please Enter your Password here:", type="password")


def check_strength(p_word):
    score = 0

    # 1.check length
    if len(p_word) > 8:
        score += 1
    else:    
        st.write("❌❕ Passwor should be at least 8 characters long.")
    
    # 2.check upper & lower case
    if re.search(r"[a-z]",p_word) and re.search(r"[A-Z]",p_word):
        score += 1
    else:
        st.write("❌❕Password Must contain at leasr one upper case'A-Z' & lower case'a-z' ")

    # 3.check digits
    if re.search(r"\d", p_word):
        score += 1
    else:
        st.write("❌❕Password must contain Numbers '1-9' ")

    # 4.check special characters
    if re.search(r"[!@#_$&/?*]", p_word):
        score += 1
    else:
        st.write("❌❕Password must contain special character '@,#,&,*,^,!,*,%,_,-,<,?,>' ")
     
    if score == 4:
        st.write("✔ Strong password")
    elif score == 2:
        st.warning(" ❕❕ Moderate")
    else:
        st.error("❌Weak Password")
if p_word:
    check_strength(p_word)
