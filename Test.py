from persistent_small_town_teller import Person, Account, Bank


zc_bank = Bank()
bob = Person(1, "Bob", "Smith")
tim = Person(2, "Tim", "Linkous")
zc_bank.add_customer(tim)
zc_bank.add_customer(bob)
tim_checking = Account(1002, "CHECKING", tim)
bob_savings = Account(1001, "SAVINGS", bob)
zc_bank.add_account(bob_savings)
zc_bank.add_account(tim_checking)
zc_bank.balance_inquiry(1001)
zc_bank.balance_inquiry(1002)
# 0
zc_bank.deposit(1001, 256.02)
zc_bank.deposit(1002, 1_000_000.01)
zc_bank.balance_inquiry(1001)
zc_bank.balance_inquiry(1002)
# 256.02
zc_bank.withdrawal(1001, 128)
zc_bank.withdrawal(1002, 500_123.01)
zc_bank.balance_inquiry(1001)
zc_bank.balance_inquiry(1002)

# 128.02