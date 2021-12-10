from time import sleep
from selenium.webdriver.common.keys import Keys
from pageobjects.base_page import BasePage
from utils.general import get_setting, getPagesFromSitemap
import allure

class HomePage(BasePage):
    search_btn_xpath = "//div[@id='search-form']//input"
    navigation_bar_xpath ="//a[contains(@class,'Navbar_sm-mobile__boCrg')]"
    login_btn_xpath = "//a[@id='LoginButton']"

    def go_to_drata(self):
        url = get_setting("URL", 'url')
        self.browser.get(url)
        self.wait_for_page_loaded()

    def get_urls(self):
        # l =  getPagesFromSitemap(get_setting("URL", 'url'))
        # print(l)
        # return l
        elements = self.browser.find_elements("xpath", "//body//a")
        urls = []
        for i in elements:
            url = i.get_attribute("href")
            if len(str(url)) > 3 and url != None and "https://drata.com" in url:
                urls.append(url)
        return set(urls)

    def verify_all_the_urls(self, url_list):
        # print(url_list)
        error_url_list = []
        error_log = ""
        logs = ""
        counter = 0
        for url in url_list:
            self.browser.get(url)
            self.wait_for_page_loaded()
            blog_title = self.browser.title
            # print("Printing logs for ", url)
            # print(blog_title)
            assert type(blog_title) is str
            assert len(blog_title) > 10
            for e in self.browser.get_log('browser'):
                logs = logs+str(e)+"\n"
                if "INFO" not in str(e):
                    error_log += str(e)+"\n"
                    counter += 1
                    if url not in error_url_list:
                        error_url_list.append(url)
        allure.attach(logs, name="OutPutLog", attachment_type=allure.attachment_type.TEXT)
        if counter > 0:
            allure.attach(f"Found {str(len(error_url_list))} have console error", name="URL count", attachment_type=allure.attachment_type.TEXT)
            allure.attach(str(error_url_list), name="URL list have console eorr", attachment_type=allure.attachment_type.TEXT)
            allure.attach(error_log, name="Console ERROR LOG", attachment_type=allure.attachment_type.TEXT)
            assert False
