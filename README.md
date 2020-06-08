

# Pitch_Blog

#### 05/06/2020
#### By **Jorim Midumbi Okong'o Opondo**

## Description
This  is a flask application that allows users to post one minute pitches and also allows other users who have signed up to comment and upvote or downvote a pitch. A user must signup to be able to access the functionalities of the application.

You can view the site at:[Heroku](https://jorim-pitch.herokuapp.com/)

## User Stories
These are the behaviours/features that the application implements depending on the selection made by a user.

* As a user, I would like to see the pitches other people have posted.
* As a user, I would like to vote on the pitch they liked and give it a downvote or upvote.
* As a user, I would like to be signed in for me to leave a comment
* As a user, I would like to receive a welcoming email once I sign up.
* As a user, I would like to view the pitches I have created in my profile page.
* As a user, I would like to comment on the different pitches and leave feedback.
* As a user, I would like to submit a pitch in any category.
* As a user, I would like to view the different categories.

## Specifications

| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Load the page | **On page load** | Get all posts, Select between signup and login|
| Select SignUp| **Email**,**Username**,**Password** | Redirect to login|
| Select Login | **Username** and **password** | Redirect to page with app pitches based on categories and commenting section|
| Select comment button | **Comment** | Form that you input your comment|
| Click on submit |  | Redirect to all comments template with your comment and other comments|


## Development Installation

To get the code..

1. Cloning the repository:
  ```bash
  https://github.com/JORIM1981/Pitch_Blog.git
    ```
2. Move to the folder and install requirements
  ```bash
  cd pitch_blog
  pip install -r requirements.txt
  ```
3. Exporting Configurations
  ```bash
  export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
  ```
4. Running the application
  ```bash
  python3.8 manage.py server
  ```
5. Testing the application
  ```bash
  python3.8 manage.py test
  ```
Open the application on your browser `127.0.0.1:5000`.


## Technology used

* [Python3.8](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Heroku](https://heroku.com)


## Known Bugs
* There are no known bugs currently but pull requests are allowed incase you spot a bug

## Contact Information 

If you have any question or contributions, please email me at [okongo.midumbi.opondo@gmail.com]

## License:

- _MIT License:_[LICENSE MIT](./LICENSE)

- Copyright (c) 2020 **Jorim Midumbi Okongo Opondo**


