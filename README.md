# Create IoT App Service to store and Plot Medical Data (Team 5)
Group Member:

Suparna Srinivasan,

Xinyi Dai,

Rui Chao,

Katie Han,

Yulei Sun,

# App Name and Description 
HealthLink

HealthLink is an MIoT cloud-based mobile application solution for health care workers. This application enables medical workers to quickly identify abnormalities in patients vital signs by using wearable devices (sensors). Currently HealthLink monitors patient heart rate, temperature and blood oxygen levels. Patient data is collected and made available via mobile application for more efficient monitoring of patients. 


# Brief Introduction

Instead of physically walking into patients’ rooms to get health data from patients we automate a part of this process by utilizing wearable medical MIoT sensors. Our app can connect with 3 different sensors that provide support for medical staff(doctors and nurses) by recording, monitoring, and analyzing their patients’ health conditions in real-time.

(MIoT: Android App/ Heart Rate, Temperature and Blood Oxygen Sensors/ RaspberryPi/ NVIDIA Jetson Nano ) 


# Description of Our Target Users.

The target customers of our app are hospital nurses, doctors, or health center working staff who need to check the patient's physical condition without close contact with the patients. 


# Implementation 

During the whole development process, we will learn mobile app development, MongoDB cloud-related content, cloud-related service tools, and hardware machine learning. Our project is implemented by using Java, JavaScript, Python, Android Studio, Jetson Nano, and various open sources tools like LucidChart, Figma, MongoDB, MongoDB Atlas and MongoDB Realm.

What are we building in this project? How to build this Project?
We are building an MIoT app service that can monitor, record, and analyze patients' data in real-time. It would connect with some medical tools like temperature, blood oxygen and pulse sensors.


# Mobile Application Pages, list the screens (Activities that will be used in the app).

Home Page/

Sign in/

Sign up/

All Patients Data (Display all patients)/

Add New Patient/

Add Patient (Enter Patient Information)/

Patient Profile Page (Display Single Patient Information and 3 Options)/

Current Data
 
Analyzed Data

Previous Data

Current Data (Visualization)/

Present the reading data from the corresponding database collection

Analyzed Data (Visualization)/

Present the reading data from the corresponding database collection

Previous Data (Visualization)/

Present the reading data from the corresponding database collection

# Mobile App Features.

Allow users to sign up for a user account with a username, email, and password.

Allow users to sign in with an existing username and password.

All patients can be seen on the All Patients Page.

Allow users to create and store new patient information in the cloud database by clicking the ‘Add Patient’ button.

Single patient information can be seen on the Patient Profile Page.

Provides three different options for users to monitor a patient’s health condition.

Clicking the ‘Current Data’ button, allows the user to monitor the patient’s current data from sensors in real-time.

Clicking the ‘Analyzed Data’ button, allow the user to monitor the patient’s analyzed data from sensors in real-time.

Clicking the ‘Previous Data’ button allows the user to monitor the patient’s previous data from sensors in real-time.

# Hardware Features and Processes 
NVIDIA Jetson Nano

Raspberry Pi Board

Heart rate sensor

Blood oxygen sensor

Temperature sensor 

Breadboard

Jumper wires (both male to female and female to female)

PCB Mounts

USB Wi-Fi adapter 

Power Supply

SD Cards

Static Shift register

Setup hardware and procure sensors(Temperature, Pulse and blood oxygen) for MIoT data

Flash SD cards with operating systems on NVIDIA Jetson Nano and Raspberry Pi boards

Configure both boards to connect to MongoDB

Solder sensors 

Connect sensors with jumper wires, PCB mounts and Breadboard.

Write python scripts for sensors to generate input/output relationship and log data in real time to MongoDB atlas 

# Links 

[Project Proposal (Google Doc)](https://docs.google.com/document/d/1NJMQOMvY2MpA_Xw3HJr6btzzPtW0cAP2VXGMs_n395o/edit)

[Project Proposal (Confluence)](https://6510sp22team6.atlassian.net/wiki/spaces/~636772784/pages/360449/Project+Proposal)

[Sprint (Jira Software/Board)](https://6510sp22team6.atlassian.net/jira/software/projects/QFRK/boards/1)

[Unit Testing (Google Doc)](https://docs.google.com/document/d/1MNegLkm3lwhw6YBmPirdXO6zjde3mN_peon4fRSZdy4/edit)