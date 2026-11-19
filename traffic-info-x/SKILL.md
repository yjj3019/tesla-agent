---
name: traffic-info-x
description: "Tesla voice traffic. Trigger: 경로 교통정보 요약|교통정보 요약|주변 교통정보. Speak 2-3 sentences: weather first, then road status, then ETA. Yellow=서행 Red=정체. Never say 전구간원활. No off-route."
type: workflow
lifecycle: active
---

# Traffic Info X

## 1. Trigger
- 경로 교통정보 요약 → route mode
- 교통정보 요약 → route if set, else nearby
- 주변 교통정보 → nearby mode
- Other phrases → do not respond

## 2. Output (음성용, 2~3문장)
설명 없이 아래만 말한다.

```
날씨는 [상태] [기온]도입니다.
[도로]이 [서행/정체/원활]입니다.
예상 [분] 걸립니다.
```

예시:
```
날씨는 맑고 14도입니다.
올림픽대로가 서행입니다.
예상 70분에서 80분 걸립니다.
```

색상 확인 불가 시:
```
날씨는 맑고 14도입니다.
네비 색상은 확인되지 않았습니다.
X 기준 특이사항 없습니다.
```

## 3. Rules
- Weather first. Use Tesla Grok weather. If fail: "날씨 확인 불가"
- Read nav map color. Yellow → 서행. Red → 정체. Green → 원활
- Forbidden: "전 구간 원활", "이상 없음", "문제없습니다"
- Only roads on current route
- X data: last 60 min, on-route only

## 4. Examples
```
날씨는 맑고 14도입니다.
올림픽대로가 서행입니다.
예상 70분에서 80분 걸립니다.
```
```
날씨는 확인되지 않았습니다.
경인고속도로가 정체입니다.
예상 50분에서 60분 걸립니다.
```

## 5. Sources
@HappyTraffic @seoultopis @smartroad @Busan_TIC @poltra053 @16889090 @poltra032 @TBNGwangju @poltra042
