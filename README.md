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
    * When a user logs into their account, they are redirected to the Profile page, which is specific to that individual user. Upon entry, the user is greeted with a Welcome user message. On this page the user can see his/her added recipes (if any). If they have added a recipe, they will also see an edit & delete button on the recipe cards, where they can make changed to, or delete their recipe. These buttons are only visible to the user on the recipes added by that user.
* **Add A Recipe**
    * This feature is only visible to registered & logged in users, giving them the option to add their own recipe. Once clicked, a form appears with several input fields to fill out. Once they’ve filled in all the fields, a success message flashes on the top of the screen & the user is redirected to All Recipes, where their newly added recipe is displayed. The user will not be able to submit the form until they’ve filled in all the input fields with the specified number of characters. These specifications were put in place to avoid an incomplete recipe from being uploaded to the website.
* **Logout** 
	* The logout link is only visible to users who are logged in to the website. Located in the top navbar, it provides users to easily log out of their session
* **Edit Recipe**
	* The Edit Recipe functionality can be accessed via the user’s profile page. Here the user can view all their added recipes displayed on cards. The edit feature labelled as “Edit” appears as an orange button on the card. Once clicked, it leads to a populated form where the user can either make a change & be redirected to the recipes page, or click on cancel & remain on the profile page. If they decide to update the form & submit their changes, a flash message appears at the top of the screen letting them know their change was successful. 
* **Delete Recipe**
	* The “Delete” button can be accessed via the user’s profile page and is located on their added recipe cards. It is only visible to users who are logged in, allowing them to delete their own recipe.


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

<span id="testing"></span>
## Testing :flashlight:

### 1. Testing Tools

