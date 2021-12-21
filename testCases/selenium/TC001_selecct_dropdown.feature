Feature: the user would like to navigate to the cards and perform some actions

  Scenario: the user should be able to select autocomplete dropdown on the page
      Given the user navigate to the dropdown section of page
      When  the user select a dropdown choice by text
      Then  the user should be able to verify the dropdown.
