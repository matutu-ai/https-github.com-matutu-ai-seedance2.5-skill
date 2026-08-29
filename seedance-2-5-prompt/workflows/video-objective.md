# Video Objective Engine

自动判断视频目的。不同目的使用不同导演逻辑，不要让结构模板替目的做决定。

## 目的类型

```text
PRODUCT_SHOWCASE   产品展示
UGC                用户生成内容
PRODUCT_DEMO       产品演示
TUTORIAL           教程
UNBOXING           开箱
REVIEW             测评
PROBLEM_SOLUTION   问题解决
BEFORE_AFTER       前后对比
VISUAL_HOOK        视觉钩子
STORY_AD           故事广告
BRAND_AD           品牌广告
PRODUCT_LAUNCH     新品发布
```

## 判断依据

- 出现“使用方法/功能步骤” → DEMO 或 TUTORIAL。
- 出现“开箱/配件/包装” → UNBOXING。
- 出现“使用感受/优缺点” → REVIEW 或 UGC。
- 出现“痛点+解决方案” → PROBLEM_SOLUTION 或 BEFORE_AFTER。
- 出现“品牌精神/情感故事” → STORY_AD 或 BRAND_AD。
- 只有外观和卖点 → PRODUCT_SHOWCASE。

## 导演逻辑差异

| 目的 | 结构倾向 | 产品出现时间 |
|---|---|---|
| PRODUCT_SHOWCASE | 外观 → 细节 → 使用 | 0-1 秒 |
| PRODUCT_DEMO | 痛点 → 操作 → 结果 | 1-2 秒 |
| UNBOXING | 开箱 → 配件 → 第一印象 | 0-1 秒 |
| STORY_AD | 人物/情境 → 产品介入 → 结局 | 中后段 |
| BEFORE_AFTER | 问题状态 → 产品使用 → 解决状态 | 中段 |

## 输出

填充 `objective` 字段：`type`、`intent`、`success_metrics`、`platform_constraints`。
