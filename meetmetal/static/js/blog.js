document.addEventListener("DOMContentLoaded", () => {
    const blogPosts = document.querySelectorAll(".blog-post")
  
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry, index) => {
          if (entry.isIntersecting) {
            setTimeout(() => {
              entry.target.style.animation = `fadeIn 0.5s ease-out ${index * 0.1}s forwards`
            }, index * 100)
            observer.unobserve(entry.target)
          }
        })
      },
      { threshold: 0.1 },
    )
  
    blogPosts.forEach((post) => {
      observer.observe(post)
    })
  })
  
  