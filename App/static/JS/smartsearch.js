document.addEventListener("DOMContentLoaded", () => {
    const searchInput = document.getElementById("search-input");
    const cards = document.querySelectorAll(".sponsor-item");

    searchInput.addEventListener("input", function () {
        const searchValue = this.value.toLowerCase().trim();

        cards.forEach(card => {
            const category = (card.getAttribute("data-category") || "").toLowerCase();
            const companyName = (card.getAttribute("data-company") || "").toLowerCase();

            if (category.includes(searchValue) || companyName.includes(searchValue)) {
                card.style.display = "block";
            } else {
                card.style.display = "none";
            }
        });
    });
});
