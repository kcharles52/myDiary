//Switch tabs on the home page
function switchTab(evt, tabName) {
    var classes = document.getElementsByClassName('tab')
    switch (tabName) {
        case 'login':
            document.getElementById(tabName).style.display = "block";
            document.getElementById('signup').style.display = "none";
            classes[0].className = classes[0].className.replace(' active', '');
            classes[1].className += ' active';
            break;

        case 'signup':
            document.getElementById(tabName).style.display = "block";
            document.getElementById('login').style.display = "none";
            classes[1].className = classes[0].className.replace(' active', '');
            classes[0].className += ' active';
            break;

    }

}