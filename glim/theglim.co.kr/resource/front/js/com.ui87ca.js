/*
 Filename:		front.ui.js
 Descript:		UI 공통 자바스크립트
 Writer--:		glim
 CreateDate :	20180828
 LatestDate:	20180918 개발 직접수정
 @20180914 : Device 이고 824 이상일때는 device 아니고 desktop 옵션붙음 (gnb 쪽은 기존과 click 동일하게 함)
 @20180918 : 직접수정
 @20180927 : Device -> Desktop 으로 버전 변경시 refresh 추가
 @20181002 : device : pagebody 일때 animationInit 삭제
*/

var _mowidth = 823;//모바일타입변경지점 900px 작을때
var _minwidth = 1260;//웹타입 바디 최소해상도(작을때는 스크롤생김)

 $(document).ready( function(){
	//console.log("ready");
	
	/* if(isMobile() ) $('body').addClass('desktop');
	else $('body').addClass('device'); */
	
	/* 20180914 수정 
	*/
	//console.log ( $(window).width() )
	if( isMobile() == false && $(window).width() <= 823 ){//false
		$('body').addClass('device');
	} else {
		$('body').addClass('desktop');
	}
	
	$(document).click(function(e){
		if( !isMobile() &&  $('.header-box').hasClass("open")){
			funcHeaderMenuOnOff(1);
		}
	});
	
		
	funcHeaderMenuOnOff(3);
	
	
	/* Layer-Request 
	******************************************/
	
	//jquery dialog - layerpopup 최초 공통 init 
	$("[data-role=dialog]").dialog({
		autoOpen: false,
		modal: true,
		closeText: "닫기",
		resize: true,
		resizable: false,
		create: function( event, ui ) {
			//console.log ("dialog");
		},
		open : function (event,ui){
			//console.log ("dialog");
			if($("body").width() < _mowidth) {
				var ww = $("body").width();
				if ( $(this).hasClass('lpop-share') ){
					ww = $("body").width()-60;
				}else{					
				}
				$(event.target).dialog("option", "width", ww);				
			}else {
				$('body, html').css('overflow', 'inherit');			
				
				$( this ).dialog("option", { "width" : $( this ).data("width"), "height" : "auto", "position": {my: "center", at: "center", "collision": "flipfit", of: window } });
			}
		}
	});
	
	
	/* *****************************************
	Layer-Request */
	
	
});

 

$(window).on('load', function () {
	console.log ('load');
    PageLoad();
    $(window).resize(function () { resize(); });
})

