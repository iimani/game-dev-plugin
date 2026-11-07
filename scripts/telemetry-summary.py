#!/usr/bin/env python3
"""Summarises a game's telemetry (docs/process/telemetry.md): one JSON object per line, from one or more runs.

Usage: python3 scripts/telemetry-summary.py <file.jsonl|dir> [...]

Reports, per place: visits, deaths, death rate and time spent (median and 90th percentile); then the economy: gained,
spent and the lowest balance seen, per item; then how runs ended. Copied into a game's scripts/ by the kickstart.
"""
import collections
import json
import pathlib
import statistics
import sys

paths = []
for arg in sys.argv[1:] or ["."]:
    p = pathlib.Path(arg)
    paths += sorted(p.glob("*.jsonl")) if p.is_dir() else [p]

events = []
for path in paths:
    for number, line in enumerate(path.read_text().splitlines(), 1):
        if line.strip():
            try:
                events.append(json.loads(line))
            except ValueError:
                sys.exit(f"{path}:{number}: not JSON")
if not events:
    sys.exit("telemetry-summary: no events found")


def pct(values, q):
    values = sorted(values)
    return values[min(len(values) - 1, int(q * len(values)))]


runs = {e.get("run") for e in events}
entered, left = {}, collections.defaultdict(list)
visits, deaths = collections.Counter(), collections.Counter()
gained, spent, lowest = collections.Counter(), collections.Counter(), {}
results = collections.Counter()

for e in sorted(events, key=lambda e: (str(e.get("run")), e.get("t", 0))):
    kind, run, place = e.get("event"), e.get("run"), e.get("place")
    if kind == "place_enter":
        visits[place] += 1
        entered[run] = (place, e.get("t", 0))
    elif kind == "place_exit" and run in entered:
        left[entered[run][0]].append(e.get("t", 0) - entered[run][1])
        del entered[run]
    elif kind == "death":
        deaths[place] += 1
    elif kind in ("item_gain", "item_spend"):
        item, amount = e.get("item"), e.get("amount", 0)
        (gained if kind == "item_gain" else spent)[item] += amount
        if "balance" in e:
            lowest[item] = min(lowest.get(item, e["balance"]), e["balance"])
    elif kind == "run_end":
        results[e.get("result")] += 1

print(f"{len(events)} events, {len(runs)} runs\n")
print("place            visits  deaths  death%  time p50 / p90 (ms)")
for place in sorted(visits, key=str):
    times = left.get(place, [])
    spread = f"{int(statistics.median(times))} / {pct(times, 0.9)}" if times else "-"
    print(f"{str(place):<16} {visits[place]:>6}  {deaths[place]:>6}  {100 * deaths[place] / visits[place]:>5.0f}%  {spread}")
if gained or spent:
    print("\nitem             gained   spent  lowest balance")
    for item in sorted(set(gained) | set(spent), key=str):
        print(f"{str(item):<16} {gained[item]:>6}  {spent[item]:>6}  {lowest.get(item, '-')}")
if results:
    print("\nruns ended: " + ", ".join(f"{k}: {v}" for k, v in results.most_common()))
