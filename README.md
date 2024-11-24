# movie-review-website
# Movie Review Website 🎥

This project is a **Movie Review Website** built using the Django framework. It allows users to browse concise reviews of movies, showcasing the power and flexibility of Django in creating dynamic, content-driven web applications.

## About Django 🛠️

Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Known for its scalability and built-in features, Django simplifies common web development tasks such as routing, database management, and template rendering.

---

## How It Works 💡

The project leverages Django's core components to deliver functionality in an organized manner:

### **1. `urls.py`**
The `urls.py` file acts as the traffic controller, routing user requests to the appropriate views. For this project:
- URLs are mapped to views for displaying movie reviews, creating new reviews, and managing user interactions.
- Example:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movie/<int:id>/', views.movie_detail, name='movie_detail'),
]
```

### **2. `views.py`**
The `views.py` file handles the logic for processing requests and returning responses. 
- For instance:
  - The `home` view fetches a list of movies and their reviews to display on the homepage.
  - The `movie_detail` view fetches and renders a detailed review for a specific movie.
```python
from django.contrib import admin
from django.urls import path,include
from blog import views

urlpatterns = [
    path('',views.home,name='home'),
    path('blog/',views.blog,name='blog'),
    path('contact/',views.contact,name='contact'),
    path('blogpost/<str:slug>',views.blogpost,name='blogpost'),
    path('search/',views.search,name='search')


   
]
```

### **3. `models.py`**
The `models.py` file defines the structure of the database using Django's ORM. 
- Example model:
```python
class Blog(models.Model):
    sno= models.AutoField(primary_key=True)
    title= models.CharField(max_length=200)
    genre=models.CharField(max_length=50,default="")
    content= models.TextField()
    short_desc=models.CharField(max_length=250,default="")
    slug=models.CharField(max_length=300)
    time=models.DateTimeField(auto_now_add=True)
    poster=models.CharField(max_length=250,default="")
  
    def __str__(self):
        return self.title
```
This model represents a movie with attributes like title, review, and name.

### **4. `settings.py`**
The `settings.py` file configures the project's behavior, including:
- Database settings: Define the backend database used to store movie data (e.g., SQLite, PostgreSQL).
- Installed apps: Register the app containing the movie review logic.
- Templates and static files: Configure the directories for HTML templates and CSS/JS assets.

---

## Features 🌟
- **Concise Reviews**: Displays quick yet meaningful movie reviews.
- **Dynamic Routing**: Seamlessly navigate between movie listings and detailed views.
- **Extensible Models**: Easily add more features like user authentication, comments, or ratings.

---

## How to Run 🏃‍♂️
1. Clone the repository:
   ```bash
   git clone https://github.com/ishmeet3105/movie-review-website.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run database migrations:
   ```bash
   python manage.py migrate
   ```
4. Start the server:
   ```bash
   python manage.py runserver
   ```
5. Access the site at your address

---

### **Happy Reviewing!** 🎬
