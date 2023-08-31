# chapter06_03
# 파이썬 패키지
# 패키지 작성 및 사용법
# 파이썬은 패키지로 분할 된 개별적인 모듈로 구성
# 상대경로 : ..(부모 디렉토리로 이동), .(현재 디렉토리)
# __init__.py : Python3.3 부터는 없어도 패키지로 인식 -> 단, 하위 호환을 위해 작성 추천
# __init__.py에서 만약 모듈이름을 적어주지 않는다면 import하지 못한다. 파이썬은 init을 먼저 검사한다.

# 예제1  # 같은 경로에 있으면 바로 이동 가능
import sub.sub1.module1
import sub.sub2.module2

# 사용
sub.sub1.module1.mod1_test1()
sub.sub1.module1.mod1_test2()

sub.sub2.module2.mod2_test1()
sub.sub2.module2.mod2_test2()

print("-" * 19)

# 예제2
from sub.sub1 import module1
from sub.sub2 import module2 as m2

module1.mod1_test1()
module1.mod1_test2()

m2.mod2_test1()
m2.mod2_test2()

print("-" * 19)

# 예제3
from sub.sub1 import *
from sub.sub2 import *

module1.mod1_test1()
module1.mod1_test2()

module2.mod2_test1()
module2.mod2_test2()

print("-" * 19)
