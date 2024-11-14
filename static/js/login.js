const messageA = document.getElementById('messageA')
const messageB = document.getElementById('messageB')
const formRegister = document.getElementById('register_form')
const loginForm = document.getElementById('login_form')


messageB.onclick = function(){
    loginForm.style.display = "none"
    formRegister.style.display = "block"
}

messageA.onclick = function(){
    formRegister.style.display = "none"
    loginForm.style.display = "block"
}