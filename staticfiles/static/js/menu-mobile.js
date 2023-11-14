const menuDiv = document.getElementById('menu-mobile');
const btnAnimar = document.getElementById('btn-menu');

menuDiv.addEventListener('click', animarMenu)

function animarMenu(){
    menuDiv.classList.toggle('open')
    btnAnimar.classList.toggle('ativar')
}