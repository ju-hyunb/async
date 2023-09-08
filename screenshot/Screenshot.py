import warnings
warnings.filterwarnings('ignore')

import asyncio
from pyppeteer import launch




async def capture_full_page_screenshot(url, savepath, idx):
    browser = await launch(headless=True)
    page = await browser.newPage()
    try:
        await page.goto(url)
    except:
        print('site not load')
        pass

    await asyncio.sleep(3)

    try :
        await asyncio.sleep(5)
            

        savepath = f'{savepath}/{idx}.png'
        await page.waitForSelector('body')
        content_height = await page.evaluate('document.body.scrollHeight')
        await page.setViewport({'width': 1920, 'height': content_height})
        await page.screenshot({'path': savepath, 'fullPage': True})

    except Exception as e:
        print('## error : ', e)




if __name__ == "__main__":

    url = 'https://www.amazon.com/'
    savepath = './screenshot'
    idx = 0

    asyncio.get_event_loop().run_until_complete(capture_full_page_screenshot(url, savepath, idx))

    print('done!')