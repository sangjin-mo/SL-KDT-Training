# SL_KDT_Traning


작성일: 2026-11-19  
기준: 현재 DAY01·DAY02 실습 코드, VS Code 설정, 환경 확인 결과와 앞서 검토한 강의 PDF.

## 1. 이틀 동안 배운 내용

**Python 실행 환경을 준비하고, 변수에 데이터를 연결한 뒤 입력·출력하고 파일로 저장하는 과정**을 배웠다.

```text
개발환경 준비 → 변수와 데이터 → 출력 형식 지정 → 키보드 입력 → 파일 저장
```

| 구분 | 주요 내용 | 실습 파일 |
|---|---|---|
| DAY01 | 기본 자료형과 변수 선언 | [hello.py](../DAY01/hello.py) |
| DAY01 | 절대·상대 경로, 현재 작업 폴더 | [ex_python_path.py](../DAY01/ex_python_path.py) |
| DAY01 | 외부 패키지 가져오기와 버전 확인 | [check_pkg.py](../DAY01/check_pkg.py) |
| DAY02 | 객체 참조, `id()`, 변수 재할당 | [ex_var01.py](../DAY02/ex_var01.py), [ex_var02.py](../DAY02/ex_var02.py) |
| DAY02 | 출력 구분자와 종료 문자 | [ex_print01.py](../DAY02/ex_print01.py) |
| DAY02 | `%` 서식과 f-string | [ex_print02.py](../DAY02/ex_print02.py) |
| DAY02 | 파일 객체와 파일 출력 | [ex_print03.py](../DAY02/ex_print03.py) |
| DAY02 | 입력과 형 변환 | [ex_input01.py](../DAY02/ex_input01.py) |
| DAY02 | 자기소개 입력·파일 저장 종합 실습 | [ex_print_input.py](../DAY02/ex_print_input.py) |

## 2. 개발환경 설정 정리

### 2.1 환경 구성

| 항목 | 확인된 내용 |
|---|---|
| 운영체제 | Windows 11, 64비트 |
| 편집기 | VS Code |
| Python 배포판 | Anaconda |
| 환경·패키지 관리 | Conda |
| 기본 환경 | `base`: Python 3.13.9 — 앞선 확인 기준 |
| 별도 환경 | `PY311`: Python 3.11.18 — 생성 및 실행 확인 완료 |
| PY311 위치 | `C:\Users\KDS18\anaconda3\envs\PY311` |
| 프로젝트 폴더 | `C:\Users\KDS18\Desktop\KDT_19SL\{00}_PRE` |

**가상환경은 Python과 패키지의 묶음이고, 작업 폴더는 파일을 읽고 쓰는 기준 위치다.** 두 개념은 서로 다르다.

현재 분석 도구의 터미널에서는 `base`가 활성화되어 있다. 사용자가 별도로 연 PowerShell에서 `PY311`을 활성화한 것과는 별개이며, VS Code의 선택 인터프리터는 프로젝트 설정 파일만으로 확정할 수 없다.

### 2.2 지금까지 실행한 환경 관련 명령

```powershell
# base의 Conda 업데이트
conda update --name base conda

# 현재 활성 환경의 패키지 전체 업데이트
conda update --all

# Python 3.11 환경 생성 — 생성 완료
conda create -n PY311 python=3.11

# 환경 목록 확인
conda env list

# 환경 활성화와 Python 버전 확인 — 실행 성공
conda activate PY311
python --version

# 환경 비활성화
conda deactivate
```

업데이트 명령은 사용자가 제공한 실행 이력에 있다. 해당 이력에는 최종 업데이트 결과가 없어 명령별 완료 여부까지 확정하지는 않는다.

- `(base)`, `(PY311)`은 현재 터미널의 활성 환경 표시다.
- `conda activate list`는 `list`라는 환경을 찾는 잘못된 명령이다. 환경 목록은 `conda env list`로 확인한다.
- 환경 생성 시 나온 `conda-pypi` 안내는 환경 생성 실패를 뜻하지 않는다.
- **base의 패키지는 PY311에 자동으로 복사되지 않는다.**

