# Camera + Lighting Engine

统一管理可执行摄影描述，避免“非常电影感”这类不可执行形容词。

## Camera 字段

```text
景别
机位
焦段感
运镜
速度
景深
对焦
运动轨迹
```

## 可执行写法

不要写：

> 非常电影感的高级镜头。

改写为：

> 50mm medium close-up，camera slowly pushes in 20cm，subject remains centered，shallow depth of field。

运镜只保留一个主方向：

```text
STATIC / PUSH IN / PULL BACK / TILT / PAN
FOLLOW / HANDHELD / TRACKING / LOW ANGLE FOLLOW / SLOW ZOOM
```

需要甩镜、俯冲、穿过前景等特殊动作时，单独写明触发点和速度。

## Lighting 字段

```text
光源
方向
强度
色温
对比度
阴影
环境光
变化轨迹
```

## 光线一致性

- 同一场景内光线变化必须合理。
- 禁止同一场景一秒白天、一秒夕阳、一秒霓虹夜景，除非用户明确要求。
- 光线变化要在时间轴中写明触发点和方向，例如“开门后晨光进入，曝光自然调整”。

## 输出

填充 `camera` 和 `lighting` 字段。最终 Prompt 按用户语言习惯输出中文或英文。
