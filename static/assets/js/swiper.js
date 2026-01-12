if (document.querySelector(".swiperInit")) {	
	var swiper = new Swiper(".swiperInit", {});
}


if (document.querySelector(".swiperNav")) {	
	var swiper = new Swiper(".swiperNav", {
		navigation: {
			nextEl: ".swiper-button-next",
			prevEl: ".swiper-button-prev",
		},
	});
}

if (document.querySelector(".swiperPagination")) {	
	var swiper = new Swiper(".swiperPagination", {
		pagination: {
			el: ".swiper-pagination",
		},
	});
}

if (document.querySelector(".swiperDynamicBullets")) {
	var swiper = new Swiper(".swiperDynamicBullets", {
		pagination: {
			el: ".swiper-pagination",
			dynamicBullets: true,
		},
	});
}

if (document.querySelector(".swiperProgressbar")) {	
	var swiper = new Swiper(".swiperProgressbar", {
		pagination: {
			el: ".swiper-pagination",
			type: "progressbar",
		},
		navigation: {
			nextEl: ".swiper-button-next",
			prevEl: ".swiper-button-prev",
		},
	});
}

if (document.querySelector(".swiperFraction")) {	
	var swiper = new Swiper(".swiperFraction", {
		pagination: {
			el: ".swiper-pagination",
			type: "fraction",
		},
		navigation: {
			nextEl: ".swiper-button-next",
			prevEl: ".swiper-button-prev",
		},
	});
}