# Test 03 Result｜人物使用产品

## Pipeline Trace

- Input Type: `CHARACTER_IMAGE + PRODUCT_IMAGE + AD_BRIEF`
- Task: `GENERATE`
- Objective: `PRODUCT_DEMO`
- Creative: 清晨办公室便携咖啡机使用流程
- Hook: `ACTION_HOOK`，第一帧咖啡机出杯
- Output Mode: `ONE_SHOT_PROMPT`

## Final Prompt

【规格】
15秒，9:16竖屏，30fps，无字幕，无背景音乐。

【导演意图】
便携咖啡机使用演示：人物取机、装粉、按压、出杯，动作连续但每镜独立，展示安静快捷；人物与产品全程一致。

【参考素材职责】
@图片1：ROLE CHARACTER_APPEARANCE；DO NOT INHERIT background/text/watermark。
@图片2：ROLE PRODUCT_APPEARANCE；INHERIT shape/color/material/logo；DO NOT INHERIT background/lighting/text。

【产品锁】
便携咖啡机：外形、颜色、材质、Logo、水箱、配件数量不变。允许变化：无。

【人物锁】
25岁亚洲女性，黑色高马尾，深色运动服，白色运动鞋；同一张脸、同一发型、同一服装，全片唯一清晰人物。

【场景锁】
简约办公室桌面。空间关系：咖啡机在画面中央偏右，人物从左侧入画。

【时间轴】

0-3秒｜钩子
第一帧已是咖啡机正在出杯的动作中间帧，咖啡液流入杯中。
镜头：MEDIUM，固定或轻微前推。声音：咖啡机低噪、咖啡滴落。

3-6秒｜取机与装粉
人物拿起咖啡机，旋开粉仓，装入咖啡粉，一次一个动作。
镜头：MEDIUM_CLOSE_UP，手部与机器同框。声音：旋盖、粉末声。

6-9秒｜加水与按压
人物加水至刻度线，盖上盖子，按下按钮。
镜头：CLOSE_UP，单一推近。声音：注水、按键声。

9-12秒｜出杯
咖啡机开始工作，杯中咖啡逐渐上升。
镜头：CLOSE_UP，固定。声音：机器工作声、杯壁轻响。

12-15秒｜收束
人物端起咖啡杯，看向镜头轻点头，画面固定。
镜头：MEDIUM，固定。声音：咖啡机声渐弱、环境音。

【摄影】
35mm medium close-up，浅景深，单一主运镜，手持轻晃但稳定。

【光线】
自然窗光加室内顶光，色温5200K，低对比，真实肤色，不做商业磨皮。

【声音】
AMBIENCE：办公室低频。SFX：旋盖、注水、按键、咖啡滴落。VOICE/DIALOGUE：无。BGM：无。

【连续性】
人物脸、发型、服装、鞋全程一致；产品外观与配件一致；左右手、杯量、产品状态按步骤变化，不跳变。

【负面约束】
不要换脸/换装/换产品；不要产品消失/复制/穿模；不要手指异常；不要字幕/Logo/水印/UI。

【结尾状态】
人物端起咖啡杯，画面固定约1秒自然收尾。

## QA

- SPEC: PASS
- PRODUCT: PASS
- CHARACTER: PASS
- SCENE: PASS
- ACTION: PASS（每镜 LOW-MEDIUM）
- CAMERA: PASS
- LIGHTING: PASS
- SOUND: PASS
- DIALOGUE: N/A
- CONTINUITY: PASS
- NEGATIVE: PASS
- ENDING: PASS
- Prompt Readiness Score: Clarity 95 / Actionability 95 / Continuity 98 / Product Fidelity 98 / Character Fidelity 98 / Camera Executability 95 / Audio Completeness 95 / Temporal Coherence 95
- Status: `READY`