### 2.3 VS Code 설정

[settings.json](../.vscode/settings.json)에는 기본 환경 관리자와 패키지 관리자를 Conda로 지정해 두었다.

```json
{
    "python-envs.defaultEnvManager": "ms-python.python:conda",
    "python-envs.defaultPackageManager": "ms-python.python:conda"
}
```

[launch.json](../.vscode/launch.json)에는 현재 파일을 실행하는 설정과 다음 작업 폴더 설정이 있다.

```json
"cwd": "${fileDirname}"
```

이 디버그 구성을 사용하면 실행하는 `.py` 파일이 있는 폴더가 현재 작업 폴더가 된다. 예를 들어 `DAY02/ex_print_input.py`에서 상대경로 파일명을 쓰면 DAY02 안에 저장된다. 다른 실행 방식에서는 작업 폴더가 다를 수 있다.

`Python > Terminal: Execute In File Dir`는 DAY01 코드에 안내되어 있지만, 현재 프로젝트의 `settings.json`에는 명시되어 있지 않다. 사용자 설정에 적용되어 있는지는 별도 확인 대상이다.

PY311 사용 여부를 확인할 때는 VS Code에서 `Ctrl + Shift + P` → `Python: Select Interpreter`로 인터프리터를 선택하고 다음 값을 확인한다.

```python
import sys
print(sys.executable)
```

PY311을 선택했다면 실행 경로는 다음과 같아야 한다.

```text
C:\Users\KDS18\anaconda3\envs\PY311\python.exe
```

### 2.4 패키지 확인 결과와 남은 구분

아래는 **앞선 base 환경 검사 결과**이며, 오늘 다시 전체 패키지를 검사한 결과는 아니다.

| 패키지 | 당시 base 확인 결과 | 용도 |
|---|---|---|
| NumPy | 2.4.6, 가져오기 성공 | 수치 계산 |
| pandas | 3.1.0, 가져오기 성공 | 표 형태 데이터 분석 |
| scikit-learn | 1.9.1, 가져오기 성공 | 머신러닝 |
| Matplotlib | 3.11.2, 가져오기 성공 | 시각화 |
| OpenCV (`cv2`) | 미설치 | 이미지·영상 처리 |

당시 base 패키지 의존성 검사에서는 충돌이 보고되지 않았다. Matplotlib 캐시 권한 경고는 분석 도구의 접근 제한 영향일 수 있어 일반 실행에서도 발생하는지는 확인하지 않았다.

`PY311`은 앞선 검사에서 Python·pip 등 기본 구성만 설치된 상태였다. `check_pkg.py`를 PY311에서 실행하려면 해당 환경에 필요한 패키지가 있는지 확인해야 한다.

```powershell
conda list -n PY311
```

별도로 제시된 CV/ML 가이드의 `ML_ENV`, Python 3.10, conda-forge·OpenBLAS 구성은 현재 확인된 환경과 다르다. `env.yml`로 해당 구성을 만들었다는 확인은 없다. 기본 입출력 실습에는 외부 분석 패키지가 필요하지 않다.

## 3. DAY01 핵심 개념

### 3.1 변수와 기본 자료형

변수는 객체를 가리키는 이름이다. `=`는 오른쪽 값을 왼쪽 변수명에 연결하는 대입 연산자다.

```python
name = "홍길동"       # str: 문자열
age = 10              # int: 정수
avg = 9.9             # float: 실수
is_ok = True          # bool: 논리값
message = """Good
luck"""               # 여러 줄 문자열
```

- `True`는 논리값이고, `"True"`는 문자열이다.
- 숫자 `10`과 문자열 `"10"`은 자료형이 다르다.
- `type(값)`으로 자료형을 확인한다.
- 빈 문자열·0 등은 조건에서 거짓으로 평가되지만, 논리값이 0과 1로만 구성된다는 설명과는 구분한다.

### 3.2 절대경로와 상대경로

