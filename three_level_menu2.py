#优化
menu = {
'北京':{
        '海淀':{
                '五道口':{
                        'soho':{},
                        '网易':{},
                        'google':{}
                         },
                '中关村':{
                        '爱奇艺':{},
                        '汽车之家':{},
                        'youku':{}
                         },
                '上地':{
                        '百度':{}
                        },
                 },
        '昌平':{
                '沙河':{
                        '老男孩':{},
                        '北航':{}
                        },
                '天通苑':{},
                '回龙观':{}
                },
        '朝阳':{},
        '东城':{}
        },
'上海':{
        '闵行':{
                '人民广场':{
                            '炸鸡店':{}
                            }
                },
        '闸北':{
                '火车站':{
                            '携程':{}
                            }
                },
         '浦东':{},
        },
'山西':{
        '晋中市':{
                '榆次区':{
                                '文化中心':{},
                                '万达':{}
                             }
                }
      },
}

varialbe = menu
li = []

while True:
    for i in varialbe:print(i)
    choice = input('输入要查看的地名(B:Back,Q:Quit)：').strip()

    if choice.lower() == 'q':exit('----byebye----')

    if choice.lower() == 'b':
        if li == []:
            print('\033[1;31;m 没有上级菜单,无法返回! \033[0m')
            continue
        varialbe = li.pop()
        continue

    if choice in varialbe:
        li.append(varialbe)
        varialbe = varialbe[choice]