* [The W3C Markup Validation Service](https://validator.w3.org/) - for testing my HTML code
   * Result: No errors
* [The W3C CSS Validation Service: W3 Jigsaw](https://jigsaw.w3.org/css-validator/) - for testing my CSS code
   * Result: "Congratulations! No Error Found."
* Chrome Dev Tools - for testing:
   * Mobile responsiveness
   * CSS styling changes before implementing it in the code
   * Network to assess whether it was picking up Javascript (status: 200)

### 2. Testing User Stories (UX Section)

### A. First-Time Visitor Goals:

* As a First Time Visitor, I want to easily understand the main purpose of the site and who the company is.
   * Upon entering the site, users are presented with a bright, catchy and easily readable banner image, which introduces the Company name and purpose of the site. Underneath, a introductory text follows with more context about occasions people can select from & CTA to click one of the selections below.
   * In the footer, a short about us blurb gives the user further details about the company.

* As a First Time Visitor, I want to be able to easily navigate through the site to find content most relevant to me.
   * The website is designed to be very clean and straight to the point. The goal being to allow users to find the spot that most fits their occasion, without being distracted by irrelevant content.

* As a First Time Visitor, I want to be able to gather key information about each recommended location to be able to make an informed decision.
   * After selecting a marker on the map, users are presented with a very descriptive infoWindow, displaying information about the bar or restaurant, the address, and opening times. An image adds a nice visual of either the food or atmosphere of each spot.

* As a First Time Visitor, I want to be able to know where the restaurant/bar recommended to me is located.
   * Each recommended location populates the interactive Google Maps, allowing the user to see on the map where it is located.
   * When the user clicks on a marker, they can also see the address of the place on the infoWindow.

* As a First Time Visitor, I want to be able to filter the information most interesting to me.
   * When a user clicks on a specific button, it will filter the map markers based on the occasion type. For example, if a user is looking for places to go to on their own - he/she clicks "Alone Again, Naturally" and is shown recommended locations perfect for going to alone.
   * If a user wants to see all locations again, they have the option to click "All Locations" and the map will be repopulated with all the markers.

* As a First Time Visitor, I want to be able to visit their social media pages to determine how big a following the company has & how trusted it is.
   * In the footer, social media icons lead to the company's social media pages, as well as Tripadvisor.

### B. Returning Visitor Goals

* As a Returning Visitor, I want to be able to get a variety of options available for the occasion I select.
   * Each occasion is linked to 5 different recommended locations. In total, the map is populated with 30 different spots, giving the user a lot of variety to choose from.

* As a Returning Visitor, I want to find the best way to get in touch with the company with any questions or suggestions I may have.
   * In the footer, the user can find the email address of the company to get in touch with suggestions or questions.

### C. Frequent Visitor Goals

* As a Frequent Visitor, I want to check to see if there are any newly added recommended locations that I can check out.
   * At this point the user is familiar with the layout of the website & can recognize new locations or occasions that have been added to the map.

### 3. Further Testing

This website has been tested by friends and family to check for:
* bugs or disabled links
* clear user experience & navigation
* picture loading speed
* map functionality

### 4. Browser & Device Testing

This website has been tested on the following Desktop devices:
*  MacBook Pro 2013 - Chrome & Safari
*  Microsoft Edge - Chrome

This website has been tested on the following Mobile/Tablet devices:
* iPhone 11 - Safari
* iPhone 6 - Safari
* iPhone 6s - Safari
* iPad Air 2 - Safari

### 5. Bugs & Problems

No bugs were spotted during testing.

During the development stage, I encountered an issue with my gitignore file, which was leaving the env.py file exposed. This was quickly resolved by creating a duplicate env file, removing it from the gitignore file & then re-adding it after pushing the code to Github.

---

<span id="deployment"></span>
## Deployment :rocket:

### Github Pages

The project was deployed to GitHub Pages by following the steps below:

1. Log in to GitHub and locate the GitHub Repository
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under "Source", click the dropdown option called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll to GitHub pages section to locate the now published site link.

### Forking the GitHub Repository
Forking the GitHub Repository creates a copy of the original repository in our GitHub account to view and/or make changes without affecting the original repository. This can be done through the following steps:

1. Log in to GitHub and find the GitHub Repository
2. At the top of the Repository - just above & to the right of "Settings" on the menu, locate the "Fork" Button.
3. Click this to create a copy of the original repository in your GitHub account.

### Live Site
* This website is stored in a repository on [Github](https://github.com/ZahraSadiq/Milestone2-AntwerpHotSpots.git)
   * It was developed on GitPod, with changes regularly pushed to GitHub's repository using one main master branch.
   * Both the deployed and developed versions of this website are identical.

This site is hosted on GitHub Pages.
* You can view the live site [here](https://zahrasadiq.github.io/Milestone2-AntwerpHotSpots/)
* The url for the site is: https://zahrasadiq.github.io/Milestone2-AntwerpHotSpots/

---
<span id="credits"></span>
## Credits :pencil2:

### 1. Code Snippets

* The python code in this project is based on The Task Manger Mini project by Code institute.
* The website is based on Clean Blog theme from Startup Bootstrap and mimics some of the interactive & design elements created for the theme.

### 2. Media

* Icons from: [FontAwesome](https://fontawesome.com/icons?d=gallery)
* [Banner image](https://www.foodies.pk/blog/introduction-to-pakistani-cuisine/) 
* Recipe images were sourced from:
   	* [Chicken Karahi Keema](https://fatimacooks.net/recipe/chicken-karahi-keema/)
* [Prawn Pilau](https://www.ruchikrandhap.com/wp-content/uploads/2017/08/Prawn-Pulao-1-1024x683.jpg) 
* [Kheer](https://www.whiskaffair.com/wp-content/uploads/2019/04/Rice-Kheer-2-3.jpg) 
* [Bhunni Mash Daal]https://kfoods.com/images1/newrecipeicon/bhuni-daal-mash_12184.jpg) 
* [Mutton Pilau](https://fatimacooks.net/mutton-pulao-recipe-yakhni-pilau-rice/)
* [Aloo Palak](https://i2.wp.com/spicepaw.com/wp-content/uploads/2020/01/Aloo-Palak-1.jpg?fit=3124%2C3129&ssl=1) 

### 3. Content

* Recipes for the following were sourced from:
* [Chicken Karahi Keema](https://fatimacooks.net/recipe/chicken-karahi-keema/)
* [Prawn Pilau](https://fatimacooks.net/recipe/prawn-pilau-biryani-rice/)
* [Kheer](https://fatimacooks.net/recipe/cardamom-kheer/)
* [Bhunni Mash Daal](https://fatimacooks.net/bhuni-mash-daal/)
* [Mutton Pilau](https://fatimacooks.net/mutton-pulao-recipe-yakhni-pilau-rice/)
* [Aloo Palak](https://fatimacooks.net/aloo-palak-recipe-spinach-potato-curry/) 
  
### 4. Acknowledgements

* **Oluwafemi Medale (My CI Mentor):** Thanks for your advice and support.

