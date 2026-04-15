# MemPalace Memory System

## Active Memory
- **Current Session**: All conversations in this session are automatically saved
- **Global Memory**: All sessions across all projects stored in ~/.mempalace/

## How It Works
- Conversations stored verbatim in ~/.mempalace/palace/
- Semantic search retrieves past context when needed
- Use `mempalace search <query>` to find past sessions

## MCP Servers for Fredun

### To Enable (Manual Setup Required)
Add to Claude Code config or create mcp_servers/ folder:

**SEO MCP** - Website auditing:
```
npx -y @apify/seo-mcp-server
```
URL: https://apify.com/nexgendata/seo-web-analysis-mcp-server

**Google Analytics MCP** - Traffic analysis:
```
npx -y @apify/google-analytics-mcp-server
```
URL: https://apify.com/constant_quadruped/google-analytics-mcp-server

**Technical SEO MCP** - PageSpeed, Core Web Vitals:
```
npx -y @apify/performance-seo-mcp-server
```
URL: https://apify.com/alizarin_refrigerator-owner/performance-seo-mcp-server

### Setup Steps
1. Get Apify account (apify.com)
2. Some MCPs are free, some require paid plan
3. Configure via Claude Code settings or project mcp_servers/

## Current Session
- Date: 2026-04-15
- Graphify: Completed on this project
- agentic-ai-apis: Cloned to ~/GitHub/agentic-ai-apis