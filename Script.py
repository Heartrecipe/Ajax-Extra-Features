class script(object):
    START_TXT = """𝙷𝙴𝙻𝙾 {},
 🙋‍♂𝙸 𝙰𝙼 𝚂𝚄𝙿𝙴𝚁 𝙰𝚄𝚃𝙾𝙵𝙸𝙻𝚃𝙴𝚁 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝙱𝙾𝚃 𝚃𝙾 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙾𝚅𝙸𝙴𝚂 𝙸𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝙶𝚁𝙾𝚄𝙿𝚂...\n\n 😉𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝚆𝙸𝚃𝙷 𝙰𝙳𝙼𝙸𝙽𝚂 𝚁𝙸𝙶𝙷𝚃𝚂 𝙰𝙽𝙳 𝙴𝙽𝙹𝙾𝚈 𝚂𝙴𝚁𝚅𝙸𝙲𝙴..💖\n\n ❣️𝙾𝚆𝙽𝙴𝚁: <a href='https://telegram.dog/heart_recipe'>➳ ✰ 𝑶𝒐 𝑰𝒕'𝒔 𝑴𝒆 🤦</a>"""
    HELP_TXT = """𝙷𝙴𝚈 {}
𝙷𝙴𝚁𝙴 𝙸𝚂 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙵𝙾𝚁 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂."""
    ABOUT_TXT = """✪ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: <a href='https://telegram.dog/heart_recipe'>➳ ✰ 𝑶𝒐 𝑰𝒕'𝒔 𝑴𝒆 🤦</a>
✪ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: <a href='https://docs.pyrogram.com'>𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼</a>
✪ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
✪ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
✪ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: 𝙷𝙴𝚁𝙾𝙺𝚄
✪ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂   : v1.0.1 [ 𝙱𝙴𝚃𝙰 ]
✪ 𝚄𝙿𝙳𝙰𝚃𝙴𝚂: <a href='https://telegram.dog/VK_LINKZ'>𝙲𝙻𝙸𝙲𝙺 𝙷𝙴𝚁𝙴</a>
✪ 𝙼𝙾𝚅𝙸𝙴𝚂 𝙲𝙷𝙰𝙽𝙽𝙴𝙻: <a href='https://telegram.dog/+XX7Ox8faMtE1ZTY1'>𝚃𝙾𝚄𝙲𝙷 𝙷𝙴𝚁𝙴</a>"""
    FILE_TXT = """➤ 𝙷𝙴𝙻𝙿: 𝙵𝙸𝙻𝙴 𝚂𝚃𝙾𝚁𝙴 𝙼𝙾𝙳𝚄𝙻𝙴../

<b>𝙱𝚈 𝚄𝚂𝙸𝙽𝙶 𝚃𝙷𝙸𝚂 𝙼𝙾𝙳𝚄𝙻𝙴 𝚈𝙾𝚄 𝙲𝙰𝙽 𝚂𝚃𝙾𝚁𝙴 𝙵𝙸𝙻𝙴𝚂 𝙸𝙽 𝙼𝚈 𝙳𝙰𝚃𝙰𝙱𝙰𝚂𝙴 𝙰𝙽𝙳 𝙸 𝚆𝙸𝙻𝙻 𝙶𝙸𝚅𝙴 𝚈𝙾𝚄 𝙰 𝙿𝙴𝚁𝙼𝙰𝙽𝙴𝙽𝚃 𝙻𝙸𝙽𝙺 𝚃𝙾 𝙰𝙲𝙲𝙴𝚂𝚂 𝚃𝙷𝙴 𝚂𝙰𝚅𝙴𝙳 𝙵𝙸𝙻𝙴𝚂.𝙸𝙵 𝚈𝙾𝚄 𝚆𝙰𝙽𝚃 𝚃𝙾 𝙰𝙳𝙳 𝙵𝙸𝙻𝙴𝚂 𝙵𝚁𝙾𝙼 𝙰 𝙿𝚄𝙱𝙻𝙸𝙲 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚂𝙴𝙽𝙳 𝚃𝙷𝙴 𝙵𝙸𝙻𝙴 𝙻𝙸𝙽𝙺 𝙾𝙽𝙻𝚈 𝙾𝚁 𝚈𝙾𝚄 𝚆𝙰𝙽𝚃 𝚃𝙾 𝙰𝙳𝙳 𝙵𝙸𝙻𝙴𝚂 𝙵𝚁𝙾𝙼 𝙿𝚁𝙸𝚅𝙰𝚃𝙴 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚈𝙾𝚄 𝙼𝚄𝚂𝚃 𝙼𝙰𝙺𝙴 𝙼𝙴 𝚃𝙷𝙴 𝙰𝙳𝙼𝙸𝙽 𝙸𝙽 𝚃𝙷𝙴𝙸𝚁 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚃𝙾 𝙰𝙲𝙲𝙴𝚂𝚂 𝚃𝙷𝙴 𝙵𝙸𝙻𝙴𝚂..../</b>

⪼ 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙰𝙽𝙳 𝚄𝚂𝙰𝙶𝙴 ›

✯ /plink ›› <b>𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰𝙽𝚈 𝙼𝙴𝙳𝙸𝙰 𝚃𝙾 𝙶𝙴𝚃 𝙻𝙸𝙽𝙺.</b>
✯ /pbatch ›› <b>𝚄𝚂𝙴 𝚈𝙾𝚄𝚁 𝙼𝙴𝙳𝙸𝙰 𝙻𝙸𝙽𝙺 𝚆𝙸𝚃𝙷 𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳.</b>
✯ /batch ›› <b>𝚃𝙾 𝙲𝚁𝙴𝙰𝚃𝙴 𝙻𝙸𝙽𝙺 𝙵𝙾𝚁 𝙼𝚄𝙻𝚃𝙸𝙿𝙻𝙴 𝙿𝙾𝚂𝚃.</b>

✎ 𝐄𝐱𝐚𝐦𝐩𝐥𝐞 ›

<code>/batch https://t.me/c/1749754594/332 https://t.me/c/1749754594/336</code>"""
    WHOIS_TXT ="""<b>𝚆𝙷𝙾𝙸𝚂 𝙼𝙾𝙳𝚄𝙻𝙴</b>

𝙽𝙾𝚃𝙴:- 𝙶𝙸𝚅𝙴 𝙰 𝚄𝚂𝙴𝚁 𝙳𝙴𝚃𝙰𝙸𝙻𝚂

✯ /whois : 𝙶𝙸𝚅𝙴 𝙰 𝚄𝚂𝙴𝚁 𝙵𝚄𝙻𝙻 𝙳𝙴𝚃𝙰𝙸𝙻𝚂"""
    FUN_TXT ="""<b>𝙶𝙰𝙼𝙴𝚂</b> 
    
<b>🎲 𝙽𝙾𝚃𝙷𝙸𝙽𝙶 𝙼𝚄𝙲𝙷 𝙹𝚄𝚂𝚃 𝚂𝙾𝙼𝙴 𝙵𝚄𝙽 𝚃𝙷𝙸𝙽𝙶𝚂</b>

𝚃𝚁𝚈 𝚃𝙷𝙸𝚂 𝙾𝚄𝚃:
 
✰ /dice - 𝚁𝙾𝙻𝙻 𝚃𝙷𝙴 𝙳𝙸𝙲𝙴
✰ /Throw 𝗈𝗋 /Dart - 𝚃𝙾 𝙼𝙰𝙺𝙴 𝙳𝚁𝙰𝚃
✰ /Runs - 𝙹𝙾𝙺𝙴𝚂 
✰ /Goal or /Shoot - 𝚃𝙾 𝙼𝙰𝙺𝙴 𝙰 𝙶𝙾𝙰𝙻 𝙾𝚁 𝚂𝙷𝙾𝙾𝚃
✰ /luck or /cownd - 𝚂𝙿𝙸𝙽 𝚃𝙷𝙴 𝙻𝚄𝙲𝙺𝚈"""
    MANUELFILTER_TXT = """ ➤ 𝙷𝙴𝙻𝙿: <b>𝙵𝙸𝙻𝚃𝙴𝚁𝚂</b>

𝙵𝙸𝙻𝚃𝙴𝚁 𝙸𝚂 𝚃𝙷𝙴 𝙵𝙴𝙰𝚃𝚄𝚁𝙴 𝚆𝙷𝙴𝚁𝙴 𝚄𝚂𝙴𝚁𝚂 𝙲𝙰𝙽 𝚂𝙴𝚃 𝙰𝚄𝚃𝙾𝙼𝙰𝚃𝙴𝙳 𝚁𝙴𝙿𝙻𝙸𝙴𝚂 𝙵𝙾𝚁 𝙰 𝙿𝙰𝚁𝚃𝙸𝙲𝚄𝙻𝙰𝚁 𝙺𝙴𝚈𝚆𝙾𝚁𝙳 𝙰𝙽𝙳 𝙸 𝚆𝙸𝙻𝙻 𝚁𝙴𝚂𝙿𝙾𝙽𝙳 𝚆𝙷𝙴𝙽𝙴𝚅𝙴𝚁 𝚃𝙷𝙰𝚃 𝙺𝙴𝚈𝚆𝙾𝚁𝙳 𝙸𝚂 𝙵𝙾𝚄𝙽𝙳 𝙸𝙽 𝚃𝙷𝙴 𝙼𝙴𝚂𝚂𝙰𝙶𝙴

<b>𝙽𝙾𝚃𝙴:</b>

✸ 𝙸 𝚂𝙷𝙾𝚄𝙻𝙳 𝙷𝙰𝚅𝙴 𝙰𝙳𝙼𝙸𝙽 𝙿𝚁𝙸𝚅𝙸𝙻𝙻𝙰𝙶𝙴.
✸ 𝙾𝙽𝙻𝚈 𝙰𝙳𝙼𝙸𝙽𝚂 𝙲𝙰𝙽 𝙰𝙳𝙳 𝙵𝙸𝙻𝚃𝙴𝚁𝚂 𝙸𝙽 𝙰 𝙲𝙷𝙰𝚃.
✸ 𝙰𝙻𝙴𝚁𝚃 𝙱𝚄𝚃𝚃𝙾𝙽𝚂 𝙷𝙰𝚅𝙴 𝙰 𝙻𝙸𝙼𝙸𝚃 𝙾𝙵 64 𝙲𝙷𝙰𝚁𝙰𝙲𝚃𝙴𝚁𝚂.

<b>𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙰𝙽𝙳 𝚄𝚂𝙰𝙶𝙴:</b>

✯ /filter - <code>𝙰𝙳𝙳 𝙰 𝙵𝙸𝙻𝚃𝙴𝚁 𝙸𝙽 𝙰 𝙲𝙷𝙰𝚃</code>
✯ /filters - <code>𝙻𝙸𝚂𝚃 𝙰𝙻𝙻 𝚃𝙷𝙴 𝙵𝙴𝙰𝚃𝚄𝚁𝙴𝚂 𝙾𝙵 𝙰 𝙲𝙷𝙰𝚃</code>
✯ /del - <code>𝙳𝙴𝙻𝙴𝚃𝙴 𝙰 𝚂𝙿𝙴𝙲𝙸𝙵𝙸𝙲 𝙵𝙸𝙻𝚃𝙴𝚁 𝙸𝙽 𝙲𝙷𝙰𝚃</code>
✯ /delall - <code>𝙳𝙴𝙻𝙴𝚃𝙴 𝚃𝙷𝙴 𝚆𝙷𝙾𝙻𝙴 𝙵𝙸𝙻𝚃𝙴𝚁𝚂 𝙸𝙽 𝙰 𝙲𝙷𝙰𝚃 (𝙲𝙷𝙰𝚃 𝙾𝚆𝙽𝙴𝚁 𝙾𝙽𝙻𝚈)</code>"""
    SONG_TXT = """<b> 🤠 𝚂𝙾𝙽𝙶 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 😉</b>

𝚂𝙾𝙽𝙶 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙼𝙾𝙳𝚄𝙻𝙴, 𝙵𝙾𝚁 𝚃𝙷𝙾𝚂𝙴 𝚆𝙷𝙾 𝙻𝙾𝚅𝙴 𝙼𝚄𝚂𝙸𝙲

<b>✰ 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 ✰</b>

- /song [Song Name] - 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙼𝚄𝚂𝙸𝙲 😉

<b>🌀 𝚄𝚂𝙰𝙶𝙴 🌀</b>

✸ 𝙲𝙰𝙽 𝙱𝙴 𝚄𝚂𝙴𝙳 𝙱𝚈 𝙴𝚅𝙴𝚁𝚈𝙾𝙽𝙴
✸ 𝚆𝙾𝚁𝙺𝚂 𝙸𝙽 𝙱𝙾𝚃 𝙿𝙼

𝙼𝙰𝙳𝙴 𝙱𝚈 <a href=https://telegram.dog/heart_recipe>➳ ✰ 𝑶𝒐 𝑰𝒕'𝒔 𝑴𝒆 🤦</a>"""
    PIN_TXT ="""<b>𝙿𝙸𝙽 𝙼𝙾𝙳𝚄𝙻𝙴</b>

<b> ➤ 𝙿𝙸𝙽 :</b>

<b>🥤 𝙰𝙻𝙻 𝚃𝙷𝙴 𝙿𝙸𝙽 𝚁𝙴𝙻𝙴𝙰𝚃𝙴𝙳 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙲𝙰𝙽 𝙱𝙴 𝙵𝙾𝚄𝙽𝙳 𝙷𝙴𝚁𝙴; 𝙺𝙴𝙴𝙿 𝚈𝙾𝚄𝚁 𝙲𝙷𝙰𝚃 𝚄𝙿 𝚃𝙾 𝙳𝙰𝚃𝙴 𝙾𝙽 𝚃𝙷𝙴 𝙻𝙰𝚃𝙴𝚂𝚃 𝙽𝙴𝚆𝚂 𝚆𝙸𝚃𝙷 𝙰 𝚂𝙸𝙼𝙿𝙻𝙴 𝙿𝙸𝙽𝙽𝙴𝙳 𝙼𝙴𝚂𝚂𝙰𝙶𝙴!</b>

<b>📚 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙰𝙽𝙳 𝚄𝚂𝙰𝙶𝙴:</b>

✯ /pin : 𝙿𝙸𝙽 𝚃𝙷𝙴 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝚈𝙾𝚄 𝚁𝙴𝙿𝙻𝙸𝙴𝙳 𝚃𝙾 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝚃𝙾 𝚂𝙴𝙽𝙳 𝙰 𝙽𝙾𝚃𝙸𝙵𝙸𝙲𝙰𝚃𝙸𝙾𝙽 𝚃𝙾 𝙶𝚁𝙾𝚄𝙿 𝙼𝙴𝙼𝙱𝙴𝚁𝚂
✯ /unpin : 𝚄𝙽𝙿𝙸𝙽 𝚃𝙷𝙴 𝙲𝚄𝚁𝚁𝙴𝙽𝚃 𝙿𝙸𝙽𝙽𝙴𝙳 𝙼𝙴𝚂𝚂𝙰𝙶𝙴. 𝙸𝙵 𝚄𝚂𝙴𝙳 𝙰𝚂 𝚁𝙴𝙿𝙻𝚈 𝚄𝙽𝙿𝙸𝙽𝚂 𝚃𝙷𝙴 𝚁𝙴𝙿𝙻𝙸𝙴𝙳 𝙼𝙴𝚂𝚂𝙰𝙶𝙴"""
    PASTE_TXT = """➤ 𝙷𝙴𝙻𝙿: <b>𝙿𝙰𝚂𝚃𝙴</b>

✯ 𝙿𝙰𝚂𝚃𝙴 𝚂𝙾𝙼𝙴 𝚃𝙴𝚇𝚃𝚂 𝙾𝚁 𝙳𝙾𝙲𝚄𝙼𝙴𝙽𝚃𝚂 𝙾𝙽 𝙰 𝚆𝙴𝙱𝚂𝙸𝚃𝙴! ✯

<b>𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙰𝙽𝙳 𝚄𝚂𝙰𝙶𝙴:</b>

✯ /paste [text] - 𝙿𝙰𝚂𝚃𝙴 𝚃𝙷𝙴 𝙶𝙸𝚅𝙴𝙽 𝚃𝙴𝚇𝚃 𝙾𝙽 𝙿𝙰𝚂𝚃𝚈

<b>𝙽𝙾𝚃𝙴:</b>

✰ 𝚃𝙷𝙴𝚂𝙴 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝚆𝙾𝚁𝙺𝚂 𝙾𝙽 𝙱𝙾𝚃𝙷 𝙿𝙼 𝙰𝙽𝙳 𝙶𝚁𝙾𝚄𝙿.
✰ 𝚃𝙷𝙴𝚂𝙴 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙲𝙰𝙽 𝙱𝙴 𝚄𝚂𝙴𝙳 𝙱𝚈 𝙰𝙽𝚈 𝙶𝚁𝙾𝚄𝙿 𝙼𝙴𝙼𝙱𝙴𝚁."""
    GTRANS_TXT = """𝙷𝙴𝙻𝙿: <b> 𝚃𝙴𝚇𝚃 𝚃𝙾 𝚂𝙿𝙴𝙴𝙲𝙷 🎤 𝙼𝙾𝙳𝚄𝙻𝙴:</b>

𝚃𝚁𝙰𝙽𝚂𝙻𝙰𝚃𝙴 𝚃𝙴𝚇𝚃 𝚃𝙾 𝚂𝙿𝙴𝙴𝙲𝙷

<b>𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙰𝙽𝙳 𝚄𝚂𝙰𝙶𝙴:</b>

✯ /tts <text> : 𝙲𝙾𝙽𝚅𝙴𝚁𝚃 𝚃𝙴𝚇𝚃 𝚃𝙾 𝚂𝙿𝙴𝙴𝙲𝙷

<b>𝙽𝙾𝚃𝙴:</b>

✰ 𝙸 𝚂𝙷𝙾𝚄𝙻𝙳 𝙷𝙰𝚅𝙴 𝙰𝙳𝙼𝙸𝙽 𝙿𝚁𝙸𝚅𝙸𝙻𝙻𝙰𝙶𝙴.
✰ 𝚃𝙷𝙴𝚂𝙴 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝚆𝙾𝚁𝙺𝚂 𝙾𝙽 𝙱𝙾𝚃𝙷 𝙿𝙼 𝙰𝙽𝙳 𝙶𝚁𝙾𝚄𝙿.
✰ 𝙸 𝙲𝙰𝙽 𝚃𝚁𝙰𝙽𝚂𝙻𝙰𝚃𝙴 𝚃𝙴𝚇𝚃𝚂 𝚃𝙾 200+ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴𝚂."""
    PINGS_TXT ="""<b>📈 𝙿𝙸𝙽𝙶:</b>

𝙷𝙴𝙻𝙿𝚂 𝚈𝙾𝚄 𝚃𝙾 𝙺𝙽𝙾𝚆 𝚈𝙾𝚄𝚁 𝙿𝙸𝙽𝙶🚶🏼‍♂️

<b>𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙰𝙽𝙳 𝚄𝚂𝙰𝙶𝙴:</b>

✯ /alive - 𝚃𝙾 𝙲𝙷𝙴𝙲𝙺 𝚈𝙾𝚄𝚁 𝙰𝙻𝙸𝚅𝙴
✯ /help - 𝚃𝙾 𝙶𝙴𝚃 𝙷𝙴𝙻𝙿
✯ /ping - 𝚃𝙾 𝙺𝙽𝙾𝚆 𝚈𝙾𝚄𝚁 𝙿𝙸𝙽𝙶 
✯ /repo - 𝚂𝙾𝚄𝚁𝙲𝙴 𝙲𝙾𝙳𝙴

<b>𝙽𝙾𝚃𝙴 :</b>

✸ 𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙲𝙰𝙽 𝙱𝙴 𝚄𝚂𝙴𝙳 𝙸𝙽 𝙿𝙼𝚂 𝙰𝙽𝙳 𝙶𝚁𝙾𝚄𝙿𝚂
✸ 𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙲𝙰𝙽 𝙱𝙴 𝚄𝚂𝙴𝙳 𝙱𝚈 𝙴𝚅𝙴𝚁𝚈𝙾𝙽𝙴 𝙸𝙽 𝚃𝙷𝙴 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙱𝙾𝚃 𝙿𝙼
✸ 𝚂𝙷𝙰𝚁𝙴 𝚄𝚂 𝙵𝙾𝚁 𝙼𝙾𝚁𝙴 𝙵𝙴𝙰𝚃𝚄𝚁𝙴𝚂"""
    TELE_TXT = """<b>➤ 𝙷𝙴𝙻𝙿: 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙿𝙷▪️</b>

𝙳𝙾 𝙰𝚂 𝚈𝙾𝚄𝚁 𝚆𝙸𝚂𝙷 𝚆𝙸𝚃𝙷 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙿𝙷.𝙿𝙷 𝙼𝙾𝙳𝚄𝙻𝙴!

</b>𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙰𝙽𝙳 𝚄𝚂𝙰𝙶𝙴:</b>

✯ /telegraph - 𝚂𝙴𝙽𝙳 𝙼𝙴 𝙰 𝙿𝙸𝙲𝚃𝚄𝚁𝙴 𝙾𝚁 𝚅𝙸𝙳𝙴𝙾 (𝚄𝙽𝙳𝙴𝚁 5𝙼𝙱)

<b>𝙽𝙾𝚃𝙴:</b>

✰ 𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 𝙲𝙰𝙽 𝙱𝙴 𝚄𝚂𝙴𝙳 𝙱𝚈 𝙴𝚅𝙴𝚁𝚈𝙾𝙽𝙴
✰ 𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 𝙲𝙰𝙽 𝙱𝙴 𝚄𝚂𝙴𝙳 𝙱𝚈 𝙴𝚅𝙴𝚁𝚈𝙾𝙽𝙴"""
    JSON_TXT ="""<b>JSON:</b>

𝙱𝙾𝚃 𝚁𝙴𝚃𝚄𝚁𝙽𝚂 𝙹𝚂𝙾𝙽 𝙵𝙾𝚁 𝙰𝙻𝙻 𝚁𝙴𝙿𝙻𝙸𝙴𝙳 𝙼𝙴𝚂𝚂𝙰𝙶𝙴𝚂 𝚆𝙸𝚃𝙷 /json

<b>𝙵𝙴𝙰𝚃𝚄𝚁𝙴𝚂:</b>

✰ 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝙴𝙳𝙸𝚃𝙸𝙽𝙶 𝙹𝚂𝙾𝙽
✰ 𝙿𝙼 𝚂𝚄𝙿𝙿𝙾𝚁𝚃
✰ 𝙶𝚁𝙾𝚄𝙿 𝚂𝚄𝙿𝙿𝙾𝚁𝚃

<b>𝙽𝙾𝚃𝙴:</b>

𝙴𝚅𝙴𝚁𝚈𝙾𝙽𝙴 𝙲𝙰𝙽 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳, 𝙸𝙵 𝚂𝙿𝙰𝙼𝙼𝙸𝙽𝙶 𝙷𝙰𝙿𝙿𝙴𝙽𝚂 𝙱𝙾𝚃 𝚆𝙸𝙻𝙻 𝙰𝚄𝚃𝙾𝙼𝙰𝚃𝙸𝙲𝙰𝙻𝙻𝚈 𝙱𝙰𝙽 𝚈𝙾𝚄 𝙵𝚁𝙾𝙼 𝚃𝙷𝙴 𝙶𝚁𝙾𝚄𝙿."""
    PURGE_TXT = """<b>𝙿𝚄𝚁𝙶𝙴</b>
    
𝙳𝙴𝙻𝙴𝚃𝙴 𝙰 𝙻𝙾𝚃 𝙾𝙵 𝙼𝙴𝚂𝚂𝙰𝙶𝙴𝚂 𝙵𝚁𝙾𝙼 𝙶𝚁𝙾𝚄𝙿𝚂! 
    
 <b>𝙰𝙳𝙼𝙸𝙽</b> 

 /purge :- 𝙳𝙴𝙻𝙴𝚃𝙴 𝙰𝙻𝙻 𝙼𝙴𝚂𝚂𝙰𝙶𝙴𝚂 𝙵𝚁𝙾𝙼 𝚁𝙴𝙿𝙻𝙸𝙴𝙳 𝚃𝙾 𝙼𝙴𝚂𝚂𝙰𝙶𝙴, 𝚃𝙾 𝙲𝚄𝚁𝚁𝙴𝙽𝚃 𝙼𝙴𝚂𝚂𝙰𝙶𝙴"""
    BUTTON_TXT = """➤ 𝙷𝙴𝙻𝙿: <b>𝙱𝚄𝚃𝚃𝙾𝙽𝚂</b>

𝙸 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙱𝙾𝚃𝙷 𝚄𝚁𝙻 𝙰𝙽𝙳 𝙰𝙻𝙴𝚁𝚃 𝙸𝙽𝙻𝙸𝙽𝙴 𝙱𝚄𝚃𝚃𝙾𝙽𝚂.

<b>𝙽𝙾𝚃𝙴:</b>

✸ 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝚆𝙸𝙻𝙻 𝙽𝙾𝚃 𝙰𝙻𝙻𝙾𝚆𝚂 𝚃𝙾 𝚂𝙴𝙽𝙳 𝙱𝚄𝚃𝚃𝙾𝙽𝙴𝚂 𝚆𝙸𝚃𝙷𝙾𝚄𝚃 𝙰𝙽𝚈 𝙲𝙾𝙽𝚃𝙴𝙽𝚃, 𝚂𝙾 𝙲𝙾𝙽𝚃𝙴𝙽𝚃 𝙸𝚂 𝙼𝙰𝙽𝙳𝙰𝚃𝙾𝚁𝚈.
✸ 𝙸 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙱𝚄𝚃𝚃𝙾𝙽𝚂 𝚆𝙸𝚃𝙷 𝙰𝙽𝚈 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝙼𝙴𝙳𝙸𝙰 𝚃𝚈𝙿𝙴.
✸ 𝙱𝚄𝚃𝚃𝙾𝙽𝚂 𝚂𝙷𝙾𝚄𝙻𝙳 𝙱𝙴 𝙿𝚁𝙾𝙿𝙴𝚁𝙻𝚈 𝙿𝙰𝚁𝚂𝙴𝙳 𝙰𝚂 𝙼𝙰𝚁𝙺𝙳𝙾𝚆𝙽 𝙵𝙾𝚁𝙼𝙰𝚃.

<b>𝚄𝚁𝙻 𝙱𝚄𝚃𝚃𝙾𝙽𝚂:</b>

<code>[Button Text](buttonurl:https://t.me/heart_recipe)</code>

<b>𝙰𝙻𝙴𝚁𝚃 𝙱𝚄𝚃𝚃𝙾𝙽𝚂:</b>
<code>[Button Text](buttonalert:𝚃𝙷𝙸𝚂 𝙸𝚂 𝙰𝙽 𝙰𝙻𝙴𝚁𝚃 𝙼𝙴𝚂𝚂𝙰𝙶𝙴)</code>"""
    AUTOFILTER_TXT = """➤ 𝙷𝙴𝙻𝙿: <b>𝙰𝚄𝚃𝙾𝙵𝙸𝙻𝚃𝙴𝚁</b>

<b>𝙽𝙾𝚃𝙴:</b>

✰ 𝙼𝙰𝙺𝙴 𝙼𝙴 𝙰𝙳𝙼𝙸𝙽 𝙸𝙽 𝚈𝙾𝚄𝚁 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝙸𝙵 𝙸𝚃'𝚂 𝙿𝚁𝙸𝚅𝙰𝚃𝙴.
✰ 𝙼𝙰𝙺𝙴 𝚂𝚄𝚁𝙴 𝚈𝙾𝚄𝚁 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝙳𝙾𝙴𝚂𝙽'𝚃 𝙲𝙾𝙽𝚃𝙰𝙸𝙽𝚂 𝙲𝙰𝙼𝚁𝙸𝙿𝚂,𝙿𝙾𝚁𝙽 𝙰𝙽𝙳 𝙵𝙰𝙺𝙴 𝙵𝙸𝙻𝙴𝚂.
✰ 𝙵𝙾𝚁𝚆𝙰𝚁𝙳 𝚃𝙷𝙴 𝙻𝙰𝚂𝚃 𝙼𝙴𝚂𝙰𝙶𝙴 𝚃𝙾 𝙼𝙴 𝚆𝙸𝚃𝙷 𝚀𝚄𝙾𝚃𝙴𝚂.

 𝙸'𝙻𝙻 𝙰𝙳𝙳 𝙰𝙻𝙻 𝙵𝙸𝙻𝙴𝚂 𝙸𝙽 𝚃𝙷𝙰𝚃 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚃𝙾 𝙼𝚈 𝙳𝙱."""
    CONNECTION_TXT = """➤ 𝙷𝙴𝙻𝙿: <b>𝙲𝙾𝙽𝙽𝙴𝙲𝚃𝙸𝙾𝙽𝚂</b>

✯ 𝚄𝚂𝙴𝙳 𝚃𝙾 𝙲𝙾𝙽𝙽𝙴𝙲𝚃 𝙱𝙾𝚃 𝚃𝙾 𝙿𝙼 𝙵𝙾𝚁 𝙼𝙰𝙽𝙰𝙶𝙸𝙽𝙶 𝙵𝙸𝙻𝚃𝙴𝚁𝚂.
✯ 𝙸𝚃 𝙷𝙴𝙻𝙿𝚂 𝚃𝙾 𝙰𝚅𝙾𝙸𝙳 𝚂𝙿𝙰𝙼𝙼𝙸𝙽𝙶 𝙸𝙽 𝙶𝚁𝙾𝚄𝙿𝚂.

<b>𝙽𝙾𝚃𝙴:</b>
✸ 𝙾𝙽𝙻𝚈 𝙰𝙳𝙼𝙸𝙽𝚂 𝙲𝙰𝙽 𝙰𝙳𝙳 𝙰 𝙲𝙾𝙽𝙽𝙴𝙲𝚃𝙸𝙾𝙽.
✸ 𝚂𝙴𝙽𝙳 <code>/connect</code> 𝙵𝙾𝚁 𝙲𝙾𝙽𝙽𝙴𝙲𝚃𝙸𝙽𝙶 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙿𝙼.

<b>𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙰𝙽𝙳 𝚄𝚂𝙰𝙶𝙴:</b>
✯ /connect  - <code>𝙲𝙾𝙽𝙽𝙴𝙲𝚃 𝙰 𝙿𝙰𝚁𝚃𝙸𝙲𝚄𝙻𝙰𝚁 𝙲𝙷𝙰𝚃 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙿𝙼</code>
✯ /disconnect  - <code>𝙳𝙸𝚂𝙲𝙾𝙽𝙽𝙴𝙲𝚃 𝙵𝚁𝙾𝙼 𝙰 𝙲𝙷𝙰𝚃</code>
✯ /connections - <code>𝙻𝙸𝚂𝚃 𝙰𝙻𝙻 𝚈𝙾𝚄𝚁 𝙲𝙾𝙽𝙽𝙴𝙲𝚃𝙸𝙾𝙽𝚂</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>𝙽𝙾𝚃𝙴:</b>

𝚃𝙷𝙴𝚂𝙴 𝙰𝚁𝙴 𝚃𝙷𝙴 𝙴𝚇𝚃𝚁𝙰 𝙵𝙴𝙰𝚃𝚄𝚁𝙴𝚂 

<b>𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙰𝙽𝙳 𝚄𝚂𝙰𝙶𝙴:</b>

✯ /id - <code>𝚃𝙾 𝙶𝙴𝚃 𝙸𝙳 𝙾𝙵 𝙰 𝚂𝙿𝙴𝙲𝙸𝙵𝙸𝙴𝙳 𝚄𝚂𝙴𝚁.</code>
✯ /info  - <code>𝙶𝙴𝚃 𝙸𝙽𝙵𝙾𝚁𝙼𝙰𝚃𝙸𝙾𝙽 𝙰𝙱𝙾𝚄𝚃 𝙰 𝚄𝚂𝙴𝚁.</code>
✯ /imdb  - <code>𝙶𝙴𝚃 𝚃𝙷𝙴 𝙵𝙻𝙸𝙼 𝙸𝙽𝙵𝙾𝚁𝙼𝙰𝚃𝙸𝙾𝙽 𝙵𝙾𝚁 𝙸𝙼𝙳𝙱 𝚂𝙾𝚄𝚁𝙲𝙴.</code>
✯ /search  - <code>𝙶𝙴𝚃 𝚃𝙷𝙴 𝙵𝙻𝙸𝙼 𝙸𝙽𝙵𝙾𝚁𝙼𝙰𝚃𝙸𝙾𝙽 𝙵𝚁𝙾𝙼 𝚅𝙰𝚁𝙸𝙾𝚄𝚂 𝚂𝙾𝚄𝚁𝙲𝙴𝚂.</code>"""
    ADMIN_TXT = """➤ 𝙷𝙴𝙻𝙿: <b>𝙰𝙳𝙼𝙸𝙽 𝙼𝙾𝙳𝚂</b>

<b>𝙽𝙾𝚃𝙴:</b>

𝚃𝙷𝙸𝚂 𝙼𝙾𝙳𝚄𝙻𝙴 𝚆𝙾𝚁𝙺𝚂 𝙾𝙽𝙻𝚈 𝙵𝙾𝚁 𝙰𝙳𝙼𝙸𝙽𝚂

<b>𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙰𝙽𝙳 𝚄𝚂𝙰𝙶𝙴:</b>

✯ /logs - <code>𝚃𝙾 𝙶𝙴𝚃 𝚃𝙷𝙴 𝚁𝙴𝚂𝙲𝙴𝙽𝚃 𝙴𝚁𝚁𝙾𝚁𝚂</code>
✯ /stats - <code>𝚃𝙾 𝙶𝙴𝚃 𝚃𝙷𝙴 𝚂𝚃𝙰𝚃𝚄𝚂 𝙾𝙵 𝙵𝙸𝙻𝙴𝚂 𝙸𝙽 𝙳𝙱.</code>
✯ /delete - <code>𝚃𝙾 𝙳𝙴𝙻𝙴𝚃𝙴 𝙰 𝚂𝙿𝙴𝙲𝙸𝙵𝙸𝙲 𝙵𝙸𝙻𝙴 𝙵𝚁𝙾𝙼 𝙳𝙱.</code>
✯ /users - <code>𝚃𝙾 𝙶𝙴𝚃 𝙻𝙸𝚂𝚃 𝙾𝙵 𝙼𝚈 𝚄𝚂𝙴𝚁𝚂 𝙰𝙽𝙳 𝙸𝙳𝚂.</code>
✯ /chats - <code>𝚃𝙾 𝙶𝙴𝚃 𝙻𝙸𝚂𝚃 𝙾𝙵 𝚃𝙷𝙴 𝙼𝚈 𝙲𝙷𝙰𝚃𝚂 𝙰𝙽𝙳 𝙸𝙳𝚂.</code>
✯ /leave  - <code>𝚃𝙾 𝙻𝙴𝙰𝚅𝙴 𝙵𝚁𝙾𝙼 𝙰 𝙲𝙷𝙰𝚃.</code>
✯ /disable  -  <code>𝚃𝙾 𝙳𝙸𝚂𝙰𝙱𝙻𝙴 𝙰 𝙲𝙷𝙰𝚃.</code>
✯ /ban_user  - <code>𝚃𝙾 𝙱𝙰𝙽 𝙰 𝚄𝚂𝙴𝚁.</code>
✯ /unban_user  - <code>𝚃𝙾 𝚄𝙽𝙱𝙰𝙽 𝙰 𝚄𝚂𝙴𝚁.</code>
✯ /channel - <code>𝚃𝙾 𝙶𝙴𝚃 𝙻𝙸𝚂𝚃 𝙾𝙵 𝚃𝙾𝚃𝙰𝙻 𝙲𝙾𝙽𝙽𝙴𝙲𝚃𝙴𝙳 𝙲𝙷𝙰𝙽𝙽𝙴𝙻𝚂.</code>
✯ /broadcast - <code>𝚃𝙾 𝙱𝚁𝙾𝙳𝙲𝙰𝚂𝚃 𝙰 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝚃𝙾 𝙰𝙻𝙻 𝚄𝚂𝙴𝚁𝚂.</code>"""
    STATUS_TXT = """<b>᚛› 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code></b>
<b>✫ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code></b>
<b>✫ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code></b>
<b>✫ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝙱</b>
<b>✫ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝙱</b>"""
    LOG_TEXT_G = """#𝐍𝐞𝐰𝐆𝐫𝐨𝐮𝐩
    
<b>᚛› 𝙶𝚁𝙾𝚄𝙿 ⪼ {}(<code>{}</code>)</b>
<b>᚛› 𝚃𝙾𝚃𝙰𝙻 𝙼𝙴𝙼𝙱𝙴𝚁𝚂 ⪼ <code>{}</code></b>
<b>᚛› 𝙰𝙳𝙳𝙴𝙳 𝙱𝚈 ⪼ {}</b>
"""
    LOG_TEXT_P = """#𝐍𝐞𝐰𝐔𝐬𝐞𝐫
    
<b>᚛› 𝐈𝐃 - <code>{}</code></b>
<b>᚛› 𝐍𝐚𝐦𝐞 - {}</b>
"""
    REPORT_TXT = """➤ 𝙷𝙴𝙻𝙿: 𝚁𝙴𝙿𝙾𝚁𝚃 ⚠️

𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙷𝙴𝙻𝙿 𝚈𝙾𝚄 𝚃𝙾 𝚁𝙴𝙿𝙾𝚁𝚃 𝙰 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝙾𝚁 𝙰 𝚄𝚂𝙴𝚁 𝚃𝙾 𝚃𝙷𝙴 𝚁𝙴𝚂𝙿𝙴𝙲𝚃𝙸𝚅𝙴 𝙶𝚁𝙾𝚄𝙿 𝙰𝙳𝙼𝙸𝙽𝚂.𝙳𝙾𝙽'𝚃 𝙼𝙸𝚂𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳.

➤ 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙰𝙽𝙳 𝚄𝚂𝙰𝙶𝙴 :

➪/report 𝗈𝗋 @admins - 𝚃𝙾 𝚁𝙴𝙿𝙾𝚁𝚃 𝙰 𝚄𝚂𝙴𝚁 𝚃𝙾 𝚃𝙷𝙴 𝙰𝙳𝙼𝙸𝙽𝚂 (𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰 𝙼𝙴𝚂𝚂𝙰𝙶𝙴)."""

    CORONA_TXT = """➤ 𝙷𝙴𝙻𝙿: 𝙲𝙾𝚅𝙸𝙳

𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 𝙷𝙴𝙻𝙿𝚂 𝚈𝙾𝚄 𝙺𝙽𝙾𝚆 𝙳𝙰𝙸𝙻𝚈 𝙸𝙽𝙵𝙾𝚁𝙼𝙰𝚃𝙸𝙾𝙽 𝙰𝙱𝙾𝚄𝚃 𝙲𝙾𝚅𝙸𝙳

➤ 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙰𝙽𝙳 𝚄𝚂𝙰𝙶𝙴:

➪ /covid - 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 𝚆𝙸𝚃𝙷 𝚈𝙾𝚄𝚁 𝙲𝙾𝚄𝙽𝚃𝚁𝚈 𝙽𝙰𝙼𝙴 𝚃𝙾 𝙶𝙴𝚃 𝙲𝙾𝚅𝙸𝙳 𝙸𝙽𝙵𝙾𝚁𝙼𝙰𝚃𝙸𝙾𝙽

✎ 𝙴𝚇𝙰𝙼𝙿𝙻𝙴:

/covid 𝖨𝗇𝖽𝗂𝖺"""

    URLSHORT_TXT = """➤ 𝙷𝙴𝙻𝙿: 𝚄𝚁𝙻 𝚂𝙷𝙾𝚁𝚃𝙽𝙴𝚁

𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 𝙷𝙴𝙻𝙿𝚂 𝚈𝙾𝚄 𝚃𝙾 𝚂𝙷𝙾𝚁𝚃 𝙰 𝚄𝚁𝙻

➤ 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙰𝙽𝙳 𝚄𝚂𝙰𝙶𝙴 :

➪ /short: 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 𝚆𝙸𝚃𝙷 𝚈𝙾𝚄𝚁 𝙻𝙸𝙽𝙺 𝚃𝙾 𝙶𝙴𝚃 𝚂𝙷𝙾𝚁𝚃𝙴𝙳 𝙻𝙸𝙽𝙺𝚂

✎ 𝙴𝚇𝙰𝙼𝙿𝙻𝙴:

/short https://t.me/VK_LINKZ"""

    VIDEO_TXT ="""𝙷𝙴𝙻𝙿 𝚈𝙾𝚄 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝚅𝙸𝙳𝙴𝙾 𝙵𝚁𝙾𝙼 𝚈𝙾𝚄𝚃𝚄𝙱𝙴.

• 𝚄𝚂𝙰𝙶𝙴

𝚈𝙾𝚄 𝙲𝙰𝙽 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙰𝙽𝚈 𝚅𝙸𝙳𝙴𝙾 𝙵𝚁𝙾𝙼 𝚈𝙾𝚄𝚃𝚄𝙱𝙴

🤔 𝙷𝙾𝚆 𝚃𝙾 𝚄𝚂𝙴

• 𝚃𝚈𝙿𝙴 /video or /mp4 𝙰𝙽𝙳 (𝚅𝙸𝙳𝙴𝙾 𝙻𝙸𝙽𝙺)

• 𝙴𝚇𝙰𝙼𝙿𝙻𝙴:

/𝘮𝘱4 https://youtu.be/Your Link"""

    ZOMBIES_TXT = """𝙷𝙴𝙻𝙿 𝚈𝙾𝚄 𝚃𝙾 𝙺𝙸𝙲𝙺 𝚄𝚂𝙴𝚁𝚂

<b>𝙺𝙸𝙲𝙺 𝙸𝙽𝙰𝙲𝚃𝙸𝚅𝙴 𝙼𝙴𝙼𝙱𝙴𝚁𝚂 𝙵𝚁𝙾𝙼 𝙶𝚁𝙾𝚄𝙿,𝙰𝙳𝙳 𝙼𝙴 𝙰𝚂 𝙰𝙳𝙼𝙸𝙽 𝚆𝙸𝚃𝙷 𝙱𝙰𝙽 𝚄𝚂𝙴𝚁𝚂 𝙿𝙴𝚁𝙼𝙸𝚂𝚂𝙸𝙾𝙽 𝙸𝙽 𝙶𝚁𝙾𝚄𝙿.</b>

<b>𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙰𝙽𝙳 𝚄𝚂𝙰𝙶𝙴:</b>

✯ /inkick - 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 𝚆𝙸𝚃𝙷 𝚁𝙴𝚀𝚄𝙸𝚁𝙴𝙳 𝙰𝚁𝙶𝚄𝙼𝙽𝙴𝚃𝚂 𝙰𝙽𝙳 𝙸 𝚆𝙸𝙻𝙻 𝙺𝙸𝙲𝙺 𝙼𝙴𝙼𝙱𝙴𝚁𝚂 𝙵𝚁𝙾𝙼 𝙶𝚁𝙾𝚄𝙿.
✯ /instatus - 𝚃𝙾 𝙲𝙷𝙴𝙲𝙺  𝙲𝚄𝚁𝚁𝙴𝙽𝚃 𝚂𝚃𝙰𝚃𝚄𝚂 𝙾𝙵 𝙲𝙷𝙰𝚃 𝙼𝙴𝙼𝙱𝙴𝚁 𝙵𝚁𝙾𝙼 𝙶𝚁𝙾𝚄𝙿.
✯ /inkick within_month long_time_ago - 𝚃𝙾 𝙺𝙸𝙲𝙺 𝙼𝙴𝙼𝙱𝙴𝚁𝚂 𝚆𝙷𝙾 𝙰𝚁𝙴 𝙾𝙵𝙵𝙻𝙸𝙽𝙴 𝙵𝙾𝚁 𝙼𝙾𝚁𝙴 𝚃𝙷𝙰𝙽 6 - 7 𝙳𝙰𝚈𝚂.
✯ /inkick long_time_ago - 𝚃𝙾 𝙺𝙸𝙲𝙺 𝙼𝙴𝙼𝙱𝙴𝚁𝚂 𝚆𝙷𝙾 𝙰𝚁𝙴 𝙾𝙵𝙵𝙻𝙸𝙽𝙴 𝙵𝙾𝚁 𝙼𝙾𝚁𝙴 𝚃𝙷𝙰𝙽 𝙰 𝙼𝙾𝙽𝚃𝙷 𝙰𝙽𝙳 𝙳𝙴𝙻𝙴𝚃𝙴𝙳 𝙰𝙲𝙲𝙾𝚄𝙽𝚃𝚂.
✯ /dkick - 𝚃𝙾 𝙺𝙸𝙲𝙺 𝙳𝙴𝙻𝙴𝚃𝙴𝙳 𝙰𝙲𝙲𝙾𝚄𝙽𝚃𝚂."""

    IMAGE_TXT = """➤ 𝙷𝙴𝙻𝙿: 𝙸𝙼𝙰𝙶𝙴

𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 𝙷𝙴𝙻𝙿𝚂 𝚈𝙾𝚄 𝚃𝙾 𝙴𝙳𝙸𝚃 𝙰 𝙸𝙼𝙰𝙶𝙴 𝚅𝙴𝚁𝚈 𝙴𝙰𝚂𝙸𝙻𝚈

➤ 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙰𝙽𝙳 𝚄𝚂𝙰𝙶𝙴:

➪ 𝙹𝚄𝚂𝚃 𝚂𝙴𝙽𝙳 𝙼𝙴 𝙰 𝙸𝙼𝙰𝙶𝙴 𝚃𝙾 𝙴𝙳𝙸𝚃 🤳

𝙼𝙰𝙳𝙴 𝙱𝚈 <a href=https://telegram.dog/heart_recipe>➳ ✰ 𝑶𝒐 𝑰𝒕'𝒔 𝑴𝒆 🤦</a>"""

    STICKER_TXT = """𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙼𝙾𝙳𝚄𝙻𝙴 𝚃𝙾 𝙵𝙸𝙽𝙳 𝙰𝙽𝚈 𝚂𝚃𝙸𝙲𝙺𝙴𝚁𝚂 𝙸𝙳.

❂ 𝚄𝚂𝙰𝙶𝙴

𝚃𝙾 𝙶𝙴𝚃 𝚂𝚃𝙸𝙲𝙺𝙴𝚁 𝙸𝙳
 
  🤔 𝙷𝙾𝚆 𝚃𝙾 𝚄𝚂𝙴
 
➳ 𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰𝙽𝚈 𝚂𝚃𝙸𝙲𝙺𝙴𝚁 [/stickerid]"""

    YTTHUMB_TXT = """𝙷𝙴𝙻𝙿𝚂 𝚃𝙾 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝙰𝙽𝚈 𝚈𝙾𝚄𝚃𝚄𝙱𝙴 𝚅𝙸𝙳𝙴𝙾 𝚃𝙷𝚄𝙼𝙱𝙽𝙰𝙸𝙻
    
🤔 𝙷𝙾𝚆 𝚃𝙾 𝚄𝚂𝙴

𝚃𝚈𝙿𝙴 /ytthumb 𝙰𝙽𝙳 𝚅𝙸𝙳𝙴𝙾 𝙻𝙸𝙽𝙺

✎ 𝙴𝚇𝙰𝙼𝙿𝙻𝙴

/ytthumb https://youtu.be/yourlink"""

    ABOOK_TXT = """➤ 𝙷𝙴𝙻𝙿: 𝙰𝚄𝙳𝙸𝙾𝙱𝙾𝙾𝙺

𝚈𝙾𝚄 𝙲𝙰𝙽 𝙲𝙾𝙽𝚅𝙴𝚁𝚃 𝙰 𝙿𝙳𝙵 𝙵𝙸𝙻𝙴 𝚃𝙾 𝙰 𝙰𝚄𝙳𝙸𝙾 𝙵𝙸𝙻𝙴 𝚆𝙸𝚃𝙷 𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 ✯

➤ 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙰𝙽𝙳 𝚄𝚂𝙰𝙶𝙴:

➪ /audiobook: 𝚁𝙴𝙿𝙻𝚈 𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 𝚆𝙸𝚃𝙷 𝙰𝙽𝚈 𝙿𝙳𝙵 𝚃𝙾 𝙶𝙴𝙽𝙴𝚁𝙰𝚃𝙴 𝚃𝙷𝙴 𝙰𝚄𝙳𝙸𝙾"""

    GTRANS_TXT = """➤ 𝙷𝙴𝙻𝙿: 𝙶𝙾𝙾𝙶𝙻𝙴 𝚃𝚁𝙰𝙽𝚂𝙻𝙰𝚃𝙴𝚁

𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 𝙷𝙴𝙻𝙿𝚂 𝚈𝙾𝚄 𝚃𝙾 𝚃𝚁𝙰𝙽𝚂𝙻𝙰𝚃𝙴 𝙰 𝚃𝙴𝚇𝚃 𝚃𝙾 𝙰𝙽𝚈 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴𝚂 𝚈𝙾𝚄 𝚆𝙰𝙽𝚃.𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 𝚆𝙾𝚁𝙺𝚂 𝙸𝙽 𝙱𝙾𝚃𝙷 𝙿𝙼 𝙰𝙽𝙳 𝙶𝚁𝙾𝚄𝙿 ✯

➤ 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙰𝙽𝙳 𝚄𝚂𝙰𝙶𝙴:

➪/tr - 𝚃𝙾 𝚃𝚁𝙰𝙽𝚂𝙻𝙰𝚃𝙴 𝚃𝙴𝚇𝚃𝚂 𝚃𝙾 𝙰 𝚂𝙿𝙴𝙲𝙸𝙵𝙸𝙲 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴

➤ 𝙽𝙾𝚃𝙴:
𝚆𝙷𝙸𝙻𝙴 𝚄𝚂𝙸𝙽𝙶 /tr 𝚈𝙾𝚄 𝚂𝙷𝙾𝚄𝙻𝙳 𝚂𝙿𝙴𝙲𝙸𝙵𝚈 𝚃𝙷𝙴 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴 𝙲𝙾𝙳𝙴

✎ 𝙴𝚇𝙰𝙼𝙿𝙻𝙴: /𝗍𝗋 𝗆𝗅
 • 𝖾𝗇 = 𝙴𝙽𝙶𝙻𝙸𝚂𝙷
 • 𝗆𝗅 = 𝙼𝙰𝙻𝙰𝚈𝙰𝙻𝙰𝙼
 • 𝗁𝗂 = 𝙷𝙸𝙽𝙳𝙸"""

    RESTRIC_TXT = """➤ 𝙷𝙴𝙻𝙿: 𝙼𝚄𝚃𝙴 🚫

𝚃𝙷𝙴𝚂𝙴 𝙰𝚁𝙴 𝚃𝙷𝙴 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂 𝙵𝙾𝚁 𝙰 𝙶𝚁𝙾𝚄𝙿 𝙰𝙳𝙼𝙸𝙽 𝚆𝙷𝙸𝙲𝙷 𝙲𝙰𝙽 𝚄𝚂𝙴 𝚃𝙾 𝙼𝙰𝙽𝙰𝙶𝙴 𝚃𝙷𝙴𝙸𝚁 𝙶𝚁𝙾𝚄𝙿 𝙴𝙵𝙵𝙸𝙲𝙸𝙴𝙽𝚃𝙻𝚈.

➪/ban: 𝚃𝙾 𝙱𝙰𝙽 𝙰 𝚄𝚂𝙴𝚁 𝙵𝚁𝙾𝙼 𝚃𝙷𝙴 𝙶𝚁𝙾𝚄𝙿.
➪/unban: 𝚃𝙾 𝚄𝙽𝙱𝙰𝙽 𝙰 𝚄𝚂𝙴𝚁 𝙸𝙽 𝚃𝙷𝙴 𝙶𝚁𝙾𝚄𝙿.
➪/tban: 𝚃𝙾 𝚃𝙴𝙼𝙿𝙾𝚁𝙰𝚁𝙸𝙻𝚈 𝙱𝙰𝙽 𝙰 𝚄𝚂𝙴𝚁.
➪/mute: 𝚃𝙾 𝙼𝚄𝚃𝙴 𝙰 𝚄𝚂𝙴𝚁 𝙸𝙽 𝚃𝙷𝙴 𝙶𝚁𝙾𝚄𝙿.
➪/unmute: 𝚃𝙾 𝚄𝙽𝙼𝚄𝚃𝙴 𝚃𝙷𝙴 𝚄𝚂𝙴𝚁 𝙸𝙽 𝚃𝙷𝙴 𝙶𝚁𝙾𝚄𝙿.
➪/tmute: 𝚃𝙾 𝚃𝙴𝙼𝙿𝙾𝚁𝙰𝚁𝙸𝙻𝚈 𝙼𝚄𝚃𝙴 𝙰 𝚄𝚂𝙴𝚁.

➤ 𝙽𝙾𝚃𝙴:
𝚆𝙷𝙸𝙻𝙴 𝚄𝚂𝙸𝙽𝙶 /tmute 𝗈𝗋 /tban 𝚈𝙾𝚄 𝚂𝙷𝙾𝚄𝙻𝙳 𝚂𝙿𝙴𝙲𝙸𝙵𝚈 𝚃𝙷𝙴 𝚃𝙸𝙼𝙴 𝙻𝙸𝙼𝙸𝚃.

✎ 𝙴𝚇𝙰𝙼𝙿𝙻𝙴: /𝗍𝖻𝖺𝗇 2𝖽 𝗈𝗋 /𝗍𝗆𝗎𝗍𝖾 2𝖽.
𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝚅𝙰𝙻𝚄𝙴𝚂: 𝗆/𝗁/𝖽. 
 • 𝗆 = 𝙼𝙸𝙽𝚄𝚃𝙴𝚂
 • 𝗁 = 𝙷𝙾𝚄𝚁𝚂
 • 𝖽 = 𝙳𝙰𝚈𝚂"""
    CREATOR_REQUIRED = """❗<b>𝚈𝙾𝚄 𝙷𝙰𝚅𝙴 𝚃𝙾 𝙱𝙴 𝚃𝙷𝙴 𝙶𝚁𝙾𝚄𝙿 𝙲𝚁𝙴𝙰𝚃𝙾𝚁 𝚃𝙾 𝙳𝙾 𝚃𝙷𝙰𝚃.</b>"""
      
    INPUT_REQUIRED = "❗ **𝙰𝚁𝙶𝚄𝙼𝙴𝙽𝚃𝚂 𝚁𝙴𝚀𝚄𝙸𝚁𝙴𝙳**"
      
    KICKED = """✔️ 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝙺𝙸𝙲𝙺𝙴𝙳 {} 𝙼𝙴𝙼𝙱𝙴𝚁𝚂 𝙰𝙲𝙲𝙾𝚁𝙳𝙸𝙽𝙶 𝚃𝙾 𝚃𝙷𝙴 𝙰𝚁𝙶𝚄𝙼𝙽𝙴𝚃𝚂 𝙿𝚁𝙾𝚅𝙸𝙳𝙴𝙳."""
      
    START_KICK = """🚮 𝚁𝙴𝙼𝙾𝚅𝙸𝙽𝙶 𝙸𝙽𝙰𝙲𝚃𝙸𝚅𝙴 𝙼𝙴𝙼𝙱𝙴𝚁𝚂 𝚃𝙷𝙸𝚂 𝙼𝙰𝚈 𝚃𝙰𝙺𝙴 𝙰 𝚆𝙷𝙸𝙻𝙴..."""
      
    ADMIN_REQUIRED = """❗<b>𝙸 𝚆𝙸𝙻𝙻 𝙽𝙾𝚃 𝙶𝙾 𝚃𝙷𝙴 𝙿𝙻𝙰𝙲𝙴 𝚆𝙷𝙴𝚁𝙴 𝚈𝙾𝚄 𝙳𝙸𝙳𝙽'𝚃 𝙼𝙰𝙳𝙴 𝙼𝙴 𝙰𝙳𝙼𝙸𝙽🥵..𝚂𝙾 𝙰𝙳𝙳 𝙼𝙴 𝙰𝙶𝙸𝙰𝙽 𝚆𝙸𝚃𝙷 𝙵𝚄𝙻𝙻 𝙰𝙳𝙼𝙸𝙽 𝚁𝙸𝙶𝙷𝚃𝚂..🧐</b>"""
      
    DKICK = """✔️ 𝙺𝙸𝙲𝙺𝙴𝙳 {} 𝙳𝙴𝙻𝙴𝚃𝙴𝙳 𝙰𝙲𝙲𝙾𝚄𝙽𝚃𝚂 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈."""
      
    FETCHING_INFO = """<b>💖 𝙻𝙴𝚃'𝚂 𝙱𝙴𝙰𝚃 𝙸𝚃 𝙰𝙻𝙻 𝙽𝙾𝚆...</b>"""
      
    STATUS = """{}\n<b>Chat Member Status</b>**\n\n```<i>Recently``` - {}\n```Within Week``` - {}\n```Within Month``` - {}\n```Long Time Ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}</i>
"""
