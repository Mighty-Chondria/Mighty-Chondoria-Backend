
    // Function to check authentication state
    function checkAuthState() {
        const user = auth.currentUser;
        return !!user; // Returns true if the user is logged in, false otherwise
      }
        
    document.addEventListener('DOMContentLoaded', function () {
        console.log('Page loaded');
        // Wait for Firebase to load
        if (app) {
            // Check authentication state when the page is loaded
            if (!checkAuthState()) {
                // User is not logged in, redirect to the login page
                window.location.href = 'login.html'; // Replace with the actual URL of your login page
            }
        }
    });