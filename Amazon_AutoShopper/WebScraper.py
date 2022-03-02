from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains as A
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import selenium
from time import sleep

PATH = "C:\Python\chromedriver.exe"

class UserCredentials():
    def __init__(self, Email, Password):
        self.Email = Email
        self.Password = Password


# the key items that we need from here are: email, password, buget, wishlist

class WebShopping():
    # where webdriver.Chrome(PATH) is passed in for driver
    def __init__(self, User, driver, wish_list2):
        self.User = User
        self.driver = driver
        self.wish_list2 = wish_list2

    def login(self):  # login to account using userinput info

        self.driver.get("https://www.amazon.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

        amz_sign_in = self.driver.find_element_by_xpath(
            "//*[@id='nav-link-accountList']")

        A(self.driver).move_to_element(amz_sign_in).click().perform()
        # Enters in Email
        login_email = self.driver.find_element_by_name("email")
        login_email.send_keys(self.User.Email)
        
        login_email.send_keys(Keys.RETURN)
        
        # Enters in Password
        login_password = self.driver.find_element_by_name("password")
        
        login_password.send_keys(self.User.Password)
        
        login_password.send_keys(Keys.RETURN)
        sleep(2)

    def find_cheapest_item(self):
        price_combined = []
        item_titles = []
        combined_price = ""

        self.driver.implicitly_wait(2)
        all_product_info = self.driver.find_elements(By.XPATH, "(//div[@class='a-section a-spacing-base'])")
        self.driver.implicitly_wait(2)


    
        
        print("Calculating cheapest item...")
        

        for product in all_product_info:

            try:
                product_name_display = product.find_element_by_css_selector(
                    "span[class='a-size-base-plus a-color-base a-text-normal']").is_displayed()
                product_price_display = product.find_element_by_css_selector(
                    "span[class='a-price']").is_displayed()

                if product_name_display is True and product_price_display is True:
                    product_name_TEXT = product.find_element_by_css_selector(
                        "span[class='a-size-base-plus a-color-base a-text-normal']").text

                    price_whole_TEXT = product.find_element_by_css_selector(
                        "span[class='a-price-whole']").text
                    price_frac_TEXT = product.find_element_by_css_selector(
                        "span[class='a-price-fraction']").text

                    combined_price = price_whole_TEXT + '.' + price_frac_TEXT
                    combined_price = float(combined_price)

                    item_titles.append(product_name_TEXT)
                    price_combined.append(combined_price)

            except NoSuchElementException:
                continue
            except None:
                continue

        print("$", min(price_combined))
        index_cheapest = price_combined.index(min(price_combined))
        cheapest_item_name = item_titles[index_cheapest]

        print(cheapest_item_name)
        return cheapest_item_name

    def search_items(self):  # search and add item to cart using WishList
        for item in self.wish_list2:
            search = self.driver.find_element_by_id(
                "twotabsearchtextbox").send_keys(item)
            self.driver.implicitly_wait(3)
            button_search = self.driver.find_element_by_id(
                "nav-search-submit-button")
            self.driver.implicitly_wait(3)
            A(self.driver).move_to_element(button_search).click().perform()
            self.driver.implicitly_wait(3)
            self.driver.execute_script("window.scrollTo(0, 700)")
            self.driver.implicitly_wait(3)

            chosen_item = self.find_cheapest_item()
            self.driver.implicitly_wait(3)

            
            ip_xpath = "//span[normalize-space()='" + chosen_item + "']"
            print(ip_xpath)
            select = self.driver.find_element(By.XPATH, ip_xpath)
            A(self.driver).move_to_element(select).click().perform()
            self.driver.implicitly_wait(3)

            
            self.add_to_cart()
            self.driver.implicitly_wait(3)        
            

            clear_search = self.driver.find_element_by_id(
                "twotabsearchtextbox")
            clear_search.send_keys(Keys.CONTROL, 'a')
            clear_search.send_keys(Keys.BACKSPACE)

    def add_to_cart(self):
        cart_button = self.driver.find_element(By.XPATH, "//input[@id='add-to-cart-button']")
        A(self.driver).move_to_element(cart_button).click().perform()
 
