document.addEventListener("DOMContentLoaded", () => {
  let currentPage = 0
  const pages = document.querySelectorAll(".page")
  const totalPages = pages.length

  function updatePagePositions() {
    pages.forEach((page, index) => {
      if (index < currentPage) {
        page.style.transform = "rotateY(-180deg)"
        page.style.zIndex = index.toString() // Flipped pages go behind
      } else {
        page.style.transform = "rotateY(0deg)"
        page.style.zIndex = (totalPages - index).toString() // Unflipped pages stay above
      }
    })
  }

  function flipNext() {
    if (currentPage < totalPages - 1) {
      currentPage++
      updatePagePositions()
    }
  }

  function flipPrev() {
    if (currentPage > 0) {
      currentPage--
      updatePagePositions()
    }
  }

  // Initialize page positions
  updatePagePositions()

  // Button event listeners
  const prevButton = document.querySelector(".controls button:first-child")
  const nextButton = document.querySelector(".controls button:last-child")

  if (prevButton) {
    prevButton.addEventListener("click", flipPrev)
  }

  if (nextButton) {
    nextButton.addEventListener("click", flipNext)
  }

  // Page click event listeners
  pages.forEach((page, index) => {
    page.addEventListener("click", () => {
      if (index === currentPage - 1) {
        flipPrev()
      } else if (index === currentPage) {
        flipNext()
      }
    })
  })

  // Function to download catalogue as PDF
  window.downloadPDF = () => {
    if (typeof window.jspdf === "undefined") {
      console.error("jsPDF library is not loaded")
      return
    }

    const { jsPDF } = window.jspdf
    const pdf = new jsPDF("portrait", "mm", "a4") // Create a new PDF

    pages.forEach((page, index) => {
      const pageFront = page.querySelector(".page-front img")
      const pageBack = page.querySelector(".page-back img")

      if (pageFront) {
        // Add the front page image to PDF
        pdf.addImage(pageFront.src, "JPEG", 10, 10, 190, 270) // Adjust the coordinates and size
      }

      if (index < totalPages - 1) {
        pdf.addPage() // Add a new page for the back side
      }

      if (pageBack) {
        // Add the back page image to PDF
        pdf.addImage(pageBack.src, "JPEG", 10, 10, 190, 270) // Adjust the coordinates and size
      }

      if (index < totalPages - 1) {
        pdf.addPage() // Add a new page for the next one
      }
    })

    // Save the PDF
    pdf.save("catalogue.pdf")
  }
})

