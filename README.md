# About the project
This project is a job search website that helps candidates find jobs and allows businesses to post job listings and find suitable candidates.

# Build with

In this project, the following technologies were utilized:

* Front-end:
  - Vue.js
  - Tailwind CSS
 
* Back-end:
  - Python
  - FastAPI
  - Firebase
 
# Installation Guide

## Step 1: Clone the Project

```bash
git clone https://github.com/namdnhn/head-hunter
cd head-hunter
```

## Step 2: Install Dependencies
### Install dependencies for the back-end
Prerequisites: Python and MySQL must be installed on your machine.

Instructions:

Navigate to the app folder in the project, create a .env file with the content of the .env.example file and modify the information to match your machine.

- Create a virtual environment: ```python -m venv head-hunter-env```
- Activate the virtual environment:
    + Windows: ```head-hunter-env\Scripts\activate```
    + MacOS and Linux: ```source head-hunter-env/bin/activate```
- Install the dependencies for the virtual environment: ```pip install -r requirements.txt```

### Install dependencies for the front-end
- From the root directory
- ```bash
  cd view
  npm install
  ```

## Step 3: Run the project

```bash
* Run the back-end
cd app
uvicorn main:app --reload

* Open a new terminal window
* Run the front-end
cd view
npm run dev
```
