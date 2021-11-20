![Logo](/static/readme-assets/logo-readme.png)
# Full-Stack Project | e-Commerce Website

# Table of Contents

1. [Overview](#overview)
2. [UX](#ux)
    * [Developer Goals](#developer-goals)
    * [User Stories](#user-stories)
    * [Design](#design)
    * [Concept & Font Choice](#concept-and-font-choice)
    * [Colours](#colours)
3. [Features](#existing-features)
    * [Existing Features](#existing-features)
    * [Future Features](#future-features)
4. [Technologies Used](#technologies-used)
    * [Django](#django)
    * [Stripe](#stripe)
    * [Coding Languages & Libraries](#coding-languages-and-libraries)
    * [Software](#software)
    * [Additional Tools](#additional-tools)
5. [Deployment](#deployment)
    * [GitPod Deployment](#gitpod-deployment)
    * [Heroku](#heroku)
6. [Testing](#testing)
7. [Credits](#credits)
    * [Acknowledgements](#acknowledgements)

<hr>
<hr>

## Overview

TechZone is an e-commerce website featuring user registration, login, product management, and providing customers with the ability to place online orders and pay for them using the Stripe checkout platform.

The website is fully responsive, utilizing simple and colourful design language and an intuitive information structure.
This project was built as part of the [CodeInstitute](https://codeinstitute.net/) Full-Stack Software Development course purely for educational purposes.

[⇧ Back to Top](#table-of-contents)

<hr>
<hr>

# UX

## Developer Goals
* Create an easy-to-use e-commerce website.
* Allow the end-user (customer) to register an account, login, add products to their cart, and purchase them.
* Create an intuitive interface for the site administrator to add, delete and edit products.
* Allow the end user to search products by search term, sort by price and other factors, and view products based on category.
* Provide links to social media pages run by the site owner.
* Create an easy-to-use contact form for customers or potential customers to send messages to the site owner.

<hr> 

## User Stories
1. As a _site administrator_, I want to upload products to the site for the _end-user_ to view and purchase. I want to be able to edit and delete these products if needed.
2. As a _site administrator_, I want to sort the products into separate categories for ease of browsing.
3. As a _site administrator_, I want to ensure that only I can alter the content of the website.
4. As an _end-user_, I want to browse products relevant to me; including searching through them using search terms, sort by price, and view items in specific relevant categories.
5. As an _end-user_, I want to send an e-mail to the site owner about an order (or potential order).
   
### How does the website function to meet the needs of the user, as described in the user stories?
1. The _Add New product_, _Edit_ and _Delete_ functions enable the administrator to fulfill these Create, Update and Delete functions.
2. The site requires administrator _authentication_ to reveal the administrator features. This is done on the _"Admin Login"_ page.
3. The homepage displays all products on the site. The searchbar allows users to search products using a search term. The category links (_All Products, Laptops, Phones, Tablets_) allow users to view by category. The _Sort Products_ dropdown allows users to sort relevant products via different factors including cost.
    A preview of the products is shown; when clicked, the user is directed to the full product page.
4. The *Contact Us* link on the footer of each page directs the user to a functional Contact form which sends an e-mail to the site administrator's inbox.

[⇧ Back to Top](#table-of-contents)

<hr>

## Design

* [Click here to view wireframes.](/static/readme-assets/wireframes.md) <br>

### Concept and Font Choice
The site is designed to appear clean, professional, and uncluttered while also appearing vibrant and welcoming.

The [Poppins](https://fonts.google.com/specimen/Poppins) font is the primary font used throughout all sections of the site.

- [Hover.CSS](https://ianlunn.github.io/Hover/) - CSS library used for hover effects on site buttons.
- [FontAwesome](https://fontawesome.com/) - Webfont library used for icons throughout the site.

### Colours

The colours used throughout the site are primarily the default BootStrap element colours; largely the _dark, success, danger_ and _info_ colour classes.

[⇧ Back to Top](#table-of-contents)

<hr>
<hr>

# Existing Features
The site's structure consists of
- **Homepage** Basic landing page with splash image and call-to-action button which leads to the main product page.
- **User registration**, fully functional and requiring the user to confirm their e-mail address by clicking a link which is emailed to them.
- **User login** which allows the user to login, with different site accessibilities between regular users (customers) and admins.
- **Products page** which displays all products, as well as search and sort-by-category functionality. When logged in as admin, relevant control panel links are also displayed.
    This uses the *get_products* python function.
- **Admin authentication** which allows the admin user to access product management and a shortcut to the Django Admin Panel.
    These utilize the *admin_login* and *logout* python functions.

    ![Admin menu](/static/readme-assets/admin-login.png)

    - _The admin-login page can be accessed by clicking the link at the top right of the navbar when logged in as admin._

    ![Admin add product page](/static/readme-assets/add-product-screenshot.png)
    - _Add Product page, accessible via the Admin menu._
- **Product Page** for each product which is loaded when a product is clicked on the homepage.
- **Delete Product** allows the admin to delete the given product.
- **Edit Product** allows the admin to edit the selected product.

    ![Edit and delete buttons](/static/readme-assets/edit-delete.png)

    - _Edit and Delete buttons as displayed when logged in as admin_
- **Messages** display a short message to the user confirming actions such as cart updates, product deletions, login actions etc.
    ![Messages](/static/readme-assets/message.png)

**Developer Notes**
- If you encounter the following error at any point running terminal commands in local deployment: ``` django.db.utils.OperationalError: FATAL:  role "qwmrksyzdlafcq" does not exist ``` , running ``` unset PGHOSTADDR ``` and re-trying the previous command will allow you to continue.

- Ensure your IDE Python linter is set to _flake8_, or you will encounter false errors related to object models not existing.

- Some files have PEP8 compliancy errors, specifically "Line too long" errors. A development decision has been made to ignore these warning as fixing them has caused bugs.

<hr>

## Future Features

- A live chat which would allow the user to correspond with the site team in real time to solve customer queries.

- Stock-keeping functionality to allow the administrator to keep a track of stock of each item.

[⇧ Back to Top](#table-of-contents)

<hr>
<hr>

# Technologies Used

## Django
The website is built using [Django](https://www.djangoproject.com/).

## Stripe
The website's payment system is built using [Stripe](https://stripe.com/en-ie).


## Coding Languages and Libraries

* [HTML5](https://www.w3.org/standards/webdesign/htmlcss.html) - Used on all pages for page structure and content.
* [CSS](https://www.w3.org/standards/webdesign/htmlcss.html) - Used on all pages for content styling and placement.
* [BootStrap 4.4.1](https://getbootstrap.com/) - Front end CSS framework.
* [jQuery](https://jquery.com/) - JavaScript library used for intilization of BootStrap features.
* [Python](https://www.python.org/) - used throughout site alongside Flask-PyMongo.

## Software

* [GitPod](https://www.gitpod.io/) - Code editor used throughout development to write code.
* [GIMP Image Editor](https://www.gimp.org/) - Used throughout to crop and edit images.

## Additional Tools

* [Balsamiq](https://balsamiq.com/) - Used to create wireframes in the design process.
* [Responsively](https://responsively.app/) - Used to test site responsiveness throughout development.
* [Am I Responsive](http://ami.responsivedesign.is/) - Browser-based preview any website's responsiveness. Screenshot featured in readme.md 
* [Google Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) - Used throughout development to view the website, test features, test JavaScript, and test responsiveness. 
* [ScreenToGif](https://www.screentogif.com/) - Used to create GIF screen-recordings for readme and testing purposes

[⇧ Back to Top](#table-of-contents)

<hr>
<hr>

# Deployment 

## Local GitPod Deployment

The following steps will allow you to deploy the project 'locally' in the cloud-based IDE, Gitpod.

*This procedure requires a [GitHub](https://github.com/login) account, and a [Stripe](https://dashboard.stripe.com/register) account.*
<hr>

**Step One: Creating a Gitpod workspace and installing requirements**
1. [Login to Gitpod](https://gitpod.io/login) using your GitHub account. (If a GitHub pop-up window asks you to authorize Gitpod, click Authorize).

2. Navigate to [this link](https://gitpod.io/#https://github.com/RoryBr1/Milestone-4) in your browser to open the repository in a new Gitpod workspace.

3. Install all required packages in your Gitpod workspace, by typing 
   ``` pip3 install -r requirements.txt ```
   in the workspace terminal and pressing enter.    
   Wait until the installation processes for all packages have completed.
<hr>

**Step Two: Setting Django & Stripe SECRET_KEYs and Stripe PUBLIC_KEY**

*Reccomended reading:*  
[What is a Django Secret Key?](https://docs.gitguardian.com/secrets-detection/detectors/specifics/django_secret_key#:~:text=Summary%3A%20The%20Django%20secret%20key,cookies%20sent%20by%20the%20application.)  
[Stripe Docs: API Keys](https://stripe.com/docs/keys)


1. Create a new file in the base directory of your project, named ".env" . This file will hold your SECRET_KEY. (We have included *.env* in our *.gitignore* file, which will prevent this sensitive data from being pushed publicly to GitHub).

2. In your *.env* file, copy and paste these lines of code:

    > DEVELOPMENT=True
    > SECRET_KEY=your-django-secret-key     
    > STRIPE_PUBLIC_KEY=your-stripe-public-key      
    > STRIPE_SECRET_KEY=your-stripe-secret-key  
    > STRIPE_WH_SECRET=your-stripe-wh-secret    
    > EMAIL_HOST_PASSWORD=your-email-host-pass   
    > EMAIL_HOST_USER=your-email-host-user   

2. Use [Djecrety.ir](https://djecrety.ir/) to generate a random Django key, and click on the key to copy it to your clipboard. 

3. In your *.env* file, replace ```your-django-secret-key``` with your new key from the generator. (Do not include any quotation marks around the key).

4. Login to [Stripe](https://dashboard.stripe.com/login) and navigate to your [Stripe Dashboard](https://dashboard.stripe.com/test/dashboard).

5.  On the bottom right of the page, click on your "Publishable Key" to copy it to your clipboard.  
    Paste it into your *.env* file, replacing ```your-stripe-public-key```. 

    In Gitpod, use the Explorer to navigate to ```checkout/views.py```. On line 44, replace the existing ```stripe_public_key``` with your own, inside the quotation marks.

6. On the bottom right of your [Stripe Dashboard](https://dashboard.stripe.com/test/dashboard), click on *Secret Key* once to reveal it.  
    Click it again to copy it to your clipboard, and paste it into your *.env* file replacing ```your-stripe-secret-key```. 
<hr>

**Step Three: Running the server, adding STRIPE_WH_SECRET .env variable**

1. In your Gitpod terminal, type the following command and press enter: ```python3 manage.py runserver``` . 
    The site is now being hosted locally, and the following prompt should appear:   
    ![Gitpod preview prompt](/static/readme-assets/gitpod-runserver-prompt.png)  
    Click "*Open Browser*", and the live site will open in a new browser tab.

2. Click "*Shop Now*", then click "*View*" on any product. Click "*Add to Cart*". On the modal window that appears, click "*Check Out*". 
    Scroll to the bottom of the *Shopping Cart* page, and click "*Checkout*". 

3. Copy the URL of this *Checkout* page to your clipboard from your browser's URL bar. 

4. Navigate to [create Stripe Webhook Endpoints](https://dashboard.stripe.com/test/webhooks/create).  
    Paste the *Checkout* URL into the *Endpoint URL* field, and in the description text-area type something such as "Techzone Checkout".    
    On the "*Select events to listen to* option, click "*Account*" and "*Payment Intent*", and tick "*Select All*" for both.    
    Click "*Add Events*", and then "*Add Endpoint*".

5. Once the endpoint is created, navigate to [Stripe Webhook Endpoints](https://dashboard.stripe.com/test/webhooks), and click on the address of the new endpoint you just created. 
On the right hand corner of this page, click the webhook code to copy it to your clipboard. 
Return to your *.env* file, and replace ```your-stripe-wh-secret``` with this new webhook code. 

At this point, the basic functionality of the site as a guest user is complete. The guest user can browse the locally deployed version of the site, add products to their cart, and complete the checkout process.
    **Note**: As your Stripe account is set by default to run in *Test mode*, you can use the following *test mode* credit card details to complete the checkout process.   

     Card Number: 4242 4242 4242 4242  
     Expiry Date: 0424     
     CVC: 242  
     ZIP: 42424    

**Note:** When ```DEVELOPMENT=True``` is in our *.env* file, e-mails (such as registration and order confirmation e-mails) will be printed to the Gitpod terminal.   
If you choose to deploy the site to [Heroku](https://www.heroku.com/) following the procedure below, steps are listed which will instruct you on how to enable emails to be sent from a live Gmail account.


[⇧ Back to Top](#table-of-contents)

<hr>

## GitHub Push, Heroku (Web) Deployment

This procedure requires that you have successfully [configured your project in a Gitpod workspace](local-gitpod-deployment) as directed.


2. In the terminal, type ``` python3 app.py > Procfile ``` . This will create a _Procfile_, which tells Heroku which file to run when the site is accessed.

3. In the _Deploy_ tab on Heroku, click "Connect to GitHub" and select the relevant repository. Click "Connect".

4. Go to the _Settings_ page in Heroku and click on "Config Vars". Click on "Reveal Config Vars".

    - Enter the _IP, SECRET_KEY, MONGO_URI,_ and _MONGO_DBNAME_ as contained in your _env.py_ file.

5. Go to the _Deploy_ tab in Heroku, scroll down and click "Enable Automatic Deploys". Click "Deploy Branch".

Once the app is deployed, click "Open App" in Heroku on the project page. The project should be successfully deployed and will update automatically when new GitHub commits are made.

[⇧ Back to Top](#table-of-contents)

<hr>
<hr>

# Testing
[Click here](/static/readme-assets/testing.md) to view the Testing.md file.

<hr>


# Credits
The skills learnt in the [Boutique Ado](https://github.com/Code-Institute-Solutions/boutique_ado_v1/tree/8486523459273dddf96932a4ae19dd9a83af679d) project on the [CodeInstitute](https://codeinstitute.net/) Full-Stack Software Development course are the basis for this project, and significant code and logic from the Boutique Ado source code is present in this project.

All images used are royalty free from [Pexels](https://www.pexels.com/license/) and [Unsplash](https://unsplash.com/license) and used within the confines of their respective licenses. 

[⇧ Back to Top](#table-of-contents)

<hr>


## Acknowledgements

- A big thanks to CodeInstitute Student Support, Tutor Support and my mentor Arnold Kyeza for his support throughout all my projects.

[⇧ Back to Top](#table-of-contents)