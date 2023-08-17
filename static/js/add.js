const title = document.querySelector('#title')
const price = document.querySelector("#price")
const startDate = document.querySelector("#start")
const endDate = document.querySelector("#end")
const amount = document.querySelector("#amount")
const selectedRate = document.querySelector("#rate")
const select = document.querySelector('.select')

amount.style.display = "none";

price.addEventListener("keyup", function(){
    if (price.value != ''){
       let result = Number(price.value) * 4;
        amount.innerHTML = result;
        amount.style.display = "inline";
        amount.style.marginLeft = "15px"
        amount.style.background = "#040"
    } else {
        amount.innerHTML = "";
        amount.style.display = "inline";
        amount.style.marginLeft = "15px"
        amount.style.background = "#b71105"
    }
})

