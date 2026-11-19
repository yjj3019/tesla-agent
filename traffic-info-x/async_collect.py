#!/usr/bin/env python3
"""Async collector pattern for traffic skill agents.
Simulates parallel Weather / X / Site with timeout.
"""
import asyncio
import random
import time

TIMEOUT = 15.0

async def weather_agent():
    await asyncio.sleep(random.uniform(0.1, 0.4))
    if random.random() < 0.2:
        raise TimeoutError("weather")
    return {"agent": "weather", "temp": 14, "cond": "맑음"}

async def traffic_x_agent():
    await asyncio.sleep(random.uniform(0.2, 0.8))
    if random.random() < 0.3:
        return {"agent": "x", "status": "empty"}
    return {"agent": "x", "cause": "반포대교 공사"}

async def site_agent():
    await asyncio.sleep(random.uniform(0.3, 1.0))
    return {"agent": "site", "grade": "서행"}

async def collect():
    tasks = [
        asyncio.wait_for(weather_agent(), TIMEOUT),
        asyncio.wait_for(traffic_x_agent(), TIMEOUT),
        asyncio.wait_for(site_agent(), TIMEOUT),
    ]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    ok = [r for r in results if not isinstance(r, Exception)]
    fail = [r for r in results if isinstance(r, Exception)]
    return ok, fail

async def bench(n=20):
    t0 = time.perf_counter()
    for _ in range(n):
        await collect()
    elapsed = time.perf_counter() - t0
    print(f"{n} rounds in {elapsed:.3f}s ({elapsed/n*1000:.1f} ms/round)")
    print("parallel: weather+x+site overlap; wall time ≈ slowest agent")

if __name__ == "__main__":
    asyncio.run(bench())
