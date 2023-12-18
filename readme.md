# Django Boilerplate

I created this as a cool boilerplate to use with Pycharm to quickly build the mundane parts of a Django app. It comes with the following:
- A custom user model named `ApplicationUser` that uses an email as a primary field rather than a username.
  - An SQLite instance with the superuser with the email: `admin@example.com` and the password `batman29` have already been created.
- A folder for project configurations called `config` with settings configured for the `ApplicationUser` model as the default user.
- A `requirements.txt` file with Django 5.0, djangorestframework 3.14, and wheel 0.42.