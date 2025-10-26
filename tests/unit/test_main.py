def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.text == (
        "<!DOCTYPE html>"
        "<html>"
        "  <body>"
        '    <a href="foo/">foo</a>'
        "  </body>"
        "</html>"
    )

