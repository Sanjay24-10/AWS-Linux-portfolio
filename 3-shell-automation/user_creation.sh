#!/bin/bash
# Script to create users from a file (users.txt)

if [ ! -f users.txt ]; then
  echo "Error: users.txt file not found!"
  exit 1
fi

while read user; do
  sudo useradd "$user"
  echo "$user:Default@123" | sudo chpasswd
  echo "User $user created."
done < users.txt
