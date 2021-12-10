import os

import allure
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from py.path import local


def before_scenario(context, scenario):
    """
    U
    :param context:
    :param scenario:
    :return:
    """

    # set browser log
    dc = DesiredCapabilities.CHROME
    dc['goog:loggingPrefs'] = {'browser': 'ALL'}
    context.browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), desired_capabilities=dc)
    context.browser.maximize_window()
    context.browser.implicitly_wait(20)


def after_step(context, step):
    project_path = local(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
    if step.status.name != 'passed':
        if not os.path.isdir(project_path.join("screenshots").strpath):
            os.mkdir(project_path.join("screenshots").strpath)
        context.browser.save_screenshot(
            project_path.join("screenshots", f"{context.scenario.name[:60]}...scn.png").strpath)


def after_scenario(context, scenario):
    stdout = context.stdout_capture.getvalue()
    stderr = context.stderr_capture.getvalue()
    if stdout:
        allure.attach(stdout, name="stdout", attachment_type=allure.attachment_type.TEXT)
    if stderr:
        allure.attach(stderr, name="stderr", attachment_type=allure.attachment_type.TEXT)
    context.browser.quit()
