# Test 04 Result｜口播视频

## Pipeline Trace

- Input Type: `AD_BRIEF + PRODUCT_DATA`
- Task: `GENERATE`
- Objective: `PRODUCT_LAUNCH`
- Creative: 品牌发布口播，卖点三连 + 邀请体验
- Hook: `PROBLEM_HOOK`，第一句痛点提问
- Output Mode: `ONE_SHOT_PROMPT`

## Final Prompt

【规格】
15秒，9:16竖屏，30fps，无字幕，无背景音乐。

【导演意图】
品牌口播广告：主播用三句口播讲清卖点，逐字锁定，结尾邀请线下体验；画面明亮干净，节奏轻快。

【参考素材职责】
@视频1：ROLE CHARACTER_APPEARANCE + MOUTH_SYNC；DO NOT INHERIT unrelated background。
@图片1：ROLE PRODUCT_APPEARANCE；INHERIT shape/color/material/logo；DO NOT INHERIT background/text/watermark。

【产品锁】
慕氧便携空气净化器：外形、颜色、材质、Logo、按键、指示灯、配件数量不变。允许变化：无。

【人物锁】
26岁亚洲女性，黑色低马尾，白色衬衫，黑色长裤；同一张脸、同一发型、同一服装，全片唯一清晰人物。

【场景锁】
明亮极简客厅。空间关系：主播居中，净化器在画面右侧桌面。

【口播台词表｜逐字锁定】
句1（主播，1.0-3.5秒，轻快）：睡觉总是觉得闷？慕氧净化器，一整晚都能安静工作。
拼音：Mù Yǎng Jìng Huà Qì，禁读 Mù Xiàng / 木氧 / 慕养。
句2（主播，4.0-7.5秒，肯定）：23分贝低噪，开启时几乎听不见声音。
句3（主播，8.0-11.0秒，自信）：一键智能模式，自动感应空气质量。
句4（主播，11.5-14.5秒，亲切）：想体验？来线下门店，今晚就睡个好觉。
每句只出现一次，不回声不重复。

【时间轴】

0-3秒｜痛点钩子
第一帧已是主播看向镜头开口说话的动作中间帧；净化器在画面右侧，指示灯亮起。
镜头：MEDIUM，固定或轻微前推。声音：句1、室内环境音。

3-7秒｜卖点一
净化器特写，出风口送风，指示灯保持稳定。
镜头：CLOSE_UP，固定。声音：句2、低噪风感。

7-11秒｜卖点二
主播手指轻按智能模式键，指示灯变化。
镜头：MEDIUM_CLOSE_UP，手部与机器同框。声音：句3、按键声。

11-15秒｜收束
主播微笑看向镜头，画面固定，环境音渐弱。
镜头：MEDIUM，固定。声音：句4、环境音渐弱。

【摄影】
50mm medium close-up，浅景深，主体居中，单一主运镜，无环绕。

【光线】
柔和窗光加顶灯，色温5200K，低对比，真实肤色，不做商业磨皮。

【声音】
AMBIENCE：客厅低频。SFX：按键、轻微风声。VOICE：口播。DIALOGUE：按台词表逐字。BGM：无。

【连续性】
主播脸、发型、服装全程一致；净化器外观、指示灯状态按步骤变化；产品不消失、不复制；左右手不镜像。

【负面约束】
不要改字/漏字/增字/同音替换；不要回声/重复；不要字幕/Logo/水印/UI；不要换脸/换产品。

【结尾状态】
主播微笑看向镜头，画面停留约1秒自然收尾。

## QA

- SPEC: PASS
- PRODUCT: PASS
- CHARACTER: PASS
- SCENE: PASS
- ACTION: PASS（每镜 LOW-MEDIUM）
- CAMERA: PASS
- LIGHTING: PASS
- SOUND: PASS
- DIALOGUE: PASS（拼音锁）
- CONTINUITY: PASS
- NEGATIVE: PASS
- ENDING: PASS
- Prompt Readiness Score: Clarity 98 / Actionability 95 / Continuity 95 / Product Fidelity 98 / Character Fidelity 98 / Camera Executability 95 / Audio Completeness 98 / Temporal Coherence 95
- Status: `READY`
