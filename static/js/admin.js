document.addEventListener('DOMContentLoaded', function() {
    const typeSelect = document.querySelector("#id_type")
    const categorySelect = document.querySelector("#id_category");
    const subcategorySelect = document.querySelector("#id_subcategory");

    if (typeSelect) {
        typeSelect.addEventListener("change", function() {
            const typeId = this.value;

            fetch(`http://127.0.0.1:8000/get-categories/?type=${typeId}`)
                .then(response => response.json())
                .then(data => {
                    categorySelect.innerHTML = '<option value="">---------</option>';

                    data.categories.forEach(function(category) {
                        const option = document.createElement("option");
                        option.value = category.id;
                        option.text = category.name;
                        categorySelect.appendChild(option);
                    });
                });
        });
    }

    if (categorySelect) {
        categorySelect.addEventListener("change", function() {
            const categoryId = this.value;

            fetch(`http://127.0.0.1:8000/get-subcategories/?category=${categoryId}`)
                .then(response => response.json())
                .then(data => {
                    subcategorySelect.innerHTML = '<option value="">---------</option>';

                    data.subcategories.forEach(function(subcategory) {
                        const option = document.createElement("option");
                        option.value = subcategory.id;
                        option.text = subcategory.name;
                        subcategorySelect.appendChild(option);
                    });
                });
        });
    }
});

