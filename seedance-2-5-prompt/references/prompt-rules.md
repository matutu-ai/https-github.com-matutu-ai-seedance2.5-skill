# Prompt Rules

## 默认值

- 画幅未指定：9:16 竖屏。
- BGM 未指定：无背景音乐。
- 字幕未指定：无字幕。
- 时长未指定：按内容复杂度选 10-15 秒。
- 帧率未指定：24fps 或 30fps，按平台习惯选。

## 输出语言

- 默认按用户语言输出。
- 中文 Prompt 保留英文专业词（景别、运镜、材质）时可混合，但必须可执行。
- 不要只输出英文分析再让用户翻译。

## 可执行描述

避免：

> 非常电影感的高级镜头。

使用：

> 50mm medium close-up，camera slowly pushes in 20cm，subject remains centered，shallow depth of field。

## 对白

- 对白按 Dialogue Lock 逐字输出。
- 品牌名、生僻词附拼音 / IPA / 明确读音。
- 禁止改字、漏字、增字、同音替换、自行发挥、重复、回声。

## 负面约束

- 只输出本项目高风险项。
- 默认候选：no deformation、no face change、no product redesign、no duplicated objects、no floating objects、no extra fingers、no mirrored direction、no unwanted subtitles、no watermark、no UI。
- 不无脑堆大量负面词。

## 输出模式

- MODE A ONE-SHOT PROMPT：一次性投喂。
- MODE B SHOT-BY-SHOT PROMPT：逐镜头生成，注明拼接顺序与转场。
- MODE C DIRECTOR PACKAGE：导演方案 + 分镜 + Prompt。

用户只要 Final Prompt 时，不输出分析过程。
