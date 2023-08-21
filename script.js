/* document.querySelector('.login100-form-btn').addEventListener('click', function(event) {
    event.preventDefault();
    
     redirect to admin page
    window.location.href = 'file:///C:/Users/i/Desktop/portfolio/admin_page.html';
    window.location.href = `admin_page.html${queryString}`;
});*/
// Add an event listener to the login button
document.getElementById("loginButton").addEventListener("click", function() {
    // Open admin_page.html in a new window or tab
    window.open("admin_page.html", "_blank");
});