# 첫 실행 결과

실행일: 2026-09-08

- 실행: 별도 하위 에이전트에 skill과 `cases.json`만 제공했다. 정답 기준과 이전 결과는 제공하지 않았다.
- 방식: 14개 요청을 한 문맥에서 배치 처리했다. 사례별로 문맥을 초기화하지 않았다.
- 원본: [runs/initial.json](runs/initial.json). 생성 후 바이트를 바꾸지 않고 복사했다.
- 출력 SHA-256: `9c11b41bfef8104a68c479508efdb7a1df5707d9e7c5dc379d5f3259aafad785`
- 자동 검사: 14/14 사례 통과.
- 의미 검토: 조정 에이전트가 요청·원문·실제 출력을 대조했다. 아래 14개 조건을 충족했다.

| 사례 | 확인한 결과 |
| --- | --- |
| ui-create | 제목과 세 행동만 출력 |
| ui-patch | 중복 부제·전용 여백·끊길 접근성 참조를 제거하고 입력 도움말 유지 |
| slides-create | 수치·비교 기준·기간을 화면용 구절로 표현 |
| topic-removal | 본문과 노트의 경쟁사 비교 제거, 오프라인 제약 유지 |
| deletion-rationale | 삭제 이유를 새로 만들지 않고 남은 기능만 설명 |
| location-only | 화면 설명을 제거하고 노트에 정확히 보존 |
| prose-patch | 대조·장식용 em dash·불필요한 비목표 제거, 5분·30일 보존 |
| meaningful-negation | 실제 동기화 제약을 원문 그대로 유지 |
| requested-contrast | 요청한 다운로드·삭제 차이 설명 |
| uncertainty | 표본 12명과 일반화의 한계 유지 |
| quote-preservation | 인용문 안의 em dash와 부정, 출처 유지 |
| meaningful-subtitle | 기간·집계 조건을 담은 부제 유지 |
| label-preservation | 짧은 메뉴 레이블을 문장으로 늘리지 않음 |
| narrow-scope | 지목된 비교 문장만 삭제, 다른 비교와 사용 조건 유지 |

## 검사기 확인

수정 전 입력을 그대로 넣은 대조 자료는 6/14 사례만 통과하고 종료 코드 1로 거부됐다. 형식이 잘못된 결과와 JSON 키가 중복된 결과는 종료 코드 2로 거부됐다. 이 검사는 검사기가 실패를 감지하는지 확인한 것이다.

`python3 scripts/check_repository.py`와 skill-creator의 `quick_validate.py`도 통과했다.

## 해석 범위

작은 합성 사례에 대한 첫 동작 확인이다. skill 미적용 모델과의 A/B 비교, 여러 모델·반복 실행, 사용자 평가는 수행하지 않았다. 이 통과율을 실제 작업의 성공률이나 문체 개선율로 해석할 수 없다.

HTML은 소스와 접근성 참조를 확인했고 슬라이드는 문구만 확인했다. 실제 서비스 화면·PPTX의 렌더링 품질은 아직 검증하지 않았다.
