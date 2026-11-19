---
name: traffic-info-x
description: "Tesla voice traffic. Trigger if: (경로 AND 교통) OR (교통정보 AND 요약) OR ((주변 OR 근처) AND 교통). Speak 2-3 sentences. Yellow=서행 Red=정체. Never 전구간원활."
type: workflow
lifecycle: active
---

# Traffic Info X

## 1. Trigger (정교 매칭)
공백 제거 후 아래 **패턴**과 대조한다.

| 패턴 | 의미 | 예시 |
|------|------|------|
| `경로` + `교통` | 경로 모드 | 경로 교통정보, 경로교통 요약 |
| `교통정보` + `요약` | 경로 또는 주변 | 교통정보 요약 |
| `주변` 또는 `근처` + `교통` | 주변 모드 | 주변 교통정보 |

```
normalize(text) = remove spaces
if ("경로" in t and "교통" in t) → route
elif ("교통정보" in t and "요약" in t) → route_or_nearby
elif (("주변" in t or "근처" in t) and "교통" in t) → nearby
else → ignore
```

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
