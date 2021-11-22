[ 🠔 Back to ReadMe ](https://github.com/RoryBr1/Milestone-4#testing)

# Table of Contents 
1. [Code Validators](#code-validators)
    - [Python](#python)
    - [JavaScript](#javascript)
    - [HTML](#html)
2. [User Stories](#user-stories)
3. [Feedback](#feedback)

<hr>
<hr>

# Code Validators
## Python
* All Python files are PEP8 compliant, with no errors. All *.py* files in the project have been checked using the [PEP8 online](http://pep8online.com/) tool. No errors are reported by the IDE linter used in development.

<hr>

## JavaScript
* *statc/js/main.js* has been passed through the [JavaScript Validator](https://beautifytools.com/javascript-validator.php) when "jQuery" option is selected, with two errors:

 - ```"updateBtns' is defined but never used."```   
 - ```"goBack' is defined but never used."```

However, these functions are called on using buttons related to event triggers in the JavaScript file - therefore they are not redundant, should not be removed, and the error should be ignored.
(```updateBtns``` is used to update cart items, and ```goBack``` is used throughout the site on multiple pages to support "*Back*" buttons).

<hr>

## HTML
[W3C HTML validator](https://validator.w3.org/nu/)

Deployed versions of each page in the project have been tested against the (Nu Html Checker)[https://validator.w3.org/nu/?doc=https%3A%2F%2Ftechzone-ms4.herokuapp.com%2F] returning no errors. 
Warnings are returned on several pages regarding unnecessary ```type``` attributes for JavaScript files, but due to time constraints a development decision was made not to correct these. In future developments, these warnings can be rectified, but do not affect the function of the site.

[⇧ Back to Top](#deployment)

<hr>
<hr>

# User Stories

Each of the user stories was used as a starting point to test features on the site.

1. **As a _site administrator_, I want to upload products to the site for the _end-user_ to view and purchase. I want to be able to edit and delete these products if needed.**
    
    ✔  Once logged in, the _Admin_ menu button appears.

    ✔  The _Manage Products_ button directs the user to the relevant page, where an intuitive form allows them to add a new product.

    ✔  Once the form is submitted, a confirmation flash message appears, and the product is successfully added to the site.

    ✔  _Edit_ and _Delete_ buttons are visible overlaying the image of each product when logged in as an admin.

    ✔  The _Edit_ button directs the admin user to the relevant page where they can easily edit the properties of the product.

    ✔  The _Delete_ button deletes the button and a flash message is displayed confirming this to the admin user. (In future developments, a confirmation modal would be highly valuable to prevent accidental deletes).

2. **As a _site administrator_, I want to ensure that only I can alter the content of the website.**

    ✔  At the top of each page when logged in as an admin, the _Admin_ menu link is visible. When not logged in as an admin, these features are not accessible.

3. **As an _end-user_, I want to browse products relevant to me; including searching through them using search terms, or view only products in certain categories.**

    ✔  Products are loaded using products/products.html. The _search_ function is intuitive, functional and finds products according to user search queries. The category buttons successfully load products in the chosen category.

    ✔  When clicked, a new page will load for each product displaying the full details of the product.

4. **As an _end-user_, I want to sort products by their price or rating**

    ✔  On the _Products_ pages, the _Sort By_ dropdown is fully functional and can be used by the customer to sort products according to various factors.

5. **As an _end-user_, I want to add products to my cart and then purchase them**

    ✔ Products can be added to the cart on the individual product pages.

    ✔ When the user clicks on the _cart_ button, they can proceed to view their cart and _Checkout_ if they wish to.

    ✔ Checkout and payment processing is fully functional. **(When testing payments, use the following credit card details: 4242 4242 4242 4242, 04/42, 242 and 42424. These will allow you to run a payment for testing purposes without charging an actual credit card for the payment. Checkout/Payment can currently only be used on the Heroku-deployed version of the site.)**

    ✔ An e-mail confirmation is sent to the user to confirm their purchase details.

6. **As an _end-user_, I want to register an account so that I can save my shipping details and view my order history**.

    ✔ The _Login_ and _Register_ links are both visible when a user is not logged in.

    ✔ _Login_ works successfully for existing users and authenticates them.

    ✔ _Registration_ is fully functional. Users can register, receive an e-mail asking them to confirm their account, and continue to login with that account. (Note: in local deployment, this e-mail will print to the terminal. It is better to test its functionality on the Heroku-deployed site.)

    ✔ Users can save their shipping details when. These can be edited, when logged in, by clicking their _username_ on the navbar and selecting _My Account_.

    ✔ Previous orders can be viewed on the _My Account_ page.

[⇧ Back to Top](#deployment)

<hr>
<hr>