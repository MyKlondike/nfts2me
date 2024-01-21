import asyncio
import random

from web3 import AsyncWeb3
from web3.middleware import async_geth_poa_middleware

from config import RPC
from settings import CHECK_GWEI, MAX_GWEI, CHAIN
from loguru import logger

async def get_gas():
    try:
        w3 = AsyncWeb3(
            AsyncWeb3.AsyncHTTPProvider(random.choice(RPC["ethereum"]["rpc"])),
            middlewares=[async_geth_poa_middleware],
        )

        gas_price = await w3.eth.gas_price
        gwei = w3.from_wei(gas_price, 'gwei')

        return gwei
    except Exception as error:
        logger.error(error)


async def get_base_gas():
    try:
        w3 = AsyncWeb3(
            AsyncWeb3.AsyncHTTPProvider(random.choice(RPC[CHAIN]["rpc"])),
            middlewares=[async_geth_poa_middleware],
        )

        gas_price = await w3.eth.gas_price
        gwei = w3.from_wei(gas_price, 'gwei')

        return gwei
    except Exception as error:
        logger.error(error)

async def wait_gas():
    logger.info("Get GWEI")
    while True:
        gas = await get_gas()
        base_gase = await get_base_gas()

        if gas > MAX_GWEI or base_gase > 0.5:
            logger.info(f'Current GWEI: {gas} > {MAX_GWEI} or {CHAIN} gase > 0.5')
            await asyncio.sleep(60)
        else:
            logger.success(f"GWEI is normal | current: {gas} < {MAX_GWEI}")
            break


def check_gas(func):
    async def _wrapper(*args, **kwargs):
        if CHECK_GWEI:
            await wait_gas()
            await get_base_gas()
        return await func(*args, **kwargs)

    return _wrapper
