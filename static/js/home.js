const toolTip = document.getElementById("tool-tip");
const endDate = "{{entry[4]}}";

const endDateFormat = new Date(endDate);

// toolTip.style.color = "orange"


const days = new Date().getDate()
toolTip.dataset.styleType = `Number of Remaining Days: ${days}`

toolTip.classList.add(days <= 3 ? "red" : days <= 7 ? "orange" : "")


console.log('toolTip', toolTip)



