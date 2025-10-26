from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return (
        "<!DOCTYPE html>"
        "<html>"
        "  <body>"
        '    <a href="foo/">foo</a>'
        "  </body>"
        "</html>"
    )

