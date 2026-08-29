# Test 02 Result｜耳机产品广告

## Pipeline Trace

- Input Type: `PRODUCT_DATA + PRODUCT_IMAGE`
- Task: `GENERATE`
- Objective: `PRODUCT_SHOWCASE`
- Creative: 无线降噪耳机多视角 + 微距细节
- Hook: `PRODUCT_HOOK`，第一帧降噪开启瞬间
- Output Mode: `ONE_SHOT_PROMPT`

## Final Prompt

【规格】
10秒，9:16竖屏，30fps，无字幕，无背景音乐。

【导演意图】
无线降噪耳机产品广告：开场用降噪开启的瞬间制造声音反差，再用多视角与微距展示做工，最后落在佩戴入耳状态；只出现产品与手部，不出现脸。

【参考素材职责】
@图片1：ROLE PRODUCT_APPEARANCE；INHERIT shape/color/material/logo/button position；DO NOT INHERIT background/lighting/text/watermark。

【产品锁】
无线降噪耳机：外形、颜色、材质、Logo、按键、充电接口、配件数量不变。允许变化：无。

【人物锁】
无清晰人脸；只允许手部入画，手指数量一致。

【场景锁】
极简产品背景（浅灰/哑光桌面）。空间关系：耳机居中，配件不散落。

【时间轴】

0-2秒｜钩子
第一帧已是手指按下降噪键的动作中间帧，耳机周围环境音瞬间变静。
镜头：MACRO，固定或轻微推近。声音：按键“嗒”、环境声骤停。

2-5秒｜多视角
front / side / top 三视角展示耳罩、头梁、Logo。
镜头：每个视角单一横移或固定。声音：轻微放置声。

5-8秒｜微距细节
耳罩缝线、按键、充电接口微距特写，材质反光真实。
镜头：EXTREME_CLOSE_UP，浅景深，单一推近。声音：布料摩擦、轻微按键声。

8-10秒｜收束
耳机被手部放回收纳盒，盒盖合上，画面固定。
镜头：中景固定。声音：收纳盒扣合声、环境音渐弱。

【摄影】
60mm macro，浅景深，焦点清晰，单一主运镜，无环绕。

【光线】
侧光加柔光箱，色温5600K，低对比，金属与布料反光真实，全程一致。

【声音】
AMBIENCE：极简空间低频。SFX：按键、放置、收纳盒扣合。VOICE/DIALOGUE：无。BGM：无。

【连续性】
同一产品：Logo、按键、接口、配件数量一致；多视角不出现版本漂移；产品不消失、不复制。

【负面约束】
不要清晰人脸；不要改产品设计；不要产品变色/消失/复制/穿模；不要手指异常；不要字幕/Logo/水印/UI。

【结尾状态】
耳机在收纳盒内，盒盖合上，画面停留约1秒自然收尾。

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
