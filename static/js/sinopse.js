let estrela_1 = document.querySelector("#estrela_1");
let estrela_2 = document.querySelector("#estrela_2");
let estrela_3 = document.querySelector("#estrela_3");
let estrela_4 = document.querySelector("#estrela_4");
let estrela_5 = document.querySelector("#estrela_5");

estrela_1.addEventListener("click", () => {
  estrela_1.style.color = "gold";
  estrela_2.style.color = "white";
  estrela_3.style.color = "white";
  estrela_4.style.color = "white";
  estrela_5.style.color = "white";
});

estrela_2.addEventListener("click", () => {
  estrela_1.style.color = "gold";
  estrela_2.style.color = "gold";
  estrela_3.style.color = "white";
  estrela_4.style.color = "white";
  estrela_5.style.color = "white";
});

estrela_3.addEventListener("click", () => {
  estrela_1.style.color = "gold";
  estrela_2.style.color = "gold";
  estrela_3.style.color = "gold";
  estrela_4.style.color = "white";
  estrela_5.style.color = "white";
});

estrela_4.addEventListener("click", () => {
  estrela_1.style.color = "gold";
  estrela_2.style.color = "gold";
  estrela_3.style.color = "gold";
  estrela_4.style.color = "gold";
  estrela_5.style.color = "white";
});

estrela_5.addEventListener("click", () => {
  estrela_1.style.color = "gold";
  estrela_2.style.color = "gold";
  estrela_3.style.color = "gold";
  estrela_4.style.color = "gold";
  estrela_5.style.color = "gold";
});
