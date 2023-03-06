from selenium.webdriver.common.by import By


class MainPageLocators:

    SELECT_LIST_USERS = (By.XPATH, "//div[@class='endpoints']/ul/li[1]")
    SELECT_SINGLE_USERS = (By.XPATH, "//div[@class='endpoints']/ul/li[2]")
    SELECT_LIST_RESOURCE = (By.XPATH, "//div[@class='endpoints']/ul/li[4]")
    SELECT_SINGLE_RESOURCE = (By.XPATH, "//div[@class='endpoints']/ul/li[5]")
    SELECT_DELETE_USERS = (By.XPATH, "//div[@class='endpoints']/ul/li[10]")
    SELECT_REGISTER_USERS = (By.XPATH, "//div[@class='endpoints']/ul/li[11]")
    SELECT_LOGIN_USERS = (By.XPATH, "//div[@class='endpoints']/ul/li[13]")
    SELECT_DELAYED_RESPONSE = (By.XPATH, "//div[@class='endpoints']/ul/li[15]")
    RESPONSE_200_STATUS = (By.XPATH, "//span[text()='200']")
    RESPONSE_204_STATUS = (By.XPATH, "//span[text()='204']")
    RESPONSE_400_STATUS = (By.XPATH, "//span[text()='400']")
    RESPONSE_404_STATUS = (By.XPATH, "//span[text()='404']")
    RESPONSE_BODY = (By.XPATH, "//pre[@data-key='output-response']")
