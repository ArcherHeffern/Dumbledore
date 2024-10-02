from pathlib import Path
from models.backend_models import Account, AccountId, AccountPermission, AccountStatus

from backend.dal import SQLiteStorage


if __name__ == "__main__":
    service = SQLiteStorage.connect(Path("./db"))
    account = Account(
        AccountId(2), "tim", "tim@gmail.com", "123", AccountStatus.UNREGISTERED, AccountPermission.ADMIN
    )
    service.account_dal.create_account(account)
    service.account_dal.get_account(AccountId(1))
    service.account_dal.get_account(AccountId(2))
