import argparse

print("命令例子D:\ProgramData\Anaconda3\python.exe ******a.py -t video -vs C:/Users/Administrator/Desktop/pose.mp4  -t video ****pose.mp4 -p holistic")

parser = argparse.ArgumentParser(description='一个简单的加法')

parser.add_argument('a', type=int,help='第1个加数')

parser.add_argument('b',  type=int,help='第2个加数')



def test(a,b):

    print(f"{a}+{b}=" + str(a+b))



if __name__ == '__main__':

    args = parser.parse_args()

    test(args.a, args.b)