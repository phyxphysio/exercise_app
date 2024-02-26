# Exercise Emailer for Patients
## Introduction
This Djanog app allows physiotherapists to generate, preview, and send emails contaning exercise prescriptions to their patients. users can also create, update, and delete exercsies from the database.  
## Features
Generate personalized exercise emails for patients.
Preview and customize emails before sending.
Add, modify, and delete exercises in the database.
Responsive design for ease of use across devices.
## Getting Started
Prerequisites
Python (3.12)
Django (5.0.1)
Other dependencies listed in requirements.txt
## Installation
Clone the repository:
`git clone https://github.com/yourusername/yourprojectname.git`
Navigate to the project directory:
`cd yourprojectname`
`Install the requirements:
`pip install -r requirements.txt`
Migrate the database:
`python manage.py migrate`
Run the development server:
`python manage.py runserver`
Open the page in your browser, and fil in the form fields as appropriate.
Click 'Generate Email Preview' to see the email preview. 
Customize email content as neccessary, then click 'Send Email'. 
## Configuration
Configure environment variables by copying the .env.example file to a a .env file and providing credentials.

You will need to generate a new DJango secret key with the python shell like so.
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```
## Testing
Run unit tests to check HHTP status codes and send mail functionality.
`pytest`