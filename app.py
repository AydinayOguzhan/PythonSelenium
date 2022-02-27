from types import CellType
from selenium import webdriver
import test
import currencyRates


driver = webdriver.Chrome()

mainObj = currencyRates.Main()
mainObj.GetCurrencyRates(driver)

# testObj = test.Test()
# testObj.Test1(driver)

