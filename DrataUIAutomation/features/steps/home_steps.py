from behave import *
from pageobjects.home_page import HomePage
from time import sleep


@given("I am on Homepage")
def step_impl(context):
    HomePage(context).go_to_home_page()

@then("I wait for five seconds patiently")
def step_impl(context):
    sleep(5)

@step('I search for "{keyword}"')
def step_impl(context, keyword):
    HomePage(context).search(keyword)


@step("I click on Navigation bar")
def step_impl(context):
    HomePage(context).click_navigation_bar()


@step("I click on Login button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    HomePage(context).click_login()


@given("I am on DrataHomePage")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    HomePage(context).go_to_drata()


@step("I collect all the url and make a list")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.url_list = HomePage(context).get_urls()


@then("Verify all the url")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    HomePage(context).verify_all_the_urls(context.url_list)