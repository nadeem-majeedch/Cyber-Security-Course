#!/usr/bin/env python3
"""Lab 15 starter - cryptographic operations and integrity checks.

Tested with: Python 3.14 (stdlib only) and OpenSSL 3.5 on the instructor
workstation. On the course VM, install the cryptography package first:

    python -m pip install cryptography

Parts of this script marked [UNTESTED] depend on that package; the stdlib
parts (hashlib/hmac) were run and verified before this file was committed.
"""
import argparse
import hashlib
import hmac
import sys


def sha256_file(path: str) -> str:
    """Part A: file digest (stdlib - TESTED on Python 3.14)."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def hmac_sha256(key: bytes, data: bytes) -> str:
    """Part B: keyed integrity (stdlib hmac - TESTED via openssl cross-check)."""
    return hmac.new(key, data, hashlib.sha256).hexdigest()


def kdf_password(password: str, salt: bytes) -> str:
    """[UNTESTED - requires hashlib.pbkdf2_hmac; API is stable stdlib, but the
    lab timing numbers must be collected on the course VM image.]"""
    return hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 600_000).hex()


def aead_encrypt(key: bytes, nonce: bytes, plaintext: bytes) -> bytes:
    """[UNTESTED - requires the cryptography package on the course VM.
    NOTE: `openssl enc` does NOT support AEAD ciphers (verified: OpenSSL 3.5
    prints 'enc: AEAD ciphers not supported'), which is exactly why this
    helper uses the Python library instead of shelling out to openssl.]"""
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM  # noqa

    return AESGCM(key).encrypt(nonce, plaintext, None)


def aead_decrypt(key: bytes, nonce: bytes, ciphertext: bytes) -> bytes:
    """[UNTESTED - cryptography package; tampered inputs must raise]."""
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM  # noqa

    return AESGCM(key).decrypt(nonce, ciphertext, None)


def main() -> int:
    p = argparse.ArgumentParser(description="Lab 15 helper")
    p.add_argument("command", choices=["sha256", "hmac", "kdf", "aead"])
    p.add_argument("path", help="input file")
    p.add_argument("--key", default="course-lab-key")
    args = p.parse_args()

    if args.command == "sha256":
        print(sha256_file(args.path))
    elif args.command == "hmac":
        with open(args.path, "rb") as f:
            print(hmac_sha256(args.key.encode(), f.read()))
    elif args.command == "kdf":
        print("requires course VM salt handout; see worksheet Part B3")
    else:
        print("aead: run on course VM after installing cryptography")
    return 0


if __name__ == "__main__":
    sys.exit(main())
