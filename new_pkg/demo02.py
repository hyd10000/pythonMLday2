import sys
#导入其他模块的方法
#方法一，导入
import pkg.demo01
print(pkg.demo01.add(1,2))

import pkg.demo01 as fs
a=fs.Son('ABC',19)
a.show()
print(fs.add(1,3))

#方法二
from pkg.demo01 import add as add2
add2(3,4)

#方法三
from pkg import *
pkg.demo01.Son

