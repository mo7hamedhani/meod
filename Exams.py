import os,time
from aiogram import *
from _class_hunt_ import *
import re
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

conex = Bot('6856868274:AAEH-fKtkaEmcqkP2u85z3F4zdcvY27nm-k', parse_mode='html')
rex=Dispatcher(conex)
import asyncio
print('BY : @mo7hamed_hani')
allowed_chat_id = 5602861672

@rex.message_handler(commands=['start'])
async def start(msg):
	print(msg.chat.id)
	if msg.chat.id == allowed_chat_id:
		hola = await msg.reply('''<b>commands are now ⬇️
	
	/qu search word here ➜ For payment gateways 
	
	/url url here ➜ To know the name of the gateway used 
	
	bot by ➜ @mo7hamed_hani</b>''')
@rex.message_handler(commands=['qu'])
async def start(msg):
    if not msg.chat.id == allowed_chat_id:
    	return
    query = msg.text[len('/qu '):]
    if not query: return await msg.reply('<b><code>/qu keywords</code></b>')
    else:
        unix  = GoogleQuey(query).getbs4()
        urls  = []
        for links in unix:
            url = links['href']
            if url.startswith('/url?q='):
                url = url[7:].split('&')[0] 
                if 'google' not in url and url not in urls: urls.append(url)

        if not urls: return await msg.reply('<b>No pages found </b>\n')
        
        hola = await msg.reply('Searching Wait...⏳')
        msgg = '<b>Pages Found</b>\n'
        await hola.edit_text(msgg)
        start_num = 0
        for url in urls:
            start_num += 1
            if "q%3D" in url: 
                msgg += '\n<b>There is an error in your search </b>\n'
                await hola.edit_text(msgg)
            else:
                
                msgg += f"""<b>[ {start_num} ] URL ➜ <code>{url}</code></b>\n
"""
            try:
                await hola.edit_text(msgg)
            except:None
        
        msgg += '\n<b>𝐃𝐎𝐍𝐄 ✅</b>'
        await hola.edit_text(msgg)

                


@rex.message_handler(commands=['url'])
async def start(msg):
    if not msg.chat.id == allowed_chat_id:
    	return
    urls = msg.text[len('/url '):]
    if not urls: return await msg.reply('<b> _use : <code>/url Page</code></b>')
    else:
        if "q%3D" in urls: 
         
            await msg.reply('<b>A scan error occurred</b>')
            
        else:
            hola = await msg.reply('Wait a moment, your gate is being scanned...⏳')
            try:
            	response =  requests.get(urls)
            	status=response.status_code
            except:
            	msg='''◆ 𝗨𝗥𝗟  ➜ {urls}
◆ 𝗦𝗧𝗔𝗧𝗘𝗦 ➜ {status} ❌
◆ 𝗥𝗘𝗦𝗨𝗟𝗧 ➜ The site was not found 
━━━━━━━━━━━━━━━━━
◆ 𝗕𝗬 ➜ @mo7hamed_hani'''
            	return
            ii=' 𝒖𝒏𝒌𝒏𝒐𝒘𝒏'
            for bins in open("gates.txt","r").read().split("\n"):
            	if bins in response.text:
            		
            		ii=bins
            msg=f'''◆ 𝗨𝗥𝗟  ➜ {urls}
◆ 𝗦𝗧𝗔𝗧𝗘𝗦 ➜ {status} ✅
◆ 𝗥𝗘𝗦𝗨𝗟𝗧 ➜ {ii}
━━━━━━━━━━━━━━━━━
◆ 𝗕𝗬 ➜ @mo7hamed_hani'''
            try:
                await hola.edit_text(msg)
            except:None



os.system('clear')
print('__Onli: True')
executor.start_polling(rex)
