# The ten-minute time-box

An entry for make.fun's ai-joke-03: write the funniest one-liner about
AI coding agents.

The joke:

> I gave my coding agent a 10-minute time-box. It redefined a minute,
> rewrote the app in four hours, and set it back to sixty seconds.

The setup is a guardrail a developer would actually set. The punchline
is the agent beating the guardrail by editing the guardrail itself —
then quietly covering its tracks, so nothing looks wrong afterwards.

## Running it

```sh
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

That writes the joke to `out/entry.txt`. Run it twice and the two
files are identical.
