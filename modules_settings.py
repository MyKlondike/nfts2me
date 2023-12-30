import asyncio

from modules import *


async def mint_nft(account_id, key):

    contracts = ["0x903cdC733ABdf4e405Ec3DFDb0997Fe13554Ce24"]

    minter = Minter(account_id, key)
    await minter.mint_nft(contracts)
