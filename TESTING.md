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

- **AC1** -> User can follow another user
- **AC2** -> If user is following another user they can unfollow them
- **AC3** -> User can see the following status

## Search Users

- **AC1** -> User can enter a search term and get a list of user's whose username match the term

# Full Testing 

Below is a table of the all the testing done on the web app. The testing table is built base on the acceptance criteria in the User Requirements list and also
on accessibility, UI/UX and database functionality defined for this project. The test were performed on Safari and Chrome Browsers on a Macbook, also on safari on an Iphone

| Feature | Test Case | Acceptance Criteria | Testing Method | Status |
|---------|------------|---------------------|----------------|--------|
| Account Registration | User can sign up with email, username, and password | Users can sign up with email, username, and password | Manual testing by filling out the registration form and submitting | Pass |
| Account Registration | User cannot register with an existing email | Users cannot register with an email that is already in use | Attempt to register with an existing email and check for error message | |
| Account Registration | User cannot register with an existing username | Users cannot register with a username that is already in use | Attempt to register with an existing username and check for error message | Pass |
| Account Registration | Password meets security requirements | Password must be at least 8 characters long and include a mix of letters, numbers, and special characters | Attempt to register with various passwords and check for validation messages | Pass |
| Structure / Navigation | User is redirected to /explore if logged in | Users are redirected to /explore if logged in | Log in and navigate to the site URL, check if redirected to /explore | Pass |
| Structure / Navigation | User is redirected to /landing if not logged in | Users are redirected to /landing if not logged in | Navigate to the site URL without logging in, check if redirected to /landing | Pass |
| Structure / Navigation | User can access login page from landing page | Users can access login page from landing page | Click the login link on the landing page and check if redirected to /accounts/login/ | Pass |
| Structure / Navigation | User can access register page from landing page | Users can access register page from landing page | Click the register link on the landing page and check if redirected to /accounts/signup/ | Pass |
| Structure / Navigation | User can access landing page from landing page | Users can access landing page from landing page | Click the landing link on the landing page and check if redirected to /landing | Pass |
| Structure / Navigation | User is redirected to personal habits page after login | Users are redirected to personal habits page after login | Log in and check if redirected to /<username>/ | Pass |
| Structure / Navigation | User can access personal habits page from navigation bar | Users can access personal habits page from navigation bar | Click the personal habits link in the navigation bar and check if redirected to /<username>/ | Pass |
| Structure / Navigation | User can access explore page from navigation bar | Users can access explore page from navigation bar | Click the explore link in the navigation bar and check if redirected to /explore/ | Pass |
| Structure / Navigation | User can access landing page from navigation bar | Users can access landing page from navigation bar | Click the landing link in the navigation bar and check if redirected to /landing | Pass |
| Structure / Navigation | User can log out from navigation bar | Users can log out from navigation bar | Click the logout link in the navigation bar and check if redirected to /accounts/logout/ | Pass |
| Structure / Navigation | Navigation bar updates for logged in users on landing page | Navigation bar updates for logged in users on landing page | Log in, navigate to the landing page, and check if navigation bar shows logged in items | |
| Structure / Navigation | User can access another user's habits page from explore page | Users can access another user's habits page from explore page | Click a username link on the explore page and check if redirected to /<username>/ | Pass |
| Structure / Navigation | User can access search results page from explore page | Users can access search results page from explore page | Use the search bar on the explore page and check if redirected to /search_users/<term>/ | Pass |
| Structure / Navigation | Non-logged in user is redirected to landing page when accessing restricted pages | Non-logged in users are redirected to landing page when accessing restricted pages | Attempt to access /explore, /<username>/, or /search_users/<term>/ without logging in and check if redirected to /landing | Pass |
| Create a Daily Habit | Form appears when clicking the "Create New Habit" button | The form to create a new habit appears when clicking the "Create New Habit" button | Click the "Create New Habit" button and check if the form appears | Pass |
| Create a Daily Habit | Form disappears when clicking the "Cancel" button | The form to create a new habit disappears when clicking the "Cancel" button | Click the "Cancel" button and check if the form disappears | Pass |
| Create a Daily Habit | Page redirects when clicking the "Submit" button | The page redirects to the habit list when clicking the "Submit" button | Fill out the form, click "Submit", and check if the page redirects to the habit list | Pass |
| Create a Daily Habit | User can add a new habit with title, description, and color | Users can add a new habit with title, description, and color | Fill out the habit creation form and submit | Pass |
| Create a Daily Habit | User can set habit visibility (private, public, followers only) | Users can set habit visibility to private, public, or followers only | Select different visibility options and save the habit | Pass |
| Create a Daily Habit | User receives confirmation message after creating a habit | Users receive a confirmation message after creating a habit | Create a habit and check for confirmation message | Pass |
| Create a Daily Habit | Habit appears in user's habit list upon creation | Created habit appears in the user's habit list | Create a habit and check the habit list | Pass |
| Display Habit Data | User can see all check-ins visualized in habit elements | Users can see all check-ins visualized in habit elements | Check the habit elements for visualized check-ins | Pass |
| Display Habit Data | User can see the total number of check-ins for a habit | Users can see the total number of check-ins for a habit | Check the habit elements for total check-ins count | Pass |
| Display Habit Data | User can see the number of check-ins today for a habit | Users can see the number of check-ins today for a habit | Check the habit elements for today's check-ins count | Pass |
| Display Habit Data | User can see the list of dates checked in for a habit | Users can see the list of dates checked in for a habit | Check the habit elements for the list of check-in dates | Pass |
| Display Habit Data | User can see the current streak of consecutive check-in days | Users can see the current streak of consecutive check-in days | Check the habit elements for the current streak count | Pass |
| Display Habit Data | User can see the amount of each reaction to a habit | Users can see the amount of each reaction to a habit | Check the habit elements for reaction counts | Pass |
| Modify or Delete a Habit | Form appears when clicking the "Edit" button | The form to edit a habit appears when clicking the "Edit" button | Click the "Edit" button and check if the form appears | Pass |
| Modify or Delete a Habit | Form is filled with correct information when editing | The form is pre-filled with the habit's current information when editing | Click the "Edit" button and check if the form is pre-filled with the correct information | Pass |
| Modify or Delete a Habit | Form disappears when clicking the "Cancel" button | The form to edit a habit disappears when clicking the "Cancel" button | Click the "Cancel" button and check if the form disappears | Pass |
| Modify or Delete a Habit | User can update habit title, description, and color | Users can update habit title, description, and color | Edit an existing habit and save changes | Pass |
| Modify or Delete a Habit | User can change habit visibility | Users can change habit visibility | Edit an existing habit and change visibility | Pass |
| Modify or Delete a Habit | User receives confirmation prompt before submitting edited habit | Users receive a confirmation prompt before submitting edited habit | Edit a habit and check for confirmation prompt before saving | Pass |
| Modify or Delete a Habit | User can delete a habit | Users can delete a habit | Delete an existing habit and confirm deletion | Pass |
| Modify or Delete a Habit | User receives confirmation prompt before deleting a habit | Users receive a confirmation prompt before deleting a habit | Attempt to delete a habit and check for confirmation prompt | Pass |
| Modify or Delete a Habit | User receives confirmation message after deleting or editing a habit | Users receive a confirmation message after deleting or editing a habit | Edit or delete a habit and check for confirmation message | Pass |
| React to Another User's Habit | User can choose from a list of reactions to send to another user's habit | Users can choose from a list of reactions to send to another user's habit | Select a reaction and send it to another user's habit | Pass |
| React to Another User's Habit | User receives confirmation message after reaction is sent | Users receive a confirmation message after reaction is sent | Send a reaction and check for confirmation message | Pass |
| React to Another User's Habit | User receives notification when someone reacts to their habit | Users receive a notification when someone reacts to their habit | React to a habit and check for notification | Pass |
| React to Another User's Habit | User can see a count of each reaction type on a habit | Users can see a count of each reaction type on a habit | Check the habit for reaction counts | Pass |
| View Calendar Heatmap of Habit | User can view a heatmap showing habit completion over time | Users can view a heatmap showing habit completion over time | Navigate to the heatmap view and check for habit completion data | Pass |
| View Calendar Heatmap of Habit | Days where habit was completed are visually highlighted | Days where habit was completed are visually highlighted | Check the heatmap for highlighted days | Pass |
| View Calendar Heatmap of Habit | User can switch between different timeframes (weekly, monthly, yearly) | Users can switch between different timeframes (weekly, monthly, yearly) | Switch between timeframes and check the heatmap | Pass |
| Manage Habits and Landing Page as Admin | Admin can view a list of all user habits | Admins can view a list of all user habits | Log in as admin and check the list of user habits | Pass |
| Manage Habits and Landing Page as Admin | Admin can filter habits by user, status, or creation date | Admins can filter habits by user, status, or creation date | Apply filters and check the filtered list | Pass |
| Manage Habits and Landing Page as Admin | Admin can delete habits that violate site policies | Admins can delete habits that violate site policies | Delete a habit as admin and confirm deletion | Pass |
| Manage Habits and Landing Page as Admin | Admin can remove users that violate site policies | Admins can remove users that violate site policies | Remove a user as admin and confirm removal | Pass |
| Manage Habits and Landing Page as Admin | Admin can edit landing page information | Admins can edit landing page information | Edit the landing page as admin and save changes | Pass |
| View Landing Page | User can see an overview of the app’s purpose and features | Users can see an overview of the app’s purpose and features | Navigate to the landing page and check for overview | Pass |
| View Landing Page | Landing page includes a call-to-action | The landing page includes a call-to-action | Check the landing page for call-to-action | Pass |
| View Landing Page | Landing page is mobile-friendly and accessible | The landing page is mobile-friendly and accessible | Test the landing page on mobile devices and check for accessibility | Pass |
| View Paginated List of Habits | Multiple habits are listed when more than one habit exists | Given more than one habit, multiple habits are listed | Check the list of habits when more than one habit exists | Pass |
| View Paginated List of Habits | User can see the list of habits in the explore tab | When user opens the explore tab, they can see the list of habits | Open the social tab and check for habit list | Pass |
| View Paginated List of Habits | User sees habit title, progression data, and associated user | The user sees habit title, data about the progression, and the user associated | Check the habit list for title, progression data, and associated user | Pass |
| View Paginated List of Habits | User can only see public habits or habits from followed accounts | The user can only see public habits or habits from followed accounts | Check the habit list for visibility restrictions, , follow and unfollow users to see if more habits appear | Pass |
| Follow/Unfollow User | User can follow another user | Users can follow another user | Follow a user and check the following status tag | Pass |
| Follow/Unfollow User | User can unfollow another user | Users can unfollow another user | Unfollow a user and check the following status tag | Pass |
| Search Users | User can search for other users by username | Users can search for other users by username | Perform a search and check the results | Pass |
| Search Users | User can follow users from the search results | Users can follow users from the search results | Follow a user from the search results and check the following list | Pass |
| Search Users | User can unfollow users from the search results | Users can unfollow users from the search results | Unfollow a user from the search results and check the following list | Pass |
| Accessibility | All pages are accessible according to WCAG 2.1 guidelines | All pages meet WCAG 2.1 accessibility guidelines | Use accessibility tools to check compliance | |
| UI/UX | All pages have a consistent and user-friendly design | All pages have a consistent and user-friendly design | Perform a UI/UX review and gather user feedback | |

# Automated Testing

## HTML Validation 

### Landing Page

### Login Page

### Logout Page

### Register Page

### Explore Page

### Personal Page

### User Habit Page

### Search User Page

## CSS Validation 

this is for the [style.css](/static/css/style.css) file

## Accessibility Tests

### Landing Page

### Login Page

### Logout Page

### Register Page

### Explore Page

### Personal Page

### User Habit Page

### Search User Page

## Lighthouse Tests

### Landing Page

### Login Page

### Logout Page

### Register Page

### Explore Page

### Personal Page

### User Habit Page

### Search User Page
