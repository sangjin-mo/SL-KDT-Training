# -----------------------------------------------------
# 파이썬 내장 함수 : 입출력 함수 실습
# [실습 조건] 간략한 지기 소개 아래와 같이 파일에 저장하세요
# 파일명: kdt19_모상진.txt
# 내용 : 이름 / 전공 / 졸업여부 / 좋아하는 것 / 싫어하는 것 / 하고싶은 것
# 보기 좋게 파일에 저장하세요
# 입력함수로 6가지 입력 받기
# -----------------------------------------------------

# 입력 받기
name = input("이름을 입력하세요 : ")
major = input("전공을 입력하세요 : ")
graduation = input("졸업여부를 입력하세요 : ")
like = input("좋아하는 것을 입력하세요 : ")
dislike = input("싫어하는 것을 입력하세요 : ")
want = input("하고싶은 것을 입력하세요 : ")

FILE_NAME = "kdt19_모상진.txt"
# 1단계 : 파일 열기
myfile = open(FILE_NAME, mode = "w", encoding = "utf-8")
# 2단계 : 파일 작업
myfile.write(f"저의 이름은 {name}입니다.\n")
myfile.write(f"저는 {major}을 전공했습니다.\n")
myfile.write(f"저는 현재{graduation} 상태입니다.\n")
myfile.write(f"좋아하는 것은 {like}이고 싫어하는 것은 {dislike}입니다.\n")
myfile.write(f"저는 {want}하고 싶습니다.\n")
# 3단계 : 파일 닫기
myfile.close()
