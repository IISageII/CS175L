# CS175L
# Delvis Rodriguez
# stocks

commission_rate_purchase = float(input("Enter commission rate percentage on stock purchase: "))
commission_rate_sale = float(input("Enter commission rate percentage on stock sale: "))
num_purchase = int(input("Enter number of shares purchased: "))
num_sold = int(input("Enter number of shares sold: "))
purchase_price = float(input("Enter purchase price per share: "))
selling_price = float(input("Enter sell price per share: "))
print()

amount_paid_for_stocks = num_purchase * purchase_price
purchase_commission = commission_rate_purchase * amount_paid_for_stocks
total_paid = amount_paid_for_stocks + purchase_commission
stock_sold_for = num_purchase * selling_price
selling_commission = commission_rate_sale * stock_sold_for
total_received = stock_sold_for - selling_commission
profit_or_loss = total_received - total_paid
print("Amount paid for stock: $" + f'{amount_paid_for_stocks:,.2f}')
print("Commission paid on the purchase: $" + f'{purchase_commission:,.2f}')
print("Amount the stock sold for: $" + f'{stock_sold_for:,.2f}')
print("Commission paid on the sale: $" + f'{selling_commission:,.2f}')
print("Profit (or lost if negative): $" + f'{profit_or_loss:,.2f}')

