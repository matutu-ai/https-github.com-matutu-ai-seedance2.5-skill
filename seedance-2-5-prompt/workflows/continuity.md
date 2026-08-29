# Continuity Engine

连续性不是最后才检查，而是在分镜阶段就锁定，最后再统一复查。

## 检查维度

### 人物

```text
脸
发型
服装
配饰
标志性特征
```

### 产品

```text
外观
数量
位置
状态
Logo
文字
```

### 场景

```text
空间布局
光线
时间
```

### 动作

```text
左右方向
运动轨迹
前后关系
```

### 摄影

```text
镜头方向
镜像
景别
```

## 禁止项

```text
人物突然换脸
产品突然变色
产品凭空消失
产品复制
手指异常
物体穿模
左右方向错误
```

## No-Face / Face Policy

用户要求 NO FACE / NO CLEAR FACE / PRODUCT ONLY / HANDS ONLY / BACK VIEW / SILHOUETTE 时，必须同时传递到：

```text
CHARACTER LOCK
CAMERA
SHOT
NEGATIVE
```

不能只在人物锁写一次。

## 输出

填充 `continuity` 字段，并把高风险禁止项写入 `negative_constraints`。
