/*
 Filename:		pager.responsive.js
 Descript:		
 Writer--:		glim
 CreateDate :	20180828
 LatestDate:	20180927
 #20180927 _lens 수정
 //20180914 조건문 변경
*/
 $(window).on('load', function () {
	
	
	/* if ($('.footer-pager-nav').length > 0 ){
		pager_footer();
	} */



});

// scroll top button
function pager_footer(){

    var $window = $(window);
    var $document = $(document);
    var $footer = $('.footer');
    var $footerBtn = $('.footer-pager-nav');

    /* $scrollBtn.on('click',function(){
        $("html, body").stop().animate({
            scrollTop: 0
        }, 600);

        return false;
    }); */

    $window.on('scroll', function() {
        if ($window.scrollTop() < $document.height() - $window.height() - $footer.outerHeight()) {
            $footerBtn.addClass('fixed');
        } else {
            $footerBtn.removeClass('fixed');
        }
        if ($window.scrollTop() < $window.height()/2 ) {
            $footerBtn.addClass('hide');
        } else {
            $footerBtn.removeClass('hide');
        }
    });

}

function pagerResponsive() {
	
	/**
	 * Vars.
	 *
	 * @type {object}
	 */
	var	$body = $('.body'),
		$pagerwrap = $body.find('.pager-wrap'),
		$pagerhome = $pagerwrap.find('.pager-home'),
		$pagernav = $pagerwrap.find('.pager-nav'),
		$pagernavTotal = $pagernav.find('.total-num'),
		$pagernavCurrent = $pagernav.find('.current-num'),
		$pagerbar = $pagerwrap.find('.pager-bar'),
		$pagerbarCurrent = $pagerbar.find('.current-bar'),
		$window = $(window),
		
		_lens = $pagerhome.length,
		_scrollYPos = [],//contentYpos	
		_dragStart = undefined,//mousedown 시작점
		_dragStartY = undefined,//mousedown 시작점
		_firstDir = undefined,//첫 방향 결정 (기존페이지 마지막페이지)
		_dragDir = undefined,//방향 결정
		_dragMoved = 0,
		_viewPage = 0,//보이는 페이지
		_movePage;//움직일 page
	
	// initialize
	var	init = function() {
		
		if ( $body.length == 0) return;
		if ( $('.pager-body').length == 0) return;
		//loadSet();
		bindEvent();
		pageNavUpdate();
	},
	bindEvent = function() {
		
		$window.resize(function() { resize(); });
		
		/* 수정필요  device 이고 824 이상일때 안나옴*/
		//if ( isMobile() == false && $(window).width() <= 823 ){//mobile
		//if ( isMobile() == false ){//mobile
		//20180914 조건문 변경
		if ( $('.pager-body').hasClass('device') ){//mobile
			if ( $body.hasEvent('touchstart') == true ) return;
			
			$(document).off('DOMMouseScroll mousewheel', wheelEvent);
			
			$body.on('touchstart', function(e){
				if ( $pagerwrap.hasClass('is-moved') ) return;
				_dragStart = x = e.originalEvent.touches[0].screenX;
				_dragStartY = y = e.originalEvent.touches[0].screenY;
				_movePage = undefined;
				dragStart('dragStart', {ex:x, oy:y}); 	
			});
			
			$body.on('touchend', function(e){
				if ( $pagerwrap.hasClass('is-moved') ) return;
				dragEnd();
			});

			$body.on('touchmove', function(e){
				if ( $pagerwrap.hasClass('is-moved') ) return;
				e.preventDefault();
				x = e.originalEvent.touches[0].screenX;
				y = e.originalEvent.touches[0].screenY;
				//console.log('touchmove(x:'+x+', y:'+y+')');
				dragUpdate({ex:x, oy:y});
			});
			
		}else{//pc
			
			$body.off( "touchstart touchend touchmove" );
						
			//$pagerwrap.find('.pager-home').css ("height", $(window).height() );
			//$pagerwrap.css( 'height', $(window).height() * $pagerwrap.find('.pager-home').length );
			
			if ( $body.hasClass('about')){//about 은 단처리
				setWebHeight();
				$(document).on('DOMMouseScroll mousewheel', wheelEvent);
			}else{//기본은 scroll
				//smooth scroll
				$("html").easeScroll();
			}			
		}
		
	},
	pageNavUpdate = function(){
		$pagernavTotal.html((_lens < 10) ? '0'+_lens:_lens);
		var c = _viewPage+1;
		$pagernavCurrent.html((c < 10) ? '0'+c:c);
		
		var ww = $(window).width();
		var per = parseInt(ww*(c/_lens));
		$pagerbarCurrent.css ('width', per);
		
		if ( $('body').hasClass('details') ){
			if (_viewPage > 0){
				$('.header').fadeOut();
			}else{
				$('.header').fadeIn();
			}
		}
	},
	resize = function (event){
		//20180914 조건문 변경
		if ( $('.pager-body').hasClass('device') ){//mobile
			$pagerhome.each(function(n) {
				var l = $(this).offset().left;
				var ww = $(window).width();
				if ( l != 0 ) $(this).css('left', -ww);
			});			
		}else{
			setWebHeight();
		}
		
	},
	setWebHeight = function (event){
		_scrollYPos = [];
		var pagerTotalHeight = 0;
		$pagerhome.each(function(n) {
			_scrollYPos.push ($(this).position().top);
			pagerTotalHeight += $(this).height();
		});
		_scrollYPos.push (pagerTotalHeight);
	},
	wheelEvent = function (e){
		e.preventDefault();

		var scrollTop = $window.scrollTop(),
		viewCnt = -1;//보여지는 tg num
		for ( var i = 0; i<_scrollYPos.length; i++){//현재 posy 가 어디인지 find
			if (_scrollYPos[i] <= scrollTop && scrollTop < (_scrollYPos[i+1])){
				//console.log ( _scrollYPos[i] ,"<=", scrolltop ,"&&", scrolltop ,"<", _scrollYPos[i+1] )
				viewCnt = i;
				break;
			}
		}
		_viewPage = $('.pager-home').eq(viewCnt);//보여질 페이지
				
		var evt = window.event || e; //equalize event object
		var delta = evt.detail? evt.detail*(-120) : evt.wheelDelta;
		//console.log ( delta )
		
		if(delta > 0) {
			console.log('scrolling up !');
			if ( scrollTop != 0 && scrollTop == _viewPage.offset().top ){
				_viewPage = _viewPage.prev();				
			}else if ( scrollTop != 0 && scrollTop != _viewPage.offset().top ){
				_viewPage = _viewPage;
			}
		}else{
			console.log('scrolling down !');
			_viewPage = _viewPage.next();
		}
		if ( _viewPage.index() == -1 ) {
			_viewPage = $('.footer');
		}
		$pagerwrap.addClass('is-moved');
		console.log ( " _viewPage = ", _viewPage)
		scrollingMove (_viewPage);
		
	},	
	scrollingMove = function (el){
				
		var tl = new TimelineLite({});		
		console.log ( el.offset().top )
		tl.kill().to($('html, body'), 0.6, {scrollTop: el.offset().top,  ease:Power2.easeOut, delay:"0",
			onComplete:function(){
				// Animation complete.
				$pagerwrap.removeClass('is-moved');
			}
		});
	},
	dragStart = function (o){},
	dragUpdate = function (o){
		if ( $pagerwrap.hasClass('is-moved') ) return;
		var ww = 0,to = 0;
		_firstDir = _dragStart - o.ex;
		var yyy  = _dragStartY - o.oy;
		
		//세로스크롤시 무빙 삭제
		if ( Math.abs(_firstDir) < Math.abs(yyy) ){ return; }
		
		//movetarget selected
		if (_movePage==undefined) {			
			if ( _firstDir > 0 ){//Left
				if ( _viewPage == (_lens-1) ) {return;}
				_movePage = $('.pager-home.actived');
			}else{//Right
				if ( _viewPage == 0 ) { return ;}
				_movePage = $('.pager-home.actived').prev();
			}
		}else{
			//무브 방향 결정 
			_dragMoved = _draged - o.ex;
		}
		
		
		if ( $(_movePage).index() < _viewPage ){//이전타겟
			to = -(_firstDir)-_dragMoved- $(window).width();
		}else{//현재타겟
			to = -(_firstDir)-_dragMoved;
			to = (to > 0 ) ? 0:to;
		}
		
		//_movePage.css('left', to );
		_movePage.css('transform' , 'translate3d(' + to + 'px, 0px, 0px)');
		//_movePage.css('transform' , 'matrix(1,0,0,1' + to + 'px, 0px)');
		
		_draged = o.ex;
	},
	dragEnd = function (t, o){
		if ( _movePage == undefined ) return;
		
		var to = $(window).width();
		if ( _dragMoved > 0 ){//Left
			//console.log ( "dragEnd - Left" );
			_viewPage = _movePage.index() + 1;
			
		}else if ( _dragMoved <= 0){//Right
			//console.log ( "dragEnd - right" )
			_viewPage = _movePage.index();
			to = 0;
		}
		$pagerwrap.addClass('is-moved');
		var tl = new TimelineLite({});		
		var ll = _movePage.css('left');
		//TweenMax.set(_movePage, {'left':0, 'transform' : 'translate3d('+ ll + 'px, 0px, 0px)'});
		TweenMax.set(_movePage, {'transform' : 'translate3d('+ _movePage.css('transform').split(',')[4] + 'px, 0px, 0px)'});
		//tl.kill().to(_movePage, 0.4, {'left' : -to + 'px',  ease:Sine.Power2, delay:"0",
		tl.kill().to(_movePage, 0.2, {'transform' : 'translate3d('+ -to + 'px, 0px, 0px)',  ease:Sine.Power2, delay:"0",
			onComplete:function(){
				// Animation complete.
				$('.pager-home.actived').removeClass('actived');
				$('.pager-home').eq(_viewPage).addClass('actived');
				$pagerwrap.removeClass('is-moved');
				pageNavUpdate();
			}
		});
	}
	
	setTimeout(function(){ 
		init();
	}, 1000);
	
}
$(pagerResponsive);

