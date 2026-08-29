# Test 02｜耳机产品广告

## 输入

产品：无线降噪耳机。
卖点：降噪、长续航、舒适佩戴、音质。
要求：产品锁、多视角、微距细节、无人物脸。

## 期望输出

```text
PRODUCT LOCK: 外形/颜色/材质/Logo/接口/配件数量不变
STORYBOARD: front / side / top / macro detail / in-use
CAMERA: 微距、浅景深、单一主运镜
CONTINUITY: 同一产品，不出现不同版本
NEGATIVE: no face, no product redesign, no duplicated object
```

## 验收标准

- [ ] 多视角产品一致，无版本漂移。
- [ ] 微距细节不改变产品结构。
- [ ] 无清晰人脸。
- [ ] QA 标记 `READY`。
