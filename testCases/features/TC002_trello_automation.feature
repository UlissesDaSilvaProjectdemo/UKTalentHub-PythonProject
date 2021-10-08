Feature: the user would like to navigate to the cards and perform some actions

  Scenario: the user should be able to login with valid credentials
      Given the user navigate to the login page
      When  the user set username "trellologin2021@gmail.com" andtrellologin20221@1234$ password "
      Then  the user click on the login button
      And   the user click on atlassian signup
      And   the user click on already have account
      Then  the user click can't login
      And   the user click return login
      And   the user enter trello password
      Then  the user click on atlassian login

  Scenario: the user should be able to navigate to the first card and perform action
      Given the user navigate to the first card
      When  the user verify first card with comment
      And   the user add new comment first card
      Then  the user close first card

  Scenario: the user should be able to navigate to the second card and perform some action
      Given the user navigate to the second card
      When  the user verify second card
      And   the user close second card
      Then  the user set card to done











