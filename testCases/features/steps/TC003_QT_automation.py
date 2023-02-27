from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from utilities.readProperties import ReadConfig
from selenium.webdriver.support.select import Select

btn_contactus = ReadConfig.clickOnContactUs()
btn_submit = ReadConfig.GetSubmitButton()
firstname = ReadConfig.getFirstName()
lastname = ReadConfig.getLastName()
phone = ReadConfig.getPhone()
company = ReadConfig.getCompanyName()
text_query = ReadConfig.getHelpSectionText()
location = ReadConfig.getLocation()
radio_option = ReadConfig.get_radio_option()
email = ReadConfig.get_email()
thankyou_msg = ReadConfig.get_thankyou_msg()
#getByType=ReadConfig.getByType()


@given('the user loads Qualitest official site')
def navigate(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.implicitly_wait(10)
    context.driver.get('https://qualitestgroup.com')
    context.driver.maximize_window()


@then('the user is able to access the Qualitest site')
def step_impl(context):
    context.driver.implicitly_wait(100)
    page_url = context.driver.current_url
    print(page_url)
    assert(page_url == "https://www.qualitestgroup.com/")


@then('the title of the page is {title}')
def step_impl(context, title):
    context.driver.implicitly_wait(100)
    page_title = context.driver.title
    print(page_title)
    assert(page_title == title)


@given('the user is on Qualitest site')
def navigate(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.implicitly_wait(10)
    context.driver.get('https://qualitestgroup.com')
    context.driver.maximize_window()
    page_url = context.driver.current_url
    print(page_url)


@when('the user clicks on Contact us button')
def step_impl(context):
    context.driver.find_element("link text", "Contact us").click()


@then('the user is able to access the Qualitest Contact us web page')
def step_impl(context):
    page_url = context.driver.current_url
    print(page_url)
    assert(page_url == "https://qualitestgroup.com/contact-us/")



@then('the page contains a form for the user')
def step_impl(context):
    firstname_textbox = context.driver.find_element("id", "firstname-34dd68e0-b077-4e95-9243-b861f3f2fd7d")
    lastname_textbox = context.driver.find_element("id", "lastname-34dd68e0-b077-4e95-9243-b861f3f2fd7d")
    assert(firstname_textbox and lastname_textbox)

@given('the user is on contact us page')
def navigate(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.implicitly_wait(10)
    context.driver.get('https://qualitestgroup.com')
    context.driver.maximize_window()
    context.driver.find_element('xpath',"a[@class='btn btn-sm btn-link text-primary']").click()
    page_url = context.driver.current_url
    print(page_url)
    context.driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
    context.driver.find_element("tag_name","body").send_keys(Keys.PAGE_DOWN)


@when('the user enters first name')
def step_impl(context):
    context.driver.implicitly_wait(100)
    context.driver.find_element_by_xpath(firstname).send_keys("tets")


@when('the user enters last name')
def step_impl(context):
    context.driver.implicitly_wait(100)
    context.driver.find_element_by_xpath(lastname).send_keys("user")


@when('the user enters company name')
def step_impl(context):
    context.driver.implicitly_wait(100)
    context.driver.find_element_by_xpath(company).send_keys("Qualitest")


@when('the user enters phone number')
def step_impl(context):
    context.driver.implicitly_wait(100)
    context.driver.find_element_by_xpath(phone).send_keys("1234567890")


@when('the user enters email')
def step_impl(context):
    context.driver.implicitly_wait(100)
    print(context.driver.find_element_by_xpath(email))
    context.driver.find_element_by_xpath(email).send_keys("abcd@efgh.com")


@when('the user selects what he wants to talk about')
def step_impl(context):
    context.driver.implicitly_wait(100)
    context.driver.find_element_by_xpath(radio_option).click()


@when('the user enters location')
def step_impl(context):
    context.driver.implicitly_wait(100)
    element = context.driver.find_element_by_xpath(location)
    context.driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
    context.driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
    context.driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
    context.driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
    print("Selecting UK & Europe")
    sel = Select(context.driver.find_element_by_xpath(location))
    sel.select_by_value("UK & Europe")
    print("Select UK & Europe")


@when('the user fills how can we help section')
def step_impl(context):
    context.driver.implicitly_wait(100)
    context.driver.find_element_by_xpath(text_query).send_keys("testing this form")


@when('the user clicks on Submit button')
def step_impl(context):
    context.driver.find_element_by_xpath(btn_submit).click()


@then('the user receives a Thank you message')
def step_impl(context):
    context.driver.implicitly_wait(100)
    msg = context.driver.find_element_by_xpath(thankyou_msg).text
    print(msg)
    assert(msg == "Thanks for contacting us.")



