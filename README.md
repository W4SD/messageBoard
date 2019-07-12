messageBoard



Activating virtualenv
1. Activate your virtualenv: source vnev/bin/activate
2. Create a requirements.txt of currently installed packages: pip freeze > requirements.txt
3. Delete the misspelled virtualenv: rm -r vnev/
4. Create a new virtualenv with correct name: virtualenv venv
5. Activate new virtualenv: source venv/bin/activate
6. Install packages from requirements.txt: pip install -r requirements.txt
