/*
 Filename:		animation.js
 Descript:		
 Writer--:		glim
 CreateDate :	20180828
 LatestDate:	20180914
*/

$(document).ready( function(){

	
	
});

function animationInit (){
	/* console.log("~~", 'animationInit'); */
	waypointMotion();
	waypointCustomMotion();
	motionBindClass();
	skrInit(); 
	
}


// skrollr init function
function skrInit(){

    //if($(window).width() < 824) {
	//20180914 조건문 변경	
    if(isMobile() == false && $(window).width() <= 823 && !$('body').hasClass('contact-body')) {//device
		//console.log("~~~~!! skrInit");
		skr = skrollr.init({
            smoothScrolling: false,
            forceHeight: false
        });
		
    } else {
       try {
			if(  skr != null ) {
				skr.destroy();
			}
		}catch(e){
			
		}
        
    }

}



// Waypoint animate class switcher  for css animation
function waypointMotion(){

	// nothing on mobile
	if(isMobile()) return;

	// use each loop the get the offset from the data attribut
	$('.gl-waypoint').each(function() {
		var $this = $(this);

		$this.waypoint(function() {
			$this.addClass('gl_animate');
			this.destroy();
		}, {
			offset: $this.attr("data-offset")
		});
	});
	
	
}


// Animate by adding a simple class
// Todo : add optional parameter using data attribute
function motionBindClass(){

	// nothing on mobile //20180914 조건문 변경	
	if(isMobile() == false && $(window).width() <= 823) return;
	
	$('.gl_animate_tit').each(function() {

		var $this = $(this);
		var tl = new TimelineLite({paused:true});
		TweenMax.set($this, {autoAlpha:0, y:50}); // avoid ie fouc
		tl.to($this, 1.6, motionArgs({ autoAlpha:1, y:0, ease:Back.easeOut}));

		$this.waypoint(function() {
			tl.play();
			this.destroy();
		}, {
			offset: "85%"
		});

	});
	
	$('.gl_animate_tit2').each(function() {

		var $this = $(this);
		var tl = new TimelineLite({paused:true});
		TweenMax.set($this, {autoAlpha:0, y:50}); // avoid ie fouc
		tl.to($this, 1.4, motionArgs({ autoAlpha:1, y:0, ease:Back.easeOut}));

		$this.waypoint(function() {
			tl.play();
			this.destroy();
		}, {
			offset: "85%"
		});

	});
	
	$('.gl_animate_tit3').each(function() {

		var $this = $(this);
		var tl = new TimelineLite({paused:true});
		TweenMax.set($this, {autoAlpha:0, y:70}); // avoid ie fouc
		tl.to($this, 1, motionArgs({ autoAlpha:1, y:0, ease:Back.easeOut}));

		$this.waypoint(function() {
			tl.play();
			this.destroy();
		}, {
			offset: "85%"
		});

	});
	
	
	$('.gl_animate_txt').each(function() {

		var $this = $(this);
		var tl = new TimelineLite({paused:true});
		TweenMax.set($this, {autoAlpha:0, y:50}); // avoid ie fouc
		tl.to($this, 1.2, motionArgs({ autoAlpha:1, y:0, ease:Back.easeOut}));

		$this.waypoint(function() {
			tl.play();
			this.destroy();
		}, {
			offset: "90%"
		});
	});
	
	$('.gl_animate_txt2').each(function() {

		var $this = $(this);
		var tl = new TimelineLite({paused:true});
		TweenMax.set($this, {autoAlpha:0, y:70}); // avoid ie fouc
		tl.to($this, 1.2, motionArgs({ autoAlpha:1, y:0, ease:Back.easeOut}));

		$this.waypoint(function() {
			tl.play();
			this.destroy();
		}, {
			offset: "90%"
		});
	});
	
	

	// images box fast
	$('.gl_animate_box').each(function() {

		var $this = $(this);
		var off_set = $this.attr('data-offset');
		var tl = new TimelineLite({paused:true});

		if(off_set == undefined){
		    off_set = '100%';
		}
		
		tl.from($this, 1.6, {autoAlpha:0, y:'30%',force3D:true, ease:Back.easeOut});

		$this.waypoint(function() {
			tl.play();
			this.destroy();
		}, {
			offset: off_set
		});

	});
	
	
	// images box slow
	$('.gl_animate_box_slow').each(function() {

		var $this = $(this);
		var off_set = $this.attr('data-offset');
		var tl = new TimelineLite({paused:true});

		if(off_set == undefined){
		    off_set = '100%';
		}
		
		TweenMax.set($this, {autoAlpha:0, y:100}); // avoid ie fouc
		tl.to($this, 1.6, {autoAlpha:1, y:0,force3D:true, ease:Back.easeOut});

		$this.waypoint(function() {
			tl.play();
			this.destroy();
		}, {
			offset: off_set
		});

	});
	
	// btn
	$('.gl_animate_btn').each(function() {

		var $this = $(this);
		var off_set = $this.attr('data-offset');
		var tl = new TimelineLite({paused:true, delay:0.6});
		//var tl = new TimelineLite({paused:true});

		if(off_set == undefined){
		    off_set = '100%';
		}
		TweenMax.set($this, {autoAlpha:1,y:0}); // avoid ie fouc
		tl.from($this, 1, {autoAlpha:0,y:'30%',ease:Back.easeOut});

		$this.waypoint(function() {
			tl.play();
			this.destroy();
		}, {
			offset: off_set
		});

	}); 
	
	// btn
	$('.gl_animate_btn2').each(function() {

		var $this = $(this);
		var off_set = $this.attr('data-offset');
		var tl = new TimelineLite({paused:true, delay:0.3});

		if(off_set == undefined){
		    off_set = '100%';
		}
		tl.from($this, 1.4, {autoAlpha:0, y:'10%',force3D:true, ease:Back.easeOut});
			
		$this.waypoint(function() {
			tl.play();
			this.destroy();
		}, {
			offset: off_set
		});

	}); 
	
	// opacity
	$('.gl_animate_opacity').each(function() {

		var $this = $(this);
		var off_set = $this.attr('data-offset');
		var tl = new TimelineLite({paused:true});

		if(off_set == undefined){
		    off_set = '100%';
		}
		
		tl.to($this, 1.2, motionArgs({ autoAlpha:1, ease:Back.easeOut}));

		$this.waypoint(function() {
			tl.play();
			this.destroy();
		}, {
			offset: off_set
		});

	}); 

}


