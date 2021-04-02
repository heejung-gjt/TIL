const $second = document.querySelector('.second');
const $minute = document.querySelector('.minute');
const $hour = document.querySelector('.hour');

// setInterval(mytimer, 100);
let now = new Date();

let secondDeg = now.getSeconds()*6;
let minuteDeg = now.getMinutes()*6;
let hourDeg =  now.getHours()*30;


// function mytimer() {
//     $second.style.setProperty('--deg',secondDeg+=0.6)
//     $minute.style.setProperty('--deg',minuteDeg+=0.01)
//     $hour.style.setProperty('--deg',hourDeg+=1/1200)
// }

setInterval(() =>{
    $second.style.setProperty('--deg',secondDeg+=0.6)
    $minute.style.setProperty('--deg',minuteDeg+=0.01)
    $hour.style.setProperty('--deg',hourDeg+=1/1200)
}, 100);


// myTimer();

console.log(neq)