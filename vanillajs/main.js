// const selectElement = document.getElementById('.calc-1');

// selectElement.addEventListener('change', (event) => {
//   const result = document.querySelector('.result');
//   result.textContent = `You like ${event.target.value}`;
// });


//alert("Hello World!");
document.getElementById("demo1").addEventListener("click", myFunction);

function myFunction() {
  console.log("clicked my function")
  document.getElementById("change").innerHTML = "YOU CLICKED ME!";
}













const input = document.getElementById('.calc-1');
const log = document.getElementById('result');

input.addEventListener('change', updateValue);

function updateValue(e){
  log.textContent = e.target.value;
}

