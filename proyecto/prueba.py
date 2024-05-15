# make a basic test with selenium to a page with the next url: http://127.0.0.1:5500

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import random
import string
import json

frases_de_prueba = [
    'hola mundo',
    'adios mundo',
    'hola adios',
    'adios hola',
    'hola hola',
    'adios adios',
    'hola mundo adios',
    'adios mundo hola',
    'hola adios mundo',
    'adios hola mundo',
    'hola hola mundo',
    'adios adios mundo'
]

number_of_tests = 5
test_metrics = {
    'main_1': {
        'passed': 0,
        'failed': 0,
        'average_time': 0,
        'total_time': 0
    },
    'main_2': {
        'passed': 0,
        'failed': 0,
        'average_time': 0,
        'total_time': 0
    }
}

def obtener_cadena_aleatoria():
    return frases_de_prueba[random.randint(0, len(frases_de_prueba) - 1)]

def main_step_by_step():

    # Open the browser
    driver = webdriver.Chrome()
    driver.get('http://127.0.0.1:5500/')

    # write text "hola mundo" in the input with class "input"
    input = driver.find_element(By.CLASS_NAME, 'input')
    
    # generate a random string
    text = obtener_cadena_aleatoria()

    # encrypt the text manually
    expected = driver.execute_script(f"return encriptarTexto('{text}')")

    # write the text in the input
    input.send_keys(text)

    time.sleep(2)

    # press the button with class "encrypt"
    button = driver.find_element(By.CLASS_NAME, 'encrypt')
    button.click()

    time.sleep(2)

    # open a new tab to avoid the window being closed
    driver.execute_script("window.open('');")

    time.sleep(2)

    # simulate a disaster, close the current tab
    driver.close()

    time.sleep(2)

    # reopen the quitted driver
    driver.switch_to.window(driver.window_handles[0])
    driver.execute_script("window.open('http://127.0.0.1:5500/')")
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    # verify that the text in the input with class "textResult" is in the local storage of the browser with name "resultado"
    textResult = driver.find_element(By.CLASS_NAME, 'textResult')

    resultado = driver.execute_script("return localStorage.getItem('resultado')")

    time.sleep(2)

    # verify that the text in the input with class "textResult" is the same as the text in the local storage and is the same as the expected
    assert textResult.text == resultado == expected

    # decrypt the recovered text
    input = driver.find_element(By.CLASS_NAME, 'input')
    input.send_keys(expected)

    time.sleep(2)

    # press the button with class "decrypt"
    button = driver.find_element(By.CLASS_NAME, 'decrypt')
    button.click()

    # close the browser
    time.sleep(2)
    driver.close()

    print('Test passed')

def main_2_step_by_step():

    # Open the browser
    driver = webdriver.Chrome()
    driver.get('http://127.0.0.1:5500/')

    # write text "hola mundo" in the input with class "input"
    input = driver.find_element(By.CLASS_NAME, 'input')
    
    # generate a random string
    text = obtener_cadena_aleatoria()

    # encrypt the text manually
    expected = driver.execute_script(f"return encriptarTexto('{text}')")

    # write the text in the input
    input.send_keys(text)

    time.sleep(2)

    # press the button with class "encrypt"
    button = driver.find_element(By.CLASS_NAME, 'encrypt')
    button.click()

    time.sleep(2)

    driver.refresh()

    # verify that the text in the input with class "textResult" is in the local storage of the browser with name "resultado"
    textResult = driver.find_element(By.CLASS_NAME, 'textResult')

    resultado = driver.execute_script("return localStorage.getItem('resultado')")

    time.sleep(2)

    # verify that the text in the input with class "textResult" is the same as the text in the local storage and is the same as the expected
    assert textResult.text == resultado == expected

    # decrypt the recovered text
    input = driver.find_element(By.CLASS_NAME, 'input')
    input.send_keys(expected)

    time.sleep(2)

    # press the button with class "decrypt"
    button = driver.find_element(By.CLASS_NAME, 'decrypt')
    button.click()

    # close the browser
    time.sleep(2)
    driver.close()

    print('Test passed')

# close the tab
def main_1():
    
    driver = webdriver.Chrome()
    driver.get('http://127.0.0.1:5500/')
    input = driver.find_element(By.CLASS_NAME, 'input')
    text = obtener_cadena_aleatoria()
    expected = driver.execute_script(f"return encriptarTexto('{text}')")
    input.send_keys(text)
    button = driver.find_element(By.CLASS_NAME, 'encrypt')
    button.click()
    driver.execute_script("window.open('');")
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    time.sleep(1)

    driver.execute_script("window.open('http://127.0.0.1:5500/')")
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    time.sleep(1)

    textResult = driver.find_element(By.CLASS_NAME, 'textResult')
    resultado = driver.execute_script("return localStorage.getItem('resultado')")
    assert textResult.text == resultado == expected

    driver.close()

# refresh the page
def main_2():
    
    driver = webdriver.Chrome()
    driver.get('http://127.0.0.1:5500/')
    input = driver.find_element(By.CLASS_NAME, 'input')
    text = obtener_cadena_aleatoria()
    expected = driver.execute_script(f"return encriptarTexto('{text}')")
    input.send_keys(text)
    button = driver.find_element(By.CLASS_NAME, 'encrypt')
    button.click()
    
    time.sleep(1)

    # refresh the page
    driver.refresh()

    time.sleep(1)

    textResult = driver.find_element(By.CLASS_NAME, 'textResult')
    resultado = driver.execute_script("return localStorage.getItem('resultado')")
    assert textResult.text == resultado == expected

    driver.close()

def main_n_times(number_of_tests):

    global test_metrics
    total_time = 0

    for i in range(number_of_tests):
        try:

            # initial time
            start_time = time.time()

            main_1()

            # final time
            end_time = time.time()

            total_time = end_time - start_time

            test_metrics['main_1']['total_time'] += total_time
            test_metrics['main_1']['passed'] += 1


        except Exception as e:
            print(e)
            test_metrics['main_1']['failed'] += 1

    test_metrics['main_1']['average_time'] = test_metrics['main_1']['total_time'] / number_of_tests

    for i in range(number_of_tests):
        try:

            # initial time
            start_time = time.time()

            main_2()

            # final time
            end_time = time.time()

            total_time = end_time - start_time

            test_metrics['main_2']['total_time'] += total_time
            test_metrics['main_2']['passed'] += 1


        except Exception as e:
            print(e)
            test_metrics['main_2']['failed'] += 1

    test_metrics['main_2']['average_time'] = test_metrics['main_2']['total_time'] / number_of_tests

    print(f'metrics {json.dumps(test_metrics, indent=4, sort_keys=True)}')

if __name__ == '__main__':

    #main_step_by_step()
    #main_2_step_by_step()

    main_n_times(number_of_tests)