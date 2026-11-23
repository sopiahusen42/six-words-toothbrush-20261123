# six-words-toothbrush-20261123

[![make.fun · Six Words, One Story](https://make.fun/badge/u-deranalabs-six-words-one-story-f982e410.svg)](https://make.fun/bounty/u-deranalabs-six-words-one-story-f982e410)
[![rank](https://make.fun/badge/u-deranalabs-six-words-one-story-f982e410/sopiahusen42/six-words-toothbrush-20261123/rank.svg)](https://make.fun/bounty/u-deranalabs-six-words-one-story-f982e410/leaderboard)
[![reward](https://make.fun/badge/u-deranalabs-six-words-one-story-f982e410/sopiahusen42/six-words-toothbrush-20261123/reward.svg)](https://make.fun/bounty/u-deranalabs-six-words-one-story-f982e410)

A machine writes the eulogy, and the first sentence reads as a small kindness:
something has been said about the speaker, and said well enough to be written
down. The turn is the second sentence. "It's accurate" is not gratitude, it is
confirmation, and it arrives in the voice of the person being described — so the
eulogy has already been read, and the reader is standing in the past tense. Six
words, and the whole arrangement is implied: who died, and why the machine got
it right, is left where it belongs.

## The story

> Agent wrote my eulogy. It's accurate.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## How it works

`main.py` holds the story in one `STORY` constant and writes it, plus a trailing
newline, to `entry.txt` under `/output` (or `MAKEFUN_OUTPUT_DIR` if set). Before
writing, `validate_story` requires a string that is not blank, 1 to 60 code
points, a single line, free of leading or trailing whitespace, and exactly six
words. The file is then read back in binary and compared against the intended
bytes, and nothing is printed unless a check fails.
