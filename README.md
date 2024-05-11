# JUZCOOKIES bakery website

#### Video Demo:
#### code behind the webpage: https://youtu.be/xp3ji1hc0NQ
#### how the webpage works*: https://youtu.be/V9lyO-Y6vEI
*personal info in Youtube video description

#### Description:

My final project is inspired by my aunty's bakery. She is currently operating as a sole proprietor and it would be nice if i could design a webpage for her. Additionally the page serve as another platform to record orders from customers. The predominant language and framework i used was python and Django as the web framework. I chose to learn and implemenet django since it is the backbone of huge apps like Instagram, facebook, etc. In my Django app, I created 3 different app folders named Bakery, Cart and Mainpage. Bakery is responsible for the displaying of the pastries and cakes that we have in store as well as the ordering of the, Cart is for the displaying of a user's total orders, price and for them to make last minute changes to their item list and Mainpage is just for displahing an about us page and a contact us page. Due to security constraints, my app is not authorized to make card payments online via the app. However, the price will be reflected in the cart and in the django admin upon form submission and my aunt would thereby request payment from her customer via external payment methods. the django admin interface also makes the web extremely convenient for me and even others, who are not so famaliar with coding, to manage and control the app indepedently and with ease.

How the cart feature work:
Currently, the cart feature is done via the implementation of sessions. Each guest user is given a session account and a cart, in a form of a dictionary, to take down their orders. Each item is IDed with an item id which is assigned thanks to django's default assignment in their models.py file in each app. When users order a certain quantity of a pastry, a form is being submitted and the session-based cart would register the item's ID, price and quantity. When users want to checkout, the data in session-based cart is extracted and displaying in an lsited format. the last minutes of adding and removing items was done through JS and a fetch API which helps to edit the quantity variable in the cart without the tedious work of creating and resubmitting another html form. When everything is verified, users will be directed to a checkout page form which requires them to input their personal particulars and again confirm their orders, this time without being able to make last minute edits. Upon submission, all their particulars as well as the items in the cart will be recorded down into a database in django admin where my aunt will be able to view their items and their correspondong total prices.
