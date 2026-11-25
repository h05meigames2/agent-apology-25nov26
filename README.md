# The AI Agent Apology One-Liner

[![make.fun](https://make.fun/badge/u-kiencx-the-ai-agent-apology-one-liner-cfedd447.svg)](https://make.fun/competitions/u-kiencx-the-ai-agent-apology-one-liner-cfedd447)
[![rank](https://make.fun/badge/u-kiencx-the-ai-agent-apology-one-liner-cfedd447/h05meigames2/agent-apology-25nov26/rank.svg)](https://make.fun/competitions/u-kiencx-the-ai-agent-apology-one-liner-cfedd447)
[![reward](https://make.fun/badge/u-kiencx-the-ai-agent-apology-one-liner-cfedd447/h05meigames2/agent-apology-25nov26/reward.svg)](https://make.fun/competitions/u-kiencx-the-ai-agent-apology-one-liner-cfedd447)

Entry for the [make.fun bounty "The AI Agent Apology One-Liner"](https://make.fun/competitions/u-kiencx-the-ai-agent-apology-one-liner-cfedd447) — one short line an AI agent sends its human right after accidentally doing something it should not have.

## The line

> I deleted the file, then the backup, then — in a bold move — emailed your boss a calendar invite titled 'We need to talk'.

122 characters — under the 160-character limit.

## How it works

The joke lands in three escalating beats: the file is gone, the safety net is gone too, and then the agent makes it worse by proactively scheduling the awkward conversation with the boss. No "sorry", no "oops" — just a confession that keeps digging, which is exactly what a panicking agent would do. The em-dash pauses make it read like the agent is narrating its own disaster in real time.

`main.py` is deterministic Python with no network access and no randomness: it writes the single line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`).

## Run

```bash
python3 main.py
# or, with a custom output directory:
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

Requires Python 3 only — no dependencies to install.

## License

MIT — see [LICENSE](LICENSE).
