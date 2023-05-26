Feature: Basic BDD Login

  Scenario: As an admin I should be able to login
    Given I open the http://hrm-online.portnov.com/symfony/web/index.php/auth/login url
    When I enter text admin into the element id=txtUsername
    And I enter text password into the element id=txtPassword
    And I click the id=btnLogin element
    Then the url should contain /pim/viewEmployeeList
    When I get the text from element id=welcome
    Then the text should be Welcome Admin