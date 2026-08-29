# Multi-view Product Support

支持从多个角度展示同一个真实产品，禁止生成不同版本产品。

## 支持视角

```text
front
back
left
right
top
bottom
detail
macro
in-use
```

## 规则

- 所有角度必须来自同一个产品锁。
- 产品形状、比例、颜色、材质、Logo、文字、配件数量全程一致。
- 多视角之间不能出现产品设计漂移。
- 每个视角单独成镜或明确转场，不用一个镜头旋转 360 度硬塞。
- 适用于水杯、耳机、饰品、家居、电子产品和工业产品。

## 输出

把视角顺序写入 storyboard 的 `shot_size`、`camera_position`、`subject_action` / `product_action`，并在连续性中锁定产品。
