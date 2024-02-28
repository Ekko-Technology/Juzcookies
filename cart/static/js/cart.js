document.addEventListener("DOMContentLoaded", () => {
    // extract all listed items in order
    function updateCart(){
        let quantity_count = 0;
        let price_count = 0;
        const items = document.querySelectorAll(".item-index");
        items.forEach(item => {
            let quantity = parseInt(item.querySelector('.quantity-bought').innerText);
            let price = parseFloat(item.querySelector('.item-price').innerText);
            let totalAmount = item.querySelector('.total-amount')
            // integer variable of total amount
            let totalAmountInt = (quantity * price).toFixed(2)

            totalAmount.innerText = "$" + totalAmountInt;
            quantity_count += quantity;
            price_count += parseFloat(totalAmountInt);
        })

        // updating cart summary details
        let total_quantity = document.querySelector(".total-quantity");
        let total_price = document.querySelector(".total-price");
        total_quantity.innerText = quantity_count;
        total_price.innerText = "$" + price_count.toFixed(2);
    }
    
    // call updateCartfunction initially
    updateCart();


    // implementing quantity change for last min user edits on quantity
    const quantityElements = document.querySelectorAll(".responsive-quantity-value");

    quantityElements.forEach(quantityElement => {
        const quantityUpButton = quantityElement.querySelector('.quantity-up');
        const quantityDownButton = quantityElement.querySelector('.quantity-down');
        const quantity = quantityElement.querySelector(".quantity-bought");
        const product_id =  quantityElement.querySelector('.product-id').value;

        // adjusts quantity value by step 1 while making adjusted quantity bolded
        quantityUpButton.addEventListener("click", () => {
            const currentQuantity = parseInt(quantity.innerText);
            quantity.innerText = `${currentQuantity + 1}`;
            quantity.classList.add("fw-bold");
            // updating front-end display
            updateCart();
            // updating backend for session-based cart
            updateCartQuantity(product_id, currentQuantity + 1)
        });

        quantityDownButton.addEventListener("click", () => {
            const currentQuantity = parseInt(quantity.innerText);
            if (currentQuantity > 1){
                quantity.innerText = `${currentQuantity - 1}`;
                quantity.classList.add("fw-bold");
               // updating front-end display
                updateCart();
                // updating backend for session-based cart
                updateCartQuantity(product_id, currentQuantity - 1);
            } else if (currentQuantity == 1){
                quantity.parentElement.parentElement.remove();
                // updating front-end display
                updateCart();
                // updating backend for session-based cart
                updateCartQuantity(product_id, currentQuantity - 1);
            }
                
        });
    });

    // function to check if cart is empty. if user tries to checkout empty cart, function creates a div= to alert this error
    function validateCart() {
        const total_quantity = parseInt(document.querySelector(".total-quantity").innerText);
        const total_price = parseFloat(document.querySelector(".total-price").innerText.slice(1)); //slice function used to remove $ sign

        if (total_quantity == 0 || total_price == 0){
            // add bootstrap warning element
            let warning = document.createElement("div"); //creates a html tag 
            warning.className = "alert alert-danger mt-3";
            warning.role = "alert";
            warning.innerText = "Cart unable to checkout with 0 items or $0.00";
    
            let container = document.querySelector(".cart-container")
            // insert the alert before the first child of the container
            container.insertBefore(warning, container.firstChild);

            return false;
        }

        return true;
    }

    document.querySelector(".btn-checkout").addEventListener("click", () => {
        if (validateCart()) {
            // proceed to checkout
            window.location.href = "/cart/checkout/";
        }
    })

    // using fetch API to constantly update database upon user's changing of item quantity
    function updateCartQuantity(item_id, quantity) {
        console.log("updating cart....");
        console.log("item_id", item_id);

        // urlpatterns's link to the cart.html page
        var url = "/cart/items/";

        // fetching over the '/items/' URL and making a post request
        fetch( url, {
            method: 'POST',
            // content of body in fetch API has be in the form of a string JSON format
            body: JSON.stringify({'item_id': item_id, 'quantity': quantity}),
            headers: {
                'X-CSRFToken': csrftoken
            }
        })
        // first Promise used to read data as json object
        .then((response) =>{
            return response.json();
        })
        // second promise used to display that data on console
        .then((data) =>{
            console.log('data:', data);
            // // Update the total quantity and total price elements on the page
            // document.querySelector(".total-quantity").innerText = data.total_quantity;
            // document.querySelector(".total-price").innerText = "$" + data.total_price.toFixed(2);
        })
        .catch(error => console.error('Error:', error));
    }
});


