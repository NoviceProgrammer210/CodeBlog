BlogWebApp

BlogWebApp is a web application built using Django that allows administrators to create, edit, and manage blog posts. Users can view these blog posts but cannot contribute content, making it a read-only platform for visitors.

Features

Admin Management:

Admin can log in to the Django admin panel to create, update, or delete blog posts.

User-Friendly Blog Display:

Posts are displayed on the website in a clean and organized manner.

Dynamic Templates:

Templates render the blog list and blog details dynamically.


Prerequisites

Python 3.8+

Django 4.0+

Virtual environment (recommended)

Installation

1. Clone the Repository

git clone https://github.com/yourusername/BlogWebApp.git
cd BlogWebApp

2. Create and Activate Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

4. Apply Migrations

python manage.py makemigrations
python manage.py migrate

5. Create a Superuser

python manage.py createsuperuser

6. Run the Development Server

python manage.py runserver

Access the app at http://127.0.0.1:8000/.

Usage

Access the Admin Panel:

Log in to http://127.0.0.1:8000/admin/ using the superuser credentials.

Add blog posts through the admin interface.

View Blog Posts:

Navigate to the home page to see the list of blogs.

Click on a blog title to view the details.

Folder Details

home/

Handles general site navigation and home page templates.

blog/

Contains the core functionality of the application, including:

Models: Defines the structure of a blog post.

Views: Handles rendering blog lists and details.

Templates: Custom templates for displaying blog content.

templates/

Shared folder containing base templates and app-specific templates.

Projectblog/

The main project configuration folder, including settings and URL configuration.
