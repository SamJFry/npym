from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
async def root():
    return HTMLResponse(
        "<!DOCTYPE html>"
        "<html>"
        "  <body>"
        '    <a href="foo/">foo</a>'
        "  </body>"
        "</html>"
    )

