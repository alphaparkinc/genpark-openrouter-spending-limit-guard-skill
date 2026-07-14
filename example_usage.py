from client import OpenRouterSpendingLimitClient
client = OpenRouterSpendingLimitClient()
print(client.evaluate(15.20, 10.00))