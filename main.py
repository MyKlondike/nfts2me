import random
import sys
import time
from loguru import logger

from config import ACCOUNTS
from settings import (
    RANDOM_WALLET,
    SLEEP_TO,
    SLEEP_FROM,
     REMOVE_WALLET,
)
from modules_settings import *
from utils.helpers import remove_wallet
from utils.sleeping import sleep
from utils.art import ascii_art, elka_art


async def run_module(module, account_id, key):
    try:
        await module(account_id, key)
    except Exception as e:
        logger.error(e)

    if REMOVE_WALLET:
        remove_wallet(key)

    await sleep(SLEEP_FROM, SLEEP_TO)


def get_wallets():
    wallets = [
        {
            "id": _id,
            "key": key,
        } for _id, key in enumerate(ACCOUNTS, start=1)
    ]

    return wallets

async def _async_run_module(module, account_id, key):
    await run_module(module, account_id, key)

async def main(module):
    wallets = get_wallets()

    if RANDOM_WALLET:
        random.shuffle(wallets)

    tasks = []

    for account in wallets:
        task = asyncio.create_task(
            _async_run_module(module, account.get("id"), account.get("key"))
        )
        tasks.append(task)

        await asyncio.sleep(random.randint(SLEEP_FROM, SLEEP_TO))

    await asyncio.gather(*tasks)

if __name__ == '__main__':
    print(elka_art)

    logger.add("logging.log")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(mint_nft))
    loop.close()
    print(ascii_art)
