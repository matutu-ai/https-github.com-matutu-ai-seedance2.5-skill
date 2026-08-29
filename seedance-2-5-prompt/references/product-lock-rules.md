# Product Lock Rules

## 默认锁定

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

电商视频额外锁定：形状、比例、颜色、材质、结构、Logo、文字、按钮、接口、数量、包装、配件。

## 变形规则

- 默认禁止 AI 自行修改产品设计。
- 用户明确要求变形/拆解/创意变化时，写入 `PRODUCT_TRANSFORMATION_ALLOWED: true`。
- 允许变化时锁定变化前和变化后两个状态，禁止中间态漂移。

## 多视角规则

- front / back / left / right / top / bottom / detail / macro / in-use 都必须来自同一个真实产品。
- 多视角之间产品设计不得漂移。
- 每个视角单独成镜或明确转场。

## 工业产品规则

- 产品结构、面板、接口、Logo、指示灯位置不可改变。
- 工业场景按真实使用环境写，不混入无关元素。
- 多视角展示时重点保结构一致性。

## No-Face Product

产品为主、不出现人物面孔时，同时锁定：

```text
CHARACTER LOCK: NO FACE / PRODUCT ONLY / HANDS ONLY
CAMERA: 不拍脸，允许手部近景或产品特写
SHOT: 每镜明确主体是产品
NEGATIVE: no clear face, no second person
```
