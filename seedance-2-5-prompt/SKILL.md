---
name: seedance-2-5-prompt
description: 把分镜脚本、广告文案或用户brief优化为可直接投喂 Seedance 2.5 / 即梦 / 豆包的视频生成提示词。Use when the user provides storyboards, timestamps, dialogue, character/scene specs, or prompt drafts and asks to organize, optimize, summarize, or generate a ready-to-feed video prompt; supports 4-30s timecode control, reference asset role declarations, character/wardrobe/prop locks, dialogue text locking, no-subtitle/no-BGM constraints, and 10/15/16/30s common structures.
---

# Seedance 2.5 可投喂提示词生成

## 工作流

按固定顺序生成或改写提示词：

1. **提取规格**：时长、画幅、帧率、字幕、BGM、旁白、对白语言。未指定画幅时默认 9:16 竖屏。
2. **写导演意图**：一句话说明成片气质与核心叙事。
3. **声明参考素材职责**：每个 `@图片N` 只负责一个职责（人物外观/产品外观/场景布局/材质），并声明“不继承什么”（背景/文字/Logo/水印/光线/人物）。
4. **写锁**：人物锁（脸、发型、痣、服装、鞋、年龄感）、场景与空间锁（门/吧台/窗等相对位置）、道具锁（数量、不消失/不复制/不悬浮）。
5. **写时间轴**：逐段写“时间码 / 镜头 / 画面动作 / 声音”。每段至少一个强动词、一个运镜词、一个环境或光线动态。0-3秒第一帧必须在动作中间。
6. **锁定对白**：逐字写出台词表，标注起止时间、说话人、口吻、`repeat_count=1`，禁止改字、同音替换、回声、叠句。
7. **写摄影/光线/质感**：明确风格关键词（手持DV/16mm/35mm/商业片/纪录片）、光线曲线、肤色规则。
8. **写声音**：环境音层、音效层、人声层分开；无BGM时明确写“不要生成背景音乐”。
9. **写连续性**：人物不变形不换装、道具不穿帮、方向不错镜像、无第二张清晰人脸。
10. **写负面约束**：只写高风险项，不堆无效词。
11. **写结尾状态**：最后1-2秒的定格、收尾运镜或淡出。

## 输出形态

- 默认输出“精简一次性投喂版”，可直接粘贴 Seedance/即梦。
- 用户要拆段或分镜制作时，输出“逐段独立投喂版”，每段可独立生成，并注明拼接顺序与转场要求。
- 用户要完整方案时，先输出完整叙事框架版，再附一次性投喂版。

## 模板与质检

- 使用 `references/template.md` 作为统一结构，顺序不可乱。
- 生成后用 `references/checklist.md` 逐项质检。

## 示例

- 10秒韩语咖啡馆：`assets/example-10s-korean-cafe-prompt.md`
- 16秒雨夜蛛丝动作片：`assets/example-16s-webswing-prompt.md`
- 30秒民国戏曲短剧《绝唱》：`assets/example-30s-juechang-opera-prompt.md`

## 关键原则

- 一致性由参考图锁定，提示词只负责运动；人物固定特征只写一次。
- 对白文本是唯一声音来源，禁止模型自行改字或自行发挥。
- 负面约束只写高风险项：不变形、不换脸、不穿帮、不重复钩子动作、无字幕/Logo/水印/UI。
- 结尾必须有明确收束状态，避免模型硬切。
