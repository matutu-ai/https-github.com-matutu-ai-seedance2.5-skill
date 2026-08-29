#!/usr/bin/env python3
"""Structural smoke test for the upgraded Seedance skill."""

import json
import sys
from pathlib import Path


SKILL = Path(__file__).resolve().parents[1]
REQUIRED_WORKFLOWS = [
    "main-pipeline",
    "input-analysis",
    "product-analysis",
    "video-objective",
    "creative-structure",
    "hook-engine",
    "storyboard",
    "shot-feasibility",
    "camera",
    "sound-design",
    "continuity",
    "product-multi-view",
    "reference-video-analysis",
    "prompt-compiler",
    "prompt-qa",
]
REQUIRED_SCHEMAS = [
    "video-project.schema.json",
    "subject-lock.schema.json",
    "storyboard.schema.json",
    "dialogue.schema.json",
]
REQUIRED_TEMPLATES = [
    "product-video",
    "ugc-video",
    "product-demo",
    "story-ad",
    "shot-by-shot",
]
REQUIRED_TESTS = [
    "product-video",
    "multi-view-product",
    "character-product",
    "dialogue-video",
    "reference-video",
    "prompt-optimization",
    "industrial-product",
]
PROMPT_SECTIONS = [
    "规格",
    "导演意图",
    "参考素材职责",
    "产品锁",
    "人物锁",
    "场景锁",
    "时间轴",
    "摄影",
    "光线",
    "声音",
    "连续性",
    "负面约束",
    "结尾状态",
]


def check(condition, message, failures):
    status = "PASS" if condition else "FAIL"
    print(f"[{status}] {message}")
    if not condition:
        failures.append(message)


def main():
    failures = []

    for name in REQUIRED_WORKFLOWS:
        check((SKILL / "workflows" / f"{name}.md").exists(), f"workflow {name}.md exists", failures)

    for name in REQUIRED_SCHEMAS:
        path = SKILL / "schemas" / name
        exists = path.exists()
        check(exists, f"schema {name} exists", failures)
        if exists:
            try:
                json.loads(path.read_text(encoding="utf-8"))
                print(f"[PASS] schema {name} is valid JSON")
            except json.JSONDecodeError as exc:
                print(f"[FAIL] schema {name} is invalid JSON: {exc}")
                failures.append(f"schema {name} JSON")

    for name in REQUIRED_TEMPLATES:
        check((SKILL / "templates" / f"{name}.md").exists(), f"template {name}.md exists", failures)

    for name in REQUIRED_TESTS:
        check((SKILL / "tests" / f"{name}.md").exists(), f"test {name}.md exists", failures)
        result = SKILL / "tests" / "results" / f"{name}.md"
        if result.exists():
            result_text = result.read_text(encoding="utf-8")
            check("Final Prompt" in result_text and "READY" in result_text, f"result {name}.md has Final Prompt + READY", failures)
        else:
            print(f"[FAIL] result {name}.md missing")
            failures.append(f"result {name}.md")

    template = (SKILL / "references" / "template.md")
    text = template.read_text(encoding="utf-8")
    for section in PROMPT_SECTIONS:
        check(f"【{section}】" in text, f"template has section {section}", failures)

    skill_md = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    check(skill_md.startswith("---"), "SKILL.md has frontmatter", failures)
    check("workflows/main-pipeline.md" in skill_md, "SKILL.md routes to main pipeline", failures)

    if failures:
        print(f"\n{len(failures)} check(s) failed")
        return 1
    print("\nAll structural checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
