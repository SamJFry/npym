Feature: simple
    A simple route api for listing all packages in the index.

    scenario: Getting a package list
        Given I'm an anonymous user
        And There are packages in the index

        When I go to the simple API

        Then I should see all the packages

