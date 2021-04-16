const $toggle = document.querySelector('.toggle');
$nav = document.querySelector('nav');

$toggle.onclick = () => {
    $nav.classList.toggle('active');
}