| 구분 | 의미 | 예시 |
|---|---|---|
| 절대경로 | 드라이브 등 시작 위치부터 지정한 경로 | `C:\data\flower.jpg` |
| 상대경로 | 현재 작업 폴더를 기준으로 지정한 경로 | `test.txt`, `../data/flower.jpg` |

```python
import os
print("현재 작업 디렉터리:", os.getcwd())
```

**상대경로는 기본적으로 `.py` 파일 위치가 아니라 현재 작업 폴더 기준이다.** 실행 방식에 따라 기준이 달라질 수 있으므로 파일이 예상한 곳에 없으면 `os.getcwd()`부터 확인한다.

### 3.3 패키지 가져오기와 버전 확인

```python
import pandas as pd
import sklearn as sk

print(pd.__version__)
print(sk.__version__)
```

- `import`: 모듈이나 패키지를 가져온다.
- `as`: 코드에서 사용할 별칭을 정한다.
- `__version__`: 해당 라이브러리가 제공하는 버전 정보다.
- 설치 이름과 import 이름은 다를 수 있다. 예: `scikit-learn` → `sklearn`, OpenCV → `cv2`.
- `ModuleNotFoundError`가 나오면 현재 Python 환경과 그 환경의 설치 상태를 확인한다.

## 4. DAY02 핵심 개념

### 4.1 객체 참조와 변수 재할당

```python
value = 3
age = 3

print(id(value))
print(id(age))

age = 100
```

`age = 100`은 기존 정수 객체 `3`을 바꾸는 것이 아니라, `age`가 다른 객체를 가리키도록 다시 연결하는 것이다. `value`는 여전히 `3`을 가리킨다.

`id()`는 객체가 살아 있는 동안 고유하고 일정한 **객체 식별값**을 반환한다. CPython에서는 메모리 주소에 해당하지만, 모든 Python 구현에서 주소라고 보장되는 것은 아니다.

작은 정수 등 일부 객체는 재사용되어 같은 `id()`가 관찰될 수 있다. 그러나 **값이 같은 모든 데이터가 언제나 하나의 객체로 저장되는 것은 아니다.** 값 비교에는 `==`, 같은 객체인지 확인할 때는 `is`를 사용한다.

### 4.2 print(): sep와 end

```python
print("홍길동", 2027)
# 홍길동 2027 + 줄 바꿈

print("홍길동", 2027, sep="*")
# 홍길동*2027 + 줄 바꿈

print("홍길동", 2027, sep="", end="★")
# 홍길동2027★ — 자동 줄 바꿈 없음
```

| 옵션 | 역할 | 기본값 |
|---|---|---|
| `sep` | 여러 출력 값 사이 구분자 | `" "` |
| `end` | 출력 마지막에 붙는 문자열 | `"\n"` |
| `file` | 출력할 대상 | 표준 출력, 일반적으로 터미널 |

`sep=""`로 지정해도 문자열 안에 직접 입력한 공백은 유지된다. `end`를 별 등으로 바꾸면 다음 `print()` 출력이 같은 줄에 이어질 수 있다.

### 4.3 문자열 출력 형식 비교

```python
year, month, day = 2026, 11, 18

print("오늘은 ", year, "년 ", month, "월 ", day, "일입니다", sep="")
print("오늘은 %d년 %d월 %d일입니다" % (year, month, day))
print(f"오늘은 {year}년 {month}월 {day}일입니다")
```

| 방식 | 특징 |
|---|---|
| 쉼표로 값 나열 | 여러 값을 전달하며 `sep`로 구분 방식 조절 |
| `%` 서식 | 자리와 변수의 개수·순서, 서식 종류를 맞춤 |
| f-string | 문자열 앞에 `f`, 삽입할 변수·표현식을 `{}`로 표시 |

| 서식 | 의미 | 예시 |
|---|---|---|
| `%d` | 정수 형식 | `2026` |
| `%f` | 실수 형식, 기본 소수점 이하 6자리 | `2026.000000` |
| `%s` | 문자열 표현 | `2026` |

