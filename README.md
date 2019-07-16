messageBoard app

HOWTO:
1. Activate python virtualenv > sourve engineRoom\Scripts\activate
    1.1 Should activate virtualenv called 'haaste'
2. Install packages from requirements.txt: pip install -r requirements.txt
3. Run application with python app.py
4. Go To localhost:5000




Notes: !!!
Exporting messages could be done multiple ways but currently the way the application is designed there is no 'good solution' to export all the messages posted in the way that is descriped in the challange.

If I would make the app again I would design it to look more like an sales page that each individual message would be its separate URL and from there you could export the page as or 'posted message' with the chosen type. 

Flask supports exporting data but the design was definately a problem here.
