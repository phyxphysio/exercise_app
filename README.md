# Exercise Emailer for Patients

## Introduction

This Django app allows physiotherapists to generate, preview, and send emails containing exercise prescriptions to their patients. users can also create, update, and delete exercises from the database.

For now, this app is designed to be run locally, and includes shell scripts ot start and stop the development server, making it easy to use the tool in a clinical setting.

## Features

Generate personalized exercise emails for patients.
Preview and customize emails before sending.
Add, modify, and delete exercises in the database.
Responsive design for ease of use across devices.

## Getting Started

Prerequisites
Python (3.12)
Django (5.0.1)
Other dependencies listed in physioexercises/requirements.txt

## Installation

Clone the repository:

```bash
`git clone https://github.com/phyxphysio/exercise_app
```

Navigate to the project directory:

```bash
cd exercise_app/physioexercises
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Migrate the database:

```bash
python manage.py migrate
```

## Configuration

Configure environment variables by copying the .env.example file to a a .env file and providing credentials.

You will need to generate a new DJango secret key with the python shell like so.

```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

## Start using the app

### Option 1 - Manual Start

Run the development server:

```bash
python manage.py runserver
```

Open the page in your browser, and fil in the form fields as appropriate.

### Option 2 - Start with shell script

First, configure the start.sh file with th path to the project directory

`path/to/exercise_app`

Then make start and stop scripts executable:

```bash
chmod +x start.sh stop.sh
```

Lastly, run start.sh to start the development server, then kill it after 8 hours

```bash
start.sh
```

To stop the server with a script, run:

```bash
stop.sh
```

These scripts can be configured with the Mac Automator app to run when a desktop icon is clicked.

## Using the App

Click 'Generate Email Preview' to see the email preview.
Customize email content as necessary, then click 'Send Email'.

## Testing

Run unit tests to check HTTP status codes and send mail functionality.
`pytest`
