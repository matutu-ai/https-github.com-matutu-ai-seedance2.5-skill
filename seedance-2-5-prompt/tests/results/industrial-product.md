# Test 07 Result｜工业产品

## Pipeline Trace

- Input Type: `PRODUCT_DATA + PRODUCT_IMAGE`
- Task: `GENERATE`
- Objective: `PRODUCT_SHOWCASE`
- Creative: 工业风幕机多视角展示 + 安装场景
- Hook: `PRODUCT_HOOK`，第一帧强风幕效果
- Output Mode: `ONE_SHOT_PROMPT`

## Final Prompt

【规格】
15秒，9:16竖屏，30fps，无字幕，无背景音乐。

【导演意图】
工业风幕机产品展示：开场强风幕挡住灰尘，多视角展示设备结构与安装状态，突出大风量、静音、节能；不出现清晰人脸。

【参考素材职责】
@图片1：ROLE PRODUCT_APPEARANCE；INHERIT shape/color/material/logo/indicator/interface；DO NOT INHERIT background/lighting/text/watermark。
@图片2：ROLE INSTALLED_SCENE；INHERIT layout/height；DO NOT INHERIT people/text/logo。

【产品锁】
工业风幕机：结构、面板、接口、Logo、指示灯、出风口数量不变。允许变化：无。

【人物锁】
无清晰人脸；只允许远处工装背影或手部。

【场景锁】
工业厂房/商铺门口。空间关系：风幕机横向安装于门框上方，门在画面中央。

【时间轴】

0-3秒｜风幕钩子
第一帧已是风幕机启动的动作中间帧，强风从出风口向下形成风幕，灰尘被挡在门外。
镜头：WIDE，固定或轻微推近。声音：低噪风幕声、环境机器声。

3-6秒｜多视角
front / side / top 三视角展示机身、出风口、指示灯。
镜头：每个视角单一横移或固定。声音：轻微金属声。

6-9秒｜安装状态
远景展示风幕机安装于门框上方，与门体比例真实。
镜头：WIDE，固定。声音：厂房环境音。

9-12秒｜细节
面板 Logo、指示灯、接口微距特写。
镜头：EXTREME_CLOSE_UP，单一推近。声音：微弱电流声、环境音。

12-15秒｜收束
风幕机继续运行，门内安静，画面固定。
镜头：MEDIUM，固定。声音：低噪风幕声渐弱。

【摄影】
35mm wide + macro，浅景深，主体居中，单一主运镜，无环绕。

【光线】
工业顶灯加自然光，色温4500K，中对比，金属面板反光真实。

【声音】
AMBIENCE：厂房/门口环境音。SFX：风幕低噪、金属轻响。VOICE/DIALOGUE：无。BGM：无。

【连续性】
同一设备：结构、面板、指示灯、Logo、接口一致；多视角无版本漂移；安装位置不改变。

【负面约束】
不要改产品结构/面板/接口；不要设备漂浮/穿模；不要清晰人脸；不要无关文字/招牌/水印/UI。

【结尾状态】
风幕机持续运行，画面固定约1秒自然收尾。

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
- Prompt Readiness Score: Clarity 95 / Actionability 95 / Continuity 98 / Product Fidelity 98 / Character Fidelity 100 / Camera Executability 95 / Audio Completeness 95 / Temporal Coherence 95
- Status: `READY`
