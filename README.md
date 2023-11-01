# My Books Store - Online Book shop

![Home page](media/multi-device.png)

## TABLE OF CONTENTS

- [Overview](#overview)
- [Strategy](#strategy)
- [Colour Scheme](#colour-scheme)
- [User Experience UX](#user-experience-ux)

# Overview

My Books Store is an E-commerce website created for a fictive books shop located in Schelklingen, Germany. The main purpose of the project was to implement a fully functional online store that will make the process of selecting and purchasing books products much easier for customers.
The users are given the possibility to see every product's detail, create a Wishlist, add items to the shopping bag, purchase with online payment method and access order history. 
The website was developed using Python (Django), HTML, CSS and JavaScript. The data was stored in a PostgreSQL database using ElephantSql for manipulation.

### Strategy

    My books store is a e-commerce business. Due to pressure of life from work and family,
    people have opted for online shopping.

### Colour Scheme

    The colour scheme eventually chosen is one based on a yellow, black and white.
    This colour scheme gives off a earthly, warm and happy feeling to the website.

## Deployment

### Deploy on Heroku

1.  Create Pipfile

In the terminal enter the command ` pip3 freeze > requirements.txt`, and a file with all the requirements will be created.

2. Setting up Heroku

    - Go to the Heroku website (https://www.heroku.com/)
    - Login to Heroku and choose _Create App_
    - Click _New_ and _Create a new app_
    - Choose a name and select your location
    - Go to the _Resources_ tab
    - From the Resources list select _Heroku Postgres_
    - Navigate to the _Deploy_ tab
    - Click on _Connect to Github_ and search for your repository
    - Navigate to the _Settings_ tab
    - Reveal Config Vars and add your Cloudinary, Database URL (from Heroku-Postgres) and Secret key.

3. Deployment on Heroku

    - Go to the Deploy tab.
    - Choose the main branch for deploying and enable automatic deployment
    - Select manual deploy for building the App

### Fork the repository

For creating a copy of the repository on your account and change it without affecting the original project, use<b>Fork</b> directly from GitHub:

-   On [My Repository Page](https://github.com/useriasminna/italianissimo-booking-website), press <i>Fork</i> in the top right of the page
-   A forked version of my project will appear in your repository<br></br>

### Clone the repository

For creating a clone of the repository on your local machine, use<b>Clone</b>:

-   On [My Repository Page](https://github.com/useriasminna/italianissimo-booking-website), click the <i>Code</i> green button, right above the code window
-   Chose from <i>HTTPS, SSH and GitClub CLI</i> format and copy (preferably <i>HTTPS</i>)
-   In your <i>IDE</i> open <i>Git Bash</i>
-   Enter the command <code>git clone</code> followed by the copied URL
-   Your clone was created
<hr>
