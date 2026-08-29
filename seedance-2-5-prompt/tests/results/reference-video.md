# Test 05 Result｜参考视频重构

## Pipeline Trace

- Input Type: `VIDEO_REFERENCE`
- Task: `ANALYZE + GENERATE`
- Objective: `PROBLEM_SOLUTION`
- Creative: 桌面收纳盒原创方案，只学参考结构
- Output Mode: `ONE_SHOT_PROMPT`

## Reference Analysis

- 0-3秒 Hook：开箱瞬间 + 一句好奇提问
- 镜头数：约8镜，单镜 1.5-2.5 秒
- 景别：CLOSE_UP / MACRO 为主
- 运镜：固定或轻微推近，无环绕
- 产品出现时间：0-1 秒
- 展示方式：开箱 → 细节 → 使用前后对比
- 声音：口语旁白 + 环境音，无 BGM
- 转场：硬切为主
- 节奏：快，前 3 秒信息密集
- 情绪：惊喜、省心
- CTA：引导到链接

## Original Concept

新项目：桌面收纳盒。原创意不复制参考视频的具体产品与台词，只复用“开箱惊喜 → 细节 → 使用前后对比 → 收束”的结构。

## Final Prompt

【规格】
12秒，9:16竖屏，30fps，无字幕，无背景音乐。

【导演意图】
桌面收纳盒问题解决广告：开场桌面杂乱特写，收纳盒出现后桌面变整洁；只出现手部，不出现脸。

【参考素材职责】
@图片1：ROLE PRODUCT_APPEARANCE；INHERIT shape/color/material/logo；DO NOT INHERIT background/text/watermark。

【产品锁】
桌面收纳盒：外形、颜色、材质、Logo、隔板数量不变。允许变化：无。

【人物锁】
无清晰人脸；只出现一双手。

【场景锁】
书桌桌面。空间关系：收纳盒放在桌面中央，乱物在两侧。

【时间轴】

0-2秒｜杂乱钩子
第一帧已是手部把散乱数据线扔到桌上的动作中间帧。
镜头：CLOSE_UP，固定。声音：数据线碰撞、环境音。

2-5秒｜收纳盒出现
手部把收纳盒放入画面，打开盖板，展示内部隔层。
镜头：MEDIUM_CLOSE_UP，固定或轻微推近。声音：盒体放置、盖板开合。

5-9秒｜整理过程
手部依次把数据线、遥控器、文具放入不同隔层，一次一个动作。
镜头：CLOSE_UP，固定。声音：放置声、轻微摩擦。

9-12秒｜整洁收束
桌面整洁，收纳盒盖好，画面固定。
镜头：WIDE，固定。声音：环境音渐弱。

【摄影】
35mm close-up，浅景深，主体居中，单一主运镜。

【光线】
柔和顶光加窗光，色温5200K，低对比，全程一致。

【声音】
AMBIENCE：室内低频。SFX：放置、开合、摩擦。VOICE/DIALOGUE：无。BGM：无。

【连续性】
同一收纳盒：隔板数量、颜色、Logo一致；乱物从有到无有明确过程；产品不消失/不复制。

【负面约束】
不要清晰人脸；不要改产品设计；不要物体凭空消失；不要穿模；不要字幕/Logo/水印/UI。

【结尾状态】
收纳盒盖好、桌面整洁，画面停留约1秒自然收尾。

## QA

- SPEC: PASS
- PRODUCT: PASS
- CHARACTER: PASS（NO FACE）
- SCENE: PASS
- ACTION: PASS（每镜 LOW-MEDIUM）
- CAMERA: PASS
- LIGHTING: PASS
- SOUND: PASS
- DIALOGUE: N/A
- CONTINUITY: PASS
- NEGATIVE: PASS
- ENDING: PASS
- Reference 结构已拆解且未复制：PASS
- Prompt Readiness Score: Clarity 95 / Actionability 95 / Continuity 95 / Product Fidelity 98 / Character Fidelity 100 / Camera Executability 95 / Audio Completeness 95 / Temporal Coherence 95
- Status: `READY`