var PageLoad = function () {
    resize();

    var tl = new TimelineLite({});
    var $footer = $('.footer');

    if ($('body').hasClass('about') && $('body').hasClass('pager-body') && $('body').hasClass('device')) {
        //console.log('about.device');

        var $pagerwrap = $('.pager-wrap');
        var $theme01_bg = $('.theme_cover');
        var $tt = $('.visual_tit');
        $('body').scrollTop(0);

        TweenMax.set($pagerwrap, { autoAlpha: 0 });
        tl.kill()
            .to($pagerwrap, 0.6, {
                autoAlpha: 1, ease: Sine.easeInOut, delay: "-=0.4"
                , onComplete: function () {
                    animationInit();
                }
            });

    } else if ($('body').hasClass('about') && $('body').hasClass('pager-body')) {
        //console.log('about , pager-body');

        var $theme_cover = $('.theme_cover');
        var $tt = $('.visual_tit');
        $('body').scrollTop(0);
        TweenMax.set($theme_cover, { autoAlpha: 0 });
        TweenMax.set($footer, { autoAlpha: 0, bottom: '-100px' });
        TweenMax.set($tt, { autoAlpha: 0, y: '20px' });
        tl.kill()
            .to($theme_cover, 0.8, {
                autoAlpha: 1, ease: Sine.easeOut, delay: "-=0.4"
                , onComplete: function () {
                    animationInit();
                    $('.pager_home').css({ 'display': 'table', 'opacity': 1 });
                }
            })
            .to($footer, .8, { autoAlpha: 1, bottom: '0', ease: Back.easeOut });;

    } else if ($('body').hasClass('details') && $('body').hasClass('pager-body') && $('body').hasClass('device')) {
        var $pagerwrap = $('.pager-wrap');
        
        var $tt = $('.visual_tit');
        $('body').scrollTop(0);

        TweenMax.set($pagerwrap, { autoAlpha: 0 });
        tl.kill()
            .to($pagerwrap, 0.6, {
                autoAlpha: 1, ease: Sine.easeInOut, delay: "-=0.4"
                , onComplete: function () {
                    //animationInit();
                }
            });
    } else if ($('body').hasClass('details') && $('body').hasClass('pager-body')) {
        var $theme01_bg = $('.theme_cover');
        var $tt = $('.visual_tit');
        $('body').scrollTop(0);
		var $pagerwrap = $('.pager-wrap');
		TweenMax.set($pagerwrap, { autoAlpha: 0 });
        TweenMax.set($footer, { autoAlpha: 0, bottom: '-100px' });
        TweenMax.set($theme01_bg, { autoAlpha: 0 });
        TweenMax.set($tt, { autoAlpha: 0, y: '20px' });
        tl.kill()
			.to($pagerwrap, 0.6, {
                autoAlpha: 1, ease: Sine.easeInOut, delay: "-=0.4"
			})
            .to($theme01_bg, 0.8, {
                autoAlpha: 1, ease: Sine.easeOut, delay: "-=0.4"
                , onComplete: function () {
                    animationInit();
                }
            })
            .to($footer, .8, { autoAlpha: 1, bottom: '0', ease: Back.easeOut });
			
		if ($('.btn-go-top').length > 0 ){
			scroll_top();
		}	

    }
    else if ($('body').hasClass('main-body') || $('body').hasClass('list-body')) {
        
        var $swiperwrap = $('.swiper-wrap');
        var $swiperwrap1 = $('.portfolio_type_wrap');
        var $swiperwrap2 = $('.swiper-container');

        TweenMax.set($footer, { autoAlpha: 0, bottom: '-100px' });
        TweenMax.set($swiperwrap, { autoAlpha: 0 , top: '50px' });
        TweenMax.set($swiperwrap1, { autoAlpha: 0, top: '50px' });
        /* TweenMax.set($swiperwrap2, { autoAlpha: 0, top: '100px' }); */

        tl.kill().to($swiperwrap, 0.8, { autoAlpha: 1,'top': 0, ease: Sine.easeOut })
			.to($swiperwrap1, 0.7, { autoAlpha: 1, 'top': 0, ease: Sine.easeOut })
			//.to($swiperwrap2, 0.7, { autoAlpha: 1, 'top': 0, delay: "-=0.4" , ease: Sine.easeOut })
			.to($footer, .6, { autoAlpha: 1, bottom: '0', delay: "-=0.4", ease: Sine.easeOut });
			

    } else if ($('body').hasClass('contact-body')) {
        var $sec = $('.body .sec');
        TweenMax.set($sec, { autoAlpha: 0 });
        TweenMax.set($footer, { autoAlpha: 0, bottom: '-100px' });
        tl.kill()
            .to($sec, 0.4, {
                autoAlpha: 1, ease: Sine.easeOut
                , onComplete: function () {
                    animationInit();
                }
            }).to($footer, .8, { autoAlpha: 1, bottom: '0', ease: Back.easeOut /* ,delay:"-=0.2" */ });
    }
}

 
$(function() {
	
	/* 20180905 mo 에서 resize 시 attr 가 지워져서 강제로 주입 css opacity 를 1로 변경 */
	//$('.swiper-wrap').css('opacity','0');
	//$('.portfolio_type_wrap').css('opacity','0');
	//$('.swiper-container').css('opacity','0');


});

var _gnbtimer = null;
/* GNB
 ************************************************/
if(isMobile()){
	//console.log("desktop");
	//PC
	$(document).ready( function(){
		$('.header-box').on('mouseover', function(e){
			clearTimeout(_gnbtimer);
			_gnbtimer = null;
            funcHeaderMenuOnOff(0);
			
		}).on('mouseleave', function(e){
			_gnbtimer = setTimeout(function(){ 
				funcHeaderMenuOnOff(1);				
			}, 1000);
		});
		$("li", '.global-menu > .navi').each(function(i){
			$(this).find('a').on('click', function (e){
                Common.EventCancelBubble(e);
                Common.EventReturnValue(e);
			});
		});
	})
	
}else{//MO
	//console.log("device");
	$(document).ready( function(){
		$('.header-box').off('mouseover mouseleave').on('click', function(e){
			if($(this).hasClass("open")){
				funcHeaderMenuOnOff(1);
			}else{	
				funcHeaderMenuOnOff(0);
			}
        })
		$("li", '.global-menu > .navi').each(function(i){
			$(this).find('a').on('click', function (e){
                Common.EventCancelBubble(e);
                Common.EventReturnValue(e);
			});
		});
	})
}


