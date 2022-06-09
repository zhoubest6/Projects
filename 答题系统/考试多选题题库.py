data=r"tiku_dan.txt"#题库
ti_ku = open(data, 'r',encoding='UTF-8').readlines()
s=[x.strip() for x in ti_ku]#去掉\n
a,b=[],0
for i in range(0,len(s),14):
    print(s[i][:-1])#题库
    luan = ti_ku[i+3:i+12]
    #random.shuffle(luan[2:])#random.shuffle(x) 打乱排序
    #print(luan)
    print("".join(luan))
    y=input("请输入正确答案：")
    dan=s[i+12][6]
    print("答案：",dan)
    if y==dan:
        print("很棒 答对了 正确答案为：",dan)
    elif y==dan.lower():
        print("很棒 答对了 正确答案为：",dan)
    else:
        print("选错了，你个憨憨  正确选项：",dan)

"""    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,"""
