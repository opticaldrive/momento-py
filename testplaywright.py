
# from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
#     browser = p.webkit.launch_server()

#     browser = p.chromium.launch_server()
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://playwright.dev/")
#     page.screenshot(path="example.png")
#     context.close()
#     browser.close()




from playwright.async_api import async_playwright

async def return_screenshot(url:str):
    async with async_playwright() as p:
        browser = await p.webkit.launch()
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
    image =await return_screenshot("https://ip.me")
    await save_image(image, "ip.png")

import asyncio
asyncio.run(main())