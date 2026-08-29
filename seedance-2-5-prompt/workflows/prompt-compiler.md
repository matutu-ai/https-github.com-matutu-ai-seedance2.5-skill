# Prompt Compiler

把导演决策编译为 Seedance 2.5 可执行 Prompt。

## 输入

```text
Product
Character
Scene
Creative
Storyboard
Camera
Lighting
Sound
Continuity
Negative
```

## 输出模式

### MODE A：ONE-SHOT PROMPT

一次性投喂版，默认输出。

### MODE B：SHOT-BY-SHOT PROMPT

逐镜头生成版，每镜可独立生成，注明拼接顺序与转场要求。

### MODE C：DIRECTOR PACKAGE

导演方案 + 分镜 + Prompt 完整包。

## 输出顺序

默认顺序不可乱：

```text
【规格】
【导演意图】
【参考素材职责】
【产品锁】
【人物锁】
【场景锁】
【时间轴】
【摄影】
【光线】
【声音】
【连续性】
【负面约束】
【结尾状态】
```

无产品时省略【产品锁】；无人物时省略【人物锁】。

## 编译规则

- 人物固定特征只写一次，时间轴只写本镜增量。
- 对白按 Dialogue Lock 逐字输出，品牌名附拼音或明确读音。
- 负面约束只写本项目的高风险项。
- 用户只要 Final Prompt 时，不输出分析过程。
