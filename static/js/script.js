let html_link = document.querySelector('#link')
let link_completo = html_link.Value
let link_id = link_completo.substring(link.length-11, link.length)

html_link.addEventListener('keyup', () => {
    if(html_link.value.indexOf('youtu.be') == -1 || inputEmail.value.indexOf('www.youtube.com') == -1){
        html_link.style.borderColor = 'red'
      emailOk = false
    } else {
        html_link.style.borderColor = 'green'
      emailOk = true
    } 
})