---
name: traffic-info-x
description: "Tesla voice traffic. Trigger: 경로 교통정보 요약|교통정보 요약|주변 교통정보. Speak 2-3 sentences: weather first, then road status, then ETA. Yellow=서행 Red=정체. Never say 전구간원활. No off-route."
type: workflow
lifecycle: active
---

# Traffic Info X

## 1. Trigger (음성 인식 허용)
아래와 **비슷하게** 들려도 이 스킬을 사용한다.

| 정확 | 허용 변형 |
|------|-----------|
| 경로 교통정보 요약 | 경로 교통 정보 요약, 경로교통정보요약, 경로 교통정보 |
| 교통정보 요약 | 교통 정보 요약, 교통정보요약, 교통 요약 |
| 주변 교통정보 | 주변 교통 정보, 주변교통정보, 근처 교통 |

- “해줘”, “알려줘”, “좀” 은 있어도 된다.
- 핵심 명사(경로/교통/주변/요약)가 있으면 발동.
- 완전히 다른 문장(“날씨 어때”, “음악 틀어”)은 무시.

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

## 3. Rules
- Weather first. Yellow → 서행. Red → 정체.
- Forbidden: "전 구간 원활"
- Only on-route roads. X data last 60 min.

## 4. Sources
@HappyTraffic @seoultopis @smartroad @Busan_TIC @poltra053 @16889090 @poltra032 @TBNGwangju @poltra042
