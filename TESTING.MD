# Testing

Back to the [README](README.md)

- Testing has taken place continuously throughout the development of the project. Each view was tested regularly.When the outcome was not as expected, debugging took place at that point.  

#### Python Validation - Pycodestyle

- Python testing was done using the Pycodestyle to ensure there were no syntax errors in the project. All python files
were entered into the checker and no errors were found in any of the custom codes.

![Pycodestyle results](/media/pythontesting.png).

#### Checked Python Files

#### App - Bag

- apps.py
- context.py
- urls.py
- views.py

#### Checkout - Bag

- admin.py
- apps.py
- forms.py
- models.py
- signals.py
- urls.py
- views.py
- webhook_handler.py
- webhooks.py

#### Home - Bag

- admin.py
- apps.py
- models.py
- urls.py
- views.py

#### Products - Bag

- admin.py
- apps.py
- context_processors.py
- forms.py
- models.py
- urls.py
- views.py
- widgets.py
  
#### Profiles - Bag

- admin.py
- apps.py
- forms.py
- models.py
- urls.py
- views.py

### Javascript

The Javascript code was validated using using [JsHint](https://jshint.com/).
At the time of deployment the validation for *script.js* has the following outcome:


<details>

<summary>script.js</summary>

![script.js](/media/script.js.png)

</details>


<details>

<summary>checkout.js</summary>

![checkout.js](/media/checkout.js.png)

- The script for defining the Stripe methods contains *Stripe* variable that generate the error in the linter. As this is a script taken and adapted from the [Stripe Documentation](https://stripe.com/docs/development), I choose to ignore this issue as there is no fix found for it.
  
</details>

<details>

<summary>profiles.js</summary>

![profiles.js](/media/profile.js.png)

</details>

- The warnings listed are caused of the EventListeners added to elements in a loop.<br>
I tried to solve the issue but no successful method has been found, so I chose to ignore the warning as it is not affecting the way my code works in any way.

### Lighthouse

Lighthouse was used to test Performance, Best Practices, Accessibility and SEO on Desktop.

##### Desktop Results:

![Lighthouse Desktop Result](/media/lighthouse-desktop.png)

###### Mobile Results:

![Lighthouse Mobile Result](/media/light-house-mobile.png)

### HTML Validation

![HTML Validation](media/htmlvalidation.png)

The following pages have been tested:

- Home
- Products
- Product details
- Bag
- Checkout
- User Profile
- Newsletter
- FAQs
- Contactus
- Wishlist
- Login/Register
- 403/404/500 custom pages

### CSS Validation

![CSS Validation](/media/cssvalidation.png)

- Custom CSS was validated using W3C Jigsaw validation service. Seventeen warnings were displayed, however,
  these are related to Google Fonts and vendor extension prefixes which will not affect the CSS performance.

## Browser Testing

- The Website was tested on Firefox, Google Chrome, and Safari browsers with no issues noted.

## Console result

![consile result ](/media/consoleresult.png)

## Manual Testing

### Home

- I confirmed logo acts as a redirect link to the home page.
- I confirmed all the links on the nav bar are clickable and redirect the user to their related page i.e. login, logout, product categories, contact us, faqs,  wishlist, product managment, newsletter-message.
- I confirmed search bar works effectively even on keywords such as 'oo'.
- I confirmed user can select products based on category and it will show only those products based on that category.
- I confirmed the page is responsive as per different screen sizes.
- I confirmed that links to privacy & policy , Terms & Conditions and social media's Opens in a new tab. 
- I confirmed that all toast message appears as expected.

### Product management 

- I confirmed admin can add product.
- I confirmed admin can add product details.

### All Products

- I confirmed all the products here are clickable and redirected the user to the product details page.
- I confirmed all the product categories and items on sale are visible here.
- I confirmed products will also display relevant information such as image, name, description and price.
- I confirmed admin can edit/delete products.
- I confirmed admin can edit/delete product details.
- I confirmed toast message appears when user/ admin make any changes.

### Product with category

- I confirmed user can filter the books according to product category.
- I confirmed user can filter the products according to price, rating, name and category.
- I confirmed only specific categories of products will be displayed here.
- I confirmed products will also display relevant information such as image, name, description and price.

### Product Detail

- I confirmed user can add/remove/update no. of quantity of that book in the cart while on the product details page.
- I confirmed user can add products to the wishlist from here.
- I confirmed user can checkout, meaning redirect to the cart page from this page.
- I confirmed user can view details of the product along with its description.

### Cart

- I confirmed user can add/remove/update items from the cart.
- I confirmed user can view relevant details of the product from the cart.
- I confirmed user can view the total price from inside the cart.
- I confirmed user can go to shipping details from the cart.
- I confirmed toast message appears when user make any changes in the cart.

### Shipping Details

- I confirmed the fields will be empty for every new user.
- I confirmed All the fields here are editable except the Method dropdown which is set to COD.
- I confirmed user can update the shipment data, each time when user places an order.
- I confirmed that the fields can't be set empty.
- I confirmed the button here completes the order process.
- I confirmed that toast message appears on top right when user places the order.

### Order Complete

- I confirmed user can see that the order was placed successfully.
- I confirmed user receives an email with order details.
- I confirmed if the user goes back to shipping and clicks finish order, the user will be redirected to order details page as the order is already placed.
- I confirmed user is given clickable options to redirect from this page.


### My Profile

- I confirmed user can see all the orders they have placed from my Profile page.
- I confirmed user can update their “user details” while being on my Profile page.
- I confirmed when user update their profile a toast message appears.

### Wishlist

- I confirmed that only items, that user had added to the Wishlist are displayed here.
- I confirmed products will also display relevant information such as image, name, description and price.
- I confirmed that user can remove items from the wishlist.
- I confirmed that only authenicated user can access wishlist page.
- I confirmed that user can filter the wishlist page according to price, rating, name and category.
- I confirmed toast message appears when item is added or remove from wishlist.


### Contact us

- I confirmed user can send their message from contact us page.

### Special offer

- I confirmed user can see new arrivals in this page.
- I confirmed user can also check new arrivals directly after completing their order by clicking on "now checkout the new arrivals!"

### Newsletter

- I confirmed that user can subscribe to newsletter.
- I confirmed that admin can sent messages to all subscribers together.

### FAQs

- I confirmed that admin can add/remove/update faqs in FAQs page.
- I confirmed that answer to faqs appears when clicked.

### Register 

- I confirmed that user can't register with an same email address if that email address is already been used.
- I confrmed that user has complete all the field required in register page to make a new account.
- I confirmed that toast message appears when a new user is register.

### Signin

- I confirmed that existing user can login by clicking on login page.
- I confirmed if the user forget the password they will redirected to forget password page.
- I confirmed that toast message appears when user signin.

### Forget password

- I confirmed that user receive an email with a link to change their password.

### Signout

- I confirmed that user can logout by clicking on logout button and a successfully signout message appears.

## Further testing

<details><summary>Details</summary><br/>
I asked friends and family to look at the application on their devices, browsers and report any issues they find. A few responsiveness and semantical issues were resolved as a result of this.
</details>

## Bugs

- In mobile and ipad device navbar toggler icon was not appering, then I have added class navbar dark and bg dark and the bug was fixed.

- There was a Problem with Header padding, because the header is implemented with position: fixed, I had to set a padding-top for the main container so it appears as if it is positioned below the header's content. In order to find the padding-top value that matches the header's height for every device, I used javascript to dynamically adjust it. This is why when testing the website for responsiveness using dev tools, the padding only changes its value on page reload. This bug is not visible when testing on real devices.

- Admin user was not able to edit the product details. Because in ProductForm class, the issue with the "category" field arises because it's defined as a forms.ChoiceField, but it should be a ModelChoiceField instead. The ModelChoiceField is specifically designed to handle foreign key relationships between models, like the "category" field in your Product model.
