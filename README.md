
# Lost & Found System

## 1. Project Description
The Lost & Found System is a web-based application designed to bridge the gap between people who have lost their belongings and people who have found them. In colleges, public places, and offices, losing valuable items like ID cards, books, wallets, keys, and electronic devices is very common. 

This system provides a centralized digital platform where users can report lost items and found items with full details. Instead of searching manually, users can simply post an item, search for it, and claim it online. The system makes the recovery process fast, secure, and organized.

The main goal of this project is to reduce the loss of valuable items and build a helpful community where people can help each other return lost belongings to their rightful owners.

## 2. Objective of the Project
- To provide an easy platform to report lost and found items.
- To reduce the time taken to find lost items.
- To maintain a secure record of all claims.
- To prevent false claims through verification and claim history.
- To create a user-friendly interface for all users.

## 3. Technologies Used
*1. Python:Main programming language used for backend logic.

*2. Flask:A lightweight Python web framework used to create the web server, handle routing, user sessions, and connect to the database.

*3. SQLite: A simple and lightweight database used to store all user data, lost items, found items, and claim history. It doesn't need a separate server setup.

*4. HTML:Used to create the structure and content of all web pages like Login, Register, Dashboard, Post Item forms.

*5. CSS: Used to design and style the website to make it attractive, responsive, and user-friendly.

## 4. Detailed Features Explanation

a) User Registration:* A new user can create an account by providing their name, email, and password. The data is securely stored in the database.

b) User Login:* A registered user can log in to the system to access all features. The system maintains a secure session for each logged-in user.

c) Post Lost Item:* If a user has lost something, they can post it with details like Item Name, Category, Description, Lost Location, Lost Date, and an Image of the item.

d) Post Found Item:* If a user finds an item belonging to someone else, they can post it as a found item with where and when they found it, so the original owner can find it.

e) Search Items:* Users can search for items using keywords, category, or location. This makes it easy to filter and find the exact item quickly.

f) Claim Item:* If a user sees their lost item in the found items list, they can request to claim it. The system will ask for proof or details to verify ownership.

*g) Claim History:* Every claim made by a user is recorded. The user and admin can see the history of claimed items, whether the claim is pending, approved, or rejected. This prevents fraud and keeps a proper record.

## 5. How It Works - System Workflow
1.  User Registers and Logs In.
2.  User posts either a Lost Item or a Found Item from their dashboard.
3.  All posted items are visible to all other users on the homepage.
4.  A user searches for their lost item in the Found Items section.
5.  User clicks on "Claim" and provides valid proof.
6.  The person who posted the item verifies the claim and contacts the owner.
7.  The transaction is saved in the Claim History.

## 6. Future Enhancements
- Add image matching using AI to automatically match lost and found items.
- Add email notification when a matching item is found.
- Add an admin panel to manage users and false claims.
- Add chat functionality between finder and owner.
- Add location tracking with Google Maps integration.

## 7. How to Run Project

1.  Install Python from http://python.org
2.  Install required modules:
    pip install flask
3.  Download or Clone this project folder.
4.  Run the application:
    py app.py
5.  Open your browser and go to:
    http://127.0.0.1:5000

## Screenshot
<img width="1360" height="575" alt="Register page" src="https://github.com/user-attachments/assets/5cf97efe-3e58-455e-a9e7-e1ed02b50736" />
<img width="1361" height="571" alt="Post item page" src="https://github.com/user-attachments/assets/37671ae0-32ee-44ac-83a6-d65ca07f16e7" />
<img width="1360" height="620" alt="Claim History" src="https://github.com/user-attachments/assets/7cda7a17-2a29-481b-a201-bcc21bd2c281" />
<img width="1364" height="580" alt="dashboard_page" src="https://github.com/user-attachments/assets/ff82f226-8952-4287-aa13-7c8204a652de" />

