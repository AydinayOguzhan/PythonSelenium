from selenium import webdriver


class Test:
    def Test1(self, driver: webdriver):
        testUrl = "https://www.w3schools.com/html/html_tables.asp"

        driver.get(testUrl)

        rowPath = "//*[@id='customers']/tbody/tr"
        row = driver.find_elements_by_xpath(rowPath)
        rowSize = len(row)
        print(f"Row size: {rowSize}")
        
        colPath = '//*[@id="customers"]/tbody/tr[2]/td'
        col = driver.find_elements_by_xpath(colPath)
        colSize = len(col)
        print(f"Col size: {colSize} \n")
        
        
        beforeXpath = "//*[@id='customers']/tbody/tr["
        afterTrXpath = ']/td['
        afterTdXpath = ']'
        
        for t_row in range(2, (rowSize + 1)):
            for t_col in range(1, (colSize + 1)):
                finalPath = beforeXpath + str(t_row) + afterTrXpath + str(t_col) + afterTdXpath
                datas = driver.find_element_by_xpath(finalPath).text
                print(datas)
            print()
        
        driver.close()
