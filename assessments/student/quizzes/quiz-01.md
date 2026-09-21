# Quiz 1 — Specimen (Week 1) · Security Foundations & Web Sessions
**Ungraded self-check · 9 marks · ~10 minutes · CLO-1, CLO-2 · Answer key discussed in class; not posted.**

## Part A — Multiple choice (1 mark each; one best answer)

**1.** During an audit, logs show someone *read* a folder of admitted-student records without authorization. Which CIA property was violated?
- A. Confidentiality
- B. Integrity
- C. Availability
- D. Non-repudiation

**2.** A university portal sends its session cookie without the `Secure` attribute. The main risk is:
- A. JavaScript can read the cookie
- B. The cookie may travel over plaintext HTTP and be intercepted
- C. The cookie expires too fast
- D. The cookie enables CSRF by itself

**3.** A test input `admin'--` typed into a login form returning an unusual empty result suggests:
- A. The server is offline
- B. Possible SQL injection via comment truncation
- C. A slow network
- D. Expired password

**4.** An attacker captures a legitimate request token and replays it later; the server accepts it. In STRIDE this is best classified as:
- A. Repudiation
- B. Spoofing
- C. Tampering
- D. Elevation of privilege

## Part B — Short answer (5 marks)

**5.** Your team runs a course-registration web app. For **each** of the four changes below, state whether it *increases* or *decreases* attack surface (1 mark each), and give the reason in one sentence (1 mark for any two reasons):
- (a) Enabling a public debug endpoint (`/debug?show=env`)
- (b) Removing a legacy `/export` API that nobody uses
- (c) Adding a second login method (SMS OTP) alongside email login
- (d) Binding the admin panel to `127.0.0.1` so only localhost reaches it

---
*Specimen items are drawn from the instructor question bank and are contaminated for grading use once shown. Review your answers against the in-class key.*
