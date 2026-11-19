# -----------------------------------------------------------------
# 데이터 자료형변환 타입 캐스팅 
# 데이터 타입을 다른 데이터 타입으로 변환한 새로운 데이터 전달
# 관련 함수들
# int() float() str() bool() => 새로운 데이터로 형변환후 전달
#------------------------------------------------------------------ 
# => 정수 데이터를 다른 데이터 타입으로 변환
#------------------------------------------------------------------
num = 4
fnum = float(num)    # 인터프리터 num => 메모리 주소 => 4 => float(4) => 실수변환
print(f"num type => {type(num)}, fnum type => {type(fnum)}")
# ----------------------------------------------------------------
# Num = 4
# Float(num) => float(4) => 4.0 
# Num = float(num) = 4.0
# 형변환을 하더라도 반드시 새로운 변수 선언 후 저장해야 새로운 주소 할당 가능
# ----------------------------------------------------------------
float(num)
print(f"num type => {type(num)}, fnum type => {type(fnum)}")

num = float(num)
print(f"num type => {type(num)}, fnum type => {type(fnum)}")
# ---------------------------------------------------------------
# int => str
num = 100
 
str(num)
snum = str(num)            # => '100' , num => int type
print(f"num type => {num},{type(num)}, snum type => {snum},{type(snum)}")
num = str(num)      # num => '100'의 주소 저장
print(f"num type => {num},{type(num)}, snum type => {snum},{type(snum)}")

# -------------------------------------------------------------------
# int => bool 
# True , nonzero / False , 0
num = 0
bnum = bool(num)
print(f"num type => {num},{type(num)}, bnum type => {bnum},{type(bnum)}")
# 0x => 16진수 0o => 8진수 0b => 2진수
