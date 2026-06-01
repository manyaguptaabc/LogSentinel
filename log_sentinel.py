import re
import mysql.connector
from datetime import datetime
from collections import defaultdict

# ─── CONFIG ───────────────────────────────────────────────
LOG_FILE = "sample_system.log"
ALERT_THRESHOLD = 3  # Alert if same error appears 3+ times

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "your_password",
    "database": "logsentinel_db"
}

# ─── PATTERNS ─────────────────────────────────────────────
PATTERNS = {
    "ERROR":          re.compile(r'\b(error|failed|failure|critical)\b', re.IGNORECASE),
    "WARNING":        re.compile(r'\b(warning|warn)\b', re.IGNORECASE),
    "AUTH_ISSUE":     re.compile(r'\b(authentication|unauthorized|invalid password|access denied)\b', re.IGNORECASE),
    "SERVICE_FAILURE":re.compile(r'\b(service.*stopped|daemon.*failed|unit.*failed)\b', re.IGNORECASE),
    "INFO":           re.compile(r'\b(info|started|success|connected)\b', re.IGNORECASE),
}

# ─── PARSE LOGS ───────────────────────────────────────────
def parse_log(filepath):
    entries = []
    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            category = "OTHER"
            for cat, pattern in PATTERNS.items():
                if pattern.search(line):
                    category = cat
                    break
            entries.append({
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "raw": line,
                "category": category
            })
    return entries

# ─── GENERATE SUMMARY ─────────────────────────────────────
def generate_summary(entries):
    counts = defaultdict(int)
    for e in entries:
        counts[e["category"]] += 1

    print("\n" + "="*55)
    print("       LogSentinel — System Log Analysis Report")
    print("="*55)
    print(f"  Total log entries parsed : {len(entries)}")
    print("-"*55)
    for cat, count in sorted(counts.items(), key=lambda x: -x[1]):
        print(f"  {cat:<20} : {count} entries")
    print("="*55)
    return counts

# ─── ALERT ENGINE ─────────────────────────────────────────
def check_alerts(counts):
    print("\n  [ALERT ENGINE]")
    alerts_fired = 0
    for cat in ["ERROR", "AUTH_ISSUE", "SERVICE_FAILURE"]:
        if counts.get(cat, 0) >= ALERT_THRESHOLD:
            print(f"  ⚠️  ALERT: '{cat}' occurred {counts[cat]} times — investigate immediately!")
            alerts_fired += 1
    if alerts_fired == 0:
        print("  ✅ No critical alerts. System looks healthy.")
    print()

# ─── STORE TO MYSQL ───────────────────────────────────────
def store_to_db(entries):
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS log_metadata (
                id INT AUTO_INCREMENT PRIMARY KEY,
                timestamp VARCHAR(30),
                category VARCHAR(30),
                raw_log TEXT
            )
        """)
        for e in entries:
            cursor.execute(
                "INSERT INTO log_metadata (timestamp, category, raw_log) VALUES (%s, %s, %s)",
                (e["timestamp"], e["category"], e["raw"])
            )
        conn.commit()
        print(f"  ✅ {len(entries)} entries stored to MySQL successfully.")
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print(f"  ⚠️  MySQL not connected (running in offline mode): {err}")
        print("  ℹ️  Log analysis completed without DB storage.\n")

# ─── MAIN ─────────────────────────────────────────────────
if __name__ == "__main__":
    print("\n  Starting LogSentinel...\n")
    entries = parse_log(LOG_FILE)
    counts  = generate_summary(entries)
    check_alerts(counts)
    store_to_db(entries)
