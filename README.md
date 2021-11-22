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

[Click here](/static/readme-assets/deployment.md) to view the Testing.md file.

[⇧ Back to Top](#table-of-contents)

<hr>
<hr>

# Testing
[Click here](/static/readme-assets/testing.md) to view the Testing.md file.

<hr>
<hr>

# Credits
The skills learnt in the [Boutique Ado](https://github.com/Code-Institute-Solutions/boutique_ado_v1/tree/8486523459273dddf96932a4ae19dd9a83af679d) project on the [CodeInstitute](https://codeinstitute.net/) Full-Stack Software Development course are the basis for this project, and significant code and logic from the Boutique Ado source code is present in this project.

All images used are royalty free from [Pexels](https://www.pexels.com/license/) and [Unsplash](https://unsplash.com/license) and used within the confines of their respective licenses. 

[⇧ Back to Top](#table-of-contents)

<hr>


## Acknowledgements

- A big thanks to CodeInstitute Student Support, Tutor Support and my mentor Arnold Kyeza for his support throughout all my projects.

[⇧ Back to Top](#table-of-contents)