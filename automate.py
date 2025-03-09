from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
import tkinter as tk
from tkinter import filedialog

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

driver.get("http://localhost:5000/")

file_input = driver.find_element("xpath", "/html/body/div/form/input[1]")

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

if file_path:
    abs_file_path = os.path.abspath(file_path)
    file_input.send_keys(abs_file_path)

    submit_button = driver.find_element("xpath", "/html/body/div/form/input[2]")
    submit_button.click()

    print("File upload and form submission completed. The browser will remain open.")
    while True:
        pass
else:
    print("No file selected. Exiting the script.")
    driver.quit()