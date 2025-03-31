
//// modo claro e modo escuro
const toggleButton = document.getElementById('toggle-mode');
const body = document.body;

if (localStorage.getItem('darkMode') === 'enabled') {
    body.classList.add('dark-mode');
}

toggleButton.addEventListener('click', () => {
    body.classList.toggle('dark-mode');
    if (body.classList.contains('dark-mode')) {
        localStorage.setItem('darkMode', 'enabled');
    } else {
        localStorage.setItem('darkMode', 'disabled');
    }
});



document.getElementById("scroll-btn").addEventListener("click", function() {
document.getElementById("minha-secao").scrollIntoView({ behavior: "smooth" });
});