# 현재 상태

검증일: 2026-09-08

- 첫 버전 작성 완료. `skills/korean-no-slop`에 공통 규칙과 매체별 참고 문서를 구성했다.
- `README.md`에 새 작성·패치·검토 호출 예와 설치 안내를 작성했다.
- 구조 검증 및 skill-creator 검증 통과. 독립 생성 14개 사례의 기본 검사와 원문 대조 완료. 실제 출력은 `evals/runs/initial.json`, 상세 판정과 한계는 `evals/RESULTS.md`에 있다.
- 사용자 환경의 기존 skill 경로 `~/.codex/skills/korean-no-slop`에 정본 폴더를 심볼릭 링크로 연결했다. 새 작업의 자동 선택 여부는 아직 확인하지 않았다.
- 원격: Chrome에서 [Kororu-lab/korean-no-slop](https://github.com/Kororu-lab/korean-no-slop) 공개 저장소를 생성했다. 실제 파일 게시와 원격 검증은 진행 중이다.
- 공개 범위: 사용자 공개 승인 확인. 배포 라이선스는 미정이다.
- 검증의 한계: 한 모델·한 문맥의 합성 사례 배치. 미적용 대비 개선율, 다른 모델, 실제 UI·PPTX 렌더링은 미검증이다.
- 다음 실행: 검증한 파일을 GitHub에 게시하고 원격 트리와 로컬 파일의 해시를 대조한다.
- 후속 검증: 새 작업에서 명시 호출과 자동 선택을 확인하고, 실제 UI 또는 발표 자료 한 건에 적용한다.
