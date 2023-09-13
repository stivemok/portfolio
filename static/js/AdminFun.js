// Select the links in the "Manage User Accounts" section
const createUserLink = document.querySelector('a[href="create_user.html"]');
const updateUserLink = document.querySelector('a[href="update_user.html"]');
const deleteUserLink = document.querySelector('a[href="delete_user.html"]');

// Add event listeners to the links
createUserLink.addEventListener('click', function(event) {
    event.preventDefault();
    // Add your code here to handle the "Create a new user account" action
});

updateUserLink.addEventListener('click', function(event) {
    event.preventDefault();
    // Add your code here to handle the "Update an existing user account" action
});

deleteUserLink.addEventListener('click', function(event) {
    event.preventDefault();
    // Add your code here to handle the "Delete a user account" action
});

// Select the links in the "Manage Inventory" section
const addCarLink = document.querySelector('a[href="add_car.html"]');
const updateCarLink = document.querySelector('a[href="update_car.html"]');
const removeCarLink = document.querySelector('a[href="remove_car.html"]');

// Add event listeners to the links
addCarLink.addEventListener('click', function(event) {
    event.preventDefault();
    // Add your code here to handle the "Add a new car to inventory" action
});

updateCarLink.addEventListener('click', function(event) {
    event.preventDefault();
    // Add your code here to handle the "Update an existing car in inventory" action
});

removeCarLink.addEventListener('click', function(event) {
    event.preventDefault();
    // Add your code here to handle the "Remove a car from inventory" action
});

// Select the links in the "Manage Orders" section
const viewOrdersLink = document.querySelector('a[href="view_orders.html"]');
const updateOrderLink = document.querySelector('a[href="update_order.html"]');
const cancelOrderLink = document.querySelector('a[href="cancel_order.html"]');

// Add event listeners to the links
viewOrdersLink.addEventListener('click', function(event) {
    event.preventDefault();
    // Add your code here to handle the "View all orders" action
});

updateOrderLink.addEventListener('click', function(event) {
    event.preventDefault();
    // Add your code here to handle the "Update an order" action
});

cancelOrderLink.addEventListener('click', function(event) {
    event.preventDefault();
    // Add your code here to handle the "Cancel an order" action
});

// Select the links in the "Manage Website Content" section
const addPageLink = document.querySelector('a[href="add_page.html"]');
const updatePageLink = document.querySelector('a[href="update_page.html"]');
const removePageLink = document.querySelector('a[href="remove_page.html"]');

// Add event listeners to the links
addPageLink.addEventListener('click', function(event) {
    event.preventDefault();
    // Add your code here to handle the "Add a new page to the website" action
});

updatePageLink.addEventListener('click', function(event) {
    event.preventDefault();
    // Add your code here to handle the "Update an existing page on the website" action
});

removePageLink.addEventListener('click', function(event) {
    event.preventDefault();
    // Add your code here to handle the "Remove a page from the website" action
});

// Select the logout link
const logoutLink = document.querySelector('a[href="/logout"]');

// Add event listener to the link
logoutLink.addEventListener('click', function(event) {
    event.preventDefault();
    // Add your code here to handle the "Sign Out" action
    // For example, you might want to make an AJAX request to the server-side logout route
    fetch('/logout', { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // If the logout was successful, redirect to the login page
                window.location.href = '/login';
            } else {
                // If there was an error, display it
                alert('Error logging out: ' + data.error);
            }
        });
});
