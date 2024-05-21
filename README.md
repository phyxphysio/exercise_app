# Physio Tools

## Introduction

This web application allows physiotherapists to generate and email therapeutic exercise prescriptions, activate patients, and visualize data

Users can create, update, and modify available exercises as needed.

## Features

- Generate personalized exercise emails for patients.
- Preview and customize emails before sending.
- Add, modify, and delete exercises in the database.
- Upload reports to send emails to inactive patients and visualize business metrics.
- Responsive design for ease of use across devices.

## Using the App

Visit https://app.liammiller.net/

Login with credentials granted by the admin

### Prescription

Enter your search parameters

Click 'Generate Email Preview' to see the email preview.
Customize email content as necessary, then click 'Send Email'.

### Activate Patients

Upload Last Attendance Report containing the names and emails of patients who have not attended the clinic in the last three weeks.

Preview email content by clicking 'Preview Email', then send email with 'Send emails'

## Tech Stack

Server: Django
Linting: Ruff
Testing: Pytest
Containerization: Docker  
Deployment: AWS Lightsail via GitHub Actions
Front End: HTML5, Bootstrap, JavaScript, HTMX
