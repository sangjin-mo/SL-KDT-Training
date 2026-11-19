# SL_KDT_Traning

2026년 11월 17일부터 진행한 SL KDT 교육 실습과 학습 기록입니다.

| 폴더 | 학습 내용 |
|---|---|
| [DAY01](DAY01) | 변수, 기본 자료형, 경로, 외부 패키지 확인 |
| [DAY02](DAY02) | 객체 참조, 출력 형식, 입력, 형 변환, 파일 저장 |
| [DAY03](DAY03) | 자료형 확인 및 실습 |
| [docs](docs) | 학습 정리와 Conda 패키지 기록 |
| [.vscode](.vscode) | 프로젝트 실행 및 자동완성 설정 |

루트의 PDF 4개는 기존에 업로드한 수업 강의자료입니다.

## 환경 설정

- Windows 11, Anaconda, VS Code
- base와 별도로 PY311 환경 생성 및 Python 3.11.18 실행 확인
- 생성: `conda create -n PY311 python=3.11`
- 활성화: `conda activate PY311`
- VS Code에서 PY311 인터프리터 선택
- 디버그 실행 작업 폴더: `${fileDirname}`
- 환경별 설치 기록: [docs/environment](docs/environment)
- base의 패키지는 PY311에 자동 복사되지 않습니다.

## DAY03 개념 정리

- `str`, `int`, `float`, `bool`과 `type()`으로 객체의 자료형 확인
- 클래스는 속성과 메서드를 묶고, 객체는 클래스를 바탕으로 만든 대상
- Python 변수는 객체를 참조하는 이름
- 기본 자료형은 항상 스택, 컨테이너는 항상 힙이라는 규칙은 없음
- C는 `malloc` 등으로 동적 할당하고 `free`로 해제
- Python은 객체 메모리를 자동 관리하며, `del`은 참조 제거로서 즉시 해제 보장이 없음
- Python 리스트는 요소 객체의 참조를 저장하므로 C의 int 배열과 구조가 다름
- Copilot 인라인 제안 한도와 ChatGPT 사용 한도는 별개

Python은 객체지향 설계를 기본으로 하되, 기본 문법 실습은 수업 원형을 보존합니다.

설치 도구, 캐시, 인증 정보, ZIP은 업로드에서 제외합니다. 자동 업로드는 설정하지 않았습니다.
