# Incident: High API Latency

**Date:** 2025-12-31  
**Severity:** High  

## Summary
API response times exceeded 2s for more than 10 minutes affecting multiple users.

## Impact
- ~20% of requests failed SLAs
- Several clients reported slow response times

## Timeline
| Time | Event |
|------|-------|
| 16:00 | Alerts triggered by Prometheus SLO rule |
| 16:05 | DevOps team acknowledged incident |
| 16:10 | Autoscaling increased replicas |
| 16:15 | Latency returned to normal |

## Root Cause
Insufficient pod replicas during traffic spike.

## Resolution
- HPA configuration updated
- Considered pre-warming pods for peak hours

## Lessons Learned
- Need more proactive alerting on upcoming traffic spikes
- Document runbooks for autoscaling checks
