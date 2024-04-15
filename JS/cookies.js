const cookieBox = document.querySelector(".wrapper"),
  buttons = document.querySelectorAll(".button");

const executeCodes = () => {
  if (document.cookie.includes("codinglab")) return;
  cookieBox.classList.add("show");

  buttons.forEach((button) => {
    button.addEventListener("click", () => {
      cookieBox.classList.remove("show");


      if (button.id == "acceptBtn") {
        document.cookie = "cookieBy= codinglab; max-age=" + 10;
      }

      if (button.id == "declineBtn") {
        document.location.href="https://www.ravbug.com/bsod/bsod10/";




      }
    });
  });
};

window.addEventListener("load", executeCodes);