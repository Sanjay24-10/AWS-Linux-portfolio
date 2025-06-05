# Hosting a Static Website on AWS EC2 with Asset Storage in S3

## 📌 Project Overview

This project demonstrates how to host a static website using an EC2 instance on AWS, with supporting assets (CSS, JS, Images, Videos, Fonts) stored on the server itself — following a clean and scalable folder structure.

It uses a professional frontend design inspired by the Villa Agency template, customized and deployed on an Apache web server.

---

## 🛠️ Technologies Used

- Amazon EC2 (Amazon Linux 2)
- Apache HTTP Server
- HTML5 / CSS3 / JavaScript
- SCP (Secure Copy Protocol) for file transfer
- AWS S3 (optional for future asset storage)

---

## 📁 Folder Structure

```bash
/var/www/html/
├── index.html          # Main HTML file (homepage)
├── css/                # Stylesheets (Bootstrap, FontAwesome, Custom)
├── js/                 # JavaScript files
├── images/             # Image assets (banners, logos, etc.)
├── videos/             # Embedded video files
├── fonts/              # Web fonts

🚀 Deployment Steps

1. Launch an EC2 Instance
Amazon Linux 2
Allow inbound HTTP (port 80) in Security Group

2. Install Apache Web Server
sudo yum update -y
sudo yum install httpd -y
sudo systemctl start httpd
sudo systemctl enable httpd

3. Upload Website Files
Use scp from your local machine:
scp -i key.pem -r * ec2-user@your-ec2-ip:/home/ec2-user/
Then move the files to the Apache root directory:
sudo mv /home/ec2-user/* /var/www/html/

4. Verify Permissions
sudo chown -R apache:apache /var/www/html

5. Restart Apache
sudo systemctl restart httpd

6. Access the Website
Visit:
http://13.220.170.250

## 🖼️ Demo Screenshot

![Website Screenshot](images/screenshot-homepage.png)