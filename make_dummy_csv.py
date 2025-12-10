import pandas as pd

data = {
    "customer_id": [10001, 10001, 10002, 10002, 10003, 10004, 10004, 10005, 10005, 10006],
    "invoice_id":  ["INV-001", "INV-003", "INV-002", "INV-005", "INV-004",
                    "INV-006", "INV-007", "INV-008", "INV-009", "INV-010"],
    "invoice_date": ["2021-01-05", "2021-02-10", "2021-01-12", "2021-03-01",
                     "2021-02-20", "2021-03-15", "2021-03-20",
                     "2021-01-25", "2021-04-01", "2021-04-10"],
    "quantity": [3, 1, 2, 5, 1, 4, 2, 1, 1, 10],
    "price":    [9.99, 19.99, 4.50, 3.00, 49.99, 7.50, 12.00, 5.00, 6.50, 2.00],
}

df = pd.DataFrame(data)
df.to_csv("dummy_retail.csv", index=False)

print("Created dummy_retail.csv in this folder")
