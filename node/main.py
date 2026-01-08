nodes = [
    {"ws_endpoint":"ws://localhost:3301/", "tasks":[], "browser": None},
    {"ws_endpoint":"ws://localhost:3302/", "tasks":[], "browser": None},
    # {"ws_endpoint":"ws://localhost:3303/", "tasks":[]},
]

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
async def retrieve_free_node(nodes):
    """
    retrieve_free_node

    :param nodes: nodes dictionary
    Returns min_tasks_node, uhhh i'll fix this later okay
    
    """
    min_tasks_node = min(nodes, key=lambda node: len(node["tasks"]))
    return min_tasks_node




from playwright.async_api import async_playwright

async def return_screenshot(url:str):
    async with async_playwright() as p:
        browser = await p.webkit.connect(ws_endpoint="ws://localhost:3301/")
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
    # image =await return_screenshot("https://google.com")


    # await save_image(image, "google.png")

    # setup/connect to all 
    browsers = []
    for node in nodes:
        async with async_playwright() as p:
            browsers.append(await p.chromium.connect(ws_endpoint=node["ws_endpoint"]))

import asyncio
asyncio.run(main())