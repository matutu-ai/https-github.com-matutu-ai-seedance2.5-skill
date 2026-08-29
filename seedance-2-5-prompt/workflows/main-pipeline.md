# Main Pipeline

本文件是 Seedance 2.5 Commercial Video Director + Prompt Compiler 的主编排流程。所有任务都从这里进入，按需读取子工作流。

## 13 步标准流程

```text
01 INPUT DETECTION
02 INPUT NORMALIZATION
03 PRODUCT / SUBJECT ANALYSIS
04 VIDEO OBJECTIVE
05 CREATIVE STRUCTURE
06 HOOK DESIGN
07 STORYBOARD
08 SHOT FEASIBILITY
09 CONTINUITY LOCK
10 SOUND DESIGN
11 SEEDANCE COMPILER
12 PROMPT QA
13 FINAL OUTPUT
```

## 步骤路由

1. 输入识别与规范化：读取 `input-analysis.md`。
2. 产品/主体理解：读取 `product-analysis.md`；无产品时跳过产品锁。
3. 视频目的：读取 `video-objective.md`。
4. 创意结构：读取 `creative-structure.md`；用户已给创意时直接执行，未给时生成 3 个概念并推荐 BEST CONCEPT。
5. Hook 设计：读取 `hook-engine.md`。
6. 分镜：读取 `storyboard.md`。
7. 镜头可行性：读取 `shot-feasibility.md`；动作过载自动拆镜。
8. 连续性锁：读取 `continuity.md`。
9. 声音设计：读取 `sound-design.md`。
10. 编译 Prompt：读取 `prompt-compiler.md`。
11. QA：读取 `prompt-qa.md`；任何关键模块缺失标记 `INCOMPLETE`，回到对应步骤修复，不假装完整。
12. 输出：按输出模式交付 FINAL READY-TO-FEED PROMPT。

## 架构边界

本 Skill 只负责“怎么拍”和“怎么告诉模型拍出来”。不承担海外市场研究、TikTok 爆款研究、用户画像、国家市场分析、竞品营销分析、广告投放策略或 TikTok Shop 运营。这些输入应来自上游 Creative Strategy Skill。

## 标准输出

用户只说“帮我生成 Seedance 视频”时，默认输出：

1. 创意方向
2. 核心 Hook
3. 分镜
4. Seedance 一次性投喂 Prompt
5. QA

用户只要 Final Prompt 时，只输出 Final Prompt。

## 数据结构

整个流程维护一个 `video-project.schema.json` 对象，子工作流只填充自己的字段。该 Schema 是未来被其他 Skill 调用的核心接口。
