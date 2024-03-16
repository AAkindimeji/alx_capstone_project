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
    let firstName = document.getElementById('first-name').value.trim();
    let surname = document.getElementById('surname').value.trim();
    let email = document.getElementById('email').value.trim();
    let message = document.getElementById('message').value.trim();

    if (firstName === '' || surname === '' || email === '' || message === '') {
        alert('Please fill in all fields');
        return;
    }

    // Email validation
    let emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        alert('Please enter a valid email address');
        return;
    }

    // Message length validation
    if (message.split(' ').length > 300) {
        alert('Message should not exceed 300 words');
        return;
    }

    // Display thank you message and hide form
    document.getElementById('thank-you-message').innerText = "Thanks for reaching out, we will get back to you soon.";
    document.getElementById('contact-form').style.display = 'none';

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
