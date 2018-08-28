goods = [{"name":"电脑","price":1999},
         {"name":"鼠标","price":10},
         {"name":"游艇","price":20},
         {"name":"美女","price":998},
         ]

user = {'user1':'qwer'}

a =True

opena = open(file='Produce_number.txt',mode='r+',encoding='GBK')
openb = open(file='balance.txt', mode='r')

while a:
    username = input('Your username-->(Q:quit):')
    if username.lower() == 'q':
        exit('----byebye----')

    if username.lower() in user:
        password = input('Your password-->')

        if password == user[username]:
            if opena.read() != '':#回到退出前的记录
                opena.seek(0)
                print('\033[0;32m Shopping_cart-->\033[0m\n', opena.read(), end=' ')
                balance = int(openb.read())
                openb.seek(0)
                print('\n\033[1;31mbalance:\033[0m', openb.read())
            else:
                salary = int(input('Your salary-->:'))
                balance = salary


            while True:
                print('----Menu----')
                for i in range(4):
                    print(i+1,goods[i]['name'],goods[i]['price'])
                choice = input('ProduceNumber-->(Q:quit):').strip()

                if choice.lower() == 'q':#退出模块
                    opena.seek(0)
                    print('\033[0;32mShopping_cart:\033[0m\n', opena.read(),end=' ')
                    opena.close()
                    openb.seek(0)
                    print('\n\033[1;31mbalance:\033[0m',openb.read(), end=' ')
                    openb.close()
                    print('----byebye----')
                    a=False
                    break

                elif choice.isdigit():#购物车, 余额 显示
                    if int(choice) > 4:
                        print('\033[1;31m 没有此商品! \033[0m')
                    else:
                        print(goods[int(choice) - 1]['name'],goods[int(choice) - 1]['price'],end=' ', sep=':',file=opena)
                        opena.seek(0)
                        print('\033[0;32mShopping_cart:\033[0m\n', opena.read(),end=' ')
                        openb.seek(0)
                        balance = balance - goods[int(choice) - 1]['price']
                        with open(file='balance.txt',mode = 'w') as openc:
                            print(balance,file=openc)
                        print('\n\033[1;31mbalance:\033[0m',openb.read())

                elif balance < goods[int(choice) - 1]['price']:  # 余额不足
                    print('\033[1;33m Have no enough balance! \033[0m')
                    continue


        else:
            print('\033[1;31m password ig wrong \033[0m')
            continue
