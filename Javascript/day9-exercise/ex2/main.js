const $scrollIcon = document.querySelector('.scroll-icon');


$scrollIcon.onclick = () => {
    // // window.scrollTo(0,0)
    // yOffset = window.pageYOffset;
    // console.log(yOffset);
    window.scroll({
        top:0,
        behavior:'smooth'
    });
}
//window.onscroll = () => {} (추천 !)
window.addEventListener('scroll',() =>{
    
    // if(window.pageYOffset >= 100){
    //     console.log(window.pageYOffset)
    //     $scrollIcon.style.display='block';
    // }
    // else{
    //     $scrollIcon.style.display='none';
    // }
    $scrollIcon.style.display = window.pageYOffset >= 100 ? 'block' : 'none';

})

