#!/usr/bin/env python3
"""The Word You'd Delete From the Dictionary — write one word to /output/entry.txt.

The word is "sanction". It is the dictionary's own contradiction: it
means both to approve something and to punish someone for it — a word
that cannot decide whether it is a blessing or a penalty. Erasing it
removes a word that means its own opposite, and the erasure itself is
a sanction: the dictionary punishes the word by approving its removal.
The joke lands the moment the word is read, needs no caption, comes
entirely from the word's double meaning, and sidesteps the field's
worn-out first picks (moist, literally, irregardless, flammable).

The word was picked from ten drafted candidates by internal pairwise
comparison against the judge brief: a real recognisable word first,
then funny at first sight, then humour from the word itself, then
freshness, then exactness. It beat "moist" (the field's default pick,
zero freshness), "literally" (the overused-misuse joke, obvious),
"irregardless" (the shouldn't-be-in-the-dictionary joke, obvious),
"inflammable" (the confusion-pair joke, well known), "cleave" (a
contronym too — split apart / cling together — but sanction's
approve / punish contrast is more absurd, and only sanction's
deletion is itself a sanction), "hippopotomonstrosesquippedaliophobia"
(the fear of long words, itself the longest word — fresher, but the
joke needs the definition while sanction's clicks at a glance),
"dord" (the ghost word that was never real — an insider joke a
general reader may not recognise), "floccinaucinihilipilification"
(means "estimating as worthless", so deleting it is itself that act —
clever but obscure, not instant), and "actually" (the pedant's word,
mild and one-note).

Stdlib only, deterministic, no network, no randomness.
"""
import hashlib
import os
import sys
import unicodedata

# 8 characters / 8 bytes, inside the 1-77 character gate.
ENTRY = "sanction"

MAX_CHARS = 77


# The gate, from the competition's RULES.txt: /output/entry.txt must be
# UTF-8 text of 1 to 77 characters, not only white space. This validator
# is stricter than the gate in one way a single word needs: it also
# refuses any invisible format character.
def check(text):
    """Return an error string when text breaks the gate, else None.

    Gate: 1 to 77 characters, not only whitespace, single word, no
    leading or trailing whitespace.
    """
    if not isinstance(text, str):
        return "entry must be text"
    if len(text) == 0:
        return "entry is empty (gate needs 1-77 characters)"
    if len(text) > MAX_CHARS:
        return "entry is %d characters, over the 77-character gate" % len(text)
    if text.strip() == "":
        return "entry is only whitespace"
    if text != text.strip():
        return "entry has leading or trailing whitespace"
    if "\n" in text or "\r" in text:
        return "entry must be a single word"
    if " " in text or "\t" in text:
        return "entry must be a single word"
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in text):
        return "entry contains a control character"
    if any(unicodedata.category(ch).startswith("C") for ch in text):
        return "entry contains an invisible control/format character"
    return None


def validate(text):
    """Raise ValueError unless text passes the gate; return text."""
    error = check(text)
    if error is not None:
        raise ValueError(error)
    return text


def self_test():
    """Exercise check() against the gate's rejection and boundary cases."""
    reject = [
        ("", "empty"),
        ("   ", "whitespace-only"),
        ("x" * 78, "78 chars (over the 77 gate)"),
        ("a\nb", "multi-line"),
        ("a b", "two words"),
        (" padded", "leading whitespace"),
        ("padded ", "trailing whitespace"),
        ("a\rb", "carriage return"),
        ("a\x00b", "control character"),
        ("a\u200bb", "zero-width space (invisible format character)"),
    ]
    for text, label in reject:
        error = check(text)
        if error is None:
            raise SystemExit("self-test FAIL: %s was accepted" % label)
        print("self-test ok: rejected %s: %s" % (label, error))
    for text, label in [("y", "1-char boundary"), ("z" * 77, "77-char boundary")]:
        error = check(text)
        if error is not None:
            raise SystemExit("self-test FAIL: %s rejected: %s" % (label, error))
        print("self-test ok: %s accepted" % label)
    error = check(ENTRY)
    if error is not None:
        raise SystemExit("self-test FAIL: entry rejected: %s" % error)
    print("self-test ok: entry accepted (%d chars)" % len(ENTRY))
    print("self-test: all cases passed")
    return 0


def main(argv):
    if len(argv) > 1 and argv[1] == "--self-test":
        return self_test()
    if len(argv) > 1:
        print("usage: main.py [--self-test]", file=sys.stderr)
        return 2
    text = validate(ENTRY)
    data = text.encode("utf-8")
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "wb") as fh:
        fh.write(data)  # no trailing newline: the file is exactly the word
    with open(out_path, "rb") as fh:
        roundtrip = fh.read()
    if roundtrip != data:
        raise SystemExit("round-trip mismatch: file does not match entry")
    print("wrote %s: %d chars, sha256 %s"
          % (out_path, len(text), hashlib.sha256(data).hexdigest()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