function resize (){
	//console.log("com.ui.js-resize");
	
	//20180927 add 
	var stat = (isMobile() == false && $(window).width() <= 823) ? 'device':'desktop';
	if( $('body').hasClass('device') && stat == 'device' ){//false
		//console.log("DEVICE");
	}else if ($('body').hasClass('desktop') && stat == 'desktop') {
		//console.log("DESKTOP");
	}else{
		//console.log ("NOT MATCH");
		location.reload();
	}
	
	
	
	$(".ui-dialog-content:visible").each(function (i) {
		var tg = $( this ).data( "dialog" );
		if($("body").width() < _mowidth) {
			$( this ).dialog("option", "width", $("body").width() );
			if( $( this ).hasClass('mofull') ){
				$( this ).closest('.ui-dialog').addClass('mofull_wrap').css('margin',0);
				$('body, html').css('overflow', 'hidden');
				$( this ).dialog("option", { "width" : window.innerWidth, "height" : window.innerHeight, "position":{my: "top", at: "top", "collision": "flipfit", of: window }});
			} 
		}else {
			$('body, html').css('overflow', 'inherit');
			$( this ).dialog("option", { "width" : $( this ).data("width"), "height" : "auto", "position": {my: "center", at: "center", "collision": "flipfit", of: window } });
		}
    });

	//adjust middle
    var _wh = $(window).height();
    var _minHeight = parseInt($('.wrap').pixels('padding-top') + $('.wrap').pixels('padding-bottom') + $('.contents-body').height());

    $('body').css({
        "min-height": _minHeight
    });

    var yy = parseInt(($('body').height() - $('.wrap').pixels('padding-top') - $('.wrap').pixels('padding-bottom')) / 2 - ($('.contents-body').height() / 2));

    if (_minHeight < _wh) {
        $('.contents-body').css("padding-top", yy);
        $('body').css({
            "overflow": "hidden"
        });
    } else {
        $('.contents-body').removeAttr('style');
        $('body').css({
            "overflow": "auto"
        });
    }
}

/* 
st == 0 열려라 로고 아웃 - mouseover MO
st == 1 닫아라 로고 인 - mouseleave MO
st == 2 닫아라 로고 아웃 - 메뉴전환 PC Only
st == 3 닫힌상태 로고인 - 최초 로딩 PC Only
 */
