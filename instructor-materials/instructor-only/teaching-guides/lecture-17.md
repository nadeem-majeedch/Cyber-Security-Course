# Teaching Guide — Lecture 17 (Symmetric Crypto & Modes)
**Instructor-only.**

## Timing Plan (120 min)

| Time | Segment | Delivery notes |
|---|---|---|
| 00–10 | Hook: ECB penguin | Let the picture teach; students name the failure. |
| 10–30 | Modes tour | Diagram walk; one failure story per mode. |
| 30–48 | Failure gallery | ECB avatar, CBC bit-flip cookie, GCM nonce reuse. |
| 48–60 | Break | — |
| 60–105 | Lab 15 (three parts) | Penguin → bit-flip → GCM tag. |
| 105–115 | Mode decision table | Six scenarios; students commit. |
| 115–120 | Exit ticket + preview | Tease L18: "who vouches for keys?" |

## Board/Projector Activities

- **Projector:** the penguin image pair (plaintext/ECB-ciphertext); the lab's bit-flip before/after.
- **Board:** the four-mode diagram (ECB/CBC/CTR/GCM) drawn live with failure annotations.

## Speaker Notes (key beats)

1. One sentence carries the lecture: *confidentiality without integrity is incomplete* — everything points at AEAD.
2. Mode failures are *usage* failures; AES itself is not the suspect. Keep primitives-vs-usage separate.
3. CBC bit-flipping: work the math on the board once (flip bit i of Cₙ → flips Pₙ₊₁-ish and garbles Pₙ); the lab makes it tangible.
4. Nonce discipline: "never reuse under the same key" is a *design constraint*, not a reminder — randomness or counters must be structured so reuse is impossible.
5. IV is not secret; unpredictable ≠ confidential — the confusion breaks designs.

## Expected Student Difficulties

- Students confuse IV with key. Fix: the two-slot table (what is secret / what must vary).
- Bit-flipping math anxiety. Fix: the lab's cookie (`role=user`→`role=admin`) is byte-level, not mathematical; the "garbled neighbor block" toleration is the trick to spot.
- GCM nonce-reuse severity feels abstract. Fix: name the consequence class (tag forgery + keystream reuse) without working the forbidden-attack math.

## Teaching Tips

- Pre-test the lab scripts on the lab image; OpenSSL/pyca version drift is the usual breakage.
- The decision-table activity needs commitment, not hedging — six rows, one mode each, one "why."
- Keep the penguin visual accessible: describe the effect in words ("the penguin's silhouette survives encryption") for anyone who can't see it.

## Answer Keys **[KEY]**

- Decision table (model): session tokens → GCM; full-disk → XTS (mention-only, awareness); streaming telemetry → GCM/CTR-with-unique-nonce; legacy interop → CBC+HMAC (encrypt-then-MAC), flagged as migration debt; key wrapping → AES-KW/GCM; deterministic search → out of scope, deterministic schemes only under expert review.
- Exit ticket: 1 ECB; 2 equal plaintext blocks encrypt differently only with a fresh random IV; 3 authenticated encryption (integrity tag).

## Lab Delivery (Lab 15)

- Minimum viable outcome: penguin done + one of (bit-flip | GCM-verify) completed; stretch = all three.
- Expected failure points: padding errors mid-bit-flip are *expected* — teach reading them as evidence; image library install time (pre-install in the image).

## Discussion Facilitation

Q2 (nonce accidents) invites war stories — steer to the structural fix (counter management, random nonces with collision-aware length). Q3 (deterministic need) is the honest teaser: note that the general problem is open-ish and research-level; curiosity over conclusions.

## Accessibility

- The penguin: full text description in the notes ("the encrypted image remains recognizable, proving pattern leakage") plus the visual.
- Crypto labs are terminal-heavy: pair the screen work with the written steps; outputs provided as text files for screen readers.
