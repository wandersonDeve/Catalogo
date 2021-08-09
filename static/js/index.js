let img1 = document.getElementById('img-1')
let img2 = document.getElementById('img-2')
let img3 = document.getElementById('img-3')
let img4 = document.getElementById('img-4')
let img5 = document.getElementById('img-5')

window.addEventListener('resize', () => {
    let w = window.innerWidth;

    if (w<500){
        img1.src = "../static/img/star_wars_home_mobile.jpg";
        img2.src = "../static/img/stranger_thing_home_mobile.jpg"; 
        img3.src = "../static/img/fringe_home_mobile.jpg";
        img4.src = "../static/img/friends_home_mobile.jpg"; 
        img5.src = "../static/img/ilha_do_medo_home_mobile.jpg"

    } else {
        img1.src = "../static/img/star_wars_home.jpg";
        img2.src = "../static/img/stranger_things_home.jpg"; 
        img3.src = "../static/img/fringe_home.jpg";
        img4.src = "../static/img/friends_home.jpg"; 
        img5.src = "../static/img/ilha_do_medo_home.jpg"
    }

})