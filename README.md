# Dailys Habit Tracker

A habit tracker for your daily commitments to help you keep on top of your game.
Dailys combines a sleek interface with a social component to make tracking your habit as easy and enjoyable as possible.

## Project Goals

### User Friendly Interface and Seamless Habit Tracking

The web app features a clean and user-friendly interface that ensures effortless habit tracking across both desktop and mobile devices. Users can create, edit, and delete daily habits. Each check-in allows users to add personal notes, making it easier to reflect on their progress.  

### Social Engagement and Secure Authentication

To encourage consistency, Dailys incorporates a social engagement element where users can react to each other’s habit check-ins, offering motivation and support. Secure authentication via email ensures a safe experience.

### Data Visualizing

For better progress tracking, the app includes a calendar heat map that visually represents habit consistency over time, helping users identify streaks and trends.  

### Built for Scalability

Dailys is built with scalability and performance in mind, optimizing database models for a seamless experience and allowing for future feature expansion.

## User Stories

### 1. Habit Tracking and Reflection  
**As a dedicated user, I want to be able to create, edit, and track my daily habits effortlessly, so that I can stay committed and monitor my progress over time.**  

- I should be able to add new habits by entering a name, description and color
- When checking in, I want to be able to add optional personal notes, allowing me to reflect on my progress, challenges, or thoughts.  
- I need the ability to edit or delete habits at any time without losing my previous check-in data.  
- The interface should be clean, intuitive, and mobile-friendly so I can track my habits easily from any device.  

### 2. Social Engagement and Motivation  
**As a socially-driven user, I want to interact with my friends' habit progress, so that I can encourage them and stay motivated through community support.**  

- I should be able to see a feed or list of my friends’ recent habit check-ins, with details like streak count and personal notes (if made public).  
- I want to react to my friends’ check-ins to show encouragement and engagement.  
- There should be a way to control my privacy settings, allowing me to choose whether my habits or check-ins are visible to others.  
- Secure authentication via email should protect my personal data while allowing me to log in and access my progress from any device.  

### 3. Progress Visualization and Insights  
**As a data-driven user, I want to see a calendar heat map of my habits, so that I can recognize trends, stay motivated, and improve consistency.**  

- The app should provide a visually appealing heat map that highlights my habit streaks, with darker colors indicating stronger consistency.  
- I want to be able to view my habit progress over different time frames (weekly, monthly, yearly) to get insights into my long-term trends.  
- If I miss a habit, I should be able to quickly identify gaps in my streak and make adjustments to stay on track.  
- The app should handle large amounts of historical data efficiently, ensuring that loading my habit history remains fast and smooth.  

## User Requirements

view list with acceptance criteria in [TESTING.md](TESTING.md)

----

## Features

### Main App Features

These are the features necessary for the minimum viable product and base on the user requirements and acceptance criteria found in [TESTING.md](TESTING.md)

#### Landing Page

User should be sent to landing page if not logged in.

Landing Page should have a clean UI/UX with main information about app. This information should be stored in the database and editable from the 
admin portal. User should be able to Navigate to log in or register pages from landing page.

#### User Authentication

User should be able to sign up with an email, username and password. 
Password should meet requirements and username must be unique.

User should be able to log in and log out.

Once logged in user should be redirected to explore page

These pages should have a clean and coherent UI/UX 

#### Explore Habits Page

User should be able to see all the habits from users they follow and from users that set the habit to "public" visibility 

Logged in user can navigate to, a habit user's profile by clicking their username 

Logged in user can react to habits on the list

Should have a clean an easy to use UI/UX

#### Personal/User Habits Page

User can see a list of all their habits along with the check in calendar and data about their check ins and reactions to that Habit.

When user is on their own habits page, the habits element include the check in button, and button to edit and delete habit
User can create from this page. 

| Desktop View | Mobile View |
|--------------|-------------|
| ![personal habit element desktop](documentation/features/habit-element-personal.png) | ![personal habit element desktop](documentation/features/habit-element-personal-mobile.png) |

