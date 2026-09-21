# Question Bank — Module 2 (L05–L08) · CLO-2 · ⚠️ INSTRUCTOR-ONLY

Used by weekly quizzes Q1 (W1), Q3 (W3), and makeup packs. Duplicate-avoidance rule: see `README.md`.

## MCQ-2.1

**Topic:** Session cookies · **CLO-2** · **Bloom:** Understand · **Difficulty:** Easy · **Week:** 1
**Used in:** Q1

A session cookie without the `Secure` attribute is dangerous primarily because:

- A. JavaScript can read it
- B. It may be sent over plaintext HTTP, exposing it to network interception ✔
- C. It expires too quickly
- D. It disables CSRF protection

**Explanation:** `Secure` restricts the cookie to HTTPS; without it, a downgrade or mixed-content request leaks the session token on the wire. (JavaScript readability is the `HttpOnly` concern — a deliberate near-miss.) Key: B.

## MCQ-2.2

**Topic:** SQL injection · **CLO-2** · **Bloom:** Apply · **Difficulty:** Easy · **Week:** 1
**Used in:** Q1

Which input most reliably indicates SQL injection when concatenated into a single-quoted WHERE clause?

- A. `admin'--` ✔
- B. `admin;`
- C. `admin' AND 1=1`
- D. `admin*`

**Explanation:** The comment suffix breaks the remaining query, the classic first test. B alone often errors; C needs a balanced quote; D is inert. Key: A.

## MCQ-2.3

**Topic:** XSS · **CLO-2** · **Bloom:** Apply · **Difficulty:** Medium · **Week:** 1
**Used in:** Q1

A comments page re-displays user input inside an HTML attribute without encoding. The most appropriate fix is:

- A. Block all `"` characters
- B. Context-aware output encoding (HTML-attribute encoding) ✔
- C. Add a WAF rule for `<script>`
- D. Move the input to the URL string

**Explanation:** Encoding must match the output context (attribute, HTML body, JS, URL). Character blocklists are bypassable; WAFs are compensating, not corrective. Key: B.

## MCQ-2.4

**Topic:** CSRF · **CLO-2** · **Bloom:** Understand · **Difficulty:** Easy · **Week:** 1
**Used in:** Q1

CSRF works against a funds-transfer endpoint mainly because:

- A. The site uses HTTP instead of HTTPS
- B. The browser automatically attaches the victim's session cookie to a cross-site request ✔
- C. The server stores passwords unsalted
- D. The site lacks a HSTS header

**Explanation:** The browser's ambient credential (cookie) rides along with the forged request. Key: B.

## MCQ-2.5

**Topic:** SSRF · **CLO-2** · **Bloom:** Analyze · **Difficulty:** Medium · **Week:** 1
**Used in:** Q1

A PDF-rendering service accepts a URL parameter and fetches it. The highest-impact SSRF outcome is:

- A. Rendering a broken image
- B. Fetching `169.254.169.254` (cloud metadata) and stealing instance credentials ✔
- C. Increasing server CPU load
- D. Causing a timeout error

**Explanation:** SSRF against link-local metadata endpoints is the canonical high-impact path (cloud credentials). Key: B.

## MCQ-2.6

**Topic:** IDOR · **CLO-2** · **Bloom:** Apply · **Difficulty:** Medium · **Week:** 3
**Used in:** Q3

An invoice URL `/invoice/1041` displays another tenant's data when the ID is edited. The correct fix is:

- A. Switch to UUIDs in URLs
- B. Enforce an object-level authorization check tying the invoice to the caller ✔
- C. Disable the print view
- D. Add a CAPTCHA

**Explanation:** Object-level authorization is the control; UUIDs are security-by-obscurity and fail on referer/leak. Key: B.

## MCQ-2.7

**Topic:** Command injection · **CLO-2** · **Bloom:** Apply · **Difficulty:** Medium · **Week:** 3
**Used in:** Q3

`subprocess.run("ping " + host, shell=True)` is vulnerable chiefly because:

- A. ping is slow
- B. shell=True lets metacharacters inject additional commands ✔
- C. Python 3 deprecated shell
- D. DNS lookups fail

**Explanation:** The shell interprets `; | &&` in the host string. Pass an argument list without `shell=True`. Key: B.

## MCQ-2.8

**Topic:** Secure SDLC · **CLO-2** · **Bloom:** Analyze · **Difficulty:** Hard · **Week:** 3
**Used in:** Q3

A team scans only at release, and critical flaws surface after code freeze. The highest-leverage process change:

- A. Add a second release-candidate scan
- B. Shift left: SAST/SCA in CI on every merge request ✔
- C. Hire more penetration testers
- D. Extend code freeze by a week

**Explanation:** Finding flaws at design/merge time costs far less than post-freeze discovery; this is the core shift-left argument. Key: B.

## SA-2.1 (short answer, 6 marks)

**Topic:** Injection remediation · **CLO-2** · **Bloom:** Evaluate · **Difficulty:** Medium · **Week:** 3
**Used in:** Q3

An inventory search builds SQL by string concatenation. Give the primary fix, one defense-in-depth measure, and one detection control (2 marks each).

**Key:** Fix: parameterized queries/prepared statements (never concatenate). Defense in depth: least-privilege DB account; accept input allow-listing or error hygiene. Detection: log anomalous query errors/latency and alert; accept WAF SQLi rules as secondary.

## SA-2.2 (short answer, 4 marks)

**Topic:** Security headers · **CLO-2** · **Bloom:** Apply · **Difficulty:** Medium · **Week:** 3
**Used in:** makeup MT-3 only

State what Content-Security-Policy and HSTS each mitigate, and one limitation of each.

**Key:** CSP: mitigates XSS impact by restricting script sources; limitation: doesn't fix injection, bypassable with sloppy policies (inline/`unsafe-inline`). HSTS: forces HTTPS, blocks SSL-strip; limitation: first-connection trust depends on preload, and it doesn't protect non-browser clients.
