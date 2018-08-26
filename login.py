dic = {'user1':'qwer',
       'user2':'asdf',
       'user3':'zxcv',
       }

x = 1
a = True
f = open(file='lock_user.txt', mode='r+', encoding='utf-8')

while a:
    x = 1
    username = input("Your username-->(Q:quit):")
    if username.lower() == 'q':exit('----byebye----')
    if username in dic:

        if username in f.read():
            f.seek(0)
            print("----用户被锁定----")
            continue
        while x <= 4:
            password = input("Your password-->:")
            if password == dic[username]:
                print("----WelCome!----")
                f.close()
                a=False
                break
            else:
                x += 1
                if x != 4:
                    print("用户名或密码错误，剩余机会：", 4 - x)
                    continue
                if x == 4:
                    f.seek(len(f.read()))
                    f.write(username)
                    f.write('\r')
                    f.close()
                    print("三次机会已用完，用户将被锁定")
                    break
    else:
        print("用户不存在")
        continue





