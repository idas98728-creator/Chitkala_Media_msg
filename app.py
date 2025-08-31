import time
import pyperclip
import shutil
import pandas as pd
import streamlit as st
import openpyxl

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Streamlit Page Config
st.set_page_config(page_title="✉️ Chitkala Media", page_icon=":tada:", layout="wide")
st.title("Welcome to ✉️ Chitkala Media !!!")

# Excel file upload
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])
if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.write("Data Preview:")
    st.dataframe(df.head())

# Message box
# msg =("""Hi Creator,

# We’re super excited to have you on board for a barter collaboration with the skincare brand Joy Skincare – known for their  skincare range.

# You’ll receive a  combo worth ₹500-600, which includes:
# Ubtan Face Wash & Hydra Gel 

# Deliverables:
# 1 IG Reel

# Important Notes:
# ✅ Content to be shared within 2 days of receiving the products.
# ❌ No backouts post form submission.
# ⛔ Any delay or ghosting will lead to blacklisting from any future barter & paid campaigns with us.
# 🔗 Fill this form only if you are interested.
# https://docs.google.com/forms/d/1q_uOQu7uSk8SzrXi1JtgVgAVbQTItvkoTbkhi66mBqw/edit

# Looking forward to seeing your magic! 💚
# Cheers,
# Team Chitkala Media
# """)

# # WhatsApp automation
if st.button("Open WhatsApp Web"):
    if not uploaded_file:
        st.error("Please upload an Excel file with phone numbers.")
    else:
        phones = df['Phone Number'].tolist()
        options = Options()
        chrome_path = shutil.which("chromedriver")
        driver = webdriver.Chrome(service=Service(chrome_path), options=options)

        # Open WhatsApp Web
        driver.get("https://web.whatsapp.com")
        st.write("Please scan the QR code to log in to WhatsApp Web.")
        WebDriverWait(driver, 90).until(
            EC.presence_of_element_located((By.XPATH, '//canvas[@aria-label="Scan me!"] | //div[@aria-label="Chat list"]'))
        )
        st.write("WhatsApp Web is now open.")
        time.sleep(5)  
        for phone in phones:
            try:
                msg =("""Hi Creator {phone},
                    We’re super excited to have you on board for a barter collaboration with the skincare brand Joy Skincare – known for their  skincare range.


                    You’ll receive a  combo worth ₹500-600, which includes:
                    Ubtan Face Wash & Hydra Gel 

                    Deliverables:
                    1 IG Reel

                    Important Notes:
                    ✅ Content to be shared within 2 days of receiving the products.
                    ❌ No backouts post form submission.
                    ⛔ Any delay or ghosting will lead to blacklisting from any future barter & paid campaigns with us.
                    🔗 Fill this form only if you are interested.
                    https://docs.google.com/forms/d/1q_uOQu7uSk8SzrXi1JtgVgAVbQTItvkoTbkhi66mBqw/edit

                    Looking forward to seeing your magic! 💚
                    Cheers,
                    Team Chitkala Media
                    """)

                new_chat = WebDriverWait(driver, 90).until(EC.presence_of_element_located((By.XPATH, '//button[@title="New chat" and @aria-label="New chat"]')))
                new_chat.click()
                search_box = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Search name or number"]')))
                search_box.click()
                search_box.clear()
                search_box.send_keys(str(phone))
                time.sleep(2)
                search_box.send_keys(Keys.ENTER)
                time.sleep(1)
                message_box = WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '//div[@contenteditable="true" and @data-tab="10"]')))
                
                pyperclip.copy(msg)
                message_box.click()
                message_box.send_keys(Keys.CONTROL, 'v')
                message_box.send_keys(Keys.ENTER)    
                st.success(f"✅ Message sent to {phone}!")
                time.sleep(4)

            except:
                st.error(f"❌ Failed to send message to {phone}")
                continue    
        st.write("🎉 All messages processed!")
        time.sleep(5) 

