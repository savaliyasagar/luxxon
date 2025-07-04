document.addEventListener("DOMContentLoaded", () => {
    const body = document.querySelector("body")
    const nav = document.querySelector("nav")
    const searchToggle = document.querySelector(".searchToggle")
    const sidebarOpen = document.querySelector(".sidebarOpen")
    const siderbarClose = document.querySelector(".siderbarClose")
  
    if (searchToggle) {
      searchToggle.addEventListener("click", () => {
        searchToggle.classList.toggle("active")
      })
    }
  
    if (sidebarOpen) {
      sidebarOpen.addEventListener("click", () => {
        if (nav) nav.classList.add("active")
      })
    }
  
    if (body) {
      body.addEventListener("click", (e) => {
        const clickedElm = e.target
        if (!clickedElm.classList.contains("sidebarOpen") && !clickedElm.classList.contains("menu")) {
          if (nav) nav.classList.remove("active")
        }
      })
    }
  
    const imageContainer = document.getElementById("imageZoomContainer")
    const productImage = document.getElementById("productImage")
  
    if (imageContainer && productImage) {
      let isZoomed = false
      let zoomLevel = 1.5
  
      function handleZoom(e) {
        const rect = imageContainer.getBoundingClientRect()
        const x = e.clientX - rect.left
        const y = e.clientY - rect.top
  
        const xPercent = x / rect.width
        const yPercent = y / rect.height
  
        if (isZoomed) {
          productImage.style.transformOrigin = `${xPercent * 100}% ${yPercent * 100}%`
          productImage.style.transform = `scale(${zoomLevel})`
        } else {
          productImage.style.transformOrigin = "center center"
          productImage.style.transform = "scale(1)"
        }
      }
  
      imageContainer.addEventListener("mouseenter", (event) => {
        isZoomed = true
        handleZoom(event)
      })
  
      imageContainer.addEventListener("mousemove", handleZoom)
  
      imageContainer.addEventListener("mouseleave", (event) => {
        isZoomed = false
        handleZoom(event)
      })
  
      function adjustZoomForMobile() {
        if (window.innerWidth <= 768) {
          zoomLevel = 1.2
        } else {
          zoomLevel = 1.5
        }
      }
  
      window.addEventListener("resize", adjustZoomForMobile)
      adjustZoomForMobile()
    }
  
    const slideUpElements = document.querySelectorAll(".slide-up")
  
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("active")
            observer.unobserve(entry.target)
          }
        })
      },
      {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px",
      },
    )
  
    slideUpElements.forEach((element) => {
      observer.observe(element)
    })
  
    const navLinks = document.querySelectorAll(".nav-link")
    const currentPath = window.location.pathname
  
    navLinks.forEach((link) => {
      const linkPath = link.getAttribute("href")
  
      // Ensure we compare properly formatted URLs
      const isHome = link.dataset.page === "home" && currentPath === "/"
      const isActive = currentPath === linkPath || (currentPath.startsWith(linkPath) && linkPath !== "/")
  
      if (isHome || isActive) {
        link.classList.add("active")
      }
  
      link.addEventListener("click", function () {
        navLinks.forEach((l) => l.classList.remove("active"))
        this.classList.add("active")
      })
    })
  
    const testimonialWrapper = document.querySelector(".testimonial-wrapper")
    const testimonials = document.querySelectorAll(".testimonial")
    const indicatorContainer = document.querySelector(".indicator-container")
    let currentIndex = 0
  
    if (testimonialWrapper && testimonials.length > 0 && indicatorContainer) {
      // Create indicators
      testimonials.forEach((_, index) => {
        const indicator = document.createElement("div")
        indicator.classList.add("indicator")
        if (index === 0) indicator.classList.add("active")
        indicator.addEventListener("click", () => goToTestimonial(index))
        indicatorContainer.appendChild(indicator)
      })
  
      function updateIndicators() {
        document.querySelectorAll(".indicator").forEach((indicator, index) => {
          if (index === currentIndex) {
            indicator.classList.add("active")
          } else {
            indicator.classList.remove("active")
          }
        })
      }
  
      function goToTestimonial(index) {
        currentIndex = index
        testimonialWrapper.style.transform = `translateX(-${currentIndex * 100}%)`
        updateIndicators()
      }
  
      function nextTestimonial() {
        currentIndex = (currentIndex + 1) % testimonials.length
        goToTestimonial(currentIndex)
      }
  
      // Auto-rotate testimonials every 5 seconds
      setInterval(nextTestimonial, 5000)
  
      // Touch events for mobile swipe
      let touchStartX = 0
      let touchEndX = 0
  
      testimonialWrapper.addEventListener("touchstart", (e) => {
        touchStartX = e.changedTouches[0].screenX
      })
  
      testimonialWrapper.addEventListener("touchend", (e) => {
        touchEndX = e.changedTouches[0].screenX
        handleSwipe()
      })
  
      function handleSwipe() {
        if (touchStartX - touchEndX > 50) {
          nextTestimonial()
        } else if (touchEndX - touchStartX > 50) {
          currentIndex = (currentIndex - 1 + testimonials.length) % testimonials.length
          goToTestimonial(currentIndex)
        }
      }
    }
  })
  
