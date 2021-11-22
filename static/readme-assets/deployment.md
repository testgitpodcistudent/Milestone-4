<a href="https://github.com/RoryBr1/Milestone-4#design">Back to ReadMe</a>

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

You will also need a [Heroku](https://signup.heroku.com/) account.

> Important
> If you get ``` FATAL: role "somerandomletters" does not exist ``` error, run ``` unset PGHOSTADDR ``` in the terminal. This should allow you to continue.


2. In the terminal, type ``` python3 app.py > Procfile ``` . This will create a _Procfile_, which tells Heroku which file to run when the site is accessed.

3. In the _Deploy_ tab on Heroku, click "Connect to GitHub" and select the relevant repository. Click "Connect".

4. Go to the _Settings_ page in Heroku and click on "Config Vars". Click on "Reveal Config Vars".

    - Enter the _IP, SECRET_KEY, MONGO_URI,_ and _MONGO_DBNAME_ as contained in your _env.py_ file.

5. Go to the _Deploy_ tab in Heroku, scroll down and click "Enable Automatic Deploys". Click "Deploy Branch".

Once the app is deployed, click "Open App" in Heroku on the project page. The project should be successfully deployed and will update automatically when new GitHub commits are made.