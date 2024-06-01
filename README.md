### Beancounter (A Personal Finance Webapp)

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Files and Folders](#files-and-folders)
- [Manual Testing](#Manual Testing)
- [Usage](#usage)



### Description:-
Beancounter is a web application designed to help users track their income, daily expenses, and view their remaining balance securely through unique login credentials. 
The application leverages Python, Django, HTML5, CSS3 (Bootstrap), and MySQL to provide a seamless and secure experience for managing personal finances.

### Features:-
- **Track Income and Expenses:** Add, categorize, and manage your income and daily expenses.
- **View Remaining Balance:** Easily view your remaining balance based on your tracked income and expenses.
- **User Authentication and Authorization:** Securely access your financial information with unique login credentials.
- **Responsive Design:** Built with HTML5 and CSS3 (Bootstrap) for a responsive and user-friendly interface.

### Technologies Used:-
- **Backend:** Python, Django, MySQL
- **Frontend:** HTML5, CSS3 (Bootstrap)
- **Template Engine:** Jinja2
- **Database Management:** Django ORM (Object Relational Mapper)

### Files and Folders
- **ExpenseTracker/:**
  - settings.py: Contains project settings such as database configuration, installed apps, static files configuration, etc.
  - urls.py: Main URL configuration for the project, including routing to app-level URLs.
  
- **Tracker/ (Django App):**
  - models.py: Defines Django models for the application, including income, expenses, user profiles, etc.
  - views.py: Contains business logic for handling requests, rendering templates, processing forms, etc.
  - urls.py: App-level URL configuration for routing requests to appropriate view functions.
    
- **static/:** Folder containing CSS files, images, JavaScript, or other static assets used in the application.
  - style.css: Custom CSS styles for the application.
  - images/: Folder containing image assets used in the application.
    
- **templates/: Folder containing HTML templates for rendering views and pages.**
  - base.html: Base template containing common elements like header, footer, etc.
  - Other HTML files for specific pages or components.

### Manual Testing:-
- **Register a New Account:**
  - Open the application in your web browser.
  - Click on the "Register" link to create a new account.
  - Enter your details and submit the form.
  
- **Log In to Your Account:**
  - After registering, log in using your credentials.
  - Verify that you can successfully access your account dashboard.
  
- **Add Income and Expenses:**
  - In your account dashboard, navigate to the "Add Income" and "Add Expense" sections.
  - Enter the necessary details (amount, category, description, etc.) and submit the forms.
  - View Remaining Balance and Total Expenses:

Check the "Remaining Balance" section to see your updated balance after adding income and expenses.
Navigate to the "Total Expenses" section to view a summary of your expenses.

### Usage
- **Run the Django development server :**
   - python manage.py runserver
- **Open your web browser and visit :**
   - http://localhost:8000/
Register or log in with your credentials to start tracking your income and expenses.
