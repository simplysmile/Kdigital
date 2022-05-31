/*
 Filename:		com.ui.helper.js
 Descript:		
 Writer--:		glim
 CreateDate :	20180828
 LatestDate:	20180828
*/
/* ********************************************* *
 * HELPERS
 * ********************************************* */
// Debug ie not smoothy text motion
function motionArgs(args){

	if($('html').hasClass('ie')){
	    args.rotation = 0.1;
	}

	return args

}

// is mobile condition
function isMobile(){
	var v = !navigator.userAgent.match(/Android|Mobile|iP(hone|od|ad)|BlackBerry|IEMobile|Kindle|NetFront|Silk-Accelerated|(hpw|web)OS|Fennec|Minimo|Opera M(obi|ini)|Blazer|Dolfin|Dolphin|Skyfire|Zune/);
	//console.log ( v )
    return (v);
	//return $('html').hasClass('mobile');
}


$.fn.hasEvent = function() {
	var ty = arguments[0], fn = arguments[1], da = $._data(this[0], 'events') || undefined;
	if (da === undefined || ty === undefined || da[ty] === undefined || da[ty].length === 0)  return false;
	if (fn === undefined) return true;
	return Boolean(fn == da[ty][0].handler);
};


/****************************************
* Common Js
*****************************************/
/* $('.quickwrap').pixels('right') */
$.fn.pixels = function(property) {
    return parseInt(this.css(property).slice(0,-2));
};

