# Input Analysis

自动识别用户输入类型，判断任务模式，并做输入规范化。不要让用户重复说明已经提供的信息。

## 输入类型

```text
A PRODUCT_IMAGE      产品图片
B CHARACTER_IMAGE    人物图片
C SCENE_IMAGE        场景图片
D PRODUCT_DATA       产品资料 / 卖点 / 参数
E VIDEO_REFERENCE    参考视频
F STORYBOARD         完整分镜
G AD_BRIEF           广告 Brief
H EXISTING_PROMPT    已有 Seedance Prompt
I MIXED              混合输入
```

判断依据：优先看是否有图片/视频附件，其次看文本是否包含分镜时间码、对白、卖点或完整 Prompt 结构。

## 任务模式

```text
GENERATE    从创意/素材生成新视频 Prompt
OPTIMIZE    优化已有 Prompt
REWRITE     在保留创意的前提下重构 Prompt
ANALYZE     只拆解参考视频或现有 Prompt，不生成
STORYBOARD  只输出分镜
COMPILE     只做 Prompt 编译
```

映射规则：

- 输入 H：先分析弱点，默认 `OPTIMIZE`，保留原创意。
- 输入 E：默认进入 `reference-video-analysis.md`，产出原创方案。
- 输入 A/D/G/F：默认 `GENERATE`。
- 用户只要分析：`ANALYZE`。
- 用户只要分镜：`STORYBOARD`。
- 用户已经给分镜和创意、只要 Prompt：`COMPILE`。

## 输入规范化

- 把所有素材编号为 `@图片1`、`@图片2`、`@视频1`，记录每个素材的职责、继承项和不继承项。
- 规格缺失时按默认值补齐：9:16、无字幕、无 BGM、时长 10-15 秒（未指定时）。
- 时间码统一为 `start-end` 秒，不保留含糊表述。
- 对白统一进入 `dialogue.schema.json` 结构。
- 多条信息冲突时，按以下优先级：

```text
用户明确指令
> 产品锁
> 人物锁
> 场景锁
> 参考图
> 模型默认推断
```

## 输出

填充 `video-project.schema.json` 的 `input` 字段：`input_type`、`detected_task`、`sources`、`raw_brief`。
