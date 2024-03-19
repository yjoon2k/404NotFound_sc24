# Git commit convention

```
TAG: message
ex) feat: add navbar component
```

### TAG

| Tag      | Description                                    |
| -------- | ---------------------------------------------- |
| feat     | 새로운 기능 추가                               |
| fix      | 버그 수정                                      |
| design   | CSS 등 사용자 UI 디자인 변경                   |
| style    | 코드 포맷 변경, 세미 콜론 누락, 코드 변경 없음 |
| refactor | 프로덕션 코드 리팩토링                         |
| comment  | 주석 추가, 변경                                |
| docs     | 문서 수정                                      |
| chore    | 빌드, 패키지 관련 수정, 코드 변경 없음         |
| rename   | 파일명 수정, 이동, 코드 변경 없음              |
| remove   | 파일 삭제, 코드 변경 없음                      |

# Git branch

- main: 직접적인 변경은 Pull Request를 통해서만 이루어집니다.
- dev: 개발용 브랜치로, 기능이나 버그 수정이 이루어집니다.
- feat: 새로운 기능을 개발할 때 사용됩니다. feature/기능-설명 형식으로 브랜치를 생성합니다.
- bugfix: 버그를 수정할 때 사용됩니다. bugfix/버그-설명 형식으로 브랜치를 생성합니다.

### 중요!

코드 작업을 시작하기 전에 항상 dev 브랜치로부터 새로운 브랜치를 생성하고, 작업이 완료되면 Pull Request를 통해 변경 사항을 dev 브랜치에 merge 합니다.
