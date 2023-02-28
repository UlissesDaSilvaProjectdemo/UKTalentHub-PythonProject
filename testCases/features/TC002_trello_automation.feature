Feature: the user would like to navigate to the cards and perform some actions


  Scenario: the user should be able to login with valid credentials
      Given the user navigate to the login page
      When  the user enters valid credentials
      And   the user clicks login
      Then  the user is logged in



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











