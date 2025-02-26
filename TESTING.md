# User Requirements

## Account registration

### Acceptance Criteria  

- **AC1** -> Users can sign up using an email, username and password.    
- **AC2** -> Users cannot register with an already existing email.  
- **AC3** -> Users cannot register with an already existing username.  
- **AC4** -> User must provide a valid password that meets the security requirements

## Create a daily habit 

### Acceptance Criteria  

- **AC1** -> Users can add a new habit with a title and optional description and color.  
- **AC2** -> Users can set a visibility for the habit (private, public, followers only).  
- **AC3** -> Users receive a confirmation message after successfully creating a habit.  
- **AC4** -> The habit appears in the user's habit list upon creation.  

## Modify or Delete a habit

### Acceptance Criteria  

- **AC1** → Users can update the habit title, description and color  
- **AC2** → Users can change the visibility of an existing habit.  
- **AC3** → Users receive a confirmation prompt before submitting an edited habit.  
- **AC4** → Users can delete a habit, which removes it from their habit list.  
- **AC5** → Users receive a confirmation prompt before deleting a habit.  
- **AC5** → Users receive a confirmation message after deleting or editing a habit.  

## React to another user's habit

### Acceptance Criteria  

- **AC1** -> Users can choose from a list of reaction to send to another user's habit.  
- **AC2** -> Users receive a confirmation message after the reaction is sent
- **AC2** -> Users receive a notification when someone reacts to their habit.  
- **AC3** -> Users can see a count of each reaction type on a habit.    

## View Calendar Heatmap of Habit

### Acceptance Criteria  

- **AC1** → Users can view a heatmap showing habit completion over time.  
- **AC2** → Days where the habit was completed are visually highlighted and the check-in amount for that day is reflected in the color.  
- **AC3** → Users can switch between different timeframes (e.g., weekly, monthly, yearly).  
- **AC4** → Users can click on a day to see detailed habit completion data.  

## Manage Habits and Landing Page information as Site Admin

### Acceptance Criteria  

- **AC1** -> Admins can view a list of all user habits.  
- **AC2** -> Admins can filter habits by user, status, or creation date.  
- **AC3** -> Admins can delete habits that violate site policies.  
- **AC4** -> Admins can remove users that violate site policies
- **AC5** -> Admin can edit landing page information  

## View a landing page that gives information about the about app and its features

### Acceptance Criteria  

- **AC1** → Users can see an overview of the app’s purpose and features.  
- **AC2** → The landing page includes a call-to-action.    
- **AC3** → The landing page is mobile-friendly and accessible.  

### View a paginated list of habits

#### Acceptance Criteria

- **AC1** -> given more than one habit the multiple habits are listed
- **AC2** -> when user open the social tab they can see the list of habits
- **AC3** -> the user see habit title, data about the progression and the user associated 
- **AC4** -> the user can only see public habits or habits from followed accounts

## Follow/Unfollow User

## Search Users

# Full Testing 

Below is a table of the all the testing done on the web app. The testing table is built base on the acceptance criteria in the User Requirements list and also
on accessibility, UI/UX and database functionality defined for this project

# Automated Testing

## HTML Validation 

## CSS Validation 

## Accessibility Tests

## Lighthouse Tests