function funcHeaderMenuOnOff (st, url){
	//console.log ("funcHeaderMenuOnOff", st);
	
	var $header = $('.header');
	if ( $header.hasClass('is-moved') ) return;
	
	var $url = url;
	var $box = $('.header-box');
	var $logo =$box.find('.logo');
	var $symbol =$box.find('.symbol');
	var $menu =$box.find('.global-menu');
	var tl = new TimelineLite({});
	var setBox, setMenu;
	
	setMenu = (ww > _mowidth) ? '109px':'88px';
	
	var bx = 1200;
	var ww = $(window).width();
	bx = Math.min(bx, $(window).width()-60 );
	
	
	
	//console.log ( $url )
	
	if ( st == 0 ){
		if ( $box.hasClass('open') ) return;
		
		setBox = (ww > _mowidth) ? {width:bx,height:'100px', ease:Sine.easeInOut}:{width:'100%',height:'435px', delay:"-=0.2", ease:Sine.easeInOut};
		
		$header.addClass('is-moved');
		$menu.show();
		$symbol.hide();
		
		tl.kill()
			.to($logo, 0.3, {autoAlpha:0, ease:Sine.easeInOut})
			.to($box, 0.3, setBox)			
			.to($menu, 0.3, {autoAlpha:1,delay:"-=0.3", ease:Sine.easeInOut, onComplete:function(){
					$box.addClass('open');
					$header.removeClass('is-moved');
				}
			});
		
	}else if (st == 1 ){
		
		if ( !$box.hasClass('open') ) return;
		
		setBox = (ww > _mowidth) ? {width:'210px',height:'100px', ease:Sine.easeInOut}:{width:'150px',height:'70px', delay:"-=0.4", ease:Sine.easeInOut};
		// Set style because Tween from has a fouc issue on ie
		TweenMax.set($box, {});
		TweenMax.set($logo, {autoAlpha:0,});
		$header.addClass('is-moved');
		tl.kill()
			.to($menu, 0.3, {autoAlpha:0, ease:Sine.easeInOut})
			.to($box, 0.3, setBox)
			.to($logo, 0.3, {autoAlpha:1, delay:"-=0.8", ease:Sine.easeInOut, onComplete:function(){
					$box.removeClass('open');
					$header.removeClass('is-moved');
					$menu.hide();
					$symbol.show();
				}
			});
	}else if (st == 2 ){
		//$('.c-transition-overlay').addClass('is-active');		
		
		setBox = (ww > _mowidth) ? {width:'210px',height:'100px', ease:Sine.easeInOut}:{width:'150px',height:'70px', delay:"-=0.1", ease:Sine.easeInOut};
		
		// Set style because Tween from has a fouc issue on ie
		$header.addClass('is-moved');
		TweenMax.set($box, {});
		TweenMax.set($logo, {autoAlpha:0});
		tl.kill()
			.to($menu, 0.3, {autoAlpha:0, ease:Sine.easeInOut})
			.to($box, 0.3, setBox)
			.to($logo, 0.3, { autoAlpha:0, ease:Sine.easeInOut, delay:"-=0.2", onComplete:function(){
					console.log ( "~~"+$url )
					location.replace($url);
					$header.removeClass('is-moved');
					$menu.hide();
					$symbol.show();
				}
			});
		
	}else if (st == 3 ){
		// Set style because Tween from has a fouc issue on ie
		TweenMax.set($box, {});
		TweenMax.set($logo, {autoAlpha:0});
		tl.kill().to($logo, 0.3, {autoAlpha:1,  ease:Sine.easeInOut});
		
	}
}


// scroll top button
function scroll_top(){

    var $window = $(window);
    var $document = $(document);
    var $footer = $('.footer');
    var $scrollBtn = $('.btn-go-top');

    $scrollBtn.on('click',function(){
        $("html, body").stop().animate({
            scrollTop: 0
        }, 600);

        return false;
    });
	
	if ($window.scrollTop() < $document.height() - $window.height() - $footer.outerHeight() + 37) {
		$scrollBtn.addClass('fixed');
	} else {
		$scrollBtn.removeClass('fixed');
	}
	if ($window.scrollTop() < $window.height()/3) {
		$scrollBtn.addClass('hide');
	} else {
		$scrollBtn.removeClass('hide');
	}

    $window.on('scroll', function() {
        if ($window.scrollTop() < $document.height() - $window.height() - $footer.outerHeight() + 37) {
            $scrollBtn.addClass('fixed');
        } else {
            $scrollBtn.removeClass('fixed');
        }
        if ($window.scrollTop() < $window.height()/3) {
            $scrollBtn.addClass('hide');
        } else {
            $scrollBtn.removeClass('hide');
        }
    });

}



//자동메일발송방지
/* var md5_norobot_key = '';
(function($) {
    var kcaptchaPath = "../resource/front/js/kcaptcha";
    if (typeof(KCAPTCHA_JS) == 'undefined') {
        var KCAPTCHA_JS = true;
        $(document).ready(function() {
            if ($('#kcaptcha_image').length > 0) {
                $('#kcaptcha_image').attr('width', '170').attr('height', '60'); //이미지 크기 원하는데로 바꾸..
                $('#kcaptcha_image').attr('title', '글자가 잘안보이는 경우 클릭하시면 새로운 글자가 나옵니다.');
                $('#kcaptcha_image').click(function() {
                    $.post(kcaptchaPath + '/kcaptcha_session.php', function(data) {
                        $('#kcaptcha_image').attr('src', kcaptchaPath + "/kcaptcha_image.php?t=" + (new Date).getTime());
                        md5_norobot_key = data;
                    });
                });
            }
            $('#kcaptcha_image').click();
        });
    }
})(jQuery); */


