## Students info:

* Name: Uriah Ballard
   * LinkedIn: ....
   * Role: BE = DB MySQL —> Models
* Name: Darius Washington
   * LinkedIn: ....
   * Role: BE = Routing / Controllers
* Name: Diego Millan
   * LinkedIn: ....
   * Role: FE = HTML / CSS / JS / Bootstrap

* GitHub repo link: Habit Tracker Group Project

### Project Name:

# Habit Tracker
  * Competition based habit tracker. Users will choose between several different habit categories and in the future receive rewards based on the length of their tracking streaks.

# MVP :
### Technology Stack:
  *   Python
  *   MySQL
  *   Flask
  *   CSS/HTML
  *   Javascript
  *   Bootstrap

## Feature list / Page’s:
  * Register [User] Page
  * Login [User] Page
  * Dashboard table’s of each category showing all the habits of all users: filter by most recent
      * Sleep 
      * Steps
      * Gym
  * Create Page for each habit to track:
      * A + button on top of the habit table on the home page.
      * When successful redirect to -> dashboard
  * Nav bar: Dashboard, Create, Account (dropdown with a selection option to logout)
  * A user view page that shows the current logged in user’s info and also their habits tracked: (shown based on logged in user session) User info:
      * (only display) username
      * (to login) email
      * Location
      * password (*****)
  * Habits (an update button at the end of each habit on the table)
      * Sleep
      * Steps
      * Gym
  * A user & habit update page
      * Email
      * Location
      * Username
      * Password (stretch goal)
      * That habits inputs: sleep
       * Hours
       * Quality
       * Time went to sleep
       * Wake up time

## CRUD implementation:
  * Using MySQL for implementations.
  * Data we are using to Create, Read, Update, Delete and for which tables: EXAMPLE:
      * Users:
       * First name
       * Last name
       * Email
       * Location
       * Password
      * Sleep
       * Hours
       * Quality  (1-5 star rating)
       * Sleep_start (going to sleep)
       * Sleep_stop (waking up)
      * Steps
       * Amount (# of steps tracked in session)
       * Location (City, St)
      * Gym
       * Reps  (num)
       * Hours (in gym)
       * Workout start (datetime-local)
       * Workout end (datetime-local)
       * Type Workout (chest, legs, etc) (not implemented)

## MVP CHECKLIST:
- [x] FE logout button & BE functionality for dashboard
- [x] FE update page boilerplate done
- [x] FE create page boilerplate done
  - [x] logout button put on all pages (update and create page added)
- [x] FE dashboard tables show
  - [x] FE all habit data shows in all tables
    - [ ] STRETCH: give a certain height to each table so it can be scrollable and not take up whole page
      - [ ] STRETCH: FE table rows to be clickable themselves to get to the view pages
- [x] BE create validation to make sure user cannot open a url link to any page unless they are signed in (have a session user_id)
- [ ] BE update functionality for each habit
  - [ ] validations for update inputs (they're pre-filled with data, they should be able to put the same data)
- [x] FE create view page
  - [x] all appropriate data for habit selected shows on page
  - [x] FE show delete button on details page
  - [x] BE route delete button to controller to work
- [x] BE create view page (routing shows up based on habit.id and queries based on habit.id as well)
  - [x] href=/habit/view/<habit_type>/{{ habit.id }} --> route
  - [ ] STRETCH: only show EDIT for users that own that habit (with jinja2)
  - [ ] STRETCH: only show DELETE for users that own that habit (with jinja2)
  - [ ] MVP: only let users that own that habit be able to DELETE THAT HABIT THROUGH THE URL
    - [ ] validations?
- [x] BE delete functionality ROUTE for each habit
- [x] BE delete functionality MODELS for each habit
  - [ ] add validations?
  - [ ] check logged in user for increased route security?
- [x] BE join queries tests to show data on html pages
- [ ] FE account page (including all habits from that user)
  - [ ] BE query to bring all habits of one user
- [ ] STRETCH: FE password reset pop message on reset button on account page (we have sent an message to your email detailing how to reset your password at [user's email])
  - [ ] STRETCH: BE query to fulfill showing all user data from current logged on user.
- [ ] STRETCH: BE update functionality for user data

## Product Backlog / Stretch Goal Features:
  * API’s:
      * [Any future API’s we might wanna use after MVP is done]
      * Maybe GitHub’s for the daily history squares
      * Maybe an API from  whoop band or my fitness pal app for history tracking visuals
  * Competition based rank system
  * Add profile photo to User name
  * API implementation
  * Rewards(logging for a week, month etc)
  * History for each user each habit(Graph)(maybe use an API or library for this)
  * Update password
  DiegoM
  * The create forms page still has input data even if validation flashes appear so the user doesn’t have to re-enter all their inputs again to create.
  
  * The create forms page still has input data even if validation flashes appear so the user doesn’t have to re-enter all their inputs again to create.
  main
