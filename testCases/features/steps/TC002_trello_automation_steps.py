from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from utilities.readProperties import ReadConfig

Login_linkBtn_xpath = ReadConfig.Login_linkBtn_xpath()
textbox_username_id = ReadConfig.textbox_username_id()
login_btn_id = ReadConfig.login_btn_id()
login_with_atlassian_id = ReadConfig.login_with_atlassian_id()
atlassian_signup_xpath = ReadConfig.atlassian_signup_xpath()
atlassian_already_have_an_account_id = ReadConfig.atlassian_already_have_an_account_id()
atlassian_click_login_xpath = ReadConfig.atlassian_click_login_xpath()
navigate_to_card_xpath = ReadConfig.navigate_to_card_xpath()
click_first_card_xpath = ReadConfig.click_first_card_xpath()
verify_firs_card_text_xpath = ReadConfig.verify_firs_card_text_xpath()
close_first_card_xpath = ReadConfig.close_first_card_xpath()
click_second_card_xpath = ReadConfig.click_second_card_xpath()
verify_second_card_text_xpath = ReadConfig.verify_second_card_text_xpath()
add_comment_second_card_xpath = ReadConfig.add_comment_second_card_xpath()
close_second_card_xpath = ReadConfig.close_second_card_xpath()
verify_first_card_with_comment_xpath = ReadConfig.verify_first_card_with_comment_xpath()
add_new_comment_first_card_xpath = ReadConfig.add_new_comment_first_card_xpath()
source_element_xpath = ReadConfig.source_element_xpath()
target_element_xpath = ReadConfig.target_element_xpath()
click_cant_login_id = ReadConfig.click_cant_login_id()
click_return_login_xpath = ReadConfig.click_return_login_xpath()
link_logout_link_text = ReadConfig.link_logout_linktext()
account_sign_up = ReadConfig.account_sign_up()
login_button = ReadConfig.login_button()


@given('the user navigate to the login page')
def navigate(context):
    context.driver =  webdriver.Chrome(ChromeDriverManager().install())
    context.driver.get('https://trello.com')
    context.driver.maximize_window()
    context.driver.find_element_by_xpath("//*[@class='btn btn-sm btn-link text-primary']").click()




@when('the user set username "{user}" and "{pwd}" password')
def username(context,user,pwd):
    context.driver.implicitly_wait(1000)
    context.driver.find_element_by_id(textbox_username_id).send_keys(user)
    context.driver.find_element_by_xpath("//*[@id='password']").send_keys(pwd)
    context.driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)


@then('the user click on atlassian signup')
def click_atlassian_signup(context):
    context.driver.get("https://id.atlassian.com/login")
    context.driver.implicitly_wait(1000)
    context.driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
    context.driver.find_element_by_xpath(atlassian_signup_xpath).click()


@then('the user click on already have account')
def already_have_account(context):
    context.driver.implicitly_wait(1000)
    context.driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
    context.driver.find_element_by_id(atlassian_already_have_an_account_id).click()


@then('the user click can\'t login')
def TC006_third_solutionPage(context):
    context.driver.implicitly_wait(10000)
    context.driver.find_element_by_id(click_cant_login_id).click()


@then('the user click return login')
def TC006_third_solutionPage(context):
    context.driver.implicitly_wait(10000)
    context.driver.find_element_by_xpath(click_return_login_xpath).click()


@then('the user enter trello password')
def TC006_third_solutionPage(context):
    context.driver.implicitly_wait(10000)
    context.driver.find_element_by_id("password").send_keys("trellologin2021@1234$")




@then('the user click on atlassian login')
def TC006_third_solutionPage(context):
    context.driver.implicitly_wait(100000)
    context.driver.find_element_by_xpath(atlassian_click_login_xpath).click()


@given('the user navigate to the first card')
def TC006_third_solutionPage(context):
    context.driver.implicitly_wait(10000)
    context.driver.set_page_load_timeout(100000)
    context.driver.find_element_by_xpath(navigate_to_card_xpath).click()


@when('the user verify first card with comment')
def TC006_third_solutionPage(context):
    context.synchronize()
    context.driver.find_element_by_xpath(click_first_card_xpath).click()


@when('the user add new comment first card')
def TC006_third_solutionPage(context):
    context.driver.implicitly_wait(1000)
    context.driver.find_element_by_xpath(add_new_comment_first_card_xpath).send_keys("add new comment")


@then('the user close first card')
def TC006_third_solutionPage(context):
    context.driver.implicitly_wait(1000)
    context.driver.find_element_by_xpath(close_first_card_xpath).click()


@given('the user navigate to the second card')
def navigate(context):
    context.driver.implicitly_wait(1000)
    context.driver.find_element_by_xpath(click_second_card_xpath).click()


@when('the user verify second card')
def TC006_third_solutionPage(context):
    context.driver.implicitly_wait(1000)


@when('the user close second card')
def step_impl(context):
    context.driver.implicitly_wait(1000)
    context.driver.find_element_by_xpath(close_second_card_xpath).click()


@then('the user set card to done')
def TC006_third_solutionPage(context):
    context.driver.implicitly_wait(1000)
