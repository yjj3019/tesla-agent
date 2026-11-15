## 데이터 융합 알고리즘

### 입력
- nav: 테슬라 네비게이션 등급 (있을 때)
- x: TrafficXAgent 결과
- site: SiteAgent 결과
- weather: WeatherAgent 결과

### 융합 단계
```
1. 유효 소스 필터
   sources = [s for s in (nav, x, site) if s.status == success and age <= 60min]

2. 등급 정규화
   grade ∈ {원활, 서행, 정체}
   severity = {원활:1, 서행:2, 정체:3}

3. 일치 판단
   if all grades equal:
     final = that grade
     confidence += 0.15
   else:
     apply Consensus with Fallback
     confidence -= 0.1

4. 가중 보조 (선택)
   score = Σ (severity × source_weight × recency_factor)
   source_weight: nav 0.8, site 0.75, x_recent 0.6, x_old 0.4
   recency_factor: ≤30min 1.0, 30~60min 0.7

5. 원인 결합
   cause = highest priority among (사고 > 공사 > 행사 > 기상 > 교통량)
   from X or site

6. 날씨 결합
   weather = WeatherAgent or "확인 불가"
   if weather impacts traffic: add to cause

7. 출력
   {
     grade: final,
     cause: cause,
     weather: weather,
     confidence: clamp(base + adjustments, 0, 1),
     sources: used_sources,
     conflict: bool
   }
```

### 신뢰도 기본값
| 소스 | 기본 |
|------|------|
| nav | 0.8 |
| site | 0.75 |
| x ≤30min | 0.6 |
| x 30~60min | 0.4 |
| weather | 0.85 |

### 조정
- 복수 일치: +0.15
- 충돌: -0.1
- 원인 명확(차선 정보): +0.1
- 소스 실패: 해당 소스 감점

### 원칙
- 안전 우선 (불확실하면 더 나쁜 쪽)
- 출처 항상 명시
- 60분 초과 데이터 제외
