from eth_account import Account
import json
import os

class WalletEngine:
    def __init__(self):
        self.wallets = {}
        self.token_ledger = {}
        self.store_path = "wallet_store.json"
        Account.enable_unaudited_hdwallet_features()

    def create_wallet(self, name: str):
        acct = Account.create()
        self.wallets[name] = {
            "address": acct.address,
            "private_key": acct.key.hex()
        }
        self._store_wallets()
        return self.wallets[name]

    def _store_wallets(self):
        with open(self.store_path, "w") as f:
            json.dump(self.wallets, f)

    def define_token(self, name: str, supply: int, symbol: str):
        self.token_ledger[symbol] = {
            "name": name,
            "total_supply": supply,
            "holders": {}
        }

    def assign_tokens(self, symbol: str, address: str, amount: int):
        if symbol in self.token_ledger:
            self.token_ledger[symbol]["holders"][address] = amount

    def export_wallets(self):
        return json.dumps(self.wallets, indent=2)

    def export_tokens(self):
        return json.dumps(self.token_ledger, indent=2)