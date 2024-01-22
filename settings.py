# RANDOM WALLETS MODE
RANDOM_WALLET = True  # True/False

# removing a wallet from the list after the job is done
REMOVE_WALLET = True  # True/False

SLEEP_FROM = 100  # Second
SLEEP_TO = 10000  # Second

# NFTcontracts - list NFT contract addresses

CHAIN = "base"

NFTcontracts = ["0x60F5731b303B3C738f1a615002fD45f15aFd9A15", "0x874ECca99028411a3Ac1c48473667ce7dBCE37dA",
                "0xE6d91Cd3cC34FC1651B1b266076371069803541a", "0xaB7f4b31f428Da842e79468334810DD37Ca042C4",
                "0xE426Bf233976118f6C73dF69A96e75d7E5A155ce",
                ]

# GWEI CONTROL MODE
CHECK_GWEI = True  # True/False
MAX_GWEI = 40

GAS_PRIORITY_FEE = {
    "ethereum": 0.05,
    "base": 0.001,
    "scroll": 0.41,
    "zksync": 0.1,
    "zora": 0.0005,
}

GAS_MULTIPLIER = 1.3

# RETRY MODE
RETRY_COUNT = 0
