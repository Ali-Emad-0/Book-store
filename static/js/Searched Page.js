// js/Searched Page.js
window.scrollSearchCarousel = function(btn, dir) {
    let container = document.getElementById('searchedBookCarousel');
    // Find a real .book width at runtime for perfect scrolling
    let book = container.querySelector('.book');
    let scrollAmount = book ? (book.offsetWidth + 20) * dir : 180 * dir;
    container.scrollBy({ left: scrollAmount, behavior: 'smooth' });
}