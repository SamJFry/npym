import httpx
from pytest_bdd import given, scenario, then, when


@scenario("simple.feature", "Getting a package list")
def test_simple_api():
    pass


@given("I'm an anonymous user")
def anon_user():
    pass


@given("There are packages in the index")
def add_packages(start_service):
    pass


@when("I go to the simple API", target_fixture="request_result")
def go_to_simple_api(add_packages):
    return httpx.get("http://localhost:8000/")


@then("I should see all the packages")
def can_see_all_packages(request_result):
    assert request_result == (
        "<!DOCTYPE html>"
        "<html>"
        "  <body>"
        '    <a href="foo/">foo</a>'
        "  </body>"
        "</html>"
    )

