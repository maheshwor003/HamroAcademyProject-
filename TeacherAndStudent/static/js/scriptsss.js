const nav = document.querySelector('.nav')
fetch('/headernav.html')
    .then(res => res.text())
    .then(data => {
        nav.innerHTML = data
    })