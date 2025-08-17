from pytest_bdd import scenario, given, when, then


@scenario("simple.feature", "Getting a package list")
def test_simple_api():
    pass


@given("I'm an anonymous user")
def anon_user():
    pass


@given("There are packages in the index")
def add_packages():
    pass


@when("I go to the simple API")
def go_to_simple_api():
    pass


@then("I should see all the packages")
def can_see_all_packages():
    pass

