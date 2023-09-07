#                                        **CI-MS4-Smartgym** - Code Institute Milestone Project 4, Full Stack Module

![Am I Responsive image of quiz game](media/iam-responsive.jpg)
#                                      
A live website can be found [here](https://smartgym1-f1d10f71d6fc.herokuapp.com/)

## **Table of Contents**

 * [About](#about)
  * [User Experience](#User-experience)
  * [Project Goals](#project-goals)
  * [Target Audience](#target-audience)
  * [User Stories](#user-stories)
  * [Design](#design)
  * [Wireframe](#wireframe-views)
  * [Features](#features)
  * [Passwords and secret keys](#passwords&secretkeys)
  * [Existing Features](#existing-features)
  * [Features Left to Implement](#features-left-to-implement)
  * [Technologies-Used](#technologies-used)
  * [Testing](#testing)
  * [Deployment](#deployment)
  * [Credits](#credits)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgements](#acknowledgements)

---
# User Experience
## User Stories

### As an unregistered, I want to :

+ to be able to browse through all products available.
+ have the ability to use the search function.
+ have the ability browse through the gym and nutrition plans available.
+ have generic questions answered without having to contact the store owner/admin.
+ be able to view my bag and any items I currently have awaiting payment in my bag.
+ be able to add, edit quantity and remove items from my bag.
+ be able to purchase from the site without having to register for an account.
+ have the ability to register to the site if I choose to.

### As a registered user, I want to:

+ have the ability to log in to the site with  my details.
+ have a record of any purchases that I have made in the past and view them in detail.
+ be able to update my shipping information.
+ be able to update my shipping information from the checkout page. 
+ be able to view the class videos offered.

### As the site administrator, I want to:

+ be able to log in to an admin panel.
+ be able to add, update or remove products, gym , nutrition plans and merchandise without vistiting the admin panel.
+ receive email notifications when a user submits through the contact page.



### **Project Goals**

- The project goals are to create a website that people can browse through gym and fitness plans and buy branded smartgym merchandise.

### **Target Audience**

- The target audience are anyone who interested in healthy lifestyle and diet.



 
# **Design**

+ **Colour Scheme** 

- I wanted to keep it colorful and fun!
  
- Bright  primary colours so to make it easy and fun to navigate.


![Coloors Pallete](assets/images/fruitbowl-colours.jpg)

  
+ **Typography**

  The main font throughout the quiz is Josefin Sans with a back up font of sans-serif.Here we used google fonts.
  [Google Fonts](https://fonts.google.com/)

+ **Imagery**
 
  The imagery for the quiz game is simple colouful and pleasing on the eye. The navigation buttons are bright primary 
  colour's with 3D effect movement with the hover over.
  
- [Pixabay](https://pixabay.com/)

- [google images](https://www.google.com/imghp?hl=en/)

- [Getti images](https://www.gettyimages.co.uk/)


   ---
 # **Sitemap**

- The site is easy to navigate functional and responsive

![sitemap](media/smartgym-sitemap.jpg)
   
 # **Wireframe views**

# **Homescreen**
![Desktop wireframe](media/homescreen-screenshot-dtop.jpg)
-
# **products**
![Desktop wireframe](media/screenshot-products-dtop.jpg)
-
# **nutrition**
![Desktop wireframe](media/screenshot-nutrition-dtop.jpg)
# **Fitness**
![Desktop wireframe](media/screenshot-fit-dtop.jpg)
# **Merchandise**
![Desktop wireframe](media/screenshot-merchandise-dtop.jpg)
# **Bag**
![Desktop wireframe](media/screenshot-bag-dtop.jpg)
# **secure-checkout**
![Desktop wireframe](media/screenshot-secure-checkout-dtop.jpg)
# **My profile**
![Desktop wireframe](media/screenshot-myprofile-dtop.jpg)

---

# **Wireframe Tablet view**

# **Homescreen**
![Tablet wireframe](media/homescreen-screenshot-tablet.jpg)
# **Products**
![Tablet wireframe](media/screenshot-products-tablet.jpg)
# **nutrition**
![Tablet wireframe](media/screenshot-nutrition-tablet.jpg)
# **Fitness**
![Tablet wireframe](media/screenshot-fitness-tablet.jpg)
# **Bag**
![Tablet wireframe](media/screenshot-bag-tablet.jpg)
# **secure-checkout**
![Tablet wireframe](media/screenshot-secure-checkout-tablet.jpg)
# **Profile**
![Tablet wireframe](media/screenshot-my-proflie-tablet.jpg)

---

# **Wireframe Mobile view**


![mobile wireframe](media/.jpg)
![mobile wireframe](media/.jpg)
![mobile wireframe](media/.jpg)
![mobile wireframe](media/.jpg)
![mobile wireframe](media/.jpg)
![mobile wireframe](media/.jpg)
![mobile wireframe](media/.jpg)
---
---

### **Features**

# **Existing Features**

- Homepage which entails a recipe page a login page which takes you to your recipes to edit etc and a sign up/in page which 
  allows you to register. 

- You can press the home page link at any time fron any page.

- You can login and edit and also add new recipes.

- You can register from the login page.

- social media links on footer.
--- 
# **Passwords and secret keys**

# *passwords*
- To log in as admin django..The name and password are  username - admin3  and  password - 123456

# *secret keys*

- Stripe public key.
 pk_test_51NXoIzFaP2UHnBHNQnB0yAOCFgXvsBTVuOVLdAbSBWUIt8I0ovbWxonKopPVHABMCCh12T6gFiFggd90ziVQwm55007Fk1JL38

- Stripe secret key.  
 sk_test_51NXoIzFaP2UHnBHNYlff8FznqNTKpdgPyD9D0Wku4HEbSZoV1WmR9hEV3ighT1BIfAtINtFDz6aYAnAHlQFQKCSJ00B33SswF0

- Stripe web hook secret.
  whsec_Pp4pxfvuV0KoEveYrG4sfI2ddfS4LW0N

- Database url.
  postgres://pcczfpfz:CG7nceuyMHvyp6_YUzDoWJlSTaL6ARv8@trumpet.db.elephantsql.com/pcczfpfz




**_Products avaliable to all users_**

All products are avaliable to all users, so that all users will get to exsperience what the website is all about, and what they can experience, then decide if they would like to explore more functionalities of the website.

**_Users can search products based on  key words.**

For products and merchandise, most people may not familiar with a specific name. or want to go to a specific product.This is what people look at when it comes to searching. This feature will meet this particular user need.


**_Users can browse each menu_**

Users can access the all products page and view everything, by price ,catogory or rating.

**_Users account management_**

- **Register** Users have the option to create an account.

- **LogIn** registered users can access their account by logging in.

- **LogOut** Once the user finished using the site, they have a option of logging out the website.

- **Profile** users can have a profile.


# **Features Left to Implement**
+ To have more choice of gym and nutrtion plans and a better description.
+ To have a better colour scheme.
+ To have more products in merchandise with better description..
+ contact us.
+ To have added more content in general.
---

# Technologies Used
## Languages
+ [HTML5](https://en.wikipedia.org/wiki/HTML5)
+ [CSS3](https://en.wikipedia.org/wiki/CSS)
+ [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
+ [Python3](https://www.python.org/)

## Frameworks and Libraries
+ [Django](https://www.djangoproject.com/)
+ [Pip3](https://pip.pypa.io/en/stable/)
+ [jQuery](https://jquery.com/)
+ [FontAwesome](https://fontawesome.com/)
+ [Google Fonts](https://fonts.google.com/)
+ [Bootstrap](https://getbootstrap.com/)

## All Others
+ [Heroku](https://www.heroku.com/) used to deploy live site.
+ [Stripe](https://stripe.com/en-ie) used for the payments system.
+ [GitHub](https://github.com/) used to host repository.
+ [GitPod](https://www.gitpod.io/) used to develop project and organise version control.
+ [Canva](https://www.canva.com/) used for the inital design. 
+ [Balsamiq](https://balsamiq.com/) used to create wireframes.
+ [RandomKeygen](https://randomkeygen.com/) used to create a strong password for required  `<SECRET_KEY>`.
+ [Transfonter](https://transfonter.org/) used to convert font from .tff to .woff and .woff2.
+ [Lighthouse](https://developers.google.com/web/tools/lighthouse) for performance review.
+ [Responsinator](https://www.responsinator.com/) used to check site was responsive on different screen sizes.
+ [Am I Responsive](http://ami.responsivedesign.is/) used to generate README intro image.
+ [favicon.io](https://favicon.io/) used to create a site favicon.
+ [Elephant SQL](https://www.elephantsql.com/) used for database.
---

   

# **Testing**

## Manually Testing Functionality
### Navigation Buttons
+ Tested each page individually and clicked each button to make sure that they navigate to the correct place.
+ Tested each page individually on desktop and hovered over each button to make sure that Hover over is applied .
+ Tested each page individually on mobile and made sure hover over isn't applied.
### Home Button
+ Smartgym  buttton tested and working correctley.
### All products Button
+ Login button also price ,rating and catogory tested and works correctly 
### Nutrition plan Button
+ nutrition plan also all options inside, button works as exspected. 
### Gym plan button
+ Gym plan and all inside performs as exspected. 
### Merchandise Button
+ Mrechandise button and all inside works correcley.
### Search our site option
+ search our site option works correcley. 
### My account button
+ My account button with login and register works correcley.
### My profile button
+ My account button with login and register works correcley.
### Bag button
+ bag button with update remove and subtotal works correcley. 
### Checkout button
+ check button works correcley. 
### Complete order button
+ complete order button  works correcley. 
 
### Social media links 
+ All social media links work as exspected. 

### Log out
+ Log in button works as exspected.


| Feature | Expected Outcome | Testing Performed |  Actual Result | Outcome |
| --- | --- | --- | --- | --- |
|The Smartgym title | Link directs the user back to the home page | Clicked title |  page reloads | Pass |
|All products | Clicked on button | Takes you to the recipes | Pass |
|Login button  | Clicked on  button | Login opens | Pass |
|Sign up button |  | Clicked button | sign up form opens | Pass |
|Register button | Takes you to sign up/ register form | Clicked on button | Form opens | Pass |
|Sign up (submit button) | clicked button |works correctley  | Pass |
|Facebook link in footer  | Clicked on button | Takes you to face book| Pass |
|Twitter link in footer  | Clicked on button | Takes you to Twitter| Pass |
|Instagram link in footer  | Clicked on button | Takes you to Instagram| Pass |
|All buttons - hover effect | All buttons have hovered over with movement. | Hover over each button on the page |button movenment correctly performing  when hovered over | Pass |
|  Cursor pointer| cursor displayed when moved over buttons | mouse positioned over each button to check the cursor changed  | cursor changed when hoverd | Pass |
|Stripe payment |all button and features |works correctley | Pass |

---
# Automatic testing

### Validation
 - W3C Validation was used:
 - HTML
 - CSS
 - pip8 was used for python.
 - JS Hint was used to validate javascript.

 #  Links to above mentioned are in languages used.

# Known bugs

 + Initially when you where logged in , it would stay show as logged in , in the nav bar.
---
+ Solved bug, (typo in code, found in app.py)

![Known fixed bugs](assets/images/known-fixedbug.jpg)



# Lighthouse performance

+ ## Desktop Home screen
 ![Desktop performance](assets/images/smoothie-desktoplh-home.jpg)
+ # Desktop Recipes 
 ![Desktop performance](assets/images/smoothie-desktoplh-recipes.jpg)
+ # Desktop Login
 ![Desktop performance](assets/images/smoothie-desktoplh-login.jpg)
 + # Desktop Dashboard
 ![Desktop performance](assets/images/smoothie-desktoplh-dashboard.jpg)
 + # Desktop Sign up
 ![Desktop performance](assets/images/smoothie-desktoplh-signup.jpg)
 + # Desktop Edit page
 ![Desktop performance](assets/images/smoothie-desktoplh-edit.jpg)
+ # Mobile view Home screen
 ![Mobile performance Home](assets/images/smoothie-homelh.jpg)
+ # Mobile view Recipes  Page
 ![Mobile performance recipes page](assets/images/smoothie-recipeslh.jpg)
+ # Mobile view login page
 ![Mobile performance login page](assets/images/smoothie-loginlh.jpg)
+ # Mobile view Dashboard  page
 ![Mobile perfomance dashboard](assets/images/smoothie-dashboardlh.jpg)
+ # Mobile view Sign up page
 ![Mobile performance signup](assets/images/smoothie-signuplh.jpg)
+ # Mobile view Edit page
 ![Mobile performance edit page](assets/images/smoothie-editlh.jpg)

 ## Deployment & Local Development

 ## **Deployment**

### **Heroku Deployment**

I deployed this project to heroku using the following steps:

#### **Deployment**

- Log into Heruko
- Under dashboard, Select "Create New App"
- Choose an app name (it shows in red if the name is already taken)
- select a region base on your location
- click "Create app"

### Deploying to Github Pages

* Choose the repository you want to deploy from the main overview.
* Go to settings by clicking on the icon on the menu.
* In the left navigation, select the "Pages" option.
* Under "Source", choose "Master" branch and click "Save".
* After it's done, you will see a message saying "Your site is ready to be published at (insert url here)".

### Local Development
#### How To Fork

Forking a repository is the process of creating a copy of the original repository. This enables you to make changes without affecting the main repository. 

To do so:-
* go to the GitHub repository you want to copy.
* select the 'Fork' button located in the top right corner, under your profile icon. 
* Once complete, you will now have your own version of the repository to make changes to.

#### How To Clone

To copy a GitHub repository:-
* first navigate to the repository you wish to copy. 
* click on the 'Code' button (which has a download icon) and copy the link provided.
* in the Gitpod Terminal, navigate to the directory where you wish to place the clone. Then, type 'git clone' and paste the link you copied earlier and press enter. This process can also be completed using VSCode.


# **Credits**

### **Content**

Throughout the process of doing this project I have done a lot from searching and investigating. All resources are referenced in the credits and the codes in the section below. 

 # Codes

   [w3schools](https://www.w3schools.com/) - [audio](https://www.w3schools.com/html/html5_audio.asp), [javascript modal](https://www.w3schools.com/howto/howto_css_modals.asp), [loader](https://www.w3schools.com/howto/howto_css_loader.asp), [cubic-bezier](https://www.w3schools.com/cssref/func_cubic-bezier.asp), [javascript objects](https://www.w3schools.com/js/js_objects.asp), [setInterval and clearInterval](https://www.w3schools.com/jsref/met_win_setinterval.asp), [setTimeout](https://www.w3schools.com/js/js_timing.asp), [Array splice](https://www.w3schools.com/jsref/jsref_splice.asp), [DOM changing CSS](https://www.w3schools.com/js/js_htmldom_css.asp), [JSON.parse()](https://www.w3schools.com/js/js_json_parse.asp), [Math.floor()](https://www.w3schools.com/jsref/jsref_floor.asp), [CSS background-image](https://www.w3schools.com/cssref/pr_background-image.asp), [CSS box-shadow](https://www.w3schools.com/cssref/css3_pr_box-shadow.asp), [Array map()](https://www.w3schools.com/jsref/jsref_map.asp)

   [stackoverflow](https://stackoverflow.com/) - [display options randomly](https://stackoverflow.com/questions/53362187/javascript-quiz-display-random-options), [difference between innerText and innerHTML](https://stackoverflow.com/questions/19030742/difference-between-innertext-innerhtml-and-value), [convert an object key value into an array](https://stackoverflow.com/questions/38824349/how-to-convert-an-object-to-an-array-of-key-value-pairs-in-javascript)

   [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/max) - [Math.max()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/max), [window.location.assign()](https://developer.mozilla.org/en-US/docs/Web/API/Location/assign), [window.localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage), [Array.prototype.join()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/join), [Element.classList](https://developer.mozilla.org/en-US/docs/Web/API/Element/classList), [parseInt()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseInt), [Spread syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Spread_syntax), [forEach](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach), [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)

   [7 Methods for Comparing Arrays in JavaScript](https://javascript.plainenglish.io/7-methods-for-comparing-arrays-in-javascript-88f10c071897)


   [How To find your Target audience..Adam Erhart..](https://youtu.be/FzEkHlYt2uA/)

   [How to write a good user story](https://stormotion.io/blog/how-to-write-a-good-user-story-with-examples-templates/#.YFM57o-2eQY.linkedin)


### **Acknowledgements**

I would like to thank:

My mentor Antonio Rodriguez for his encouragement and patience when my frustration kicked in at the start of this project. Thanks to his guidence and tips, I have gotten over the dip and made it to the end.

Help and support from fellow students in the Slack community.

Tutor support and student care team.

My wife Lyndsay cutmore support and help with testing and encouragement.

Should you have any queries please reach me on rob_cutmore@hotmail.com


