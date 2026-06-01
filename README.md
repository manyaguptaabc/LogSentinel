# LogSentinel

A Python-based Linux log monitoring and alerting system that analyzes system logs, classifies events, generates alerts, and stores log metadata for troubleshooting.

## Features

* Parse Linux system log files
* Classify events into ERROR, WARNING, INFO, and AUTH_ISSUE categories
* Generate rule-based alerts for recurring issues
* Produce structured log summaries
* Store log metadata in MySQL
* Support offline execution when database connectivity is unavailable

## Technologies Used

* Python
* MySQL
* Git & GitHub

## Project Structure

```text
LogSentinel/
│
├── log_sentinel.py
├── requirements.txt
├── sample_system.log
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python log_sentinel.py
```

## Sample Output

```text
Starting LogSentinel...

Total log entries parsed : 20

ERROR      : 10 entries
INFO       : 4 entries
AUTH_ISSUE : 3 entries
WARNING    : 3 entries

ALERT: 'ERROR' occurred 10 times
ALERT: 'AUTH_ISSUE' occurred 3 times
```

## Learning Outcomes

* Linux log analysis
* Python automation
* Rule-based alerting
* Database integration
* Troubleshooting workflows
* System monitoring fundamentals

## Future Improvements

* Email notifications
* Dashboard for log visualization
* Real-time log monitoring
* Docker deployment
* Advanced alert rules
