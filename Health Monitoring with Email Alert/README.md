# Smart System Health Monitor & Auto-Healer

This project monitors the system's health in real time (CPU & Memory usage) and sends email alerts if thresholds are exceeded.

## 📌 Features

- Real-time CPU and memory monitoring
- Automatic logging to `system_health.log`
- Email alerts using Gmail SMTP
- Simple simulation of high CPU usage

## 🚀 How to Run

1. Install dependencies:
   ```bash
   pip install psutil
   ```

2. Edit your email & password in `health_monitor.py`.

3. Run the script:
   ```bash
   python3 health_monitor.py
   ```

4. Simulate high CPU:
   ```bash
   python3 tests/simulate_high_cpu.py
   ```

## 🖼 Sample Screenshots

![CPU Alert](images/cpu_alert.png)
![Email Received](images/email_received.png)

## 📂 Folder Structure

```
system-health-monitor/
├── health_monitor.py
├── README.md
├── requirements.txt
├── logs/
│   └── system_health.log
├── images/
│   └── (Add screenshots here)
└── tests/
    └── simulate_high_cpu.py
```
