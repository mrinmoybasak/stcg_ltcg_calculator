import  time
import math
print("Welcome to Short Term Capital Gain Tax & Long Term Capital Gain tax Calculator ")
time.sleep(1)
print("Calculator Create By Mrinmoy Basak Developer Email id mrinmoybasak@mbwealth.in")
time.sleep(1)
while(True):
    invAmount = int(input("Please enter Investment Amount \n"))
    costNav = int(input("Please enter Purchase NAV \n"))

    redeemAmount = int(input("Please Redemption Amount \n"))
    reedeemNav = int(input("Please Enter current nav \n"))

    reedeemYear = int(input("Please enter 1 if Redeem within 1 year if not enter 2 \n"))

    unit_redeem = (redeemAmount/reedeemNav)
    print(f"Unit redeem {unit_redeem}")

    cost_of_investment = (unit_redeem*costNav)
    print(f"Cost of Investment is Rs.{cost_of_investment}")

    gain_loss_nav= (reedeemNav-costNav)
    print(f"NAV Gain or Loss Rs.{gain_loss_nav}")

    investment_loss_gain = (unit_redeem*gain_loss_nav)
    print(f"Investment Gain or Loss Rs.{investment_loss_gain}")

    tax_free_unit = 100000/gain_loss_nav

    STCG = (gain_loss_nav*unit_redeem)



    def taxcal(investment_loss_gain):
        if investment_loss_gain > 100000:
            t= (investment_loss_gain-100000)



            return t
        elif investment_loss_gain <= 100000:
            return (0)




    LTGCtax = taxcal(investment_loss_gain)
    a = LTGCtax
    LTGCtaxpayable = a/10


    STCGtax = (STCG * 15) / 100

    if reedeemYear == 1:

        print(f"You have to pay Short Term Capital Gain Tax @15% Rs. {STCGtax}")
        print(f"If you redeem after 1 year then you have pay Capital Gain tax just Rs.{LTGCtaxpayable}")
    elif reedeemYear == 2:
        print(f"your Long Term Capital Gain taxable Amount Rs.{LTGCtax}")
        print(f"You have to pay Long Term Capital Gain Tax @10% Rs.{LTGCtaxpayable} ")
        print(f"LTGC Tax Free Unit is {tax_free_unit}")


    again = input(
        'Do you want to use Tax Calculator again? \n Press y for yes and n for no: ')
    if again == 'y':
        continue
    else:
        print('See you again!')
        break
