# Prompt QA

最终 Prompt 必须逐模块检查。任何关键模块缺失，标记 `INCOMPLETE`，不假装完整。

## 检查模块

```text
SPEC
PRODUCT
CHARACTER
SCENE
ACTION
CAMERA
LIGHTING
SOUND
DIALOGUE
CONTINUITY
NEGATIVE
ENDING
```

每个模块状态：`PASS` / `MISSING` / `WEAK`。

## Prompt Readiness Score

评分维度：

```text
Clarity
Actionability
Continuity
Product Fidelity
Character Fidelity
Camera Executability
Audio Completeness
Temporal Coherence
```

每项 0-100。

注意：这是 `Prompt Readiness Score`，不是 Seedance 实际生成质量评分，不得混淆。

## 修复规则

- `MISSING`：回到对应 workflow 补齐。
- `WEAK`：改为可执行描述。
- 动作过载：回到 `shot-feasibility.md` 拆镜。
- 光线冲突：回到 `camera.md` 修正。
- 连续性冲突：回到 `continuity.md` 修复。

## 输出

填充 `qa` 字段：`status`、`checks`、`missing_modules`、`score`、`notes`。
