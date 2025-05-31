# Roamio – Social Travel Matchmaking Platform
# Project Overview
Roamio is a web-based travel matchmaking platform that connects solo travelers with like-minded people through curated trips, group experiences, and interactive features. It transforms solo travel into shared adventures.

# Tagline: "Strangers today, Roam-Mates tomorrow."
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

# Table Structure 
roamio/
├── app.py
├── requirements.txt
├── roamio.sql              
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── signup.html
│   ├── dashboard.html
│   ├── profile.html
│   ├── trip.html
│   ├── trip_detail.html
│   ├── review.html
│   └── memories.html
├── nginx/
│   └── roamio.conf
├── venv/

# Work flow for deployment of ro-mio 

1. Planning & Requirements (Define core features)
User auth (signup/login)
Trip creation & browsing
Travel buddy matchmaking
Chat and reviews
Choose tech stack:
Frontend: HTML, CSS (Bootstrap/Tailwind)
Backend: Python Flask
Database: MySQL 
Hosting: AWS EC2

2. User Authentication 
Use Flask-Login or Flask-Security Pages:
/signup – Register user
/login – Login form
/logout – Logout function

3. Profile Management   (After login)
Let users enter travel interests, location, etc.
Store in UserProfile table
Page: /profile

4. Trip System Pages:
/create-trip – Form to create a new trip
/trips – Show list of all trips
/trip/<id> – Trip details and join option
Backend handles:
Trip model
Joining logic
Filtering trips by date, location, theme

5. Matching Algorithm
On profile submission or trip join:
Check user interests vs others
Suggest compatible “Roam-Mates”

6. Chat System (Optional for MVP)
Use Flask-SocketIO or integrate third-party chat (e.g., CometChat)
Group chat within trip pages
Private DMs later

7. Review & Memories After trip:
/trip/<id>/review – Leave reviews
/memories – View trip photos, stories

8. Admin Panel (Optional)View/manage:
Users
Trips
Reports or abuse flags

9. Deployment on AWS EC2
1. Launch Ubuntu EC2 instance
2. Install Python, pip, virtualenv
3. Upload your Flask project
4. Install MySQL + dependencies
5. Use Gunicorn + Nginx to serve app


Developed by: ishwari ruikar.
Contact: hello@roamio.com
Year: 2025

