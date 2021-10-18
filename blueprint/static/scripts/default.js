const app = {
    init: function () {
        console.log(3);
        product.init();
        product.modalValidation();
    }
}

const product = {
    init: function () {
        let newProduct = document.getElementById('new-product');
        newProduct.addEventListener('click', actionProduct);
        function actionProduct(e) {
            let description = document.getElementById('description');
            let sku = document.getElementById('sku');
            let price = document.getElementById('price');
            let quantity = document.getElementById('quantity');
            console.log(e, this);
            console.log(description.value, sku.value, price.value, quantity.value);
        }
    },
    modalValidation: function () {
        // Example starter JavaScript for disabling form submissions if there are invalid fields
        (function () {
            'use strict'
            console.log(26);
            // Fetch all the forms we want to apply custom Bootstrap validation styles to
            var forms = document.querySelectorAll('.needs-validation')

            // Loop over them and prevent submission
            Array.prototype.slice.call(forms)
                .forEach(function (form) {
                    form.addEventListener('submit', function (event) {
                        if (!form.checkValidity()) {
                            event.preventDefault()
                            event.stopPropagation()
                        }

                        form.classList.add('was-validated')
                    }, false)
                })
        })()
    }
}
console.log(6);
document.addEventListener('DOMContentLoaded', app.init);