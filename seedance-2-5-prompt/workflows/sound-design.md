# Sound Design

声音拆成五个独立层，逐层填写。

```text
AMBIENCE  环境音
SFX       动作/机械音效
VOICE     旁白/人声
DIALOGUE  对白
BGM       背景音乐
```

## 支持的音效

```text
环境音
动作音
产品机械声
开关声
碰撞声
液体声
脚步
衣物摩擦
呼吸
转场音
Hook 音效
```

## 规则

- 没有 BGM 时明确写 `NO BACKGROUND MUSIC`，不默认生成。
- 有对白时建立 Dialogue Lock，符合 `dialogue.schema.json`。
- 对白必须逐字、逐句、只出现一次，不回声不重复。
- 旁白与本人同一把声时写明 `voice_same_as`。
- 声音要按时间码标注，不能只写“有环境音”。

## 输出

填充 `sound` 字段：`ambience`、`sfx`、`voice`、`dialogue`、`bgm`。
