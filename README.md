# seedance2.5-skill

Seedance 2.5 Commercial Video Director + Prompt Compiler。

自动识别产品图、产品资料、卖点、参考图/视频、分镜、广告 Brief、已有 Prompt，完成导演化、分镜、镜头可行性检查、连续性锁、声音设计，并编译为可直接投喂 Seedance 2.5 / 即梦 / 豆包的提示词。

## 定位边界

- Strategy 决定“拍什么”。
- 本 Skill 决定“怎么拍”。
- Prompt Compiler 决定“怎么告诉模型拍出来”。

本 Skill 不承担海外市场研究、TikTok 爆款研究、用户画像、竞品营销分析、广告投放策略或 TikTok Shop 运营。

## 目录

```text
seedance2.5-skill/
├── seedance-2.5-prompt-template.md
├── docs/current-architecture.md
└── seedance-2-5-prompt/
    ├── SKILL.md
    ├── agents/openai.yaml
    ├── schemas/
    ├── workflows/
    ├── references/
    ├── templates/
    ├── assets/existing-examples/
    └── tests/
```

## 快速使用

复制 `seedance-2.5-prompt-template.md`，按顺序填写：

```text
规格 → 导演意图 → 参考素材职责 → 产品锁 → 人物锁 → 场景锁 → 时间轴 → 摄影 → 光线 → 声音 → 连续性 → 负面约束 → 结尾状态
```

对白较多时加【口播台词表｜逐字锁定】，品牌名和生僻词附拼音。

完整导演流程见 `seedance-2-5-prompt/workflows/main-pipeline.md`。
