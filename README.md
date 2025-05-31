# Roamio – Social Travel Matchmaking Platform
# Project Overview
Roamio is a web-based travel matchmaking platform that connects solo travelers with like-minded people through curated trips, group experiences, and interactive features. It transforms solo travel into shared adventures.
Tagline: "Strangers today, Roam-Mates tomorrow."
________________________________________
# Key Features
Feature	Description
User Authentication	Sign up and log in via email
Travel Profiles	Define location, interests, preferences
Trip Creation	Organize trips with themes, locations, and dates
Trip Browsing	View and join curated trips
Matching Algorithm	Suggests compatible Roam-Mates based on profile data
Group Chat (MVP)	In-trip chat and bonding tools
Review System	Post-trip reviews and feedback
Memory Sharing	Upload and view trip photos and captions
________________________________________
# Tech Stack
Layer	Technology
Frontend :	HTML, CSS (Tailwind)
Backend	: Python Flask
Database : MySQL,
Hosting	: AWS EC2 
Others :	Nginx, Gunicorn

# Application Flow Diagram
+------------+       +----------------+       +------------------+
|   Signup   | ----> |   Create/View  | <---- |   Login/Profile  |
|   /signup  |       |   Trips        |       |   /profile       |
+------------+       |   /trips       |       +------------------+
                      |   /create-trip|
                      +----------------+
                             |
                             v
                    +--------------------+
                    | View Trip Details  |
                    | Join & Chat        |
                    | /trip/<id>         |
                    +--------------------+
                             |
                             v
                    +-------------------+
                    | Leave Review      |
                    | Upload Memory     |
                    | /review /memories |
                    +-------------------+


# Deployment Instructions
1.	Launch EC2 : Amazon Linux : open ports 22/80/443
2.	SSH & Setup:
ssh -i roamio-key.pem ec2-user@<public-ip>
sudo apt update && sudo apt install python3-pip python3-venv nginx mysql-server
3.	Clone Project & Install:
git clone <repo-url>
cd roamio
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
4.	Configure MySQL
CREATE DATABASE roamio_db;
CREATE USER 'roamio_user'@'localhost' IDENTIFIED BY 'yourpassword';
GRANT ALL ON roamio_db.* TO 'roamio_user'@'localhost';
5.	Run Gunicorn:
gunicorn -w 4 -b 127.0.0.1:8000 app:app
6.	Setup Nginx:
sudo nano /etc/nginx/sites-available/roamio
7.  (Add proxy config)
sudo ln -s /etc/nginx/sites-available/roamio /etc/nginx/sites-enabled/
sudo systemctl restart nginx






















Developed by: ishwari ruikar.
Contact: hello@roamio.com
Year: 2025

