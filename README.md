# VITYARTHI-PROJECT
Vityarthi project
# Attendance Analyzer

I made a web application that helps students track their attendance and figure out how many classes they need to attend to get the required 75 percent attendance. I used Streamlit to build this application.

---

## The Problem

A lot of students have a time calculating their attendance percentage. They often find out late that they do not have enough attendance. My project solves this problem by doing a things.

* It calculates attendance automatically

* It tells students how classes they need to attend

* It shows students how classes they can safely skip

---

## What It Can Do

My Attendance Analyzer has a few features.

* It calculates the attendance percentage

* It warns students if their attendance is below 75 percent

* It suggests how classes students need to attend to get 75 percent attendance

* It has a bunk calculator that shows students how classes they can skip

* It has a clean and interactive user interface thanks to Streamlit

---

## The Technology Used

I used the following technologies to build my project.

* Python

* Streamlit

---

## Project Structure

My project is organized like this.

```

Attendance-analyzer/

│

├── app.py # The Streamlit application

├── requirements.txt # The list of dependencies

└── README.md # The project documentation

```

---

## Setting It Up

To use my Attendance Analyzer follow these steps.

### Step 1: Get The Code

First you need to get the code from the repository. You can do this by running the following command.

```Bash

git clone https://github.com/your-username/attendance-analyzer.git

cd attendance-analyzer

```

### Step 2: Install The Dependencies

Next you need to install the dependencies. You can do this by running the following command.

```Bash

pip install -r requirements.txt

```

### Step 3: Run The Application

Finally you can run the application by running the following command.

```Bash

streamlit run app.py

```

---

## How It Works

My Attendance Analyzer uses a formula to calculate attendance.

It calculates attendance like this:

Attendance = (Attended Classes / Total Classes) * 100

If attendance is below 75 percent it calculates the required classes like this:

Required Classes = (0.75 * Attended) / 0.25

This makes sure that the attendance is predicted accurately.

---

## Who Can Use It

My Attendance Analyzer is useful for students who want to track their attendance.

* College students can use it to track their attendance

* Students can use it to avoid detention due, to attendance

* Students can plan when to attend or skip classes

---

## Future Plans

I want to add features to my Attendance Analyzer.

* I want to add -subject tracking

* I want to save attendance history

* I want to add charts and analytics

* I want to deploy it for public access

---

## About The Author

My name is Praful Tharwani.

---

## Acknowledgment

I made this project as part of a Bring Your Own Project assignment. The goal was to apply real-world problem-solving using programming concepts.
