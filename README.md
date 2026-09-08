# Korean No Slop

한국어 글·UI·슬라이드를 작성하고 수정하는 공통 skill.

[GitHub 저장소](https://github.com/Kororu-lab/korean-no-slop)

상투적인 대조와 부정 열거, 장식용 em dash, 화면을 채우는 부제, 슬라이드의 과도한 문장, 삭제한 내용이 설명으로 돌아오는 문제를 다룬다.

## 예시

| 요청·상황 | 적용 결과 |
| --- | --- |
| `알림 설정` 아래 제목을 반복하는 설명 | 설명 요소와 전용 여백 제거 |
| 슬라이드 항목 `처리 시간이 30% 감소했습니다.` | `처리 시간 30% 단축` |
| `A 비교를 빼줘` | A 비교와 그 제외를 설명하는 문구가 빠진 결과 |
| `X가 아니라 Y입니다`라는 장식적 대조 | 필요한 내용을 직접 서술 |
| 이미 충분히 간결한 화면 | 기존 구성 유지 |

숫자·조건·불확실성·필수 경고와 제품 동작을 보존한다. 요청한 비교나 의미 있는 부정, 필요한 도움말도 유지한다. 매체와 사용자의 지시에 따라 생략할 요소를 판단한다.

## 사용

새로 작성할 때:

```text
$korean-no-slop을 적용해 알림 설정 화면을 만들어줘.
이메일 알림과 푸시 알림을 각각 켜고 끌 수 있으면 돼.
```

기존 결과를 고칠 때:

```text
$korean-no-slop으로 이 발표 자료를 패치해줘.
중복 부제를 없애고, 항목을 화면에서 읽기 쉽게 줄여줘.
경쟁사 비교는 자료 전체에서 빼줘.
```

검토만 할 때:

```text
$korean-no-slop으로 이 보고서를 검토해줘.
수정이 필요한 위치와 제안만 알려줘.
```

`SKILL.md`가 새 작성·패치·검토를 구분하고 필요한 매체별 규칙을 읽는다. 패치는 에이전트가 원본 파일에 적용한다. 실행 스크립트로 문장을 일괄 치환하는 방식은 제공하지 않는다.

## 설치

이 저장소의 `skills/korean-no-slop` 폴더가 배포 단위다. `SKILL.md`, `references/`, `agents/`를 함께 둔다. 도구 의존성 없이 Markdown 지침으로 동작한다.

Codex에서는 skill 폴더를 프로젝트의 `.agents/skills/korean-no-slop` 또는 개인용 skill 디렉터리에 복사하거나 연결한다. 공식 문서의 개인용 경로는 `~/.agents/skills`다. 기존 환경이 `~/.codex/skills`를 사용하는 경우 실제 로딩 경로를 확인해 하나만 선택한다. 같은 이름을 두 경로에 중복 설치하면 선택기에 중복 표시될 수 있다. [공식 설치·탐색 문서](https://learn.chatgpt.com/docs/build-skills)

저장소의 최신 파일을 프로젝트에 연결하는 예:

```sh
mkdir -p /path/to/project/.agents/skills
ln -s /path/to/korean-no-slop/skills/korean-no-slop \
  /path/to/project/.agents/skills/korean-no-slop
```

위 경로를 실제 절대 경로로 바꿔 사용한다. 기존 대상이 있으면 현행 내용을 확인하고 보존한다. 새 skill이 표시되지 않으면 새 작업에서 확인하거나 앱을 다시 시작한다.

다른 에이전트에서는 해당 환경의 skill 경로에 같은 폴더를 배치하거나, `SKILL.md`와 필요한 참고 문서를 작업 지침으로 제공한다. 호스트별 설치·자동 선택 동작은 별도로 확인한다.

## 검증과 개선

`evals/cases.json`에는 새 작성과 편집 요청, `evals/rubric.json`에는 관찰 가능한 판정 기준이 있다. 응답을 만드는 실행에는 rubric을 주지 않는다. 실제 출력은 별도 파일로 보존해 평가한다.

```sh
python3 scripts/check_repository.py
python3 scripts/check_cases.py evals/runs/initial.json
```

첫 명령은 파일 구조·참조·평가 자료를 확인한다. 두 번째는 저장된 출력의 필수 조건과 금지 문자열을 검사한다. 문맥·의미는 원문 대조로, 화면 품질은 렌더링으로 별도 확인한다. 평가 방법은 [evals/README.md](evals/README.md), 첫 실행의 결과와 한계는 [evals/RESULTS.md](evals/RESULTS.md)에 있다.

새 실패 사례를 발견하면 실제 요청, 최소 입력, 문제가 된 결과, 기대 동작을 추가한다. 정상적으로 남겨야 할 유사 사례도 함께 두고 규칙을 수정한다.

배경 자료는 [SOURCES.md](SOURCES.md), 프로젝트 범위는 [PROJECT_BRIEF.md](PROJECT_BRIEF.md), 현재 검증 상태는 [STATE.md](STATE.md)에 있다.
