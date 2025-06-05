# Automation Utilities with Shell Scripting on AWS Linux

This project includes a collection of simple and practical shell scripts created to automate routine system administration tasks on an AWS EC2 Linux instance. These scripts save time, reduce human error, and help in managing system tasks efficiently.

---

## 📌 Features

- ✅ Automatic user creation with password setting
- ✅ Directory and permission setup
- ✅ Simple backup script for important files/folders
- ✅ System update automation
- ✅ Log management utilities

---

## 🛠️ Technologies Used

- AWS EC2 (Amazon Linux)
- Bash / Shell Scripting
- Linux Command Line

---

## 📂 Project Structure

```
3-shell-automation/
├── user_creation.sh         # Creates users from a list
├── backup_script.sh         # Backs up important folders
├── system_update.sh         # Updates packages automatically
├── log_cleanup.sh           # Deletes old logs
```

---

## 🚀 How to Use

1. **Connect to your EC2 instance**:
```bash
ssh -i your-key.pem ec2-user@your-public-ip
```

2. **Make the script executable**:
```bash
chmod +x user_creation.sh
```

3. **Run the script**:
```bash
./user_creation.sh
```

Repeat the same for other scripts.

> 💡 Tip: You can schedule these scripts using `crontab` for regular automation.

---

## 🧪 Example: User Creation Script

### Sample `user_creation.sh`
```bash
#!/bin/bash
while read user; do
  sudo useradd "$user"
  echo "$user:Default@123" | sudo chpasswd
  echo "User $user created."
done < users.txt
```

`users.txt` file:
```
john
alice
bob
```

---

## 📧 Author

**Sanjay Kumar J**  
📧 sanjaykumar24tech@gmail.com  
📞 9677224830

---

## 📌 Notes

These scripts are tested on:
- **Amazon Linux 2023**
- **Ubuntu 20.04+**

Please run them with caution and always test in a staging environment first.
