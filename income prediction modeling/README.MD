**How to Launch**

Step 1: Download and Extract the Project Files
    1. Download the project files from the income prediction modeling folder within the repository.
    2. Extract the files to a desired location on your computer.

Step 2: Navigate to the Project Directory
    1. Utilizing a source code editor like VScode, open the terminal or command prompt and navigate to the project folder.
    2. Create and Activate a Virtual Environment:
        - Windows  -- python -m venv myenv
                        - Activate the Enviornment
                            -- myenv\Scripts\activate
        - macOS/Linux -- python3 -m venv myenv
                        - Activate the Enviornment
                            -- source myenv/bin/activate
    3. Install the required packages:
        -- pip install -r requirements.txt

Step 3: Verify Project Structure
    1.  Navigate to the flask_app/
Step 4: Run the Flask Application
    1.  Run the Flask Server:
        - Windows - In terminal -- flask run
                                -- python app.py
        - macOS/Linux -- In terminal -- flask run
                                     -- python3 app.py
    2.  Access the Application:
        - To open the application for the form you must open it in the development enviornment - once you have run Flask in your terminal the web browser -- http://127.0.0.1:5000/
Step 5: Verify and Use the Application
    1. Ensure that the home page loads correctly with the background image, styled form, and jumbotron.
    2. Use the Application:
        - Fill out the form with the required details (age, gender, race, education level, and marital status).
        - Submit the form to receive a prediction on the individual's income.

Summary
- Download and extract the project files.
- Navigate to the project directory using cd.
- Create and activate a virtual environment using python -m venv myenv and source myenv/bin/activate or myenv\Scripts\activate.
- Install required packages using pip install -r requirements.txt.
- Run the Flask server using flask run or python app.py.
- Access the application via a web browser at http://127.0.0.1:5000.
- Following these steps will allow someone to successfully launch and use your - Flask application for income prediction on both Windows and macOS/Linux systems.


