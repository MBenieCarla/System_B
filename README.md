#Travel System project

**Project description:**
Django-based web application for managing travel bookings
This system includes key templates such as the 
a. login and logout of users feauture
b. A registration feature to take into account new users
c. a template for the users profile


**How to run the system**
system starts at the home page with buttons optioning to register or login

Users log into the system via the login page using their email and password
authenticated users are logged in successfully while unauthorized user i.e users without existing accounts register through the registration page using their full name, email and password.
upon succesfull login, users (redirected to the create booking page where the destinations are displayed and their options saved to the database)
//welcomed into their profile page with their name and email displayed on the screen and the date since they were registered as users. users can then view their profile pictures//
users can then logout of the system.

**administrative rights**
implemented an admin module with restricted access to its dashboard 

**additional apps**
destination and booking pages
booking pages include destinations and dates booked by the user
in the booking app users fill in their information with their name, email and date
users can update their profiles and save changes 

destination page featuring available destinations

**databases**
implemented mySQL workbench/ postgreSQL to create a database connection to validate and authenticate users and register new users
