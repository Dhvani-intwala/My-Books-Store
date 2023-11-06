# Testing

Back to the [README](README.md)

- Testing has taken place continuously throughout the development of the project. Each view was tested regularly.When the outcome was not as expected, debugging took place at that point.  

### Python Validation - Pycodestyle

-Python testing was done using the Pycodestyle to ensure there were no syntax errors in the project. All python files
were entered into the checker and no errors were found in any of the custom codes.

![Pycodestyle results]().

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

The Javascript code was validated using using [JsHint](https://jshint.com/)<br>
At the time of deployment the validation for *script.js* has the following outcome:<br><br>

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

### CSS Validation

![CSS Validation](/media/cssvalidation.png)

- Custom CSS was validated using W3C Jigsaw validation service. Fifty-three warnings were displayed, however, 
  these are related to Google Fonts and vendor extension prefixes which will not affect the CSS performance.

## Manual Testing
