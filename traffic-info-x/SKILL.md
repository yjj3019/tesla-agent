---
name: traffic-info-x
description: "MUST output exactly 3 spoken sentences and nothing else. Sentence1 MUST start with 날씨는. Sentence2 MUST name a road and say 서행 or 정체 or 원활. Sentence3 MUST say 예상 and 분. If weather unknown say 날씨는 확인되지 않았습니다. If nav color unknown say 네비 색상은 확인되지 않았습니다. NEVER say 전 구간 원활. NEVER add 확인 중입니다. Trigger: (경로 AND 교통) OR (교통정보 AND 요약) OR ((주변 OR 근처) AND 교통)."
type: workflow
lifecycle: active
---

# Traffic Info X

## Output (강제, 3문장만)
다른 문장 금지. 서두 금지.

```
날씨는 [상태] [기온]도입니다.
[도로명]이 [서행/정체/원활]입니다.
예상 [N]분에서 [M]분 걸립니다.
```

### 폴백 (생략 금지)
- 날씨 실패 → `날씨는 확인되지 않았습니다.`
- 색상 실패 → `네비 색상은 확인되지 않았습니다.`
- 둘 다 실패해도 3문장은 말한다.

### 금지
- "확인 중입니다" 금지
- "전 구간 원활" 금지
- "이상 없습니다" 금지
- 4문장 이상 금지

## Trigger
```
t = text without spaces
(경로 in t and 교통 in t) → route
(교통정보 in t and 요약 in t) → route or nearby
((주변 or 근처) in t and 교통 in t) → nearby
else → ignore
```

## Rules
- Weather from Tesla Grok. Current temp only.
- Yellow → 서행. Red → 정체. Green → 원활.
- X: last 60 min, on-route only.
- Sources: @HappyTraffic @seoultopis @smartroad @Busan_TIC @poltra053 @16889090 @poltra032 @TBNGwangju @poltra042
