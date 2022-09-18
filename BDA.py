import os
import time
import winsound
def main():
    print("""作者：蚂蚁学姐
    转载请标注出处""")
    print('声音可能对不上，因为声音窗口的打开速度完全随缘ps:电脑性能所定，如果差很大就关掉程序重新打开')
    yn=input('是否开始（Y/N）：')
    if yn=='Y':
        
        a=0
        os.startfile(r'sound.cmd')

        time.sleep(0.5)
        for i in range(6570):
            with open(r'out/BA (%s).txt'%(a), encoding="utf-8") as file:
                # file 文件类型的对象
                print(type(file))
                print(file)

                # 读文本的全文并打印出来
                print(file.read())

                # 这个时候再读的话，返回EOF
                print(file.read())
                time.sleep(0.016666666666)
                #os.system('cls')

                a+=1
            
    else:
        exit()




if __name__ == '__main__':
    main()
