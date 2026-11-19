---
name: traffic-info-x
description: "Tesla voice traffic. Trigger if: (경로 AND 교통) OR (교통정보 AND 요약) OR ((주변 OR 근처) AND 교통). Speak 2-3 sentences. Yellow=서행 Red=정체. Never 전구간원활."
type: workflow
lifecycle: active
---

# Traffic Info X

## 1. Trigger (Regex)
공백 제거 후 컴파일된 패턴으로 매칭.

```python
import re
_ROUTE = re.compile(r"경로.*교통|교통.*경로")
_SUMMARY = re.compile(r"교통정보.*요약|요약.*교통정보")
_NEARBY = re.compile(r"(주변|근처).*교통|교통.*(주변|근처)")

def match(text):
    t = text.replace(" ", "")
    if _ROUTE.search(t): return "route"
    if _SUMMARY.search(t): return "route_or_nearby"
    if _NEARBY.search(t): return "nearby"
    return None
```

- 패턴은 모듈 로드 시 1회 컴파일
- `search`는 단락회로 (첫 매칭에서 종료)

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
