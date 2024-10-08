# Django Blog

User Authentication Views
Registration
View Name: register
Functionality: Allows users to create a new account.
Form Used: CustomUserCreationForm
Redirects: Upon successful registration, redirects to the profile page.
Login
View Name: user_login
Functionality: Handles user login.
Form Used: AuthenticationForm
Redirects: Redirects to the profile page after successful login.
Logout
View Name: user_logout
Functionality: Logs the user out.
Redirects: Redirects to the home page after logout.
Profile
View Name: profile
Functionality: Allows authenticated users to view and edit their profile information.
Form Used: UserChangeForm
Functionality: Handles POST requests to update user details.
Custom Forms
Custom Registration Form
Form Name: CustomUserCreationForm
Base Class: UserCreationForm
Additional Fields: Email
Usage: Handles user registration with additional fields.
Templates
Registration
Template File: register.html
Purpose: Provides a form for user registration.
Fields: Username, Email, Password
Login
Template File: login.html
Purpose: Provides a form for user login.
Fields: Username, Password
Profile
Template File: profile.html
Purpose: Allows users to view and update their profile information.
Fields: Email, (Optional) Profile Picture, Bio
URL Configuration
Authentication URLs
/register/: Maps to the register view.
/login/: Maps to the user_login view.
/logout/: Maps to the user_logout view.
/profile/: Maps to the profile view.
Testing the Authentication System
Testing Registration:

Navigate to /register/.
Fill out the registration form and submit.
Verify that a new user is created and redirected to the profile page.
Testing Login:

Navigate to /login/.
Enter valid credentials and submit.
Verify that the user is logged in and redirected to the profile page.
Testing Logout:

Log in first.
Navigate to /logout/.
Verify that the user is logged out and redirected to the home page.
Testing Profile Management:

Log in.
Navigate to /profile/.
Update profile details and submit.
Verify that the changes are saved and displayed correctly.
Security Considerations
CSRF Protection:

Ensure all forms include {% csrf_token %} to protect against CSRF attacks.
Password Security:

Django’s built-in password hashing is used to secure user passwords.
Troubleshooting
Issue: "User cannot log in after registration"

Solution: Ensure the registration form is saving user details correctly and that the login view is authenticating users properly.
Issue: "Profile changes are not saved"

Solution: Verify that the profile view is handling POST requests and saving updates correctly.



CRUD Features:

Overview of each CRUD operation (List, Detail, Create, Update, Delete).
Instructions on how to use the features.
Permissions and access control details.
Setup Instructions:

How to set up and test the CRUD features.
Any additional configuration required.
Usage:

How to create, view, edit, and delete posts.
Details on authentication requirements for different actions.
Deliverables:
Code Files:

views.py
forms.py
models.py
urls.py
Template Files:

post_list.html
post_detail.html
post_form.html
post_confirm_delete.html



## Comment Functionality

The blog has a comment system that allows users to interact with blog posts by leaving comments. Here’s how it works:

### Adding a Comment
- Navigate to a blog post and add a comment using the form provided at the bottom of the post detail page.

### Editing a Comment
- If you are the author of a comment, you can edit it by clicking the "Edit" link next to your comment.

### Deleting a Comment
- If you are the author of a comment, you can delete it by clicking the "Delete" link next to your comment.

### Comment Display
- Comments are displayed under each blog post and are visible to all users.


Tagging and Search Functionality in django_blog
Tagging Feature:
Adding Tags: When creating or updating a post, you can now add tags via the form.
Displaying Tags: Tags associated with a post are displayed at the bottom of each post.
Filtering by Tag: Users can click on a tag to filter posts that share the same tag.
Search Functionality:
Search Bar: A search bar is available at the top of the blog.
Search Query: Users can search for posts by entering keywords. The system searches through post titles, content, and tags.
Search Results: The results page displays posts matching the query.
