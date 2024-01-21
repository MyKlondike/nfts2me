import asyncio

from modules import *


async def mint_nft(account_id, key):
    """
    Mint NFT on NFTS2ME
    ______________________________________________________
    contracts - list NFT contract addresses
    """

    contracts = ["0x0f521a264AEF763BEf6C2cc801C609ca7a1e3498", "0x834e111D46378B2AB15E96B52Bb5390b77FB84F1",
                 "0x1cDB5C9094DA645892A32b5DE593ef32965CE785", "0x056Ff28Bb574b971954BdEF378d254054c6dC23c",
                 "0x43Ab7465c802Ea8c74AB8C5C5F04F952D4860f53", "0x3d814F24Ab9D12b9d5d24F1963227a1F7CaB9109"
                ]

    minter = Minter(account_id, key)
    await minter.mint_nft(contracts)