**실습의 `%f` 출력은 `%d`, `%s` 출력과 다르다.** 정수를 넣어도 소수점 이하가 표시된다. 일반적인 문장 조합에는 f-string을 기본으로 활용한다.

```python
score = 95.567
print(f"점수: {score:.2f}")  # 점수: 95.57
```

### 4.4 input(): 입력과 형 변환

```python
first = input("숫자 1 입력: ")
second = input("숫자 2 입력: ")

print(first + second)
print(int(first) + int(second))
```

`7`, `3`을 입력하면 첫 출력은 문자열 연결 결과 `73`, 두 번째는 숫자 덧셈 결과 `10`이다.

- `input()`은 Enter를 누를 때까지 기다리며, 입력 결과를 문자열로 반환한다.
- 정수 계산에는 `int()`, 실수 계산에는 `float()` 등을 사용한다.
- `int("안녕")`처럼 변환할 수 없는 문자열을 넣으면 `ValueError`가 발생한다.

### 4.5 파일 처리: 열기 → 작업 → 닫기

```python
FILE_NAME = "test.txt"

myfile = open(FILE_NAME, mode="w", encoding="utf-8")
myfile.write("good luck!\n")
myfile.write("Happy Python!")
myfile.close()
```

| 항목 | 의미 |
|---|---|
| `open()` | 파일을 열고 파일 객체 반환 |
| `mode="r"` | 읽기, 기본 모드 |
| `mode="w"` | 쓰기, 기존 파일이 있으면 내용 삭제 후 기록 |
| `mode="a"` | 기존 내용 뒤에 추가 |
| `encoding="utf-8"` | 텍스트를 저장·해석할 문자 인코딩 지정 |
| `write(문자열)` | 문자열 기록, 줄 바꿈은 자동 추가하지 않음 |
| `close()` | 버퍼 내용을 반영하고 파일 자원 해제 |

`r`, `w`, `a`는 이 예제에서 **파일 열기 모드**이며 `myfile.w()` 같은 메서드가 아니다. 대문자 `FILE_NAME`은 상수처럼 사용한다는 명명 관례이며, Python이 값 변경을 금지하지는 않는다.

`print()`로도 파일에 기록할 수 있다.

```python
logfile = open("log.txt", mode="w", encoding="utf-8")
print(1 + 2 + 3 + 4 + 5, file=logfile)
logfile.close()
```

`write()`와 달리 `print()`는 기본적으로 마지막에 줄 바꿈을 붙이며 숫자도 바로 출력할 수 있다.

추후에는 파일을 자동으로 닫는 `with` 문법으로 확장할 수 있다. 현재 실습은 열기·작업·닫기의 기본 흐름을 익히는 단계다.

### 4.6 종합 실습: 자기소개 파일 만들기

[ex_print_input.py](../DAY02/ex_print_input.py)는 지금 배운 내용을 연결한 프로그램이다.

1. `input()`으로 이름·전공·졸업 여부·좋아하는 것·싫어하는 것·하고 싶은 것, 총 6개를 입력받는다.
2. 변수에 입력 결과를 연결한다.
3. UTF-8 쓰기 모드로 자기소개 파일을 연다.
4. f-string으로 자기소개 문장을 만들고 `write()`로 저장한다.
5. `close()`로 파일을 닫는다.

출력 문장과 입력값이 자연스럽게 이어지는지도 확인한다. 현재 코드는 `저는 현재{graduation}`에 공백이 없고, 전공 뒤 조사가 `을`로 고정되어 있어 입력에 따라 문장 다듬기가 필요하다.

## 5. 객체지향과 연결해서 이해하기

앞으로의 기본 구현 방향은 **클래스에 관련 데이터와 메서드를 묶는 객체지향**이다. 다만 현재 DAY01·DAY02 파일은 변수와 내장 함수를 순서대로 실행하며 기본 문법을 연습하는 단계로, 직접 클래스를 정의하지는 않았다.

이미 파일 실습에서는 객체와 메서드를 사용했다.

```python
myfile = open("test.txt", "w", encoding="utf-8")
myfile.write("안녕하세요")
myfile.close()
```

