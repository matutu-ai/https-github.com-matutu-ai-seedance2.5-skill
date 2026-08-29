# Test 06 Result｜已有 Prompt 优化

## Pipeline Trace

- Input Type: `EXISTING_PROMPT`
- Task: `OPTIMIZE`
- Objective: `PRODUCT_DEMO`
- Creative: 保留“桌面风扇三档风力”原创意
- Output Mode: `ONE_SHOT_PROMPT`

## Analyze（原始弱点）

- 时间轴：没有分段，动作与时间混写。
- 动作过载：一镜同时“拿起、旋转、调档、倒水、放回”。
- 连续性：产品 Logo 和档位状态没有锁。
- 声音：只有“环境音”，没有分层。
- 结尾：没有收束状态。

## Preserve

保留原始创意：桌面风扇、三档风力、手部操作、无字幕。

## Repair

- 拆成 4 镜：出风钩子 → 调档 → 风力对比 → 收束。
- 每镜只保留一个产品动作。
- 增加产品锁、场景锁、声音分层、连续性。

## Final Prompt

【规格】
10秒，9:16竖屏，30fps，无字幕，无背景音乐。

【导演意图】
桌面风扇产品演示：开场强风瞬间吸引注意，再演示三档调节，最后落在安静桌面收束；只出现手部。

【参考素材职责】
@图片1：ROLE PRODUCT_APPEARANCE；INHERIT shape/color/material/logo/button position；DO NOT INHERIT background/text/watermark。

【产品锁】
桌面风扇：外形、颜色、材质、Logo、按键位置、档位指示灯不变。允许变化：无。

【人物锁】
无清晰人脸；只出现一双手。

【场景锁】
简洁书桌。空间关系：风扇居中，纸张在出风方向。

【时间轴】

0-2秒｜风力钩子
第一帧已是风扇叶片转动加速的动作中间帧，纸张被吹起。
镜头：CLOSE_UP，固定。声音：风声、纸张翻动。

2-5秒｜调档
手部按下二档键，指示灯变化。
镜头：MEDIUM_CLOSE_UP，固定或轻微推近。声音：按键“嗒”、风声变化。

5-8秒｜三档
手部按下三档键，风力增强，桌布轻摆。
镜头：CLOSE_UP，固定。声音：风声增强、桌布摆动。

8-10秒｜收束
风扇停在一档，桌面安静，画面固定。
镜头：MEDIUM，固定。声音：风声渐弱、环境音。

【摄影】
35mm close-up，浅景深，主体居中，单一主运镜。

【光线】
柔和侧光，色温5200K，低对比，全程一致。

【声音】
AMBIENCE：室内低频。SFX：按键、风声、纸张翻动。VOICE/DIALOGUE：无。BGM：无。

【连续性】
同一风扇：Logo、按键、指示灯状态按步骤变化；纸张位置合理；产品不消失/不复制；左右手不镜像。

【负面约束】
不要改产品设计；不要产品消失/复制/穿模；不要手指异常；不要字幕/Logo/水印/UI。

【结尾状态】
风扇停在桌面中央，画面固定约1秒自然收尾。

## QA

- SPEC: PASS
- PRODUCT: PASS
- CHARACTER: PASS（NO FACE）
- SCENE: PASS
- ACTION: PASS（每镜一个产品动作）
- CAMERA: PASS
- LIGHTING: PASS
- SOUND: PASS
- DIALOGUE: N/A
- CONTINUITY: PASS
- NEGATIVE: PASS
- ENDING: PASS
- 原始创意保留：PASS
- Prompt Readiness Score: Clarity 98 / Actionability 95 / Continuity 98 / Product Fidelity 98 / Character Fidelity 100 / Camera Executability 95 / Audio Completeness 95 / Temporal Coherence 98
- Status: `READY`
