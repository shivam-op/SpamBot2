from decouple import config
import logging
from telethon import TelegramClient
from telethon.sessions import StringSession
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# Basics
APP_ID = config("APP_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
BOT_TOKEN = config("BOT_TOKEN", default=None)


from os import getenv
#gj.

STRING = getenv("STRING")
STRING2 = getenv("STRING2")
STRING3 = getenv("STRING3")
STRING4 = getenv("STRING4")
STRING5 = getenv("STRING5")
STRING6 = getenv("STRING6")
STRING7 = getenv("STRING7")
STRING8 = getenv("STRING8")
STRING9 = getenv("STRING9")
STRING_10 = getenv("STRING_10")
API_ID = getenv("API_ID")
API_HASH = getenv("API_HASH")
BIO_MESSAGE = getenv("BIO")
PING_MESSAGE = getenv("PING_MESSAGE")
SUDO = list(map(int, getenv("SUDO").split()))

a = APP_ID
b = API_HASH
smex = STRING
smexx = STRING2
smexxx = STRING3
smexxxx = STRING4
smexxxxx = STRING5
sixth = STRING6
seven = STRING7
eight = STRING8
ninth = STRING9
tenth = STRING_10

otext = "© SpamBot"

que = {}

SMEX_USERS = []
for x in SUDO:
    SMEX_USERS.append(x)

async def start_bot():
    global idk
    global ydk
    global wdk
    global sdk
    global hdk
    global adk
    global bdk
    global cdk
    global ddk
    global edk
    if smex:
        session_name = str(smex)
        print("String 1 Found")
        idk = TelegramClient(StringSession(session_name), a, b)
        try:
            print(f"Starting Client 1 {otext}")
            await idk.start()
            botme = await idk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            idk = "smex"
            print(f"{e} for 1")
    else:
        print("Session 1 not Found")
        session_name = "startup"
        idk = TelegramClient(session_name, a, b)
        try:
            await idk.start()
        except Exception:
            pass

    if smexx:
        session_name = str(smexx)
        print("String 2 Found")
        ydk = TelegramClient(StringSession(session_name), a, b)
        try:
            print(f"Starting Client 2 {otext}")
            await ydk.start()
            botme = await ydk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(f"{e} for 2")
    else:
        print("Session 2 not Found")
        session_name = "startup"
        ydk = TelegramClient(session_name, a, b)
        try:
            await ydk.start()
        except Exception:
            pass

    if smexxx:
        session_name = str(smexxx)
        print(f"Starting Client 3 {otext}")
        wdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 3")
            await wdk.start()
            botme = await wdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(f"{e} for 3")
    else:
        print("Session 3 not Found")
        session_name = "startup"
        wdk = TelegramClient(session_name, a, b)
        try:
            await wdk.start()
        except Exception:
            pass

    if smexxxx:
        session_name = str(smexxxx)
        print("String 4 Found")
        hdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print(f"Starting Client 4 {otext}")
            await hdk.start()
            botme = await hdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(f"{e} for 4")
    else:
        print("Session 4 not Found")
        session_name = "startup"
        hdk = TelegramClient(session_name, a, b)
        try:
            await hdk.start()
        except Exception:
            pass

    if smexxxxx:
        session_name = str(smexxxxx)
        print("String 5 Found")
        sdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print(f"Starting Client 5 {otext}")
            await sdk.start()
            botme = await sdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(f"{e} for 5")
    else:
        print("Session 5 not Found")
        session_name = "startup"
        sdk = TelegramClient(session_name, a, b)
        try:
            await sdk.start()
        except Exception:
            pass

    if sixth:
        session_name = str(sixth)
        print(f"String 6 Found")
        adk = TelegramClient(StringSession(session_name), a, b)
        try:
            print(f"Starting Client 6 {otext}")
            await adk.start()
            botme = await adk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(f"{e} for 6")
    else:
        print("Session 6 not Found")
        session_name = "startup"
        adk = TelegramClient(session_name, a, b)
        try:
            await adk.start()
        except Exception:
            pass

    if seven:
        session_name = str(seven)
        print("String 7 Found")
        bdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print(f"Starting Client 7 {otext}")
            await bdk.start()
            botme = await bdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(f"{e} for 7")
    else:
        print("Session 7 not Found")
        session_name = "startup"
        bdk = TelegramClient(session_name, a, b)
        try:
            await bdk.start()
        except Exception:
            pass

    if eight:
        session_name = str(eight)
        print("String 8 Found")
        cdk = TelegramClient(StringSession(session_name), a, b)
        try:
            print(f"Starting Client 8 {otext}")
            await cdk.start()
            botme = await cdk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(f"{e} for 8")
    else:
        print("Session 8 not Found")
        session_name = "startup"
        cdk = TelegramClient(session_name, a, b)
        try:
            await cdk.start()
        except Exception:
            pass

    if ninth:
        session_name = str(ninth)
        print("String 9 Found")
        ddk = TelegramClient(StringSession(session_name), a, b)
        try:
            print(f"Starting Client 9 {otext}")
            await ddk.start()
            botme = await ddk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(f"{e} for 9")
    else:
        print("Session 9 not Found")
        session_name = "startup"
        ddk = TelegramClient(session_name, a, b)
        try:
            await ddk.start()
        except Exception:
            pass

    if tenth:
        session_name = str(tenth)
        print("String 10 Found")
        edk = TelegramClient(StringSession(session_name), a, b)
        try:
            print(f"Starting Client 10 {otext}")
            await edk.start()
            botme = await edk.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            print(f"{e} for 10")
    else:
        print("Session 10 not Found")
        session_name = "startup"
        edk = TelegramClient(session_name, a, b)
        try:
            await edk.start()
        except Exception:
            pass


loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())


