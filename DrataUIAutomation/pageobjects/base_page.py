from retry import retry
from selenium.common.exceptions import StaleElementReferenceException, ElementClickInterceptedException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self, context):
        self.browser = context.browser

    def wait_for_page_loaded(self, timeout=120):
        WebDriverWait(self.browser, timeout).until(PageLoaded())


    def send_text(self, locator, element_value):
        """
        Locates the element by specified locator and then sets its value
        :param locator: Element locator strategy
        :param element_value: value to be written
        """
        webelement = self.browser.find_element_by_xpath(locator)
        try:
            webelement.send_keys(element_value)
        except Exception as e:
            raise Exception("Could not write on the the element {} due to {}".
                            format(webelement, e))

    @retry(StaleElementReferenceException, tries=1)
    def click(self, locator):
        """
        Clicks the given element
        :param locator: Element locator strategy
        :return: element
        """
        element = None
        if isinstance(locator, str):
            element = self.browser.find_element_by_xpath(locator)
        elif isinstance(locator, WebElement):
            element = locator

        if element is not None:
            try:
                element.click()
            except ElementClickInterceptedException:
                self.browser.execute_script("""
                                    var element = arguments[0];
                                    element.click();
                                    """, element)
        else:
            raise Exception("Could not click on locator " + element)

class PageLoaded:
    def __call__(self, dr):
        ready = dr.execute_script(
                "return document.readyState=='complete';"
            )
        if ready:
            return True
        else:
            return False