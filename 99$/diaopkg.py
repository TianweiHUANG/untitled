#from mypkg import pkg     #from 包/文件夹 import 模块/文件 
#if __name__=='__main__':
    #pkg.test()            #模块之内函数

#from mypkg.pkg import test
#if __name__=='__main__':
    #test()

import mypkg.pkg
if __name__=='__main__':
    mypkg.pkg.test()
