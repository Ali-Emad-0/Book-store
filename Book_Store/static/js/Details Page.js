function scrollCarousel(button, direction) {
    const container = button.parentElement.querySelector(".book-carousel");
    const scrollAmount = 900;
    container.scrollBy({ left: direction * scrollAmount, behavior: "smooth" });
}