function waypointCustomMotion(){
	
	if(isMobile()) return;
	
	
	$('.msec_history_animate_line').each(function() {
		
		var $this = $(this).find(' > .line');
		var off_set = $this.attr('data-offset');
		var tl = new TimelineLite({paused:true, delay:2});

		if(off_set == undefined){
		    off_set = '100%';
		}
		
		tl.to($this, 1, { right:0, ease:Back.easeOut});

		$this.waypoint(function() {
			tl.play();
			this.destroy();
		}, {
			offset: off_set
		});

	});

	
	TweenMax.set('.msec_service_animate_list li',{autoAlpha:0});
	$('.msec_service_animate_list').waypoint(function() {
		$('.msec_service_animate_list li').each(function(index) {

			var $this = $(this);
			var $box = $(this).find('.box');
			var $title = $(this).find('strong');
			var $txt1 = $(this).find('p.tit_3');
			var $txt2 = $(this).find('p.txt_1');

			var tl = new TimelineLite({delay: index * .20 + .1});

			// Set style because Tween from has a fouc issue on ie
			TweenMax.set($box, {autoAlpha:0, y:0});
			TweenMax.set($title, {autoAlpha:0, y:50});
			TweenMax.set($txt1,{autoAlpha:0, y:30});
			TweenMax.set($txt2, {autoAlpha:0, y:50});
			
			TweenMax.set($this,{autoAlpha:1});

			tl.to($box, 0.8, {autoAlpha:1, ease:Back.easeOut})
				.to($title, .8, {autoAlpha:1, y:0, ease:Back.easeOut}, "-=0.6")
				.to($txt1, .8, {autoAlpha:1, y:0, ease:Back.easeOut}, "-=0.4")
				.to($txt2, 1.8, {autoAlpha:1, y:0, ease:Back.easeOut}, "-=0.2");
		});

		this.destroy();
	}, {
		offset: "80%"
	});
	
	
	
}

