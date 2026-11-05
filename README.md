# Natural Writing KR

[한국어](README.ko.md)

A Korean writing skill for AI agents. It helps write, revise, and review Korean with attention to context, meaning, and the reader.

Use it for product interfaces, notices, emails, documentation, and other Korean writing. The skill follows the voice of the service or document instead of assuming that every product should use the same tone.

## What it does

- Preserves the original meaning, including who does what, conditions, reasons, and numbers.
- Uses a requested voice or representative existing copy. Both formal `합니다` and conversational `해요` can be appropriate.
- Keeps familiar loanwords, technical terms, and established product vocabulary when they fit the audience and context.
- Leaves an already natural sentence alone instead of rewriting it for the sake of change.
- Considers the current screen and user action when writing interface labels and messages.
- Separates verified product behavior from information that still needs confirmation.

For example, where a user applies a filter, `필터를 걸러주세요` confuses the filter with the items being filtered. Depending on the screen and action, `필터를 적용해 주세요` may be clearer. This is an illustration, not a replacement rule for every use of `필터`.

## Install

Install the skill from this repository with the [skills CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add slobbie/natural-writing-kr --skill natural-writing-kr
```

Choose Codex, Claude Code, or both when prompted. Node.js and npm are required. This installs in the current project by default; add `-g` to install for your user.

### Manual installation

The same skill files can be copied for Codex and Claude Code. The commands below install for the current user on macOS or Linux. Download this project, then run the commands from its root directory, where `skills/natural-writing-kr/SKILL.md` exists.

### Codex

```bash
mkdir -p "$HOME/.agents/skills"
if [ -e "$HOME/.agents/skills/natural-writing-kr" ]; then
  echo "A skill already exists at $HOME/.agents/skills/natural-writing-kr; review it before updating."
else
  cp -R skills/natural-writing-kr "$HOME/.agents/skills/natural-writing-kr"
fi
```

Open a new Codex session and explicitly request `$natural-writing-kr`. Codex may also select a relevant skill automatically; selection depends on the request and environment. See the [Codex skills documentation](https://learn.chatgpt.com/docs/build-skills).

### Claude Code

```bash
mkdir -p "$HOME/.claude/skills"
if [ -e "$HOME/.claude/skills/natural-writing-kr" ]; then
  echo "A skill already exists at $HOME/.claude/skills/natural-writing-kr; review it before updating."
else
  cp -R skills/natural-writing-kr "$HOME/.claude/skills/natural-writing-kr"
fi
```

Start a new Claude Code session and invoke `/natural-writing-kr`. Claude may also select the skill based on its description. These personal directories apply to local sessions; Claude Code cloud and Cowork sessions use different skill sources. See the [Claude Code skills documentation](https://code.claude.com/docs/en/skills).

The commands do not overwrite an existing installation. To update one, compare and back up the existing folder before replacing it. If another Korean writing skill or global instruction conflicts, review those settings; installing this skill does not automatically disable them.

## Use the skill

For example, after installing the skill, provide the relevant product context:

```text
Write the confirmation and error messages for a reservation settings screen.
Use the service's existing 해요 tone and preserve the stated product behavior.
```

```text
Review the Korean in this notice. Keep the dates, conditions, and intended meaning.
If something is already natural, leave it unchanged.
```

When an established voice matters, provide representative copy or the service's writing guide. If necessary context is missing, the skill should state the uncertainty rather than invent product behavior. An explicit skill invocation improves discoverability but does not guarantee identical outputs across models.

## Optional text audit

The included Python script flags text patterns for review. A match is not proof of an error or AI authorship, and no findings do not guarantee natural Korean.

```bash
python3 skills/natural-writing-kr/scripts/audit_korean_text.py path/to/file.md
python3 skills/natural-writing-kr/scripts/audit_korean_text.py --quality --genre product-copy path/to/file.md
python3 skills/natural-writing-kr/scripts/audit_korean_text.py --after-examples
```

By default, findings do not cause a failing exit status. Use `--fail-on-findings` only when a workflow explicitly needs a nonzero status for any signal. Missing input and missing bundled examples are errors.

## Testing and limitations

Run the audit script tests from the project root:

```bash
python3 -m unittest discover -s tests -v
```

The audit script is pattern-based; it cannot understand the full context or verify product behavior. Review important copy with representative context and relevant product specifications.

## Third-party material

This project incorporates and modifies material from `humanizer-kr`, including reference guides and an audit script. The original copyright and MIT license are preserved in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). The starting local installation's exact upstream revision has not been established.