When user is on another user's habit page, the habit is show with the reaction select element

| Desktop View | Mobile View |
|--------------|-------------|
| ![personal habit element desktop](documentation/features/habit-element-personal.png) | ![personal habit element desktop](documentation/features/habit-element-personal-mobile.png) |


#### Habits CRUD Operations

User can create Habits with title, description, color and visibility.
They do this by clicking the 'Create new Habit' Button, which opens a form to create the habit where the button was

This forms are made with **django crispy forms**

![create habit btn](/documentation/features/new-habit-btn.png)

| Desktop View | Mobile View |
|--------------|-------------|
| ![create habit form](documentation/features/new-habit-form.png) | ![create habit form mobile](documentation/features/new-habit-form-mobile.png) |

They can edit each of these fields and they can delete them.

The Data is shown in the habit card in both the personal habits and explore habits page

#### Habit Check-Ins

User can check in to a habit and leave a note. they can do this aas much aas they want each day. this data will be show in the calendar 

#### Habit Calendar Heatmap

Each user habit in the personal habits page and the explore page contain a calendar heatmap that visualizes the check-in data for that habit

This calendar can be set to year, month and week viewing modes.

#### Reaction to Habits and their Notifications

User can choose from a range of reaction to a habit. Once reacted, the other user will see this as a notification they can dismiss
(note: not realtime notification)

#### Search Users

User should be able to enter a search term and get a list of users whose username match that term.

User can follow the users returned in the list.

#### Follow/Unfollow Users

User can follow and unfollow other users. This can be done in the search page or in the other user's profile page

User can see a badge on the explore page that shows if users are followed or not

#### Admin Page

The superuser should be able to access the admin page, from there they can manage all the habits and check ins data.
They can also add or remove users

They should also have access to change the data displayed in the landing page

### Django App Structure

The application is built on a root project that includes the the requirements file and the Procfile, which are used to build the project in Heruko. 
There is the main **dailys** Django project which includes the project settings file and the main urls file.

There are also two main django Apps, the **landing app** which includes the models, views and templates for the the landing page and the **habit_tracker** app which includes the 
views, template and models for the main habit tracking side of the web app. These are separate because there are not connected logically in the designed database. 

Further, there is a **templates directory** in the project root that include the base template which is inherited by the other templates. Also there is the **static/staticfiles** directory which 
include the css files and the javascript files used in the project.

Finally the **manage.py** file in the root is used to run the application locally and control to the django app 

- root
    - manage.py
    - requirements
    - Procfile
    - dailys project
        - settings.py
        - urls.py
    - habit-tracker app
        - views.py
        - models.py
        - /templates/
    - landing
        - views.py
        - models.py
        - /templates/
    - templates
        - base.html
    - staticfiles
    

### Database design

The database used a PostgreSQL instance in a server provided by Code Institute. Django is used to connect to that database and create the models

**User Model ERD**

note: using default django user model 

![user erd](documentation/erd/user-erd.png)

**Habit Model ERD**

![habit erd](documentation/erd/habit-erd.png)

**CheckIn Model ERD**

![checkIn erd](documentation/erd/check-in-erd.png)

**Reaction Model ERD**

![reaction erd](documentation/erd/reaction-erd.png)

**FollowerLookup Model ERD**

![followerLookup erd](documentation/erd/follower-lookup-erd.png)

**The Models below are only for the landing page and not connected to the Habit Tracking**

![landing page models erd](documentation/erd/landing-erd.png)


#### Complete Entity Relationship Diagram

![complete erd](documentation/erd/complete-erd.png)

### User Features

## UI / UX

Using Default Bootstrap colors for consistency and time efficiency

![bootstrap colors](documentation/ui-ux/bootstrap-colors.png)

### Mockups

**Paper Mockups**

The first thing I did design-wise was to create a hand drawn mockup to get the initial set of features into a coherent visual form

![hand drawn mockup](/documentation/mockups/paper-mockup.jpg)

