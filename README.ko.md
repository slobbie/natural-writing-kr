# Natural Writing KR

[English](README.md)

AI 에이전트가 문맥과 독자에 맞는 한국어를 작성하고 다듬도록 돕는 스킬입니다. 단어와 종결어미만 바꾸는 데 그치지 않고, 원래 의미와 글이 쓰이는 상황을 함께 살핍니다.

서비스 화면, 공지사항, 이메일, 문서 등에서 사용할 수 있습니다. 모든 서비스에 같은 말투를 적용하지 않고, 해당 서비스나 문서의 말투를 따릅니다.

## 어떤 일을 하나요?

- 누가 무엇을 하는지, 조건과 이유, 숫자 등 원문의 의미를 지킵니다.
- 사용자가 지정한 말투나 기존 문구를 참고합니다. 합니다체와 해요체 모두 상황에 따라 사용할 수 있습니다.
- 독자에게 익숙하고 문맥에 맞는 외래어, 전문 용어, 서비스 용어는 그대로 씁니다.
- 원문이 자연스러우면 억지로 고치지 않습니다.
- 화면 문구는 사용자가 보고 있는 화면과 수행할 행동을 고려합니다.
- 확인된 제품 동작과 확인이 필요한 내용을 구분합니다.

예를 들어 사용자가 필터를 적용하는 화면에서 `필터를 걸러주세요`는 필터와 걸러낼 항목이 혼동되는 표현입니다. 화면과 동작에 따라 `필터를 적용해 주세요`가 더 적절할 수 있습니다. 이 예시는 모든 `필터` 표현을 바꾸라는 규칙이 아닙니다.

## 설치하기

[skills CLI](https://github.com/vercel-labs/skills)로 이 저장소의 스킬을 설치할 수 있습니다.

```bash
npx skills add slobbie/natural-writing-kr --skill natural-writing-kr
```

설치 과정에서 Codex, Claude Code 또는 둘 다 선택하세요. Node.js와 npm이 필요합니다. 기본 설치 범위는 현재 프로젝트이며, 사용자 전체에 설치하려면 `-g`를 추가합니다.

### 수동 설치

Codex와 Claude Code에 같은 스킬 파일을 복사할 수도 있습니다. 아래 명령은 macOS 또는 Linux에서 현재 사용자에게 설치하는 방법입니다. 프로젝트를 내려받고 `skills/natural-writing-kr/SKILL.md`가 있는 프로젝트 폴더에서 실행하세요.

### Codex

```bash
mkdir -p "$HOME/.agents/skills"
if [ -e "$HOME/.agents/skills/natural-writing-kr" ]; then
  echo "이미 설치된 스킬이 있습니다. 업데이트 전에 기존 파일을 확인하세요."
else
  cp -R skills/natural-writing-kr "$HOME/.agents/skills/natural-writing-kr"
fi
```

새 Codex 세션을 열고 `$natural-writing-kr`을 지정해 요청하세요. 요청과 환경에 따라 Codex가 관련 스킬을 자동으로 선택할 수도 있습니다. [Codex 스킬 공식 문서](https://learn.chatgpt.com/docs/build-skills)

### Claude Code

```bash
mkdir -p "$HOME/.claude/skills"
if [ -e "$HOME/.claude/skills/natural-writing-kr" ]; then
  echo "이미 설치된 스킬이 있습니다. 업데이트 전에 기존 파일을 확인하세요."
else
  cp -R skills/natural-writing-kr "$HOME/.claude/skills/natural-writing-kr"
fi
```

새 Claude Code 세션에서 `/natural-writing-kr`을 호출하세요. Claude가 스킬 설명을 보고 자동으로 선택할 수도 있습니다. 위 개인 설치 경로는 로컬 세션용이며 Claude Code의 클라우드 세션과 Cowork는 스킬을 불러오는 방식이 다릅니다. [Claude Code 스킬 공식 문서](https://code.claude.com/docs/en/skills)

위 명령은 기존 설치를 덮어쓰지 않습니다. 업데이트할 때는 기존 폴더를 확인하고 백업한 뒤 교체하세요. 다른 한국어 글쓰기 스킬이나 전역 지침과 충돌한다면 해당 설정을 확인해야 합니다. 이 스킬을 설치해도 기존 설정은 자동으로 해제되지 않습니다.

## 스킬 사용하기

설치한 뒤 서비스의 맥락을 함께 제공해 요청할 수 있습니다.

```text
예약 설정 화면의 확인 문구와 오류 문구를 작성해 주세요.
서비스의 기존 해요체를 따르고, 명시된 제품 동작을 지켜 주세요.
```

```text
이 공지문의 한국어를 검토해 주세요. 날짜와 조건, 원래 의미는 유지하고
이미 자연스러운 문장은 그대로 둬 주세요.
```

말투를 맞추는 것이 중요하다면 서비스의 글쓰기 기준이나 대표 문구를 함께 제공해 주세요. 필요한 맥락이 없다면 제품 동작을 지어내지 않고 확인이 필요한 부분을 밝힙니다. 스킬을 명시해 호출할 수 있지만, 모델에 따라 답변이 완전히 같지는 않을 수 있습니다.

## 보조 검사 도구

동봉된 Python 스크립트는 검토할 만한 표현을 찾습니다. 발견된 표현이 반드시 오류이거나 AI가 쓴 글이라는 뜻은 아닙니다. 발견된 항목이 없어도 자연스러운 한국어임을 보장하지 않습니다.

```bash
python3 skills/natural-writing-kr/scripts/audit_korean_text.py path/to/file.md
python3 skills/natural-writing-kr/scripts/audit_korean_text.py --quality --genre product-copy path/to/file.md
python3 skills/natural-writing-kr/scripts/audit_korean_text.py --after-examples
```

기본 설정에서는 표현이 발견돼도 실패 종료 코드가 나오지 않습니다. 신호가 발견될 때 실패 코드가 필요한 작업에서만 `--fail-on-findings`를 사용하세요. 입력 파일이나 동봉 예시가 없으면 오류로 처리합니다.

## 테스트와 한계

프로젝트 폴더에서 검사 도구 테스트를 실행합니다.

```bash
python3 -m unittest discover -s tests -v
```

검사 도구는 문자열 패턴을 찾는 방식이므로 전체 문맥이나 제품 동작을 이해하지 못합니다. 중요한 문구는 대표 문맥과 제품 명세를 함께 확인해 주세요.

## 서드파티 자료

이 프로젝트는 `humanizer-kr`의 참고 문서와 검사 도구 등을 가져와 수정했습니다. 원본 저작권과 MIT 라이선스는 [서드파티 고지](THIRD_PARTY_NOTICES.md)에 보존했습니다. 통합의 출발점이 된 로컬 설치본의 정확한 원본 버전은 확인되지 않았습니다.
