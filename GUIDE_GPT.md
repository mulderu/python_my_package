🚀 Python Wheel 패키지 만들기
1️⃣ 프로젝트 디렉토리 구조 생성
먼저, 프로젝트 폴더를 만듭니다.

```
mkdir my_package
cd my_package
📌 기본 디렉토리 구조:
ruby
복사
편집
my_package/
│── my_package/        # 실제 패키지 소스 코드
│   ├── __init__.py    # 패키지 초기화 파일
│   ├── module.py      # 원하는 기능이 들어간 모듈 파일
│
├── tests/             # 테스트 코드 (선택)
│   ├── test_module.py
│
├── setup.py           # 패키지 설정 파일
├── pyproject.toml     # 패키지 빌드 설정 파일
├── README.md          # 패키지 설명 파일
└── LICENSE            # 라이선스 파일 (선택)
```

2️⃣ 패키지 코드 작성
📌 my_package/module.py 파일을 생성하고 기능을 추가합니다.

```python
# my_package/module.py

def hello_world():
    """Returns a simple greeting message."""
    return "Hello, World!"
```

📌 my_package/__init__.py 파일을 생성하여 모듈을 불러올 수 있도록 설정합니다.

```python
# my_package/__init__.py
from .module import hello_world
```

3️⃣ setup.py 파일 작성
📌 setup.py는 패키지의 메타 정보를 포함합니다.

```python
from setuptools import setup, find_packages

setup(
    name="my_package",  # 패키지 이름
    version="0.1.0",  # 버전
    packages=find_packages(),  # 패키지 자동 검색
    install_requires=[],  # 의존성 패키지 (없으면 빈 리스트)
    author="Your Name",
    author_email="your_email@example.com",
    description="A simple Python package example",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my_package",  # GitHub URL (선택)
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
```

4️⃣ pyproject.toml 작성 (선택)
📌 pyproject.toml을 추가하면 build 모듈을 사용하여 빌드할 수 있습니다.

```toml
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"
```

5️⃣ 패키지 빌드하기
📌 wheel 패키지를 이용하여 빌드합니다.

```sh
# 필요한 패키지 설치
pip install setuptools wheel

# 패키지 빌드
python setup.py sdist bdist_wheel
```

✅ 실행 후 dist/ 폴더에 .whl 파일이 생성됩니다.

6️⃣ 로컬에서 패키지 설치 및 사용
📌 빌드된 .whl 파일을 직접 설치합니다.

```sh
pip install dist/my_package-0.1.0-py3-none-any.whl
```

📌 패키지를 테스트해 봅니다.

```python
import my_package

print(my_package.hello_world())  # Hello, World!
```

7️⃣ (선택) PyPI 업로드하기
- 만약 패키지를 PyPI (Python Package Index) 에 올리고 싶다면, twine을 사용합니다.

```sh
pip install twine
```

# PyPI 업로드
- twine upload dist/*
- 이후, pip install my_package 명령어로 어디서든 패키지를 설치할 수 있습니다. 🎉

🎯 정리

- 프로젝트 폴더를 만들고 패키지 코드 작성
- setup.py, pyproject.toml 작성
- setuptools, wheel로 빌드 (python setup.py sdist bdist_wheel)
- pip install dist/my_package-0.1.0-py3-none-any.whl 로 설치
- (선택) twine upload 로 PyPI에 배포
- 🚀 이제 나만의 Python 패키지를 만들어 활용할 수 있습니다! 😃