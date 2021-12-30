hours = (input("Enter hours: "))
rate = (input("Enter rate: "))

try:
    hrs = float(hours)
    ra  = float(rate)
except:
    print("Error! check entered values")    


if hrs > 40:
    pay1 = hrs * ra
    exPay = (hrs - 40) * (ra * 0.5)  # rate increment by 0.5% for extra hours
    finalPay = pay1 + exPay 
else:
    finalPay = hrs * ra

print("Pay:", finalPay) 