from selenium import webdriver
import currency

class CurrencyRates:
    def GetCurrencyRates(self, driver:webdriver):
        url = "https://uzmanpara.milliyet.com.tr/doviz-kurlari/"
        driver.get(url)

        rowPath = "/html/body/div[9]/div[7]/div[2]/div[1]/table/tbody/tr"
        colPath = "/html/body/div[9]/div[7]/div[2]/div[1]/table/tbody/tr[2]/td"
        col = driver.find_elements_by_xpath(colPath)
        row = driver.find_elements_by_xpath(rowPath)
        colSize = len(col)
        rowSize = len(row)

        print(f"Row size: {colSize}")
        print(f"Col Size: {rowSize}")

        datas = []


        beforeXPath = "/html/body/div[9]/div[7]/div[2]/div[1]/table/tbody/tr["
        afterTdXPath = "]/td["
        afterTrXPath = "]"


        for t_row in range(2, (rowSize + 1)):
            currencyObj = currency.Currency()
            currencyObj.name = driver.find_element_by_xpath(beforeXPath + str(t_row) + afterTdXPath + str(2) + afterTrXPath).text
            currencyObj.purchasePrice = driver.find_element_by_xpath(beforeXPath + str(t_row) + afterTdXPath + str(3) + afterTrXPath).text
            currencyObj.salePrice = driver.find_element_by_xpath(beforeXPath + str(t_row) + afterTdXPath + str(4) + afterTrXPath).text
            datas.append(currencyObj)

        for i in datas:
            print(f"{i.name} \n {i.purchasePrice} \n {i.salePrice} \n --------------------------------------------------------")

        driver.close()
