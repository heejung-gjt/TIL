// 디스트럭처링

const [$startBtn, $resetBtn] = [...document.querySelectorAll('.stopwatch >.control')];

let msCnt = 0;
$startBtn.onclick = () => {
    setInterval(() =>{

    }, 100);

}


$increase.onclick = () => {
    $count.textContent = +$count.textContent +1 
}
