# Quiz 3 — Specimen (Week 3) · Web Vulnerabilities & Malware Basics
**Ungraded self-check · 12 marks · ~12 minutes · CLO-2, CLO-3 · Answer key discussed in class; not posted.**

## Part A — Multiple choice (1 mark each)

**1.** An invoice page fetches `/invoice/1041` and shows another department's data when the number is changed. The correct fix is:
- A. Use UUIDs in the URL instead
- B. Enforce an object-level authorization check tying the invoice to the requesting user
- C. Disable the print view
- D. Add a CAPTCHA to the page

**2.** `subprocess.run("ping " + host, shell=True)` is dangerous chiefly because:
- A. Ping floods the network
- B. The shell interprets metacharacters inside `host`, enabling command injection
- C. Python cannot resolve DNS
- D. `shell=True` disables logging

**3.** A comments field renders user input inside an HTML attribute unencoded. The most appropriate fix:
- A. Block all quotation marks
- B. Context-aware output encoding (HTML-attribute encoding)
- C. A WAF rule blocking `<script>`
- D. Store comments in a separate database

**4.** A rendering service accepts a URL and fetches it. The highest-impact SSRF outcome is:
- A. A broken image renders
- B. Fetching the cloud metadata address and stealing instance credentials
- C. Slightly higher CPU use
- D. A timeout in the logs

**5.** Before executing an unknown sample, the correct first step is:
- A. Run it and watch the task manager
- B. Compute a hash and check it against threat-intelligence sources
- C. Forward it to a colleague to open
- D. Rename the extension and double-click

**6.** A snapshot/revert capability in the malware VM exists chiefly to:
- A. Make analysis faster
- B. Guarantee each sample meets a clean state and contamination never persists
- C. Save disk space
- D. Hide the VM from the sample

**7.** A sample creates a scheduled task and a Run key after first run. The ATT&CK tactic is:
- A. Defense Evasion
- B. Persistence (Boot or Logon Autostart Execution)
- C. Collection
- D. Exfiltration

**8.** A phishing email from "the CEO" demands an urgent wire and forbids phone verification. The strongest red flag:
- A. The logo is slightly blurry
- B. The request bypasses normal verification and applies urgency + authority
- C. It arrived in the morning
- D. The body is one line

## Part B — Short answer (4 marks)

**9.** An inventory search builds SQL by string concatenation. Give the primary fix (1), one defense-in-depth measure (1), and one detection control (1). Then one sentence: why is a WAF alone not sufficient? (1)

---
*Specimen items are contaminated for grading use once shown. Review answers against the in-class key.*
