# -----------------------------------------------------------------------
# 파이썬 데이터 종류 - 문자열 str 타입
# - 연산자 : + => 문자열 연결  
#           * => 문자열 반복
#     비교연산 => True/False
# 원소의 개수 반환 => len
msg1 = "good"
msg2 = "luck"

# => 덧셈 : str + str
print(f"{msg1} + {msg2} => {msg1 + msg2}")
print(f"{msg1} + {2027} => {msg1 + str(2027)}")
print(f"{msg1} + {'msg2'} => {msg1 + 'msg2'}")

# => 곱셈 : str * 정수 => 문자열 반복 연결
print(f"{msg1} * 3 => {msg1 * 3}")

# => 비교 : > < >= <= == != 
# => 결과 : True/False
# 같은 인덱스의 원소끼리 비교
print(f'"a" > "b"   => {"a" > "b"}')
print(f'"ac" > "ab" => {"ac" > "ab"}')

# => 멤버 연산자 : 원소 in 데이터, 원소 not in 데이터
# => 결과 : True/False
msg = "Luck"

print(f' l in {msg} => {"l" in msg}')
print(f' L in {msg} => {"L" in msg}')
print(f' uc in {msg} => {"uc" in msg}')
print('-' * 30)
print(f' l not in {msg} => {"l" not in msg}')
print(f' L not in {msg} => {"L" not in msg}')
print(f' uc not in {msg} => {"uc" not in msg}')

print(f' 1 in {"123"} => {"1" in "123"}')