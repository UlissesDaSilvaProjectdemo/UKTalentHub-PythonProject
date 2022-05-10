Feature: the user would like to login into the application

  Scenario Outline: the user should not  not login with invalid credentials - Negative path
    Given the user launch chrome browser
    When  the user open the trello application homepage
    Then  the user enter username "<username>" and password "<password>"
    And   the user click on the login button
    And   the user do not successfully login into the application homepage
    Then  the user close the browser

    Examples:
      | username           | password        |
      | admin@gmail.com    | admin123!       |
      | admin34@yahoo.com  | admin1965@      |
      | userXZY@gmailcom   | userXZY76&      |
      | novauser@gmail.com | nova@123$       |
      | myser@gmail.com    | meuser@23*&     |
      | myserxxx@gmail.com | mexxxxuser@23*& |



#UI Test Scenarios of Login Page
#Verify that the login screen contains elements such as Username, Password, Sign in button, Remember password check box, Forgot password link, and create an account link.
#Verify that all the fields such as Username, Password has a valid placeholder
#Verify whether all the text boxes have a minimum and maximum length.
#Verify that the labels float upward when the text field is in focus or filled (In case of the floating label)
#Verify to see if the font style and size of the labels, as well as the text on each object, are clearly visible.
#Verify that the application’s user interface (UI) is responsive, so it will adapt to different screen resolutions and devices.
#Verify the login page and all the fields in the login page are displaying without any break in different browsers


#Functional Test Scenarios of Login Page
#Verify that cursor is focused on the “Username” text box on the page load (login page)
#Verify that tab functionality is working properly or not
#Verify that Enter/Tab key works as a substitute for the Sign-in button
#Verify that the User is able to Login with Valid Credentials
#Verify that the User is not able to Login with an invalid Username and invalid Password
#Verify that the User is not able to Login with a Valid Username and invalid Password
#Verify that the User is not able to log in with an invalid Username and Valid Password
#Verify that the User is not able to log in with a blank Username or Password
#Verify that the User is not able to Login with inactive credentials
#Verify that the reset button clears the data from all the text boxes in the login form
#Verify that the login credentials, mainly password stores in a database in an encrypted format
#Verify that clicking on the browser back button after successful login should not take the User to log out mode
#Verify that validation message is displayed in the case when User leaves Username or Password as blank
#Verify that validation message is displayed in case of exceeding the character limit of the Username and Password fields
#Verify that validation message is displayed in case of entering special character in the Username and password fields
#Verify that the “Keep me logged in” checkbox is unselected by default (depends on business logic, it may be selected or unselected)
#Verify that the timeout of the login session (Session Timeout)
#Verify that the logout link is redirected to login/home page
#Verify that User is redirected to appropriate page after successful login
#Verify that the User is redirected to the Forgot password page when clicking on the Forgot Password link
#Verify that the User is redirected to the Create an account page when clicking on the Signup / Create an account link
#Verify that the User should be able to login with the new password after changing the password
#Verify that the user should not be able to login with the old password after changing the password
#Verify that spaces should not be allowed before any password characters attempted
#Verify whether the user is still logged in after a series of actions such as sign-in, close the browser, and reopen the application.
#Verify that the ways to retrieve the password if the user forgets the password

#Non-functional Security Test Cases for Login Page
#Verify that clicking on the browser back button after successful logout should not take the User to a logged-in mode
#Verify that there is a limit on the total number of unsuccessful login attempts (No. of invalid attempts should be based on business logic. Based on the business logic, User will be asked to enter the captcha and try again or user will be blocked)
#Verify that the password is in encrypted form (masked format) when entered in the password field.
#Verify the password can be copy-pasted. System shouldn’t allow users to copy paste password.
#Verify that encrypted characters in the “Password” field should not allow deciphering if copied
#Verify that the “Remember password” checkbox is unselected by default (depends on business logic, it may be selected or unselected)
#Verify whether the login form is revealing any security information by viewing the page source
#Verify that the login page is vulnerable to SQL injection.
#Verify whether Cross-site scripting (XSS ) vulnerability works on a login page. XSS vulnerability may be used by hackers to bypass access controls.

#Peformance Test Cases for Login Page
#Verify that how much time the application is taking to load the home page after entering the valid user name and password in the login page.
#Test Cases for CAPTCHA & Cookies (If there is a captcha on the login page)
#Verify that whether there is a client-side validation when the User doesn’t enter the CAPTCHA
#Verify that the refresh link of CAPTCHA is generating the new CAPTCHA
#Verify that the CAPTCHA is case sensitive
#Verify whether the CAPTCHA has audio support to listen
#Verify whether virtual keyboard is available and working properly to enter login credentials incase of banking applications.
#Verify two-way authentication through OTP is working properly incase of banking applications.
#Verify SSL certificate is implemented or not



#Cookie Testing:
# Verify that whether the application is creating cookies on disk
#Verify whether the user is able to access the application after disabling the cookies.
#Disabling Cookies: Web pages may crash if we disable the cookies. Disable cookies on your browser. Access the website after all the cookies are disabled on your browser. There shouldn’t be any crashers or blockers.
#Here you need to verify two things:
#i. Is there an appropriate message displaying to the Users to enable cookies to access the site
#ii. Is there any workaround to access the site for the browsers with cookies disabled.
#Verify whether the user is able to access the application after removing the cookies.
#Removing Cookies: Remove all the cookies related to the website you are testing and check whether the website is working without any crash. Removal of cookies may result in loss of data and leads to system crash.
#Verify whether the user is able to access the application after deleting the cookies.
#Deleting Cookies: Make sure your website is creating cookies. Once the cookie is created, close the browser and delete cookies manually. Now open the browser and navigate to the website and test the behavior of the website. Deleting the cookies may sometimes break the website.
#Verify whether the user is able to access the application after corrupting (by editing) the cookies
#Corrupting Cookies: Manually edit the cookie using any plugin. You can also open cookies using notepad. Earlier we have mentioned where cookies are stored. Change the values (such as expiry date of the cookie or name of the cookie) of the cookies with irrelevant data.
#Try to change the login credentials of a User in the cookie with another valid User and try to do login. System shouldn’t allow you to log in with the modified User details.
#Verify whether all the sensitive data (user credentials) stored in a cookie is in the form of encrypted or not. (Cookies Encryption)
#Verify whether the cookies are being written correctly on all supported browsers. (Cross Browser Testing)
#Learn More About Cross Browser Testing & CrossBrowserTesting Tool
#Verify that the user is able to access the site by not accepting all the cookies.
#Accept or Reject Cookies: Make sure your browser is writing cookies. Access the website and allow the browser to write cookies. Now disable the cookies and try to access the site. Doing this may crash your site.
#Verify that there should not be overuse of cookies.
#No Overuse of Cookies: Overuse of cookies bring the site traffic down. Also, prompting for cookies quite often irritates the Users. Ultimately your site will lose traffic. Loss of traffic brings your business down.
#Verify that no personal or sensitive data is stored in the cookie.
#Privacy testing: In some cases, websites collect personal or sensitive data and store it in cookies. Make sure that the personal or sensitive data stored in a cookie is in an encrypted format.











