# House of Masala | Recipe Book for Pakistani Cuisine

## Index:
* <a href="#project-background">Project Background :information_desk_person:</a> 
* <a href="#ux">UX :iphone:</a> 
* <a href="#features">Features :clipboard:</a>
* <a href="#technologies">Technologies Used :wrench:</a>
* <a href="#testing">Testing :flashlight:</a>
* <a href="#deployment">Deployment :rocket:</a>
* <a href="#credits">Credits :pencil2:</a>

---
<span id="project-background"></span>
## Project Background :information_desk_person:

This is the website for House of Masala - a recipe book for Pakistani dishes. It targets anybody looking for Pakistani dishes to create at home. Through an interactive & responsive design with data-driven functionalities, users are able to view a variety of recipes, create new recipes, store them on the site to share with others & edit or delete them.

---

<span id="ux"></span>
## UX :iphone:

### 1. Who is this website for?

This website can be used by Pakistanis and non-Pakistanis interested in learning more about or cooking Pakistani food. By allowing users to create recipes, it also targets those who desire to store their recipes in one place to share with others.

### 2. First-Time User Goals:

* As a First Time Visitor, I want to easily understand the main purpose of the site and who the company is.
* As a First Time Visitor, I want to be able to easily navigate throughout the site to find content most relevant to me.
* As a First Time Visitor, I want to be able to register my profile.
* As a First Time Visitor, I want to be able to access my profile.
* As a First Time Visitor, I want to be able to gather key information about each recipe to be able to create the desired recipe at home.
* As a First Time Visitor, I want to be able to add a new recipe with ease.
* As a First Time Visitor, I want to be able to access, edit or delete my created recipe.
* As a First Time Visitor, I want to be able to visit their social media pages to determine how big a following the company has & how trusted it is.

### 3. Returning Visitor Goals

* As a Returning Visitor, I want to be able to log in to my profile with the credentials that were registered.
* As a Returning Visitor, I want to be able to log out of my profile.
* As a Returning Visitor, I want to be able to get a variety of new recipe options.
* As a Returning Visitor, I want to be able to see and access my added recipes.
* As a Returning Visitor, I want to be able to access my profile.
* As a Returning Visitor, I want to be able to edit or delete my added recipes.
* As a Returning Visitor, I want to be able to to get in touch with the company with any questions or suggestions I may have.

### 4. Frequent User Goals 

* As a Frequent Visitor, I want to check to see if there are any newly added recipes that have been created on the website that I can cook. 
* As a Frequent Visitor, I want to be able to log in & log out of my profile with ease. 

### Design:

I opted for a clean and fresh look & feel for this website. The background is kept white to allow for the imagery of the food to stand out, while the bright green buttons add a nice pop of color to break up the whitespace without being too distracting for the user. 

* Color Scheme:
   * The main colors used are 2 shades of Green, Dark Grey, and White. 

* Typography:
   * All Headers use Open Sans & Helvetica Neue. These are both sans-serif font with nice letter-spacing - which makes it easy-to-read & clean.
   * Arial is my secondary font, used for paragraphs. It has a lighter font-weight, which pairs nicely with other sans-serif fonts and is easy to read on smaller devices.
   * Sans-Serif is used as the backup font for both Open Sans, Helvetica Neue & Arial.

* Imagery:
   * A bright, colorful image showing popular Pakistani dishes is used for the hero image to be eye-catching & inviting to the user. In general, Pakistani food consists of different shades of brown, yellows, reds and greens and I wanted the user to get a sense of this right off the bat. Images for the recipes are also bright & vibrant, allowing the food to speak for itself.

### Wireframes & Mockups:

* View website wireframes for desktop [here](https://drive.google.com/file/d/15ZmioN0w8vPz3TuhpdIQcyuUIX5oD5v9/view?usp=sharing)
* View website wireframes for mobile [here](https://drive.google.com/file/d/1Svbf2IyMygzqkQPFNg-TqXWZ9xfA7PxV/view?usp=sharing) 
 
---

<span id="features"></span>
## Features :clipboard:

The site contains certain features which are not visible or available to unregistered/logged in users. These features include the ability to add a recipe, edit it, store it, and delete it (CRUD operations). Content available to all users includes the ability to view all recipes including the 3 most recently added.

### Features visible to All Users:
* **All Recipes:** 
    * * The All Recipes page contains an assortment of recipes added by House of Masala, as well as the users of the website. Each recipe card displays an image of the dish, the name, short description prep time, yield, and a CTA button to view the recipe. The creator of the recipe is also visible. 
* **Register**
	* The register feature is one visible to all users as a link on the navigation bar. Once clicked, it leads to a form where users can create a unique username and password. If the username is already taken, a message saying “Username already exists” will flash at the top of the page. Once the user has registered successfully, they will be redirected to the homepage. A success message also flashes at the top of the page signalling a successful registration.
* **Login** 
    * The login feature is also visible to all users and can be found in the navigation bar. It enables users who already have a profile to login with their credentials. If the credentials don't match those entered during registration, an error message “Incorrect Username and/or Password” will flash across the screen. For users who have not registered yet, a CTA link at the bottom of the form directs them to register. Alternatively, if the login is successful and the username & password match those stored in the database, a welcome message will flash & the user will be redirected to the profile page. 
* **Recently Added Recipes**
	* The three most recently added recipes are also visible to all users on the homepage. This section retrieves the newest recipes from the database in descending order. A CTA link at the bottom of the section leads users to the All Recipes page to view all the recipes.
* **Footer**
    * Located at the bottom of each page of the website, the footer consists of a contact us section with an email address, a short about section, and social media links leading to Pakistani food accounts intended to give users more food inspiration & recipe choices.
* **Navbar**
	* The navigation bar at the top of each page of the website enables the user to easily access all pages of the website. On smaller devices, the navbar transforms into a burger menu, where links are only visible in a dropdown menu. There are two different views of the navigation bar - one view to all users, and the other to those users who are logged in to the website. 

### Features visible to Logged In/Registered Users:
* **Profile** 
* **Add A Recipe**
* **Logout** 
* **Edit Recipe**
* **Delete Recipe**


### Features to implement in the Future

* Functionality to let users like or save recipes they’d like to make later 
* A warning dialog box that adds an extra step before a user deletes a recipe 
* Function to allow user to drag & drop an image instead of having to copy paste the img url

---
<span id="technologies"></span>
## Technologies Used :wrench:

### 1. Languages

This User Centric Frontend Project focused on the use of the following languages:
* HTML5 - for website structure 
* CSS3 - for styling 
* JavaScript - for running interactive features 
* Python for automating tasks & scripting, including:
    * Flask 
    * Flask pymongo
    * Jinja templating
    * BSON
    * Werkzeug
    * Dnspython

### 2. Other Programs & Frameworks Used 

* FontAwesome - for all icons used on the buttons
* Balsamiq - for creating wireframes 
* Bootstrap 4.4.1 - for assisting in responsiveness and layout of website 
* Startup Bootstrap - for website theme 
* MongoDB - database for storing user info & recipes 

### 3. IDE's 

This website was developed on GitPod.

### 4. External Hosting

This website is saved in a repository on GitHub.

---
