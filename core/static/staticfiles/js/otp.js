// CSRF Token Handling for Django Form Submission
document.addEventListener('DOMContentLoaded', function() {
    // Function to get CSRF token from cookies
    function getCsrfToken() {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Looking for the CSRF cookie (typically named csrftoken in Django)
                if (cookie.substring(0, 10) === 'csrftoken=') {
                    cookieValue = decodeURIComponent(cookie.substring(10));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // Function to add CSRF token to AJAX requests
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    // Setup AJAX to include CSRF token
    function setupAjaxCSRF() {
        const csrftoken = getCsrfToken();

        // Use Fetch API or XMLHttpRequest for AJAX submissions
        const form = document.querySelector('form');
        if (form) {
            form.addEventListener('submit', function(e) {
                e.preventDefault(); // Prevent default form submission

                // Create FormData object to capture form inputs
                const formData = new FormData(form);

                // Add CSRF token to FormData if not already present
                if (!formData.get('csrfmiddlewaretoken')) {
                    formData.append('csrfmiddlewaretoken', csrftoken);
                }

                // Fetch API submission example
                fetch(form.action, {
                    method: 'POST',
                    body: formData,
                    headers: {
                        'X-CSRFToken': csrftoken, // Django expects this header
                        // Uncomment if needed:
                        // 'X-Requested-With': 'XMLHttpRequest'
                    },
                    credentials: 'same-origin' // Important for cookie-based authentication
                })
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.json(); // or response.text() depending on server response
                })
                .then(data => {
                    // Handle successful submission
                    console.log('Success:', data);
                    // Optional: Show success message to user
                    alert('Form submitted successfully!');
                })
                .catch(error => {
                    // Handle errors
                    console.error('Error:', error);
                    // Optional: Show error message to user
                    alert('There was a problem submitting the form.');
                });
            });
        }
    }

    // Initialize CSRF protection
    setupAjaxCSRF();

    // Optional: Alternative method using jQuery if you're using it
    // Uncomment and adapt if jQuery is available
    /*
    $(document).ready(function() {
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type)) {
                    xhr.setRequestHeader("X-CSRFToken", getCsrfToken());
                }
            }
        });
    });
    */
});

// Additional Notes:
// 1. Ensure your Django view is configured to accept AJAX requests
// 2. Make sure CSRF_COOKIE_HTTPONLY is set appropriately in Django settings
// 3. This script assumes the CSRF token is in a cookie named 'csrftoken'