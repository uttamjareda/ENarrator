/* ########## WOW ########## */
$(function () {
    new WOW().init();
});

/* ########## BLOGS ########## */
$(function () {
    $(".blogs-plural").owlCarousel({
        items: 1,
        autoPlay: true,
        smartSpeed: 700,
        loop: true,
        autoplayHoverPause: true,
        autoPlaySpeed: 5000,
        autoPlayTimeout: 5000,
        responsive: {
            // breakpoint from 0 up
        }
    });
})

/* ########## TEAM ########## */
$(function () {
    $("#team-members").owlCarousel({
        items: 3,
        autoplay: true,
        smartSpeed: 700,
        loop: true,
        autoplayHoverPause: true,
        responsive: {
            0: { items: 1 },
            680: { items: 2 },
            1000: { items: 3 }
        }
    });
})

/* ######### NAVBAR ######### */
$(function () {
    $(window).scroll(function () {
        if ($(this).scrollTop() < 50) {
            $("nav").removeClass("vesco-top-nav");
            $("#back-to-top").fadeOut();
        }
        else {
            $("nav").addClass("vesco-top-nav");
            $("#back-to-top").fadeIn();
        }
    });
});


/* ######### EVENTS ########## */
const track = document.querySelector('.carousel__track');
const slides = Array.from(track.children);
const nextButton = document.querySelector('.carousel__button--right');
const prevButton = document.querySelector('.carousel__button--left');
const dotsNav = document.querySelector('.carousel__nav');
const dots = Array.from(dotsNav.children);
const slideSize = slides[0].getBoundingClientRect();
const slideWidth = slideSize.width;


//arrange the slides to one another 

const setSlidePosition = (slide,index) => {
    slide.style.left = slideWidth*index + 'px';
};

slides.forEach(setSlidePosition);

const moveToSlide = (track,currentSlide,targetSlide) => {
    track.style.transform = 'translateX(-' + targetSlide.style.left + ')'; 
    currentSlide.classList.remove('current-slide');
    targetSlide.classList.add('current-slide');
}

const updatDots = (currentDot, targetDot) =>{
    currentDot.classList.remove('current-slide');
    targetDot.classList.add('current-slide');
}

const hideShowArrows = (slides, prevButton, nextButton, targetIndex)=>{
    if(targetIndex === 0){
        prevButton.classList.add('is-hidden');
        nextButton.classList.remove('is-hidden');
    } else if(targetIndex === slides.length - 1){
        prevButton.classList.remove('is-hidden');
        nextButton.classList.add('is-hidden');
    } else {
        prevButton.classList.remove('is-hidden');
        nextButton.classList.remove('is-hidden');
    }
}

//when I click left move slids to the left
prevButton.addEventListener('click', e=>{
    const currentSlide = track.querySelector('.current-slide');
    const prevSlide = currentSlide.previousElementSibling;
    const currentDot = dotsNav.querySelector('.current-slide');
    const prevDot = currentDot.previousElementSibling;
    const prevIndex = slides.findIndex(slides => slides === prevSlide);
    //move to the prev slide
    hideShowArrows(slides, prevButton, nextButton, prevIndex);
    moveToSlide(track,currentSlide,prevSlide);
    updatDots(currentDot,prevDot);
});

//when I click right move the slides to the right 
nextButton.addEventListener('click', e => {
    const currentSlide = track.querySelector('.current-slide');
    const nextSlide = currentSlide.nextElementSibling;
    const currentDot = dotsNav.querySelector('.current-slide');
    const nextDot = currentDot.nextElementSibling;
    const nextIndex = slides.findIndex(slides => slides === nextSlide);    
    //move to the next slide
    hideShowArrows(slides, prevButton, nextButton, nextIndex);
    moveToSlide(track,currentSlide,nextSlide);
    updatDots(currentDot,nextDot);
});

//when I click the nav indicators, move to that slide
dotsNav.addEventListener('click', e =>{
    //what indicator was clicked on?
    const targetDot = e.target.closest('button');
    if(!targetDot) return;
    const currentSlide = track.querySelector('.current-slide');
    const currentDot = dotsNav.querySelector('.current-slide');
    const targetIndex = dots.findIndex(dot => dot === targetDot);
    const targetSlide = slides[targetIndex]; 

    moveToSlide(track,currentSlide,targetSlide);
    updatDots(currentDot, targetDot);
    hideShowArrows(slides, prevButton, nextButton, targetIndex);
})