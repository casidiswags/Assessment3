# Gym Web Application

## Overview
This is a Flask-based web application that provides information about powerlifting events and meets. The application uses a SQLite database to store and retrieve powerlifting and meet data.

## Maintenance

### Adding Data
- Powerlifting data should be provided in a CSV file named `powerlift.csv`.
- Meet data should be provided in a CSV file named `meets.csv`.

### Database Maintenance
- The SQLite database is stored in a file named `gym.db`.
- Tables: The application creates two tables in the database - `powerlift` and `meets_data`. Any changes to the database schema should be reflected in the code.
- **Caution:** Ensure data integrity when modifying the database structure.

## Testing

### Unit Testing
- The application includes a unit test script `test.py`.
- Run tests using the command: `python3 -m unittest test.py`.
- Ensure all tests pass before deploying.

## Running the Application

### Prerequisites
- Python 3.7 installed.
- Required Python packages installed. Install using: `pip install -r requirements.txt`.
- Required Python package installed. Install using: `pip3 install Flask`.
- Required python packages installed. Install using: `pip install SQLite and SQLAlchemy`

### Steps
1. **Clone Repository:**
    ```bash
    git clone https://github.com/casidiswags/Assessment3.git
    cd Assessment3
    ```

2. **Create Virtual Environment:**
    ```bash
    python3 -m venv venv
    ```

3. **Activate Virtual Environment:**
    ```bash
    source venv/bin/activate
    ```

4. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5. **Run Application inside codio (recommended):**
    ```bash
    cd Assessment3
    python app.py


6. **Access the Application:**
    Open a web browser and go to https://modestothello-radaredward-5000.codio-box.uk/

## Deployment
- For production deployment, consider using a production-ready web server like Gunicorn or uWSGI.
- Configure the server to serve the application and set up appropriate security measures.
- Use a reverse proxy (e.g., Nginx or Apache) for added performance and security.

## Contributors
- Cassidy Jeremiah Imhanlahimi - 52318847