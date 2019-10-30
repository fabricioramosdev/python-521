'use strict';

var tooglePasswordButton = document.getElementById('toggle-password');
tooglePasswordButton.onclick = ()=> {
    let passwordInput = document.getElementById('password');
    if (passwordInput.type == 'password') {
        passwordInput.type = 'text';
    } else {
        passwordInput.type = 'password';
    }
}
