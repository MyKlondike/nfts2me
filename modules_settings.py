import asyncio

from modules import *
from settings import NFTcontracts

async def mint_nft(account_id, key):

    contracts = NFTcontracts

    minter = Minter(account_id, key)
    await minter.mint_nft(contracts)
