# Django Boilerplate

I created this as a cool boilerplate to use with Pycharm to quickly build the mundane parts of a Django app. 
It comes with the following:
- A custom user model named `ApplicationUser` that uses an email in place of a username.
- Forms for creating and editing a user.
- Class-based views to create a new user, login/logout a user, list all users, and get user details.
- Templates to go along with each of the views.
- An SQLite instance with the superuser with the email: `admin@example.com` and the password `batman29` have already 
been created.
- A folder for project configurations called `config` with settings configured for the `ApplicationUser` model
as the default user.
- A `requirements.txt` file with Django 5.0, djangorestframework 3.14, and wheel 0.42.

How to setup:
1. `git clone https://www.github.com/codewriter3000/django-boilerplate`.
2. Go to File -> Settings -> Project: django-boilerplate -> Python Interpreter.
3. Click on "Add Interpreter", a button that will display a dropdown which is located towards the top-right of the 
Settings window.
4. Click on "Add Local Interpreter", which should be the highest item on the dropdown.
   1. When making your new local interpreter, you want a "New" environment in the `/venv/` folder inside of your project.
   2. Make sure you have Python installed so that your PC can use it.
   3. After you create the local interpreter, you should see the new virtual environment being created
as well as `pip install -r requirements.txt` being ran automatically.
5. Locate your run/debug configurations, which should be situated towards the up-right corner of your IDE 
and click on the dropdown. If you don't see "config" as an option, then this step will show you how to get it up there.
   1. The dropdown should display an "Edit Configurations..." button.
   2. Click on the "+" button on the toolbar in the upper-left corner of the run configuration panel.
      1. This should display a dropdown with all of the run configurations that you can select.
   3. Click on "Django Server".
   4. The name doesn't matter, but pick something like "config" or "runserver".
   5. Copy and paste this as your environment variables: `PYTHONUNBUFFERED=1;DJANGO_SETTINGS_MODULE=config.settings`
      1. If you see an error at the bottom saying "Django is not importable in this environment", try the following:
         1. Go to your terminal, which should appear by clicking on one of the tab buttons on the bottom of your screen.
         2. Type in `pip install -r requirements.txt`.
6. Run 'config' by clicking the play button or use the keyboard shortcut `Shift+F10`.
7. If there is something you don't understand, an error, or know a more efficient way to configure this, 
please raise an issue in this repository.