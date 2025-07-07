document.addEventListener('DOMContentLoaded', () => {
    const productSections = document.querySelectorAll('.product-section');
    const navLinks = document.querySelectorAll('.nav-links a');
    const hero = document.querySelector('.hero');
    const imageContainer = document.querySelector(".image-container");
    const productImage = document.getElementById("productImage");
    const tableRows = document.querySelectorAll("tbody tr");
    const inquiryButtons = document.querySelectorAll(".inquiry-btn");

    if (productSections.length > 0) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate');
                } else {
                    entry.target.classList.remove('animate');
                }
            });
        }, { threshold: 0.1 });

        productSections.forEach(section => {
            observer.observe(section);
        });
    }

    if (navLinks.length > 0) {
        navLinks.forEach(link => {
            link.addEventListener('click', (e) => {
                if (link.getAttribute('href').startsWith('#')) {
                    e.preventDefault();
                    const targetId = link.getAttribute('href');
                    const targetElement = document.querySelector(targetId);

                    if (targetElement) {
                        targetElement.scrollIntoView({
                            behavior: 'smooth',
                            block: 'start'
                        });
                    }
                }
            });

            if (link.getAttribute('href') === window.location.pathname) {
                link.setAttribute('aria-current', 'page');
            }
        });
    }

    if (hero) {
        window.addEventListener('scroll', () => {
            const scrollPosition = window.pageYOffset;
            hero.style.backgroundPositionY = `${scrollPosition * 0.7}px`;
        });
    }

    if (imageContainer && productImage) {
        imageContainer.addEventListener("mousemove", (e) => {
            const { left, top, width, height } = imageContainer.getBoundingClientRect();
            const x = (e.clientX - left) / width;
            const y = (e.clientY - top) / height;
            productImage.style.transformOrigin = `${x * 100}% ${y * 100}%`;
        });

        imageContainer.addEventListener("mouseleave", () => {
            productImage.style.transformOrigin = "center center";
        });
    }

    if (tableRows.length > 0) {
        tableRows.forEach((row) => {
            row.addEventListener("mouseenter", () => {
                row.style.backgroundColor = "#f0f0f0";
                row.style.transition = "background-color 0.3s ease";
            });
            row.addEventListener("mouseleave", () => {
                row.style.backgroundColor = "";
            });
        });
    }

    if (inquiryButtons.length > 0) {
        inquiryButtons.forEach((button) => {
            button.addEventListener("click", function () {
                const row = this.closest("tr");
                if (row) {
                    const productCode = row.querySelector("td:first-child")?.textContent;
                    const size = row.querySelector("td:nth-child(2)")?.textContent;
                    if (productCode && size) {
                        alert(`Inquiry sent for Product Code: ${productCode}, Size: ${size}`);
                    }
                }
            });
        });
    }
});