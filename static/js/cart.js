var updateBtns = document.querySelectorAll(".update-cart");
console.log(updateBtns);
updateBtns.forEach((updateBtn) => {
  updateBtn.addEventListener("click", function () {
    var productId = this.dataset.product;
    var action = this.dataset.action;
    console.log(productId, action);

    console.log("User:", user);

    if (user == "AnonymousUser") {
      console.log("User is not authenticated");
    } else {
      console.log("User Logined sending data");
    }
  });
});
