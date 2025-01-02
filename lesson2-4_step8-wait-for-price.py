from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

# функция для расчёта значений
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
 
link = "http://suninjuly.github.io/explicit_wait2.html"


try: 
    browser = webdriver.Chrome()
    browser.get(link)
    
    # говорим Selenium проверять в течение 12 секунд, пока цена не станет 100
    WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "100") # тут двойные скобки, т.к. значение передаётся в виде кортежа
        )
    button1 = browser.find_element(By.ID, "book")
    button1.click()
    
    # Код, который расчитывает хначение у и подставляет в поле
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    # Отправляем заполненную форму
    button2 = browser.find_element(By.ID, "solve")
    button2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

