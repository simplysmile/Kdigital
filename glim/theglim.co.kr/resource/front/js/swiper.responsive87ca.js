/*
 Filename:		swiper.responsive.js
 Descript:		
 Writer--:		glim
 CreateDate :	20180828
 LatestDate:	20180828
*/

(function($) {
	function setSwiper() {
		if ($(".swiper-container").length > 0) {
			setSwiperPadding();
			var swiper = new Swiper('.swiper-container', {
				slidesPerView: 3,
      			spaceBetween: 40,
				centeredSlides: true,
				mousewheel: true,
				speed:500,
				pagination: {
					el: '.swiper-pagination',
					type: 'progressbar',
				},
				breakpoints: {
					1200: {
						slidesPerView: 2,
						spaceBetween: 40,
						centeredSlides: false,
					},
					823: {
						slidesPerView: 1,
						spaceBetween: 15,
						centeredSlides: false,
					},
				}
			});
		}

		if ($(".portfolio_type_wrap").length > 0) {
			$(".portfolio_type_wrap .portfolio_select_button").on("click", function(event) {
				$(".portfolio_type_wrap .portfolio_type_list").toggleClass("show");
			});

			$(".portfolio_type_wrap .portfolio_type_list button").on("click", function(event) {
				$(".portfolio_type_wrap .portfolio_type_list li").removeClass("selected");
				$(this).closest("li").addClass("selected");
				$(".portfolio_type_wrap .portfolio_select_button").text($(this).text());
				$(".portfolio_type_wrap .portfolio_type_list").removeClass("show");
			});
		}
	}

	function setSwiperPadding() {
		var paddingLeft, calcWidth;
		if ($(window).outerWidth() > 1200) {
			paddingLeft = ($(window).outerWidth() - 1200) / 2;
			calcWidth = 1580 + paddingLeft;
		}
		else {
			paddingLeft = 0;
			calcWidth = "auto";
		}

		if ($(".swiper-container").length > 0) {
			$(".swiper-container").css({
				"padding-left": paddingLeft,
				"width": calcWidth,
			});
		}

		if ($(".portfolio_type_wrap").length > 0) {
			$(".portfolio_type_wrap").css({
				"padding-left": paddingLeft,
				"width": calcWidth,
			});
		}
	}

	$(window).on("resize", function() {
		setSwiperPadding();
	});

	$(document).ready(function () {
		setSwiper();
	});
})(jQuery);
