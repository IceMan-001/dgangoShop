async function removeItemFetch(event) {
    let productId = event.target.parentElement.parentElement.querySelector("#productId").value

    let itemInfo = {
        productIdValue: productId,
    };

    let response = await fetch('/cart/remove_fetch/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json;charset=utf-8',
        },
        body: JSON.stringify(itemInfo),
    });
}

async function removeItem(event) {
    await removeItemFetch(event);
    afterRemoveItem(event.target.parentElement.parentElement)
    setTimeout(updatePrice.bind(null, event), 2000);
}

async function getCartLength() {
    let response = await fetch('/cart/length/', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json;charset=utf-8',
        },
    });
    let result = await response.json();
    alert(result.cart_length, result.message);
};

function getTotalPriceCart() {
    let itemPriceInputs = document.querySelectorAll("#itemPrice");
    let totalPrice = 0;
    itemPriceInputs.forEach((item, index) => {
        totalPrice += +item.textContent;
    });
    let totalPriceCart = document.querySelector("#totalPriceCart");
    totalPriceCart.textContent = totalPrice;
    return totalPrice;
}

function getQuantityInCart() {
    let cartLengthHeader = document.querySelector("#cartLengthHeader")
    let quantityInputs = document.querySelectorAll("#prod_quantity");
    let allQuantity = 0;
    quantityInputs.forEach((item, index) => {
        allQuantity += +item.value;
    });
    let cartLength = document.querySelector("#cartLength");
    cartLength.textContent = allQuantity;
    cartLengthHeader.textContent = allQuantity;
    return allQuantity;
}

function updatePrice(event) {
    let quantity = event.target.value;
    let itemPrice = event.target.parentElement.parentElement.querySelector("#itemPrice")
    let productPrice = event.target.parentElement.parentElement.querySelector("#productPrice").textContent
    productPrice = Number(productPrice.replace(",", "."))

    let newItemPrice = productPrice * quantity;
    itemPrice.textContent = newItemPrice;
    getQuantityInCart();
    getTotalPriceCart();

};

function afterRemoveItem(item) {
    item.remove()
}

async function saveCartInSession(event) {
    let productId = event.target.parentElement.parentElement.querySelector("#productId").value
    let quantity = event.target.value;

    let cartInfo = {
        productIdValue: productId,
        quantityValue: quantity,
        totalQuantity: getQuantityInCart(),
        totalPrice: getTotalPriceCart(),
    };

    let response = await fetch('/cart/update_cart_session/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json;charset=utf-8',
        },
        body: JSON.stringify(cartInfo),
    });

    let result = await response.json();
};

const quantityInput = document.querySelectorAll("#prod_quantity")
quantityInput.forEach((item) => {
    item.addEventListener('change', updatePrice)
})
quantityInput.forEach((item) => {
    item.addEventListener('change', saveCartInSession)
})

const newOrderBtn = document.querySelector("#newOrder")
newOrderBtn.addEventListener('click', getCartLength)


const itemsRemove = document.querySelectorAll(".removeFetch")
itemsRemove.forEach((item) => {
    item.addEventListener('click', removeItem)
})

//ORDER MODAL
// Получаем элемент модального окна
const orderModal = document.querySelector("#orderModal")
const orderFormModal = document.querySelector("#orderFormModal")

// Получаем кнопку для открытия модального окна
const orderBtn = document.querySelector("#newOrder")
const quickOrderBtn = document.querySelector("#quickOrderBtn")


// Получаем кнопку для закрытия модального окна
const closeOrder = document.querySelector("#closeOrder")
const closeOrderForm = document.querySelector("#closeOrderForm")


// Открываем модальное окно по клику на кнопке оформить заказ
orderBtn.onclick = function () {
    orderModal.style.display = "block";
}


// Открываем модальное окно формы по клику на кнопке купить в 1 клик
quickOrderBtn.onclick = function () {
    orderModal.style.display = "none"; //закрываем предыдущее окно
    orderFormModal.style.display = "block";
}

// Закрытие модальное окна
closeOrder.onclick = function () {
    orderModal.style.display = "none";
}

closeOrderForm.onclick = function () {
    orderFormModal.style.display = "none";
}

//Закрываем модальное окно при клике вне его области
window.onclick = function (event) {
    if (event.target === orderModal) {
        orderModal.style.display = "none";
    }
    if (event.target === orderFormModal) {
        orderFormModal.style.display = "none";
    }
}

//CREATE ORDER
const createQuickOrderBtn = document.querySelector("#createQuickOrderBtn")

async function createQuickOrder(event) {
    const myForm = event.target.parentElement;
    const name = myForm.name.value;
    const lastName = myForm.last_name.value;
    const email = myForm.email.value;
    const phone = myForm.phone.value;
    const payment = myForm.payment.value;
    const delivery = myForm.delivery.value;

    let orderInfo = {
        "name": name,
        "lastName": lastName,
        "email": email,
        "phone": phone,
        "payment": payment,
        "delivery": delivery,
    };

    let response = await fetch('/orders/new/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json;charset=utf-8',
        },
        body: JSON.stringify(orderInfo),
    });

    let result = await response.json();
    alert('Заказ успешно создан!')
    window.location.replace(result.url);
};

createQuickOrderBtn.addEventListener('click', createQuickOrder)
