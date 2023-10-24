import logging
from playwright.sync_api import Browser


def process(body: bytes, /, browser: Browser, job_id: str | None = None) -> None:
    url = body.decode()
    with browser.new_context() as ctx:
        with ctx.new_page() as page:
            page.goto(url)
            title = page.title()
            logging.info(f"Title of {url!r} is {title!r}")
