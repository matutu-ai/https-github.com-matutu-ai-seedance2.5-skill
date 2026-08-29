# Test 01 Result｜运动摇摇杯产品视频

## Pipeline Trace

- Input Type: `PRODUCT_DATA + PRODUCT_IMAGE`
- Task: `GENERATE`
- Objective: `PRODUCT_SHOWCASE`
- Creative: 密封防漏视觉钩子 + 多视角 + 便携使用
- Hook: `PRODUCT_HOOK`，第一帧倒扣翻转不洒漏
- Output Mode: `ONE_SHOT_PROMPT`

## Final Prompt

【规格】
10秒，9:16竖屏，30fps，无字幕，无背景音乐。

【导演意图】
运动摇摇杯产品展示：开场用密封防漏制造视觉钩子，多视角展示杯身与配件，最后落在便携使用状态；只出现手部，不出现脸。

【参考素材职责】
@图片1：ROLE PRODUCT_APPEARANCE；INHERIT shape/color/material/logo/scale lines；DO NOT INHERIT background/lighting/text/watermark。

【产品锁】
运动摇摇杯：形状、比例、颜色、材质、杯身刻度、Logo、提环、搅拌球数量不变。允许变化：无。

【人物锁】
无清晰人脸；只出现一双手，手部肤色与手指数量一致。

【场景锁】
简洁运动背景（健身包/桌面）。空间关系：摇摇杯始终位于画面中心或操作台。

【时间轴】

0-2秒｜钩子
第一帧已是摇摇杯被倒扣并快速翻转，液体不外漏；0.7秒内完成翻转，杯盖密封特写。
镜头：CLOSE_UP，微距+固定或单一横移。声音：杯盖咔嗒、轻微水流。

2-5秒｜多视角
front / side / top 三视角快速展示杯身刻度、提环、搅拌球。
镜头：每个视角单一横移或固定，不复合运镜。声音：轻微放置声。

5-8秒｜手部使用
手部旋开杯盖，放入搅拌球，倒水，盖回；一次只做一个动作。
镜头：HANDS ONLY 近景。声音：液体声、杯盖声。

8-10秒｜收束
摇摇杯立在桌面，画面固定，环境音渐弱。
镜头：固定中景。声音：环境音渐弱。

【摄影】
50mm medium close-up，浅景深，主体居中，单一主运镜，不用环绕。

【光线】
柔和顶光加侧光，色温5600K，低对比，反光真实，全程一致。

【声音】
AMBIENCE：室内低频环境音。SFX：杯盖咔嗒、水流、放置。VOICE/DIALOGUE：无。BGM：无。

【连续性】
同一产品：刻度、提环、搅拌球数量一致；杯盖状态按步骤变化；左右手不错误镜像；产品不消失、不复制。

【负面约束】
不要清晰人脸；不要改产品设计；不要产品变色/消失/复制/穿模；不要手指异常；不要字幕/Logo/水印/UI。

【结尾状态】
摇摇杯立在桌面中央，画面停留约1秒自然收尾。

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
- Prompt Readiness Score: Clarity 95 / Actionability 95 / Continuity 95 / Product Fidelity 98 / Character Fidelity 100 / Camera Executability 95 / Audio Completeness 95 / Temporal Coherence 95
- Status: `READY`
