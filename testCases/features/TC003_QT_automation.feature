Feature: User launches Qualitest site and explores

  Scenario: The user launches Qualitest site
      Given the user loads Qualitest official site
      Then  the user is able to access the Qualitest site
      And   the title of the page is The World’s Leading AI-Led Quality Engineering Company | Qualitest

  Scenario: The user opens contact us page
      Given the user is on Qualitest site
      When  the user clicks on Contact us button
      Then  the user is able to access the Qualitest Contact us web page
      And   the page contains a form for the user

  Scenario: The user fills up Contact Us form
      Given the user is on contact us page
      When  the user enters first name
      And   the user enters last name
      And   the user enters company name
      And   the user selects what he wants to talk about
      And   the user enters email
      And   the user enters phone number
      And   the user enters location
      And   the user fills how can we help section
      And   the user clicks on Submit button
      Then  the user receives a Thank you message

      #d