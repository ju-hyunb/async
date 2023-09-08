
## Screenshot with pyppeteer


#### - background
Sometimes you need a screenshot of the page when you crawl the web.
But some pages's screenshots are often cut off because of moving banners or fixed headers.
Although I tried many solutions about that problem(ex. selenium- execute_script, screenshot function, set_window_size etc.),
I can't solve this problem and screenshot have repeated headers continually.

Along the way, I found __async programming__ and __pyppeteer modules in python__.


#### - installation

Pyppeteer requires python 3.6+.

```python
python3 -m pip install pyppeteer
```


#### - Example

```python
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
```

```python
if __name__ == "__main__":

    url = 'https://www.amazon.com/'
    savepath = './screenshot'
    idx = 0

    asyncio.get_event_loop().run_until_complete(capture_full_page_screenshot(url, savepath, idx))

    print('done!')
```

![0](https://github.com/ju-hyunb/async/assets/104177526/2131d7ea-03fd-4d1b-b9d9-143c2dc1d79b)
