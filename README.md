#Project name:

Fridge Whisperer Ammachi

##Basic Details

Team Name: ScriptForge
Team Members
Team Lead: Abijith V S - NSS Collge Of Engineering, Palakkad.
Member 2: Aiswarya S - NSS Collge Of Engineering, Palakkad.

##Project Description
Fridge Whisperer Ammachi is an interactive web app that analyzes your fridge contents through image upload and suggests personalized recipes. Using AI-powered ingredient detection with YOLOv8 on the backend, it offers fun, mood-based dialogues from Ammachi, the virtual grandma. The frontend features a charming UI and dynamic speech bubbles that respond to user moods. This project combines computer vision, natural language, and playful UX to make cooking inspiration delightful and accessible.

##The Problem (that doesn't exist)
Ever stood in front of your fridge confused about what to cook? Most apps expect you to know your ingredients perfectly—yeah right! So we made Fridge Whisperer Ammachi, a sassy grandma who tells you what to cook and keeps you entertained. Because sometimes, the real problem is just being hungry and clueless!

##The Solution (that nobody asked for)
Introducing a grandma who actually listens to your fridge chaos and throws sarcastic, hilarious cooking ideas your way — because sometimes what you really need is a little sass with your snacks. Problem solved... or at least entertained!

##Technical Details 
Technologies/Components Used
For Software:
Frontend: HTML, CSS, JavaScript 

Backend: Python with FastAPI framework

AI Model: Open-source YOLOv8 for fridge ingredient detection

Image Processing: Integration with YOLOv8 to detect fridge items from uploaded images

User Interaction: Mood selector affecting Ammachi’s dialogues and voice tone

FastAPI – Lightweight Python web framework for backend APIs

VS Code – Development

##Implementation
For Software:
Installation
 1. Clone the repository  
git clone https://github.com/yourusername/fridge-whisperer-ammachi.git  

2. Navigate into the project folder  
cd fridge-whisperer-ammachi  

3. Install dependencies  
pip install -r requirements.txt  


Run
Start the backend server (FastAPI)
uvicorn main:app --reload  

Open the frontend in your browser
open index.html   # or just double-click the file


##Project Documentation
For Software:

Screenshots 
![fridge1](https://github.com/user-attachments/assets/b04c6c97-ea25-4b45-a82b-99e8baf9b7c4)
The home page features Ammachi with mood-based witty dialogues in manglish, and buttons to enter ingredients or upload a fridge image—set against a lively falling veggies animation.

![fridge4](https://github.com/user-attachments/assets/bc5528ec-db22-4cc1-bed7-b8ab088ec9a5)
Users can select Ammachi’s mood from Sad, Happy, Sarcastic, or Angry to change her dialogue style dynamically.

![fridge2](https://github.com/user-attachments/assets/90105e12-7d1d-4e44-9203-51f31880abbb)
The upload page lets users choose and submit a fridge image while Ammachi cheerfully guides them with mood-based messages.

![fridge3](https://github.com/user-attachments/assets/d09a3ef6-bad1-4d87-9653-f662ef49b46e)
The recipe page displays personalized cooking suggestions based on detected fridge ingredients.


Diagrams
![Workflow](https://github.com/user-attachments/assets/e5cee3ad-eb79-42c5-96ba-2cdd3a0b28a1)
*Figure: Workflow/Architecture of Fridge Whisperer Ammachi*




##Build Photos

Build Process:
![Build](Add photos of build process here) Explain the build steps
We wrote the frontend in HTML, CSS, and JavaScript, and integrated the backend powered by Python and YOLOv8 using FastAPI.
The build process involved coding, testing locally, and deploying the web application to a live environment for user interaction.

final photos:
![fridge1](https://github.com/user-attachments/assets/b04c6c97-ea25-4b45-a82b-99e8baf9b7c4)
![fridge2](https://github.com/user-attachments/assets/90105e12-7d1d-4e44-9203-51f31880abbb)
![fridge3](https://github.com/user-attachments/assets/d09a3ef6-bad1-4d87-9653-f662ef49b46e)
Users can manually enter ingredients or upload a fridge image, which is analyzed by a YOLOv8 backend to detect items.
Ammachi then delivers funny, sarcastic Manglish comments through popups and speech bubbles.
Finally, the app suggests recipes based on the detected ingredients for users to try.


##Project Demo
Video
[Add your demo video link here] Explain what the video demonstrates

##Team Contributions
Abijith V S: Backend, Integration
Aiswarya S: Frontend

Made with ❤ at TinkerHub Useless Projects
