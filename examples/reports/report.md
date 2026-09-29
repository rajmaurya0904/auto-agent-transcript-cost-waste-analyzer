# Cost & Waste Report

**Sessions:** 2
**Total tokens:** 22,790
**Total cost:** $0.1222
**Cache hit ratio:** 65.7%

## Per-tool spend
| Tool | Calls | Output | Carried | Cost |
|----|-----|------|-------|-------|
| Bash | 2 | 10,898 | 43,592 | $0.0516 |
| Read | 6 | 866 | 2,612 | $0.0058 |
| Edit | 2 | 20 | 40 | $0.0002 |

## Repeated re-reads (top 10)
| Path | Reads | Wasted Reads | Wasted Tokens |
|-------------------------|-----|------------|-------------|
| payment_service.go | 3 | 2 | 243 |
| src/auth/login_handler.py | 3 | 1 | 175 |

## Oversized outputs (top 10)
| Tool | Command | Tokens |
|----|------------------------------------------|------|
| Bash | cat /var/log/demo-app/access.log | 5,673 |
| Bash | bash -lc go test ./... -run TestPayment -v | 5,225 |

## Cache misses (top 10)
| Turn | Tokens | Gap (s) | Extra Cost |
|----|------|-------|----------|
| 4 | 4,200 | 9.0 | $0.0567 |

## Suggestions (top 10)
- **[cache_miss]** Batch work to stay within cache TTL (~4,200 tok, ~$0.0567)
- **[oversized_output]** Add head/tail or grep filter to cat /var/log/demo-app/access.log (~4,538 tok, ~$0.0045)
- **[oversized_output]** Add head/tail or grep filter to bash -lc go test ./... -run TestPayment -v (~4,180 tok, ~$0.0042)
- **[repeated_reread]** Note file payment_service.go in CLAUDE.md to avoid re-reads (~243 tok, ~$0.0002)
- **[repeated_reread]** Note file src/auth/login_handler.py in CLAUDE.md to avoid re-reads (~175 tok, ~$0.0002)
