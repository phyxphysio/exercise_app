# Physio Tools

A web app that saves physiotherapists admin time. In one place they can send exercise prescriptions, re-engage patients who've stopped attending, and see clinic business metrics.

## Why I built it

I worked as a physiotherapist before becoming an engineer. Clinics without tools like PhysiTrack or a data dashboard were stitching this work together by hand. I built this for them, with server-rendered Django and HTMX to keep it fast and simple to run.

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

- **Server:** Django
- **Front end:** HTML5, Bootstrap, JavaScript, HTMX
- **Testing / linting:** Pytest, Ruff
- **Containerisation:** Docker
- **Deployment:** AWS Lightsail via GitHub Actions

## License
This project is under the MIT License, available in LICENSE.text