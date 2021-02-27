var updateBtns = document.querySelectorAll(".update-cart");

updateBtns.forEach((updateBtn) => {
  updateBtn.addEventListener("click", function () {
    var productId = this.dataset.product;
    var action = this.dataset.action;
    console.log(productId, action);

    console.log("User:", user);

    if (user == "AnonymousUser") {
      console.log("User is not authenticated");
    } else {
      updateUserOrder(productId, action);
    }
  });
});

function updateUserOrder(productId, action) {
  console.log("User is authenticated, sending data...");

  var url = "/update_item/";

  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({ productId: productId, action: action }),
  })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      location.reload();
    });
}