- `myfile`: 파일 객체를 참조하는 변수
- `write()`, `close()`: 해당 객체가 제공하는 메서드
- 함수: `print()`, `input()`, `open()`처럼 호출
- 메서드: `myfile.write()`처럼 객체를 통해 호출

향후 자기소개 프로그램을 클래스 설계로 확장한다면 이름·전공 등을 속성으로, 자기소개 생성·저장을 메서드로 묶을 수 있다. 이번 정리에서는 기존 실습 코드를 변경하지 않는다.

## 6. 복습 체크리스트

- [ ] Python 실행 환경과 현재 작업 폴더의 차이를 설명할 수 있다.
- [ ] base에 설치된 패키지가 PY311에서 자동으로 사용되지 않는 이유를 안다.
- [ ] `sys.executable`과 `os.getcwd()`의 확인 목적을 구분한다.
- [ ] 변수 재할당과 객체 변경의 차이를 이해한다.
- [ ] 같은 값이라고 반드시 같은 `id()`를 갖는 것은 아님을 안다.
- [ ] `sep`와 `end`를 구분해 사용할 수 있다.
- [ ] `%d`, `%f`, `%s`, f-string의 차이를 설명할 수 있다.
- [ ] `input()` 결과가 문자열임을 알고 숫자로 변환할 수 있다.
- [ ] `write()`에 줄 바꿈이 자동 추가되지 않음을 안다.
- [ ] `w` 모드의 기존 내용 삭제와 `a` 모드의 추가 기록을 구분한다.
- [ ] UTF-8을 지정해 한글 문장을 파일에 저장할 수 있다.
- [ ] 입력 → 변수 → 문장 조합 → 파일 저장 과정을 스스로 작성할 수 있다.

## 7. 강의자료와의 연결

| 자료 | 이번 실습과 연결되는 부분 |
|---|---|
| `PYTHON_Programming.pdf` | 개발환경, 변수, 기본 자료형, 콘솔 입출력, 문자열 형식, 파일 입출력 |
| `VSCODE_PYTHON_환경구축 (1).pdf` | VS Code, Python 확장, 작업 폴더, 인터프리터 선택 |
| `가상환경_아나콘다_개발환경.pdf` | Conda 업데이트, 환경 생성·활성화·종료, 패키지 확인·설치 |

자료에 나오는 Python 버전과 사용자 경로는 예시다. 현재 사용 환경과 구분하며, 문서의 설정·설치 명령을 이번 정리 작업에서 실행한 것은 아니다.

편집 팁: VS Code에서 여러 줄을 선택한 뒤 `Ctrl + /`를 누르면 줄 주석을 추가하거나 해제할 수 있다.

## 8. DAY03 — 기존 개념 확장 (2026-11-19)

DAY01의 변수·기본 자료형과 DAY02의 객체 참조·형 변환을 바탕으로, 자료형이 클래스라는 점과 변환 결과를 변수에 연결하는 과정을 확장해서 배웠다.

### 8.1 값과 자료형 함께 확인

실습: [ex_datatype_01.py](../DAY03/ex_datatype_01.py)

```python
msg = "Hello Python"
value = 100.4
age = 100
isok = True

print(f"{msg} 타입 => {type(msg)}")
print(f"{value} 타입 => {type(value)}")
print(f"{age} 타입 => {type(age)}")
print(f"{isok} 타입 => {type(isok)}")
```

각각 str, float, int, bool 클래스의 객체다. `isok`는 사용자가 정한 변수명이며, 예약된 논리값은 `True`와 `False`다.

### 8.2 형 변환과 재할당

실습: [ex_datatype_02.py](../DAY03/ex_datatype_02.py)

```python
num = 4
float(num)          # 반환값을 저장하지 않음: num은 여전히 정수
fnum = float(num)   # 변환 결과를 다른 변수로 참조
num = float(num)    # 기존 이름을 실수 객체에 다시 연결
```

