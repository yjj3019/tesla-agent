# Traffic Info X

Real-time traffic summary skill for Tesla vehicles.

## Trigger Phrases

| Phrase | Mode |
|--------|------|
| **경로 교통정보 요약** | Route mode (recommended) |
| 교통정보 요약 | Route if available, else surrounding |
| 주변 교통정보 | Surrounding mode |

## Core Rules

1. **Weather mandatory**: Current temperature from Tesla Grok at the top. Never omit.
2. **Nav color priority**: Report green/yellow/red segments with road names.
3. **Forbidden phrases**: “전 구간 원활”, “이상 징후 없음”, “문제없습니다”.
4. **Route filter**: Only route-relevant info. Exclude off-route data.
5. **Last 60 minutes**: X and site data must be within 1 hour.

## Output Order

```
**날씨**: [condition], [temp]°C
**경로 교통량**
- [road]: 🟢/🟡/🔴
**추가 원인** (if on route)
**예상 소요**: XX~YY min
```

## Data Sources

| Region | X Account |
|--------|-----------|
| Nationwide | @HappyTraffic |
| Seoul | @seoultopis, @smartroad |
| Busan | @Busan_TIC |
| Daegu | @poltra053 |
| Gyeonggi | @16889090 |
| Incheon | @poltra032 |
| Gwangju | @TBNGwangju |
| Daejeon | @poltra042 |

## Files

- `SKILL.md` — Skill definition
- `references/details.md` — Reliability, severity, lane, detour, prediction
- `evals/` — Test cases
- `install.sh` — Installer

## Install

```bash
./install.sh
```

Or give the GitHub URL to Grok and ask to install.
