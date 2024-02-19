cd /Users/liammiller/Desktop/Coding\ Projects/exercise_app/
source .venv/bin/activate
python physioexercises/manage.py runserver &
open -a "Google Chrome" http://127.0.0.1:8000/&


# Save the PID of the server process
SERVER_PID=$!

# Wait for 8 hours (8 hours * 60 minutes * 60 seconds = 28800 seconds)
sleep 28800

# Kill the server process
kill $SERVER_PID

# Optionally, deactivate the virtual environment
deactivate