형 변환에 반드시 새 변수명이 필요한 것은 아니다. 기존 이름에도 재할당할 수 있다. 변환은 원본 변수의 자료형을 직접 바꾸는 작업으로 이해하지 말고, 반환값을 어떻게 사용하는지 구분한다. 변환 함수가 언제나 새 객체를 생성한다는 보장도 없다.

| 함수 | 목적 | 예시 |
|---|---|---|
| int | 정수 변환 | `int("100")` → `100` |
| float | 실수 변환 | `float(4)` → `4.0` |
| str | 문자열 변환 | `str(100)` → `"100"` |
| bool | 참·거짓 변환 | `bool(0)` → `False`, `bool(-1)` → `True` |

문자열 `"False"`와 `"0"`은 비어 있지 않으므로 bool 변환 결과가 True다. 숫자의 진법 표기 접두사는 `0b`(2진수), `0o`(8진수), `0x`(16진수)다.

### 8.3 구조체에서 클래스와 객체로

학생 이름·나이·성별·전공·전화번호를 하나의 자료형으로 묶을 수 있다. C의 구조체는 관련 데이터를 묶고, 클래스는 속성과 메서드를 묶는다. 객체는 클래스를 바탕으로 만든 실제 대상이다.

학생 한 명의 평균 계산은 Student에, 여러 학생의 석차·나이순 정렬·전공 통계는 학생 관리 클래스에 두는 식으로 책임을 나눈다. OOP는 객체지향 프로그래밍(Object-Oriented Programming)의 약자다.

### 8.4 C와 Python의 메모리 관리 비교

기본 자료형은 무조건 스택, 컨테이너는 무조건 힙이라는 규칙은 없다. C 구조체는 멤버 구성이 정해지면 구조체 자체 크기도 정해진다.

| 비교 | C | Python |
|---|---|---|
| 동적 할당 | malloc, calloc 등으로 확보 | 객체 생성 시 실행 환경이 관리 |
| 크기 변경 | realloc 등 | 리스트 등 자료구조가 관리 |
| 해제 | free 호출 | 사용되지 않는 객체를 자동 회수 |

동적 할당은 실행 중 메모리를 확보하는 것이다. CPython은 일반적으로 객체를 힙에서 관리한다. Python의 del은 이름·참조를 제거하며 즉시 메모리 해제를 보장하지 않는다. 리스트는 요소 객체에 대한 참조를 저장하므로 C의 연속된 int 배열과 구조가 다르다.

C int 크기는 구현에 따라 다르며 항상 4바이트라고 단정할 수 없다. Python int도 C int와 달리 크기가 고정된 4바이트 정수가 아니다.

### 8.5 개발 도구와 GitHub 연결

- Pylance의 일반 자동완성(Ctrl + Space)과 Copilot의 회색 인라인 제안은 별개다.
- Copilot은 내장 확장일 수 있어 일반 설치 목록만으로 미설치라고 단정하면 안 된다.
- 확인 당시 Copilot Inline Suggestions 사용량은 100%였다. Credits나 ChatGPT 이용 한도와 별도로 관리된다.
- Git과 GitHub CLI를 로컬 .tools에 준비하고, 브라우저에서 sangjin-mo 계정 인증을 완료했다.
- 저장소: https://github.com/sangjin-mo/SL-KDT-Training
- 기존 main 이력을 가져온 뒤 커밋·푸시했다. 인증 정보와 설치 도구는 추적하지 않는다.
- 앞으로 실습 파일을 갱신하면서 이 학습 문서에도 내용을 누적한다. 요청 없이 실행되는 자동 푸시는 설정하지 않았다.

### 8.6 추가 복습

- [ ] float(num)만 호출할 때와 num = float(num)의 차이를 설명한다.
- [ ] bool("0")과 bool(0)의 차이를 설명한다.
- [ ] 구조체·클래스·객체·메서드의 관계를 설명한다.
- [ ] C의 free와 Python의 del이 같은 동작이 아님을 이해한다.
- [ ] 기존 변수·입출력 실습과 자료형·메모리 개념을 연결한다.
