import asyncio, sys
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width":1080,"height":1350})
        for n in ["weekend","coming"]:
            await pg.goto(f"file:///home/claude/mock/out/{n}.html"); await pg.wait_for_timeout(300)
            h = await pg.evaluate("document.body.scrollHeight"); print(n, h)
            await pg.screenshot(path=f"out/{n}.png", full_page=True)
        m = await b.new_page(viewport={"width":390,"height":844}, device_scale_factor=2)
        await m.goto("file:///home/claude/mock/out/home.html"); await m.wait_for_timeout(300)
        await m.screenshot(path="out/home_phone.png", full_page=False)
        await m.screenshot(path="out/home_full.png", full_page=True)
        await b.close()
asyncio.run(main())
