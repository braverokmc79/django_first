# Django 공식 튜토리얼 따라하기

이 프로젝트는 [점프 투 장고]
(https://wikidocs.net/book/4223)을 기반으로 학습 목적으로 만든 웹 애플리케이션입니다.

## 📁 프로젝트 구조
```
Django_OfficialDocumentTutorial/  
├── mysite/ # Django 프로젝트 디렉토리  
├── polls/ # 튜토리얼에서 생성한 앱  
├── venv/ # (가상환경 - .gitignore에 의해 제외됨)  
├── db.sqlite3 # SQLite DB 파일  
└── .gitignore
```

## ⚙️ 개발 환경
- Python 3.12.3
- Django 5.2.1
- 가상환경: venv 사용

## ▶️ 실행 방법
1. 가상환경 활성화:
```bash
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

2. 패키지 설치: 
```bash
pip install -r requirements.txt
```

3. 수정



## 📦 Commit 메시지 컨벤션 (Conventional Commits)

본 프로젝트는 [Conventional Commits](https://www.conventionalcommits.org/) 표준을 따릅니다.

### ✅ 기본 형식



### ✍️ 커밋 타입 예시

| 타입        | 설명                                |
|-------------|-------------------------------------|
| `feat`      | 새로운 기능 추가                    |
| `fix`       | 버그 수정                           |
| `docs`      | 문서 변경 (README 등)              |
| `style`     | 코드 포맷팅, 세미콜론 누락 등       |
| `refactor`  | 코드 리팩토링 (기능 변화 없음)       |
| `test`      | 테스트 코드 추가 또는 수정          |
| `chore`     | 빌드, 패키지 설정 등 기타 변경사항   |

### 💡 예시

```bash
git commit -m "feat: 사용자 로그인 기능 추가"
git commit -m "fix: 게시글 생성 시 오류 수정"
git commit -m "docs: README에 커밋 규칙 추가"
git commit -m "style: 코드 들여쓰기 수정"
git commit -m "refactor: DB 모델 구조 개선"
git commit -m "test: 유저 모델 테스트 추가"
git commit -m "chore: 패키지 의존성 업데이트"

