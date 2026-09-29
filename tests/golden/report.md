# Cost & Waste Report

**Sessions:** 2
**Total tokens:** 7,370
**Total cost:** $0.0271
**Cache hit ratio:** 0.0%

## Per-tool spend
| Tool | Calls | Output | Carried | Cost |
|----|-----|------|-------|-------|
| Read | 2 | 5,101 | 10,102 | $0.0183 |
| Bash | 2 | 200 | 0 | $0.0006 |

## Repeated re-reads (top 10)
| Path | Reads | Wasted Reads | Wasted Tokens |
|--------|-----|------------|-------------|
| src/a.py | 2 | 1 | 100 |

## Oversized outputs (top 10)
| Tool | Command | Tokens |
|----|--------|------|
| Read | src/a.py | 5,001 |

## Cache misses (top 10)
| Turn | Tokens | Gap (s) | Extra Cost |
|----|------|-------|----------|
| 2 | 6,000 | 1140.0 | $0.0162 |

## Suggestions (top 10)
- **[cache_miss]** Batch work to stay within cache TTL (~6,000 tok, ~$0.0162)
- **[oversized_output]** Use Read with offset/limit for src/a.py (~4,000 tok, ~$0.0040)
- **[repeated_reread]** Note file src/a.py in CLAUDE.md to avoid re-reads (~100 tok, ~$0.0001)
