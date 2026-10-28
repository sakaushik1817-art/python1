Algorithm
1. Start.
2. Input the opening balance and validate it.
3. Input the number of transactions.
4. Initialize total deposits, total withdrawals, and rejected transaction count to zero.
5. Repeat for each transaction:
   - Input transaction type and amount.
   - Reject the transaction if the amount is not positive.
   - If it is a deposit, add the amount to the balance and deposit total.
   - If it is a withdrawal, check the withdrawal limit and available balance.
   - Process a valid withdrawal or reject an invalid one.
   - Display the current balance.
6. Display total deposits, total withdrawals, rejected transactions, and final balance.
7. Stop.
Flowchart
START

Input opening balance and transaction count
Initialize balance totals and rejected count
Input transaction type and amount
Valid amount?

If no, reject the transaction.
Deposit or withdrawal?

Deposit: add to balance. Withdrawal: check limit and available funds.
Update balance and transaction totals; repeat until all transactions are processed
Display transaction summary and final balance
STOP

balance = float(input("Enter opening balance: "))
limit = 10000

deposits = 0
withdrawals = 0
rejected = 0

if balance < 0:
    print("Invalid opening balance")

else:
    n = int(input("Enter number of transactions: "))

    if n <= 0:
        print("Invalid number of transactions")

    else:
        for i in range(n):
            print("\n1. Deposit")
            print("2. Withdraw")

            choice = int(input("Enter transaction type: "))
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Rejected: Invalid amount")
                rejected += 1

            elif choice == 1:
                balance += amount
                deposits += amount
                print("Deposit successful")

            elif choice == 2:
                if amount > limit:
                    print("Rejected: Withdrawal limit exceeded")
                    rejected += 1
                elif amount > balance:
                    print("Rejected: Insufficient balance")
                    rejected += 1
                else:
                    balance -= amount
                    withdrawals += amount
                    print("Withdrawal successful")

            else:
                print("Rejected: Invalid transaction type")
                rejected += 1

            print("Current balance =", round(balance, 2))

        print("\n--- ATM TRANSACTION SUMMARY ---")
        print("Total Deposits =", round(deposits, 2))
        print("Total Withdrawals =", round(withdrawals, 2))
        print("Rejected Transactions =", rejected)
        print("Final Balance =", round(balance, 2))


Enter opening balance: 5000
Enter number of transactions: 4

1. Deposit
2. Withdraw
Enter transaction type: 1
Enter amount: 2000
Deposit successful
Current balance = 7000.0

1. Deposit
2. Withdraw
Enter transaction type: 2
Enter amount: 3000
Withdrawal successful
Current balance = 4000.0

1. Deposit
2. Withdraw
Enter transaction type: 2
Enter amount: 12000
Rejected: Withdrawal limit exceeded
Current balance = 4000.0

1. Deposit
2. Withdraw
Enter transaction type: 3
Enter amount: 500
Rejected: Invalid transaction type
Current balance = 4000.0

--- ATM TRANSACTION SUMMARY ---
Total Deposits = 2000.0
Total Withdrawals = 3000.0
Rejected Transactions = 2
Final Balance = 4000.0
