# Shipping Cost Calculator

##Input package weight and shippiing rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per Kilogram: "))

#Calculate Shipping Cost
shipping_cost = weight*rate

#display the results 
print(f"Shipping Cost : {shipping_cost} USD ")
