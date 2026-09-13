#!/usr/bin/env python
"""PreToolUse guard (Bash matcher): blocks any command that would delete,
move, or overwrite the trained model artifact (models/cacao_leaf_classifier.pt).
This project has no local copy of the original dataset/notebook run to
regenerate it from, so losing this file is not a quick fix."""
import json
import re
import sys

TARGET = r"models/cacao_leaf_classifier\.pt"

PATTERNS = [
    rf"(^|[\s;&|])(rm|mv|truncate)[^|;&]*{TARGET}",
    rf"(^|[\s;&|])cp[^|;&]*{TARGET}\s*($|[;&|])",
    rf">>?\s*{TARGET}",
    rf"sed[^|;&]*-i[^|;&]*{TARGET}",
]


def main():
    payload = json.load(sys.stdin)
    command = payload.get("tool_input", {}).get("command", "") or ""

    if any(re.search(p, command) for p in PATTERNS):
        reason = (
            "Bloqueado pelo hook guard-model-artifact: este comando afeta "
            "models/cacao_leaf_classifier.pt (o modelo treinado). Não há "
            "dataset/notebook local neste repositório para retreinar caso o "
            "arquivo seja perdido ou sobrescrito. Se a ação for mesmo "
            "intencional, faça manualmente fora do agente (ou ajuste/desative "
            "este hook em .claude/settings.json)."
        )
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": reason,
            }
        }))
        return 0

    return 0


if __name__ == "__main__":
    sys.exit(main())
