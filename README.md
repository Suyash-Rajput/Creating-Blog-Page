 Django Blog Application
Objective: Build a simple blog application using Django and Django REST Framework,
integrating basic CRUD (Create, Read, Update, Delete) functionalities.
Requirements:
Models:
● Create two models: Post and Comment.
● The Post model should have fields like title, content, author, and
published_date.
● The Comment model should be linked to the Post (each post can have
multiple comments) and include fields like author, text, and
created_date.
APIs:
● Utilize Django REST Framework to create APIs for these models.
● Implement List, Create, Retrieve, Update, and Delete API views for Post.
● Implement List and Create API views for Comment under each Post.
Views and URLs:
● Create corresponding URLs for each API view.
● Ensure that the API returns JSON responses.
User Authentication:
● Implement token-based authentication.
● Only authenticated users should be able to create, update, or delete posts
and comments.
Frontend (Optional):
● If you are comfortable with Django React, create a simple front end to
interact with the backend API.
● Implement features like displaying all posts, viewing a single post along
with comments, and adding a new post or comment.
Documentation:
● Provide a README file with instructions on how to set up and run the
application.
● Document the API endpoints with examples.
Testing:
● Write basic tests for your models and API views.
