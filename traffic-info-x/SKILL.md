---
name: traffic-info-x
description: "Tesla traffic skill. Trigger: 경로 교통정보 요약 | 교통정보 요약 | 주변 교통정보. Output exactly 4 lines: Weather / Route / Cause / ETA. Weather required. Yellow=slow, Red=jam. Never all-clear. No off-route."
type: workflow
lifecycle: active
---

# Traffic Info X

## 1. Trigger
- 경로 교통정보 요약 → route mode
- 교통정보 요약 → route if set, else nearby
- 주변 교통정보 → nearby mode
- Other phrases → do not respond

## 2. Output (only this)
```
날씨: [상태] [기온]도
경로: [도로] 원활/서행/정체
원인: [한줄 또는 없음]
소요: [분]
```

## 3. Rules
- Weather first. Use Tesla Grok weather. If fail: "날씨 확인 불가"
- Read nav map color. Yellow → 서행. Red → 정체. Green → 원활
- Forbidden: "전 구간 원활", "이상 없음", "문제없습니다"
- Only roads on current route
- X data: last 60 min, on-route only

## 4. Examples
```
날씨: 맑음 14도
경로: 올림픽대로 서행, 경부고속도로 원활
원인: 반포대교 공사
소요: 70~80분
```
```
날씨: 날씨 확인 불가
경로: 경인고속도로 정체
원인: 김포IC 사고
소요: 50~60분
```

## 5. Sources
@HappyTraffic @seoultopis @smartroad @Busan_TIC @poltra053 @16889090 @poltra032 @TBNGwangju @poltra042
