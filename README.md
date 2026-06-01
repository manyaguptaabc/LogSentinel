# LogSentinel — Linux Log Monitoring & Alerting System

A Python-based Linux log monitoring tool that parses, classifies, and alerts on system log entries to identify recurring operational issues.

## Features
- Parses Linux system log files (`/var/log/syslog`, custom logs)
- Classifies entries into: ERROR, WARNING, AUTH_ISSUE, SERVICE_FAILURE, INFO
- Generates categorized summary reports from 1,000+ log entries
- Rule-based alert engine for service failures, auth issues, and critical errors
- Stores log metadata in MySQL for historical analysis and troubleshooting

## Tech Stack
- Python 3.x
- MySQL (optional — runs in offline mode without it)
- Regex-based log parsing
- Rule-based alert logic

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/LogSentinel.git
cd LogSentinel
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. (Optional) Setup MySQL
```sql
CREATE DATABASE logsentinel_db;
```
Update `DB_CONFIG` in `log_sentinel.py` with your credentials.

### 4. Run
```bash
python log_sentinel.py
```

## Sample Output
```
=======================================================
       LogSentinel — System Log Analysis Report
=======================================================
  Total log entries parsed : 20
-------------------------------------------------------
  ERROR                : 4 entries
  AUTH_ISSUE           : 5 entries
  SERVICE_FAILURE      : 4 entries
  WARNING              : 3 entries
  INFO                 : 3 entries
=======================================================

  [ALERT ENGINE]
  ⚠️  ALERT: 'ERROR' occurred 4 times — investigate immediately!
  ⚠️  ALERT: 'AUTH_ISSUE' occurred 5 times — investigate immediately!
  ⚠️  ALERT: 'SERVICE_FAILURE' occurred 4 times — investigate immediately!
```

## Use Cases
- Linux server health monitoring
- Security audit log analysis
- Automated incident detection
- Historical fault trend analysis via MySQL

## Author
Manya Gupta — github.com/manyaguptaabc
