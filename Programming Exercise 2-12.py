# Named constants
COMMISSION_RATE = 0.03
NUM_SHARES = 2000
PURCHASE_PRICE = 40
SELLING_PRICE = 42.75

#Variables
amountPaidForStock = 0.0 #80,000
purchaseCommission = 0.0 #2,400
totalPaid = 0.0
stockSoldFor = 0.0
sellingCommission = 0.0
totalRecieved = 0.0
profitOrLoss = 0.0

#Calculate the amount that Joes paid for the stock, not including the commission
amounntPaidForStock = PURCHASE_PRICE*NUM_SHARES

#Calculate the amount of commission Joe paid for his broker when he brought the stock
purchaseCommission = amountPaidForStock*COMMISSION_RATE

#Calculate the total ammount that Joe paid, which is the amount he paid for the stock plus the commisssion he paid his broker
totalPaid = amountPaidForStock + purchaseCommission

#Calculate the amount that Joe sold the stock for.
stockSoldFor = NUM_SHARES*SELLING_PRICE

#Calculate the amount of commission that Joe paid his broker when he sold the stock
sellingCommission = SELLING_PRICE*COMMISSION_RATE

#Calculate the amount of money left over, after Joe paid his broker.
totalRecieved = stockSoldFor-sellingCommission

#Calculate the amount of profit or loss. If this amount is a positive number, it is profit. If this is a negative number it is a loss
profitOrLoss = totalRecieved-totalPaid 

print ("Amount paid for the stock: $", format(amountPaidForStock, '.2f'))
print("Commission paid on the purchase: $", format(purchaseCommission, '.2f'))
print(" Amount the stock sold for: $", format(stockSoldFor, '.2f'))
print("Commission paid on the sale: $", format(sellingCommission, '.2f'))
print("Profit (or loss if negative): $", format(profitOrLoss, '.2f'))




