# PythonTestSample

Python 학습을 위한 샘플 코드 모음입니다. 기초 문법부터 클래스, 스레드, 웹 크롤링, Selenium 자동화, 단위 테스트까지 다양한 예제를 포함합니다.

## 프로젝트 구조

```
PythonTestSample/
├── Test/                   # Python 기초 문법 예제
├── unittest_sample/        # unittest 단위 테스트 예제
├── selenium_test/          # Selenium 웹 자동화 예제
├── webcrawler/             # 웹 크롤러 예제
└── PhantomJS_Sample/       # PhantomJS 브라우저 자동화 예제
```

## 모듈별 설명

### Test/ — Python 기초 문법

| 파일 | 설명 |
|------|------|
| `Hello.py` | 문자열 기본 연산 |
| `Class.py` | 클래스 정의 및 인스턴스 생성 (`Robot` 클래스) |
| `FourCal.py` | 사칙연산 클래스 (`FourCal`) |
| `Function.py` | 함수 정의, 가변 인자, 전역 변수(`global`) 사용 |
| `first_class_function.py` | 일급 함수(First-class function) 및 고차 함수 `my_map` 예제 |
| `Loging_functon.py` | 클로저(Closure)를 활용한 로거 함수 |
| `Thread.py` | `threading` 모듈을 이용한 멀티스레드 예제 |
| `ThreadClass.py` | 스레드 클래스 기반 예제 |
| `Except.py` | 예외 처리(`try/except`) |
| `FileReadWrite.py` | 파일 읽기/쓰기 |
| `For_loop.py` | 반복문 예제 |
| `while_condition.py` | while 조건문 예제 |
| `Calc_Class.py` | 계산기 클래스 |
| `MyError.py` | 사용자 정의 예외 클래스 |
| `module.py` | 모듈 사용 예제 |
| `pickle_test.py` | pickle 직렬화/역직렬화 |
| `full_filename.py` | 파일 경로 처리 |
| `sys.py` | sys 모듈 예제 |
| `game/` | 패키지 구조 예제 (`graphic`, `sound` 서브패키지) |
| `Example/` | 추가 테스트 메서드 예제 |

### unittest_sample/ — 단위 테스트

Python 내장 `unittest` 프레임워크를 사용한 테스트 예제입니다.

| 파일 | 설명 |
|------|------|
| `Sample_unittest.py` | 문자열 메서드 테스트 (`upper`, `isupper`, `split`) |
| `ArithTest.py` | 산술 연산 테스트 (`failUnless`, `failIf`, `failUnlessEqual`) |
| `SkipTest.py` | 테스트 건너뛰기(`@unittest.skip`) 예제 |
| `SkipAnotherTest.py` | 조건부 테스트 스킵 예제 |

### selenium_test/ — Selenium 웹 자동화

Selenium WebDriver를 이용한 브라우저 자동화 테스트입니다.

| 파일 | 설명 |
|------|------|
| `ChromeTest.py` | ChromeDriver로 python.org 검색 테스트 |
| `GeckoDriverTest.py` | Firefox GeckoDriver 예제 |
| `IETest.py` | IE WebDriver 예제 |
| `example.py` | Selenium 기본 사용 예제 |

> **참고:** ChromeDriver 경로는 로컬 환경에 맞게 수정이 필요합니다.

### webcrawler/ — 웹 크롤러

`urllib`, `requests`, `BeautifulSoup`을 사용한 웹 크롤링 예제입니다.

| 파일 | 설명 |
|------|------|
| `webcrawlerTest.py` | `urllib` + `BeautifulSoup`으로 HTML 파싱 |
| `webcrawler_test.py` | `requests` + `BeautifulSoup`으로 페이지 순회 크롤러 |

### PhantomJS_Sample/ — PhantomJS 자동화

PhantomJS 헤드리스 브라우저를 이용한 자동화 예제입니다.

| 파일 | 설명 |
|------|------|
| `phantom_example.py` | PhantomJS로 naver.com 타이틀 출력 |

> **참고:** PhantomJS는 공식 지원이 종료되었습니다. 헤드리스 브라우저가 필요한 경우 Chrome Headless 사용을 권장합니다.

## 의존성

```
selenium
requests
beautifulsoup4
lxml
```

설치:

```bash
pip install selenium requests beautifulsoup4 lxml
```

## 실행 환경

- Python 3.x
- OS: Windows / macOS / Linux
- Selenium 사용 시 각 브라우저에 맞는 WebDriver 별도 설치 필요
