const $count = document.querySelector('.counter');
const $increase = document.querySelector('.increase');
const $decrease = document.querySelector('.decrease');

// $count.textContent = 0

$increase.onclick = () => {
    $count.textContent = +$count.textContent +1 
}


$decrease.onclick = () => {
    if($count.textContent <= 0)return;
    $count.textContent = +$count.textContent -1; 
}

