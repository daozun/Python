from pri import *
print(num)
print(_num2)
print(__num3)

#  在上面引入模块的方式下，无论是_num还是__num2都会不显示

import pri
print(pri.num)
print(pri._num2)
print(pri.__num3)

# 在这种引入模块的方式下，是都可以显示的