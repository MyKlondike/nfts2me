# RANDOM WALLETS MODE
RANDOM_WALLET = True  # True/False

# removing a wallet from the list after the job is done
REMOVE_WALLET = True  # True/False

SLEEP_FROM = 100  # Second
SLEEP_TO = 300  # Second

CHAIN = "zksync"

# GWEI CONTROL MODE
CHECK_GWEI = True  # True/False
MAX_GWEI = 20

GAS_PRIORITY_FEE = {
    "ethereum": 0.05,
    "base": 0.001,
"scroll": 0.41,
"zksync": 0.1,
}

GAS_MULTIPLIER = 1.3

# RETRY MODE
RETRY_COUNT = 0
