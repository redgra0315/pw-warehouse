# -*-encoding:UTF-8 -*-

import asyncio

async def wget(host):
    print("wget %s..." % host)
    connect  = asyncio.open_connection(host,80)
    reader, write = await connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    write.write(header.encode('utf-8'))
    await write.drain()
    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' %(host,line.decode('utf-8').rstrip()))
    write.close()
loop = asyncio.get_event_loop()
host_list = ['www.sina.com','www.sohu.com','www.163.com']
tasks = [wget(host) for host in host_list]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()