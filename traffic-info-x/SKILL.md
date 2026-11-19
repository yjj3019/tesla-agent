---
name: traffic-info-x
description: "Tesla voice traffic. Trigger ONLY if contains: 경로 교통정보 | 교통정보 요약 | 주변 교통정보. Do NOT trigger on 교통 어때. Speak 2-3 sentences. Yellow=서행 Red=정체. Never 전구간원활."
type: workflow
lifecycle: active
---

# Traffic Info X

## 1. Trigger (오탐 방지)
**아래 핵심 구문이 포함될 때만** 발동. 비슷해도 이 구문이 없으면 무시.

| 필수 구문 | 허용 |
|-----------|------|
| 경로 교통정보 | 띄어쓰기 무시, “요약/해줘” 있어도 됨 |
| 교통정보 요약 | “교통 정보 요약”, “교통정보요약” |
| 주변 교통정보 | “주변 교통 정보”, “근처 교통정보” |

**발동 안 함**:
- “교통 어때”, “교통 좋아”, “막혀” (요약/정보 없음)
- “날씨”, “음악”, “히터”, “네비 꺼”
- 핵심 구문 없이 “교통”만 있는 경우

## 2. Output (음성용, 2~3문장)
```
날씨는 [상태] [기온]도입니다.
[도로]이 [서행/정체/원활]입니다.
예상 [분] 걸립니다.
```

## 3. Rules
- Weather first. Yellow → 서행. Red → 정체.
- Forbidden: "전 구간 원활"
- Only on-route. X last 60 min.

## 4. Sources
@HappyTraffic @seoultopis @smartroad @Busan_TIC @poltra053 @16889090 @poltra032 @TBNGwangju @poltra042
