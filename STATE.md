# 현재 상태

검증일: 2026-09-08

- 첫 버전 작성 완료. `skills/korean-no-slop`에 공통 규칙과 매체별 참고 문서를 구성했다.
- `README.md`에 새 작성·패치·검토 호출 예와 설치 안내를 작성했다.
- 구조 검증 및 skill-creator 검증 통과. 독립 생성 14개 사례의 기본 검사와 원문 대조 완료. 실제 출력은 `evals/runs/initial.json`, 상세 판정과 한계는 `evals/RESULTS.md`에 있다.
- 사용자 환경의 기존 skill 경로 `~/.codex/skills/korean-no-slop`에 정본 폴더를 심볼릭 링크로 연결했다. 새 작업의 자동 선택 여부는 아직 확인하지 않았다.
- 원격: Chrome에서 [Kororu-lab/korean-no-slop](https://github.com/Kororu-lab/korean-no-slop) 공개 저장소를 생성하고 skill·평가·안내 19개 파일을 게시했다. 최초 게시 트리 `1bf73f820c11173f79cda38864c797c84768cf42`가 로컬과 일치함을 확인했다.
- 공개 범위: 사용자 공개 승인 확인. 배포 라이선스는 미정이다.
- 검증의 한계: 한 모델·한 문맥의 합성 사례 배치. 미적용 대비 개선율, 다른 모델, 실제 UI·PPTX 렌더링은 미검증이다.
- 로컬 이력: 원격 초기화 전 커밋은 `local-bootstrap` 브랜치에 보존하고, `main`은 원격 `main`을 추적하도록 연결한다.
- 다음 실행: 새 작업에서 `$korean-no-slop`으로 실제 산출물 한 건을 작성하거나 패치하고 결과를 검토한다.
- 후속 검증: 새 작업에서 명시 호출과 자동 선택을 확인하고, 실제 UI 또는 발표 자료 한 건에 적용한다.
