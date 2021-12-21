Feature: the user would like to click and sendKeys in the application

  Scenario: the user should be able to click and sendkeys on the page
      Given the user navigate to the text field section of page
      When  the user select a text field and perform sendkeys action
      Then  the user should be able to sendkeys action in the page.
