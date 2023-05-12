import vedro
from vedro_playwright import BrowserEngine as Browser
from vedro_playwright import opened_firefox_page, opened_chromium_page, opened_webkit_page


class Scenario(vedro.Scenario):
    subject = "reset password (via {browser})"

    @vedro.params(Browser.CHROMIUM, opened_chromium_page)
    @vedro.params(Browser.FIREFOX, opened_firefox_page)
    @vedro.params(Browser.WEBKIT, opened_webkit_page)
    def __init__(self, browser, opened_page):
        self.opened_page = opened_page

    async def given_opened_app(self):
        self.page = await self.opened_page()
        await self.page.goto("http://localhost:8080/reset")

    async def given_filled_email(self):
        form_email = self.page.locator("#form-email")
        await form_email.type("user@email")

    async def when_user_submits_form(self):
        await self.page.click("#form-submit")

    async def then_it_should_redirect_to_root_page(self):
        pathname = await self.page.evaluate("window.location.pathname")
        assert pathname == "/"
