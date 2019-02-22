"""
aiohttp - 异步HTTP网络访问
异步I/O（异步编程）- 只使用一个线程（单线程）来处理用户请求
用户请求一旦被接纳，剩下的都是I/O操作，通过多路I/O复用也可以达到并发的效果
这种做法与多线程相比可以让CPU利用率更高，因为没有线程切换的开销
Redis/Node.js - 单线程 + 异步I/O
Celery - 将要执行的耗时间的任务异步化处理
异步I/O事件循环 - uvloop
"""
import asyncio
import re

import aiohttp

PATTERN = re.compile(r'\<title\>(?P<title>.*)\<\/title\>')


async def fetch_page(session, url):
    async with session.get(url, ssl=False) as resp:
        return await resp.text()


async def show_title(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch_page(session, url)
        print(PATTERN.search(html).group('title'))


def main():
    urls = ('https://www.python.org/',
            'https://git-scm.com/',
            'https://www.jd.com/',
            'https://www.taobao.com/',
            'https://www.douban.com/')
    loop = asyncio.get_event_loop()
    tasks = [show_title(url) for url in urls]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


if __name__ == '__main__':
    main()
