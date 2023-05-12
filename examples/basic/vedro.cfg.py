import vedro
import vedro_playwright as playwright


class Config(vedro.Config):

    class Plugins(vedro.Config.Plugins):

        class Playwright(playwright.Playwright):
            enabled = True
