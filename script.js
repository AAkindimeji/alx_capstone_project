// Smooth scrolling
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Form validation
document.getElementById('contact-form').addEventListener('submit', function(e) {
    e.preventDefault();
    let name = document.getElementById('name').value.trim();
    let email = document.getElementById('email').value.trim();
    let message = document.getElementById('message').value.trim();

    if (name === '' || email === '' || message === '') {
        alert('Please fill in all fields');
        return;
    }

    // You can add more advanced validation logic here for email format, etc.

    // If all fields are filled, you can submit the form via AJAX or perform other actions.
    // For demonstration purposes, let's just log the form data.
    console.log('Name:', name);
    console.log('Email:', email);
    console.log('Message:', message);
    // Reset the form
    document.getElementById('contact-form').reset();
});

// Add active class to the navigation item based on scroll position
window.addEventListener('scroll', function() {
    let sections = document.querySelectorAll('section');
    let navLinks = document.querySelectorAll('.nav-item a');

    sections.forEach(section => {
        let top = section.offsetTop - 50;
        let height = section.clientHeight;
        let id = section.getAttribute('id');

        if (window.pageYOffset >= top && window.pageYOffset < top + height) {
            navLinks.forEach(link => {
                link.classList.remove('active');
            });
            document.querySelector(`.nav-item a[href="#${id}"]`).classList.add('active');
        }
    });
});
