# Hook Engine

前 1-3 秒必须重点设计。Hook 必须与产品真实卖点相关。

## Hook 类型

```text
VISUAL_HOOK          视觉反差
ACTION_HOOK          动作瞬间
PROBLEM_HOOK         痛点提问
CURIOSITY_HOOK       好奇缺口
RESULT_HOOK          结果前置
TRANSFORMATION_HOOK  变化过程
PRODUCT_HOOK         产品本体
CONTRAST_HOOK        对比反差
SPEED_HOOK           速度感
SOUND_HOOK           声音吸引
```

## 设计规则

- 第一帧必须已经在动作中间，不能是空镜或慢速入场。
- 0.7 秒内出现视觉变化或信息触发。
- 3 秒内完成状态改变。
- Hook 与产品卖点必须直接相关。
- 禁止为了吸引注意力制造与产品无关的夸张内容。

## 输出

填充 `hook` 字段：`type`、`description`、`start`、`duration`、`relation_to_selling_point`。
