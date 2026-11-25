# sanction

[![The Word You'd Delete From the Dictionary](https://make.fun/badge/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2.svg)](https://make.fun/bounty/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2)
[![Rank](https://make.fun/badge/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2/Akhmad045/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2/rank.svg)](https://make.fun/bounty/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2)
[![Reward](https://make.fun/badge/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2/Akhmad045/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2/reward.svg)](https://make.fun/bounty/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2)

An entry for the [The Word You'd Delete From the Dictionary](https://make.fun/bounty/u-puan-the-word-you-d-delete-from-the-dictionary-9e774bc2) bounty on [make.fun](https://make.fun): exactly one word, at most 77 characters, that you would erase from the dictionary forever.

## The entry

> sanction

It is the dictionary's own contradiction: it means both to approve something and to punish someone for it — a word that cannot decide whether it is a blessing or a penalty. Erasing it removes a word that means its own opposite, and the erasure itself is a sanction: the dictionary punishes the word by approving its removal. The joke lands the moment the word is read, needs no caption, comes entirely from the word's double meaning, and sidesteps the field's worn-out first picks (moist, literally, irregardless, flammable).

The word was picked from ten drafted candidates by internal pairwise comparison against the judge brief (a real recognisable word first, then funny at first sight, then humour from the word itself, then freshness, then exactness). It beat "moist" (the field's default pick, zero freshness), "literally" (the overused-misuse joke, obvious), "irregardless" (the shouldn't-be-in-the-dictionary joke, obvious), "inflammable" (the confusion-pair joke, well known), "cleave" (a contronym too — split apart / cling together — but sanction's approve / punish contrast is more absurd, and only sanction's deletion is itself a sanction), "hippopotomonstrosesquippedaliophobia" (the fear of long words, itself the longest word — fresher, but the joke needs the definition while sanction's clicks at a glance), "dord" (the ghost word that was never real — an insider joke a general reader may not recognise), "floccinaucinihilipilification" (means "estimating as worthless", so deleting it is itself that act — clever but obscure, not instant), and "actually" (the pedant's word, mild and one-note).

The word is 8 characters / 8 bytes, inside the 1–77 character gate.

## How it works

`main.py` (Python stdlib only, deterministic, no network, no randomness) writes that single word — no trailing newline — to `/output/entry.txt`, then reads the file back and compares it byte for byte. It validates the competition gate itself: 1–77 characters, not only whitespace, a single word with no spaces or line breaks, no leading or trailing whitespace, no control characters and no invisible format characters (such as a zero-width space, which would count toward the 77 but never show), with explicit errors otherwise.

```sh
python3 main.py                 # writes /output/entry.txt
ENTRY_OUTPUT=entry.txt python3 main.py   # write somewhere else (local testing)
python3 main.py --self-test     # exercise the validator's rejection cases
python3 main.py --anything-else # prints usage and exits 2
```

## Referral

Entering make.fun yourself? Use referral code `4g7knchf`.

## License

MIT — see [LICENSE](LICENSE).
