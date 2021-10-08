Feature: the user would like to login into the application

  Scenario Outline: the user should not  not login with invalid credentials - Negative path
    Given the user launch chrome browser
    When  the user open the trello application homepage
    Then  the user enter username "<username>" and password "<password>"
    And   the user click on the login button
    And   the user do not successfully login into the application homepage
    Then  the user close the browser

    Examples:
    |username|password|
    |admin@gmail.com|admin123!|
    |admin34@yahoo.com|admin1965@|
    |userXZY@gmailcom|userXZY76&|
    |novauser@gmail.com|nova@123$|
    |myser@gmail.com|meuser@23*&|













