console.log("Hello JavaScript!");
document.querySelector("h1").style.color = "blue";
document.addEventListener("DOMContentLoaded", () => {
    const message = document.createElement("h1");
    message.textContent = "Vai se fuder Febba";
message.style.color = "red";
    document.body.appendChild(message);
});