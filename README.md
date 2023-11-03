<h1>My Books Store - Online Book shop</h1>

![Home page](media/multi-device.png) 

## [TABLE OF CONTENTS](#table-of-contents)<!-- omit in toc -->

- [Overview](#overview)
- [User Experience (UX)](#user-experience-ux)
  - [Project goals](#project-goals)
  - [Project Objectives:](#project-objectives)
- [User Stories](#user-stories)
    - [Strategy](#strategy)
    - [Scope](#scope)
    - [Structure](#structure)
    - [Skeleton](#skeleton)
    - [Surface](#surface)
- [Agile Methodology](#agile-methodology)
- [Testing](#testing)
- [Deployment](#deployment)
  - [Deploy on Heroku](#deploy-on-heroku)
  - [Fork the repository](#fork-the-repository)
  - [Clone the repository](#clone-the-repository)
- [Credits](#credits)
  - [Code](#code)
  - [Media](#media)
  - [Acknowledgements](#acknowledgements)


## Overview

My Books Store is an E-commerce website created for a fictive books shop located in Schelklingen, Germany. The main purpose of the project was to implement a fully functional online store that will make the process of selecting and purchasing books products much easier for customers.
The users are given the possibility to see every product's detail, create a Wishlist, add items to the shopping bag, purchase with online payment method and access order history.
The website was developed using Python (Django), HTML, CSS and JavaScript. The data was stored in a PostgreSQL database using ElephantSql for manipulation.


## User Experience (UX)

### Project goals

- To create an e-commerce application - My Books Store that is used for ordering Books by customers.

### Project Objectives:

- To create a website with a simple and intuitive User Experience;
- To add content that is relevant and helps create a better image of the books shop.
- To differentiate between client and staff member accounts.
- To implement fully functional features that will ease upgrade clients' experience with the books store services.
- To make the website available and functional on every device.

## User Stories

#### Strategy
<hr>

- As a website user, I can:

1. Navigate around the site and easily view the desired content.
2. View a list of products and choose accordingly.
3. Search products to find a specific product.
4. Click on a product to read and view the details.
5. Register for an account.


- As a logged in website user, I can:

1. make wishlist products page in which I can edit or/and buy books at any time
2. Subscribe to a newsletter, so I can always be up to date with the latest promotions
3. Save my data under my personal profile.
4. Manage my profile by updating my details.
6. Logout of the website.
7. Using my personal profile, buy a product by using the website checkout system.

- As a website Superuser, I can:

1. Create and publish a new product.
2. Create a new user, products, and categories.
3. Delete user, products, categories and Ratings.
4. Change a user’s permissions on the website
5. Upload new banners to be displayed on the website.


#### Scope
<hr>

<h4> Simple and intuitive User Experience</h4>
- Ensure the navigation menu is visible and functional at every step;
- Ensure every page has a suggestive name that fits its content;
- Ensure the users will get visual feedback when navigating through pages;
- Create a design that matches the requirements of an e-commerce website.

<h4> Relevant content</h4>
- Add a representative cover image;
- Add the website title and details about its purpose;
- Add a section that includes information about the shop's name, description, location and contact data;
- Make a clear and beautiful designed presentation of the menu elements;

<h4> Features for upgraded experience</h4>
- Create a list with all the products and group them by category;
- Create a Bag feature that allows the user to add, update and remove products from the shopping bag;
- Create a Wishlist feature that gives the user the possibility to add and remove items from the wishlist;
- Create a Checkout feature for giving the user the possibility to complete an order on the website;
- Create a Profile page for the user to add/update his delivery details and see his orders' history;
- Create a Newsletter feature that allows the user to subscribe with his email;
- Create a page for the staff members to manage all the orders for all the users;
- Create a feature for the staff members to add/edit products on the website;

<h4> Different client and staff member Accounts</h4>
- Allow the clients to add/edit reviews and the staff members only the option to read them;
- Give the client permission to add/remove products from wishlist and remove the feature for staff members;
- Only guest and client users to access the shopping bag and its features;
- Only guest and client users can make an order on the website;
- Give permission only for staff members to add/edit products; 
- Allow access to Profile page only for clients users;
- Allow access to Wishlist page only for clients users;
- Allow access to Orders page only for staff member users;

<h4> Responsiveness</h4>
- Create a responsive design for desktop, tablet and mobile devices.<br><br>

#### Structure
<hr>

The structure of the website is divided into multiple pages and the content is displayed depending on authentication and client/admin type of user. <br>
- **Register/Login** pages give the user the possibility to create an account and authenticate for accessing different features.<br>
- **Logout** feature is a modal that helps user exit their current account;<br>
- The **Home** page is visible for both types of users and includes relevant information about the websites' purpose and details about the book store, location and contact;<br>
-The **All products** page displays a list with all the products available for selling;<br>
- The **Books** navigation link gives the user the possibility to access the list of products grouped by category, <b>Action and Adventure</b>, <b>Classics</b>, <b>Comic Book or Graphic Novel</b>, <b>Detective and Mystery</b> <b>Fantasy</b> <b>Historical Fiction</b>, <b>Horror</b>, <b>Literary Fiction</b> and <b>Suspense and Thrillers</b>;<br>
- The **Product details** page displays full specifications for a product. It also includes a feature for updating the shopping bag for users that are not admins. Staff members have access to the feature for editing/removing current product;<br>
- The **Profile** page is available for authenticated users and gives access to personal delivery details and orders' history;<br>
- The **Profile order details** page gives access to the user to full specifications only for orders placed by him.<br>
- The **Wishlist** page contains a list with all the products added by the user and cannot be accessed by guest or admin users;<br>
- The **Bag** page displays all the items added in the shopping bag with associated features;<br>
- The **Checkout page** includes an order summary and a form for personal, delivery and payment details;<br>
- The **Checkout success** page displays full specification for the successful order;<br>
- The **Orders** page gives access only to staff members and displays all the bookings registered.<br>

* FLOWCHARTS<br>
The Flowchart for my program was created using <b>LucidChart</b> and it visually represents how the system works.<br>

#### Skeleton
<hr>

**Wireframes**<br>
The wireframes for mobile and desktop were created with [Balsamiq](https://balsamiq.com/) tool and can be viewed [here]()<br>

**Database**<br>
The project uses the relational database PostgreSQL to store the data. Two diagrams were created to show the relationships between the tables.


<details>
  <summary>Final Schema</summary>
<img src=""><br>
</details><br>

#### Surface
<hr>

<h4>Color Scheme</h4>

## Agile Methodology

This project was developed using the agile methodology. All progress in implementing Epics and User Stories was captured using Trello. Necessary goals and priorities were well defined throughout the project. In addition, labels were used to define the priority of each user story on the Kanban board. As user stories were completed, they were moved from the To Do, Progress, and Done lists in the Trello board.

## Testing
The testing documentation can be found at [TESTING.MD](TESTING.MD)

## Deployment

### Deploy on Heroku
 1. Create Pipfile 
 
 In the terminal enter the command ` pip3 freeze > requirements.txt`, and a file with all the requirements will be created. 
 
 2. Setting up Heroku

    * Go to the Heroku website (https://www.heroku.com/) 
    * Login to Heroku and choose *Create App* 
    * Click *New* and *Create a new app*
    * Choose a name and select your location
    * Go to the *Resources* tab 
    * From the Resources list select *Heroku Postgres*
    * Navigate to the *Deploy* tab
    * Click on *Connect to Github* and search for your repository
    * Navigate to the *Settings* tab
    * Reveal Config Vars and add your Cloudinary, Database URL (from Heroku-Postgres) and Secret key.    

3. Deployment on Heroku

    * Go to the Deploy tab.
    * Choose the main branch for deploying and enable automatic deployment 
    * Select manual deploy for building the App 
    
### Fork the repository
For creating a copy of the repository on your account and change it without affecting the original project, use<b>Fork</b> directly from GitHub:
- On [My Repository Page](https://github.com/useriasminna/italianissimo-booking-website), press <i>Fork</i> in the top right of the page
- A forked version of my project will appear in your repository<br></br>

### Clone the repository
For creating a clone of the repository on your local machine, use<b>Clone</b>:
- On [My Repository Page](https://github.com/useriasminna/italianissimo-booking-website), click the <i>Code</i> green button, right above the code window
- Chose from <i>HTTPS, SSH and GitClub CLI</i> format and copy (preferably <i>HTTPS</i>)
- In your <i>IDE</i> open <i>Git Bash</i>
- Enter the command <code>git clone</code> followed by the copied URL
- Your clone was created
<hr>

## Credits

- The texts and images that are used for testimonials were taken from google.

### Code

- [Django Documenation](https://www.djangoproject.com/) was used to provide examples of code solutions and Django functionality.
- [Bootstrap Documenation](https://getbootstrap.com/) was used to provide examples of Bootstrap functionality and building blocks.
- [Code Institute walkthrough](https://codeinstitute.net/) as inspiration and code examples, the code institute walkthroughs "Hello Django" and "I Think Therefore I Blog" was used.
- [newsletter reference](https://www.youtube.com/watch?v=hWtlskOaFNI)
- The wiggle animation was taken and adapted from [codepen](https://codepen.io/beben-koben/pen/PZYjwX)

### Media

- Most of the pictures for the project was taken from [Pexels] (https://www.pexels.com/) and [Pixabay] (https://pixabay.com)
- All products images used on the site were taken from [Google](https://www.google.com/)


### Acknowledgements

- The tutor support team at Code Institute for their support.
- My Code Institute Mentor for feedback and suggestions.
- The Code Institute Slack community.

[Back to top](#table-of-contents)