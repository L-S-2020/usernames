# Usernames (my first project on github)
  
This is a Django-based web application that allows users to create personal profiles to show their usernames in different games/applications. The application is built with Python and Django, and uses HTML and CSS for the frontend.  
The profile can then be shared over a personal link.  
  
## Features  
  
- User Authentication: Users can sign up, log in, and log out.  
- Profile Management: Users can create, edit, and delete their profiles.  
- Game Management: Users can add and delete games from their profiles.  
  
## Installation  
  
1. Clone the repository:  
      
  ```git clone https://github.com/L-S-2020/usernames.git```  
   
2. Navigate to the project directory:  

  ```cd usernames``` 
    
 3. Install the required dependencies:  
      
  ```pip install -r requirements.txt```  
  
 4. Run the Django migrations:  
      
  ```python manage.py migrate```  
  
 5. Create a superuser (to use the Django admin module):  
      
  ```python manage.py createsuperuser``` 
   
 6. Start the Django server:  
      
  ```python manage.py runserver```  
 
 Now, you can navigate to `http://localhost:8000` in your web browser to view the application.  
  
## Usage  
  
- To create a new profile, navigate to the signup page and fill out the form.  
![Registration form](https://raw.githubusercontent.com/L-S-2020/IMP_Projekt_2022/master/images/register.png)
- To log in, navigate to the login page and enter your credentials.  
- Once logged in, you can add usernames to your profile, edit your profile, or delete usernames from your profile.
![Edit profile](https://raw.githubusercontent.com/L-S-2020/IMP_Projekt_2022/master/images/edit.png)  
- You can share you're profile over the given link
![shared profile](https://raw.githubusercontent.com/L-S-2020/IMP_Projekt_2022/master/images/shared.png)
- To log out, click the logout button.  
  
## License  
  
This project is licensed under the MIT License.
