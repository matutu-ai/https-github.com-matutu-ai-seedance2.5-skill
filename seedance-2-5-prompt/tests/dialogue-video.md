# Test 04｜口播视频

## 输入

品牌：某新品牌名（生僻读音）。
要求：台词逐字锁定、品牌名读音、环境音、无回声。

## 期望输出

```text
DIALOGUE LOCK: speaker/start/end/tone/speed/text/repeat_count/pronunciation
PRONUNCIATION: 品牌名附拼音，禁止同音替换
SOUND: AMBIENCE + VOICE，无BGM
NEGATIVE: no echo, no repeated line, no subtitle
```

## 验收标准

- [ ] 每句只出现一次，不回声不重复。
- [ ] 品牌名附拼音或明确读音。
- [ ] 台词逐字输出，无改字/漏字/增字。
- [ ] QA 标记 `READY`。