**Basic UI Mockup**

Using the drawn design I created a basic mockup using Sketch to have a more flexibility in editing the design 

![basic mockup](/documentation/mockups/basic-sketch-mockup.png)

**Final UI Mockup**

I Finally created a more complex mockup on Sketch to show more elements and features that I had thought of.
This was still note representative of the complete final product as some features where added and the design on the site 
conforms more the the bootstrap standard as those are the styling classes used

### Pages

In this section are screenshots for each page on a desktop and mobile.

#### Login Page

| Desktop View | Mobile View |
|--------------|-------------|
| ![login page desktop](documentation/pages/sign-in-page.png) | ![login page mobile](documentation/pages/sign-in-page-mobile.png) |

#### Register Page

| Desktop View | Mobile View |
|--------------|-------------|
| ![register page desktop](documentation/pages/sign-up-page.png) | ![register page mobile](documentation/pages/sign-up-page-mobile.png) |

#### Logout Page

| Desktop View | Mobile View |
|--------------|-------------|
| ![logout page desktop](documentation/pages/logout-page.png) | ![logout page mobile](documentation/pages/logout-page-mobile.png) |

#### Landing Page

| Desktop View | Mobile View |
|--------------|-------------|
| ![landing page desktop](documentation/pages/landing-page.png) | ![landing page mobile](documentation/pages/landing-page-mobile.png) |

#### Explore Page

#### Personal Habits Page / User Habit Page

#### Search Page

### Structure / Navigation

When a user users the site URL in the web browser, there is a check_redirect view that is opened by django
this view checks if a user is already logged in and redirects the user to one of the following:

- **/explore** if there are logged in 
- **/landing** if there are not

If a user in not logged in, from the landing page they can use the navigation bar items to access, 

- **/accounts/login/** - login page 
- **/accounts/signup/** - register page
- **/landing/** - landing page

![nav landing not logged in](/documentation/navigation/nav-landing-not-logged-in.png)

When a user does log in they are redirected to their personal habits page, **/\<username>/**
They can now use the navigation bar to access the following pages 

- **/\<username>/** - Personal Habits page
- **/explore/** - Explore other users' habits
- **/landing/** - landing page
- **/accounts/logout/** - logout page

![nav person page](/documentation/navigation/nav-personal.png)

now if the user returns to the landing page they will see that the navigation bar has the items for logged in users 

![nav landing logged in](/documentation/navigation/nav-landing-logged-in.png)


From the **/explore** page a user can also access

- **/\<username>/** - Another User's Habits page. through the username hyperlink on the user habit
- **/search_users/\<term>/>** - The Search Result Page, through using the search bar

The explore, user habit pages and search pages are only accessible to a logged in user, if the user enter the url in the browser and are not logged in 
they will be redirected back to the landing page

### Accessibility

#### User Feedback For Buttons and Navigation

**Navbar Hover and Selected Item**

**Button Hover**

### Defensive Design

**Confirmation Dialogues when performing database operations**

## Deployment

Deployment done through Heruko

## Testing

see full testing in [Testing.md](TESTING.md)

## Future Consideration

These are some features that at some point were considered for this project but due to time constraints where not able to be added

**More Efficient Heatmap Calendar**

Although I am happy with the current implement of the heatmap calendar, ideally I would have tried to make it have a more efferent generation function 
and that the year view would end in the current month instead of going from January to February

## Credits

### Technologies 

- HTML/CSS/JS - Frontend and templates
- Bootstrap - CSS library
- Python, Django - Backend 
- PostgreSQL - Database
- Heroku - Hosting
- Git/Github - Version Control
- django SummerNote - styling django admin panel
- django crispy forms - for handling and creating forms
- Sketch App - Used to create Mockups

### Resources 

- CodeInstitute blog project [repo](https://github.com/Code-Institute-Solutions/blog) and walkthrough used as guidance
- [Bootstrap Docs](https://getbootstrap.com/docs/4.0/)