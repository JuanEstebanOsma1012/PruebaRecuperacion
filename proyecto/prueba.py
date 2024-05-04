# make a basic test with selenium to a page with the next url: http://127.0.0.1:5500

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def main():

    # Open the browser
    driver = webdriver.Firefox()
    driver.get('http://127.0.0.1:5500/')

    # write text "hola mundo" in the input with class "input"
    input = driver.find_element(By.CLASS_NAME, 'input')
    input.send_keys('hola mundo')

    # press the button with class "encrypt"
    button = driver.find_element(By.CLASS_NAME, 'encrypt')
    button.click()

    # verify that the text in the input with class "textResult" is in the local storage of the browser with name "resultado"
    textResult = driver.find_element(By.CLASS_NAME, 'textResult')
    resultado = driver.execute_script("return localStorage.getItem('resultado')")
    assert textResult.text == resultado

    # close the browser
    time.sleep(2)
    driver.close()

    print('Test passed')

if __name__ == '__main__':
    main()