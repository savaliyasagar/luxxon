document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("contactForm")
    const status = document.getElementById("status")
  
    form.addEventListener("submit", (e) => {
      e.preventDefault()
  
      const formData = new FormData(form)
  
      fetch(form.action, {
        method: "POST",
        body: formData,
        headers: {
          "X-CSRFToken": formData.get("csrfmiddlewaretoken"),
        },
      })
        .then((response) => response.text())
        .then((html) => {
          // Replace the entire page content with the response
          document.documentElement.innerHTML = html
  
          // Scroll to the top of the page
          window.scrollTo(0, 0)
        })
        .catch((error) => {
          console.error("Error:", error)
          status.textContent = "An error occurred. Please try again."
          status.style.color = "red"
        })
    })
  })
  
  