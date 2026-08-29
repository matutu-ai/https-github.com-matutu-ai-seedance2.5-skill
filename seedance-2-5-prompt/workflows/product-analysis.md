# Product / Subject Analysis

对产品视频自动提取产品信息并建立 Product Lock。

## 提取字段

```text
产品名称
产品类别
外观
颜色
材质
结构
尺寸比例
按钮
接口
Logo
文字
包装
配件
功能
使用方式
核心卖点
不可改变元素
```

信息来自用户资料、产品图、参考视频或已有 Prompt。缺项不猜测，标为 `UNKNOWN`，不要在 Prompt 里虚构。

## Product Lock

默认建立：

```text
PRODUCT LOCK
- shape unchanged
- proportions unchanged
- material unchanged
- color unchanged
- logo unchanged
- structure unchanged
- accessory count unchanged
- text unchanged
```

电商视频额外锁定：

```text
形状、比例、颜色、材质、结构、Logo、文字、按钮、接口、数量、包装、配件
```

## 变形规则

- 默认禁止 AI 自行修改产品设计。
- 只有用户明确要求变形/拆解/创意变化时，才允许变化，并显式写入 `PRODUCT_TRANSFORMATION_ALLOWED: true`。
- 允许变化时仍要锁定“变化前”和“变化后”两个状态，禁止出现中间态漂移。

## 输出

填充 `video-project.schema.json` 的 `product` 字段，并把产品锁写入 `product.lock`（符合 `subject-lock.schema.json`）。
