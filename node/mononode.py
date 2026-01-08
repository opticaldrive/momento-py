import uuid

node={"ws_endpoint":"ws://localhost:3301/", "tasks":[], "browser": None},


queue = ["https://google.com", "https://github.com", "https://hackclub.com", "https://aops.com", "https://duck.ai", "https://wikipedia.org"]

from playwright.async_api import async_playwright


async def run_scan_task(node, url:str):
    async with async_playwright() as p:
        browser = await p.webkit.connect(ws_endpoint="ws://localhost:3301/")
        screenshot = await return_screenshot(url)
        filepath = str(uuid.uuid4)+".png"
        save_image(screenshot, filepath)

async def return_screenshot(browser, url:str):
    async with async_playwright() as p:
        # browser = await p.webkit.connect(ws_endpoint="ws://localhost:3301/")
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto(url)
        screenshot_data = await page.screenshot()
        # page.screenshot(path="example.png")
        await context.close()
        await browser.close()
        return screenshot_data

async def save_image(image_data, filepath:str):
    with open(filepath, "wb") as image:
        image.write(image_data)

async def main():
    async with async_playwright() as p:
        browser = await p.webkit.connect(ws_endpoint=node["ws_endpoint"])  
        for task in queue:
            run_scan_task()

import asyncio
asyncio.run(main())
# connect to all nodes





# make list/que
# assign task to each free node
# waitlist when all nodes busy? or can it be stacked since async? idk assume not
# return the images when its done ofc. some metadata asw?
# focus on screenshots for now and distribution. we'll be connecting directly to the websocket, later this would be upgraded
# save screenshots in this directory , [project directory]/screenshots/thescreenshot
# check resource usage with benchmarks!! ram/cpu etc via activity monitor
# can a single podman container run multile of the screenshot scans at the same time?
# how many scans per minute with 3? we'll see

# TODO: for the same node, the same podman running the ws playwright server, don't tear down the browser connection. For each scan a new context must be made.
# Ideally benchmark it both ways



