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

### Django Structure

- root
    - dailys project
    - habit-tracker app
        - templates
    - landing
        - templates
    - templates
    

### Database design

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

### Structure / Navigation

### Accessibility

## Deployment

Deployment done through Heruko

## Testing

see full testing in [Testing.md](TESTING.md)

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

### Resources 

- CodeInstitute blog project [repo](https://github.com/Code-Institute-Solutions/blog) and walkthrough used as guidance
- [Bootstrap Docs](https://getbootstrap.com/docs/4.0/)