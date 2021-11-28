// DOM
const navigationSwitch = document.getElementById("navigationSwitch");
const navigation = document.getElementById("navigation");
const navigationCloseButton = document.getElementById("navigationCloseButton");
const toTopButton = document.getElementById("toTopBtn");
const textarea_ce = document.getElementById("textarea_ce")
const cancelCross = document.getElementById("cancelCross");
const dismiss = document.getElementById("dismiss");
const modal = document.getElementById("modal");
textarea_ce.setAttribute("contenteditable", false)

// Functions

function dismissModal() {
    modal.classList.remove("visible", "grid");
    modal.classList.add("invisible", 'hidden')
}

function navigationToggle(){
    // Visibility Toggle
    navigation.classList.toggle('invisible');
    navigation.classList.toggle("-right-3/4");
    navigation.classList.toggle("right-0");
    // ARIA Expansion
    let ariaExpanded = this.getAttribute('aria-expanded');
    if(ariaExpanded.toString() === "true"){
        navigationCloseButton.setAttribute('aria-expanded', "false");
        navigationSwitch.setAttribute('aria-expanded', "false");
    }else{
        navigationCloseButton.setAttribute('aria-expanded', "true");
        navigationSwitch.setAttribute('aria-expanded', "true");
    }
}

// Scroll To Top Button Visibility
function onScrollSetTopButton(){
    const invisibility = ["invisible", "opacity-0"];
    if(document.body.scrollTop > 100 || document.documentElement.scrollTop > 100){
        toTopButton.classList.remove(...invisibility);
    }else{
        toTopButton.classList.add(...invisibility);
    }
}

// Scroll To Top
function scrollToTop(){
    document.getElementById("topSection").scrollIntoView({"behavior": "smooth"});
}

// DOM Events
navigationSwitch.addEventListener("click", navigationToggle);
navigationCloseButton.addEventListener("click", navigationToggle);
toTopButton.addEventListener("click", scrollToTop);
cancelCross.onclick = dismissModal
dismiss.onclick = dismissModal
window.addEventListener("scroll", onScrollSetTopButton);
AOS.init({startEvent: 'DOMContentLoaded', once: true});
