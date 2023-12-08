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

The Javascript code was validated using using [JsHint](https://jshint.com/)
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

![HTML Validation](/media/htmlvalidation.png)

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

## Manual Testing

| Feature | Test  | Expected Result | Actual Result |
| -------------| ----- | ----- | :----: |
| My Books Store  | Selecting logo on homepage |  directs user back to homepage |  Pass |
| Search | Using the search box | Entering a search returns expected result  |  Pass |
| Search no results | No search | Entering a no results search returns error message and shows all products  |  Pass |
| Navigation Links  | Selecting navigation links |  directs user to relevant pages |  Pass |
| All products  | Selecting all products |  directs user to all products |  Pass |
| Back to top | Back to top arrow | Select the arrow box on the products page brings the user back to the top of the page  |  Pass |
| Sort By  | Selecting the filter Sort |  successfully sort by price, name and category options |  Pass |
| Shop our button  | Selecting Shop our button |  directs user to all  products page |  Pass |
| Adjust quantity | Plus or minus button |  adjust the quantity of product |  Pass |
| Add to bag | Adding to bag | successfully add products to bag| Pass |
| Keep Shopping | Keep shopping button |  directs user back to all products page  |  Pass |
| Delete from bag | deleting products from bag | successfully delete products from bag| Pass |
| Shopping bag  | Shows the added products and total |  directs user to checkout page |  Pass |
| Secure Checkout button  | Using the secure checkout button |  directs user to checkout form and payment details |  Pass |
| Sign up for our newsletter | selecting Sign up for our newsletter |  directs user Sign up for our newsletter page |  Pass |
| Privacy policy | Selecting privacy policy |  directs user to privacy policy|  Pass |
| facebook icon | Selecting  facebook icon |  directs user to facebook page |  Pass |
| Special offers | Selecting all specials |  directs user to all special offers |  Pass |
| Leave a Comment when signed in | Submitting comment|  successfully submit and display comment |  Pass |
| Edit a Comment when signed in | Editing comment|  successfully submit and edit comment |  Pass |
| Delete a Comment when signed in | Deleting comment|  successfully deleted comment |  Pass |
| As Admin Delete Comment | Deleting comment|  successfully remove comment |  Pass |
| Contact | Selecting Contact | directs user to contact page  |  Pass |
| Contact form submission | submitting contact form | successfully sends submit form and can seen be in admin |  Pass |
| My account | Selecting my account as admin | displays dropdown menu unique to admin apart from profile and logout  |  Pass |
| Add product | Adding a new product| successfully add new product to products page  |  Pass |
| Add Product | no image is selected | default image is used |  Pass |
| As Admin edit product | editing product |  successfully edited the product |  Pass |
| As Admin Delete product | Deleting product|  successfully remove product |  Pass |
| Register | Register for an account | selecting Register in my account directs user signup page |  Pass |
| Register | Registering as a new user | Registering as a new user form works |  Pass |
| Login | Login to an account | selecting Login in my account directs user to Login page |  Pass |
| Login | Login to an account | login-in as a new user form works |  Pass |
| Login as admin| Login to as admin gives access to blog/product management | login-in as a new user form works |  Pass |
| Logout | message shown | Logging out message shown |  Pass |
| Newsletter | Subscribe to newsletter|  successfully showed subscribed|  Pass |

## Bugs

- In mobile and ipad device navbar toggler icon was not appering, then I have added class navbar dark and bg dark and the bug was fixed.

- There was a Problem with Header padding, because the header is implemented with position: fixed, I had to set a padding-top for the main container so it appears as if it is positioned below the header's content. In order to find the padding-top value that matches the header's height for every device, I used javascript to dynamically adjust it. This is why when testing the website for responsiveness using dev tools, the padding only changes its value on page reload. This bug is not visible when testing on real devices.

- Admin user was not able to edit the product details. Because in ProductForm class, the issue with the "category" field arises because it's defined as a forms.ChoiceField, but it should be a ModelChoiceField instead. The ModelChoiceField is specifically designed to handle foreign key relationships between models, like the "category" field in your Product model.
