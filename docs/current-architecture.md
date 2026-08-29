# Current Architecture Audit

审计日期：2026-08-29  
仓库：`matutu-ai/seedance2.5-skill`  
技能：`seedance-2-5-prompt`

## 1. 当前功能

- 把分镜脚本、广告文案、用户 Brief、已有 Prompt 优化为可直接投喂 Seedance 2.5 / 即梦 / 豆包的视频生成提示词。
- 支持 4-30 秒时间码控制、9:16 默认画幅、参考素材职责声明、人物/场景/道具/对白锁、无字幕、无 BGM。
- 支持三种输出形态：一次性投喂版、逐段独立投喂版、完整叙事框架版。

## 2. 当前输入

- 产品图片 / 人物图片 / 场景图片
- 产品资料 / 卖点
- 参考视频 / 参考图片
- 完整分镜
- 广告 Brief
- 已有 Prompt
- 视频创意 / 规格（时长、画幅、帧率、字幕、BGM）

## 3. 当前输出

- 默认：精简一次性投喂版，可直接粘贴 Seedance / 即梦。
- 拆段需求：逐段独立投喂版，注明拼接顺序与转场要求。
- 完整方案需求：先输出叙事框架，再附一次性投喂版。

## 4. 当前目录结构

```text
seedance2.5-skill/
├── README.md
├── seedance-2.5-prompt-template.md
└── seedance-2-5-prompt/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── references/template.md
    ├── references/checklist.md
    └── assets/
        ├── example-10s-korean-cafe-prompt.md
        ├── example-15s-hitachi-elevator-prompt.md
        ├── example-16s-webswing-prompt.md
        └── example-30s-juechang-opera-prompt.md
```

## 5. 当前模板规则

统一结构顺序不可乱：

`规格 → 导演意图 → 素材职责 → 锁 → 时间轴 → 摄影/声音 → 负面约束 → 结尾状态`

- 对白较多时增加【口播台词表｜逐字锁定】，逐字输出、禁止同音替换、每句只出现一次。
- 品牌名、生僻词附拼音或明确读音（例如日立=Rì Lì、自建房=Zì Jiàn Fáng）。
- 提供 10 / 15 / 30 秒常用时长骨架。

## 6. 当前规则

- 0-3 秒第一帧必须在动作中间，不是空镜、不是慢慢走进房间。
- 每个参考素材声明“负责什么 + 不负责什么”。
- 人物固定特征只写一次，时间轴只写本镜增量。
- 对白标注起止时间、说话人、口吻、repeat_count=1、不回声。
- 负面约束只写高风险项：不变形、不换脸、不穿帮、不重复钩子动作、无字幕/Logo/水印/UI。
- 结尾必须有明确收束状态，避免模型硬切。
- 未指定画幅时默认 9:16；未指定 BGM 时明确无 BGM。

## 7. 当前示例

- `example-10s-korean-cafe-prompt.md`：10 秒韩语咖啡馆，16:9、24fps、手持 DV/16mm 质感。
- `example-15s-hitachi-elevator-prompt.md`：15 秒日立别墅电梯广告，9:16、口播拼音锁。
- `example-16s-webswing-prompt.md`：16 秒雨夜蛛丝动作片，9:16、女性主角、紫色耳机。
- `example-30s-juechang-opera-prompt.md`：30 秒民国戏曲短剧《绝唱》，9:16、逐字台词表。

## 8. 当前限制

- 没有自动输入类型识别（GENERATE / OPTIMIZE / REWRITE / ANALYZE / STORYBOARD / COMPILE）。
- 没有标准 JSON Schema，无法作为稳定的跨 Skill 接口。
- 没有独立 Product Lock / No-Face Policy / Multi-view / Camera / Lighting / Sound Engine。
- 没有参考视频反向拆解工作流。
- 没有 Prompt Readiness Score 与 QA 分级。
- 创意结构主要依赖固定时长骨架，缺少动态结构选择。
- 没有测试集。

## 9. 可复用模块（升级时保留）

- 参考素材职责格式：`@图片N 负责什么 + 不负责什么`。
- 人物锁 / 场景锁 / 道具锁 / 对白锁写法。
- 对白拼音防错规则。
- 时间码结构：`时间 / 镜头 / 画面动作 / 声音`。
- 连续性检查项：人物、产品、道具、走位、镜像。
- 负面约束策略：只写高风险项。
- 结尾状态写法。
- 10 / 15 / 30 秒常用骨架。
- 现有四个示例 Prompt。

## 10. 不允许破坏的功能

1. 4-30 秒视频支持
2. 9:16 默认画幅
3. 参考素材职责声明
4. 人物锁
5. 场景锁
6. 道具锁
7. 对白锁
8. 无字幕
9. 无 BGM
10. 时间码
11. 摄影
12. 声音
13. 连续性
14. 负面约束
15. 结尾状态
16. 10/15/30 秒常用结构
17. 现有示例
