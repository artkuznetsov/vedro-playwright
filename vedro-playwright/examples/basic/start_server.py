import jj


@jj.match("GET", "/reset")
async def reset_handler(request: jj.Request) -> jj.Response:
    html = """
        <form action="/">
            <label for="form-email">Email:</label><br>
            <input type="text" id="form-email" name="form-email" value=""><br>
            <input type="submit" id="form-submit" value="Submit">
        </form>
    """
    return jj.Response(text=html, headers={"Content-Type": "text/html"})


@jj.match("*")
async def root_handler(request: jj.Request) -> jj.Response:
    return jj.Response(text="OK")


jj.serve(port=8080)
