# Tests

测试用途：验证 Skill 升级后仍能完成核心导演流程，并保留既有能力。

## 测试列表

| 文件 | 场景 | 核心断言 |
|---|---|---|
| `product-video.md` | 运动摇摇杯，无脸、多视角、10秒 | PRODUCT LOCK、无清晰人脸、同一产品多视角 |
| `multi-view-product.md` | 耳机，产品锁、多视角、微距、无脸 | 产品不漂移、视角完整 |
| `character-product.md` | 人物使用产品 | 人物/产品一致、连续动作 |
| `dialogue-video.md` | 口播视频 | 对白逐字、品牌读音、无回声 |
| `reference-video.md` | 参考视频重构 | 原创方案、不复制内容 |
| `prompt-optimization.md` | 已有 Prompt 优化 | 保留原创意、修复时间轴/过载/连续性 |
| `industrial-product.md` | 工业产品 | 结构不变、工业场景、多视角 |

## 运行方式

1. 用 `run_tests.py` 做结构校验。
2. 对每个测试执行 `workflows/main-pipeline.md`，把 Final Prompt 放入 `results/`。
3. 用 `references/checklist.md` 逐项复查，QA 标记 `READY` 才算通过。

Seedance 实际生成质量不在本测试范围；测试只验证 Prompt 就绪度。
