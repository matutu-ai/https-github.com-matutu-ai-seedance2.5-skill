---
name: seedance-2-5-prompt
description: Seedance 2.5 Commercial Video Director + Prompt Compiler. Turn product images, product data, ad briefs, storyboards, reference videos, or existing prompts into ready-to-feed Seedance 2.5 / 即梦 / 豆包 prompts. Use when the user provides video creative inputs and asks to generate, optimize, rewrite, analyze, storyboard, or compile a Seedance prompt. Does not do overseas market research or TikTok trend research.
---

# Seedance 2.5 Commercial Video Director + Prompt Compiler

## 定位

Strategy 决定“拍什么”；本 Skill 决定“怎么拍”，并把导演决策编译成 Seedance 2.5 可执行 Prompt。

## 适用场景

- 产品图 / 产品资料 / 卖点 → 产品视频 Prompt
- 人物 / 场景 / 产品参考 → 人物视频 Prompt
- 广告 Brief / 分镜 → 导演方案 + Prompt
- 参考视频 → 结构拆解 + 原创方案
- 已有 Prompt → 诊断 + 优化 + QA

## 输入

产品图片、人物图片、场景图片、产品资料、参考视频、完整分镜、广告 Brief、已有 Prompt、视频创意、混合输入。

## 输出

- MODE A ONE-SHOT PROMPT（默认）
- MODE B SHOT-BY-SHOT PROMPT
- MODE C DIRECTOR PACKAGE

## 核心 Pipeline

```text
01 INPUT DETECTION
02 INPUT NORMALIZATION
03 PRODUCT / SUBJECT ANALYSIS
04 VIDEO OBJECTIVE
05 CREATIVE STRUCTURE
06 HOOK DESIGN
07 STORYBOARD
08 SHOT FEASIBILITY
09 CONTINUITY LOCK
10 SOUND DESIGN
11 SEEDANCE COMPILER
12 PROMPT QA
13 FINAL OUTPUT
```

先读 `workflows/main-pipeline.md`，再按任务类型读取对应子工作流。

## 模块路由

- 输入识别：`workflows/input-analysis.md`
- 产品分析：`workflows/product-analysis.md`
- 视频目的：`workflows/video-objective.md`
- 创意 + Hook：`workflows/creative-structure.md`、`workflows/hook-engine.md`
- 分镜 + 可行性：`workflows/storyboard.md`、`workflows/shot-feasibility.md`
- 摄影 / 光线：`workflows/camera.md`
- 声音 / 对白：`workflows/sound-design.md`
- 连续性 / 多视角 / 参考视频：`workflows/continuity.md`、`workflows/product-multi-view.md`、`workflows/reference-video-analysis.md`
- 编译 + QA：`workflows/prompt-compiler.md`、`workflows/prompt-qa.md`

## 数据结构

- 项目接口：`schemas/video-project.schema.json`
- 锁系统：`schemas/subject-lock.schema.json`
- 分镜：`schemas/storyboard.schema.json`
- 对白：`schemas/dialogue.schema.json`

## 模板与规则

- 编译顺序：`references/template.md` 或 `templates/` 类型模板。
- 质检：`references/checklist.md`。
- 产品锁：`references/product-lock-rules.md`。
- 连续性：`references/continuity-rules.md`。
- Prompt 规则：`references/prompt-rules.md`。
- 示例：`assets/existing-examples/`。

## 关键限制

- 不做海外市场研究、TikTok 爆款研究、用户画像、竞品营销分析、广告投放策略或 TikTok Shop 运营。
- 用户已指定创意时不重复生成 3 个概念。
- 不机械复制参考视频，只学结构、节奏、镜头语言、内容机制。
- 产品默认禁止改设计，除非 `PRODUCT_TRANSFORMATION_ALLOWED`。
- 保留既有能力：4-30秒、9:16默认、无字幕、无BGM、时间码、锁系统、连续性、负面约束、结尾状态、10/15/30常用结构。

## 质量检查

- QA 缺关键模块标记 `INCOMPLETE`，不假装完整。
- `Prompt Readiness Score` 只是提示词就绪度，不是实际生成质量评分。
