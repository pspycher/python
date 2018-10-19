def backcoins():
    price = input('Enter Price: ')
    paid = input('Enter amount paid: ')
    payback = float(paid) - float(price)
    print(payback)

    mod = 1

    while mod != 0:
        print(payback)
        mod = payback % bill_10
        payback = payback / bill_10
        ret10 = payback * bill_10
        mod = payback

        mod =  (payback - ret10) % coin5
        payback = payback / coin5
        ret5 = payback * coin2
        mod = payback

        mod = (payback - ret5) % coin2
        payback = payback / coin2
        ret2 = payback * coin1
        mod = payback


        print(payback)




coin005 = float(0.05)
coin01 = float(0.1)
coin02 = float(0.02)
coin1 = float(1)
coin2 = float(2)
coin5 = float(5)
bill_10 = float(10)


backcoins()