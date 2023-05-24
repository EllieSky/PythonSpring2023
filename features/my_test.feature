Feature: My first features file

  Scenario: Count letters in my first name
    Given my name is Arthur
    When I count the letters in my name
    Then there should be 6 letters in total

  Scenario: Count letters in my full name
    Given my name is Arthur
    And my last name is Json
    When I count the letters in my name
    Then there should be 10 letters in total


  Scenario Outline: Count letters in a word: <word>
    Given my word is <word>
    When I count the letters in my word
    Then there should be <count> letters in total
    Examples:
      | word            | count |
      | endocrinologist | 15    |
      | Python          | 6     |
      | FANTASTIC       | 9     |

