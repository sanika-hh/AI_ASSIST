# College Attendance Smart System

This project is a simple Flask-based web page for a college attendance smart system.

## Project purpose
The application allows a user to enter:
- college name
- class start time
- class end time
- break start time
- break end time
- student attendance message

It then displays the submitted information in a summary panel.

## Refactoring understanding
Refactoring means improving the code structure without changing how the program works.

In this project, the code was cleaned up to make it easier to read and maintain.

### Improvements made
- grouped repeated default values into one dictionary
- removed repeated assignments across the route
- kept logic in small helper functions
- separated form processing from status logic
- kept the HTML inside a single template string for simplicity

### Why refactoring matters
Refactoring helps because:
- code becomes easier to read
- future updates are easier to make
- bugs are easier to find
- the project is easier for others to understand

## Run the project
1. Open the project folder.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the app:
   ```bash
   py app.py
   ```
4. Open in the browser:
   ```text
   http://127.0.0.1:5000
   ```

## Files in the project
- `app.py` - main Flask application
- `requirements.txt` - Python dependencies
- `README.md` - project notes and explanation

## Future improvements
This project can be extended with:
- login system
- student list
- attendance database
- dashboard reports
- admin panel
