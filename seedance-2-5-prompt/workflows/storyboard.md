# Storyboard Engine

每个镜头必须完整、可执行，并控制动作负载。

## 镜头字段

```text
时间
景别
镜头位置
镜头运动
主体动作
产品动作
环境变化
光线
声音
对白
转场
```

景别使用可执行枚举：

```text
EXTREME_WIDE / WIDE / FULL / MEDIUM
MEDIUM_CLOSE_UP / CLOSE_UP / EXTREME_CLOSE_UP / MACRO
```

## 时间轴逻辑

每个时间段按以下顺序推进，不能只写形容词：

```text
第一帧状态
↓
动作
↓
视觉变化
↓
信息出现
↓
结果
```

每个时间段必须明确：

```text
SHOT
ACTION
CAMERA
AUDIO
```

## 动作负载

- 一个镜头只设置有限数量核心动作。
- 主体动作、产品动作、运镜各自独立。
- 动作过载时先拆镜，不硬塞。
- 0-3 秒第一帧必须已经在动作中间。

## 输出

填充 `storyboard` 数组，每项符合 `storyboard.schema.json`。
