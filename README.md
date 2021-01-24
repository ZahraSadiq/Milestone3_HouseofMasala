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

* Color Scheme: 
    * The three main colors used are Black, Pink & Beige.

* Typography:
    * All Headers use Karla. Karla is a sans-serif font with nice letter-spacing - which makes it easy-to-read & clean.
    * Montserrat is my secondary font, used for paragraphs. Like Karla, it is both clean & easy to read especially on smaller devices & pairs nicely with Karla. 
    * Sans-Serif is used as the backup font for both Karla & Montserrat.

* Imagery: 
    * A bright, colorful image was used for the hero image to be eye-catching to the user. It also compliments the color scheme, adding an element of consistency to the website. 

### Wireframes & Mockups:

* View website wireframes for desktop [here](https://drive.google.com/file/d/15ZmioN0w8vPz3TuhpdIQcyuUIX5oD5v9/view?usp=sharing)
* View website wireframes for mobile [here](https://drive.google.com/file/d/1Svbf2IyMygzqkQPFNg-TqXWZ9xfA7PxV/view?usp=sharing) 
 
---

<span id="features"></span>
## Features :clipboard:

The site contains certain features which are not visible or available to unregistered/logged in users. These features include the ability to add a recipe, edit it, store it, and delete it (CRUD operations). Content available to all users includes the ability to view all recipes including the 3 most recently added.

### Features visible to All Users:
* **All Recipes:** 
* **Register**
* **Login** 
* **Recently Added Recipes**
* **Footer** Contact link for email, social links 
* **Navbar**

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
* JavaScript - 
* Python including:
    * Flask 
    * Flask pymongo
    * Jinja templating
    * BSON
    * Werkzeug
    * Dnspython
* MongoDB

### 2. Other Programs & Frameworks Used 

* Webformatter - to beautify my CSS, HTML, JS code 
* FontAwesome - for all icons used on the buttons
* Balsamiq - for creating wireframes 
* Bootstrap 4.4.1 - for assisting in responsiveness and layout of website 
* Photopea | Online Photo Editor - for resizing images 
* Inkscape - for creating custom map markers 

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
* [Syntax Validator - Esprima](https://esprima.org/demo/validate.html)
    * Result: Code is syntactically valid. 
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

* Inspiration for the [Jumbotron](https://courses.codeinstitute.net/courses/course-v1:codeinstitute+FE+2017_T3/courseware/a4b90d17e5c94220a0f83f00ce7fa606/4b3b1b062b01424997c8fd052e177b8e/?activate_block_id=block-v1%3Acodeinstitute%2BFE%2B2017_T3%2Btype%40sequential%2Bblock%404b3b1b062b01424997c8fd052e177b8e) (styling)
* Inspiration for the [Banner Image](https://www.w3schools.com/howto/howto_css_hero_image.asp) 
* Inspiration for [Footer](https://courses.codeinstitute.net/courses/course-v1:codeinstitute+FE+2017_T3/courseware/616289d66b5641a3808cc43e53842695/b51f7b8b815c4bcd9979d2281b6d97a9/?activate_block_id=block-v1%3Acodeinstitute%2BFE%2B2017_T3%2Btype%40sequential%2Bblock%40b51f7b8b815c4bcd9979d2281b6d97a9) (styling)
* Tutorial for adding [Google Maps API](https://courses.codeinstitute.net/courses/course-v1:CodeInstitute+IFD101+2017_T3/courseware/03d3f6524ad249d9b33e3336d156dfd0/3b2af8636ea54a4d9dc45126f7498633/?activate_block_id=block-v1%3ACodeInstitute%2BIFD101%2B2017_T3%2Btype%40sequential%2Bblock%403b2af8636ea54a4d9dc45126f7498633)
* Code used for adding the [InfoWindow & Custom Map Markers](https://www.youtube.com/watch?v=Xptz0GQ2DO4)
* Help with adding image to [InfoWindow](https://stackoverflow.com/questions/33788841/adding-image-in-infowindow-of-google-maps)
* Help with adding description to [InfoWindow](https://developers.google.com/maps/documentation/javascript/examples/infowindow-simple)
* Help with filtering markers based on occasion type from my mentor 
* Code used for [Email link](https://www.tutorialspoint.com/html/html_email_links.htm) in footer 

### 2. Media 

* Icons from: [FontAwesome](https://fontawesome.com/icons?d=gallery)
* Karla & Montserrat Fonts from: [Google Fonts](https://fonts.google.com/?category=Sans+Serif)
* Banner image from: [Unsplash](https://unsplash.com/)
* Recommended Location images were sourced from:
    * [Salon de the Claude](https://www.google.com/search?q=salon+de+th%C3%A9+claude+antwerpen&rlz=1C5CHFA_enMY503MY503&sxsrf=ALeKk01sQiAHICXEc59eElrNFDgRuOrcCg:1603059383675&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjhkvjIlb_sAhWk4IUKHZNYDasQ_AUoAnoECAQQBA&biw=1271&bih=643#imgrc=2b27vpjSjth1CM)
 

### 3. Content 

* Unmodified descriptions for Recommended Locations on the map were taken from the following sources:
    * [Luddites Books & Wine](https://www.tripadvisor.com/Attraction_Review-g188636-d21011255-Reviews-Luddites_Books_Wine-Antwerp_Antwerp_Province.html)

    
### 4. Acknowledgements 

* **Oluwafemi Medale (My CI Mentor):** Thanks for your advice and support.