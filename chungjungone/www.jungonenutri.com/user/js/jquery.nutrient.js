$(function(){
	inpCk();
	
	var $nav = $(".tabNav ul li"),
		maxLi = $nav.length,
		loc = location.href,
		now = 0;
	
	for(var i=0;maxLi>i;i++){
		$nav.eq(i).find("a").append("<img src='../images/common/btn_lnb"+i+"_on.gif' class='on' alt='' />");
	}
	
	if(loc.indexOf("/product/") > -1){
		now = 0;		
	}else if(loc.indexOf("/diet/") > -1){
		now = 1;
		
	}else if(loc.indexOf("/mydiet/") > -1){
		now = 2;
		
	}else if(loc.indexOf("/notice/") > -1){
		now = 3;
		
	}
	$nav.eq(now).addClass("on");
	
	$nav.each(function(i){
		$(this).hover(
			function(){
				$(this).find("img.on").stop().animate({
					"opacity" : "1"
				},200);
			},
			function(){
				if(i != now){
					$(this).find("img.on").stop().animate({
						"opacity" : "0"
					},200);					
				}
			}
		);
	});
	
});

var inpCk = function(){
	$inp = $(".inp");
	$inp.each(function(idx){
		$(this).each(function(){
			$(this).find("input").bind("keyup focusout", function() {
				if($(this).val() != ""){
					$inp.eq(idx).addClass("on");
				}else{
					$inp.eq(idx).removeClass("on")
				}
			});
			$(this).find("input").bind("focusin", function() {
				$inp.eq(idx).addClass("on");
			});
		});
	});
}
/************************************************************
	 Recommend Jacascript
	 Data : 2014.12.17
	 Developer : Sung Min Chang
************************************************************/

var recomFn = function(){

	if($("input[name=age]").is(":checked") == true){
		var on = $("input[name=age]:checked").index("input[name=age]");
		$("dl.sexBox dd ul li").eq(on).addClass("on");
	}
	
	if($("input[name=sea]").is(":checked") == true){
		var on = $("input[name=age]:checked").index("input[name=age]");
		$("dl.seaBox dd ul li").eq(on).addClass("on");
	}
	$("ul.foodBox li").each(function(i){
		$(this).find("label").bind({
			click : function(){
				$("ul.foodBox li").removeClass("on").eq(i).addClass("on");
			}
		});
	});

	$("dl.seaBox dd ul li").each(function(i){
		$(this).find("label").bind({
			click : function(){
				$("dl.seaBox dd ul li").removeClass("on").eq(i).addClass("on");
			}
		});
	});

	$("dl.sexBox dd ul li").each(function(i){
		$(this).find("label").bind({
			click : function(){
				$("dl.sexBox dd ul li").removeClass("on").eq(i).addClass("on");
			}
		});
	});
	
	$(".recomList .box").each(function(idx){
		$(this).find(".name").each(function(i){
			$(this).find(".kcal").css({ "left" : -1*($(this).find(".kcal").outerWidth()+7)+"px" });
		});
	});
};

var recomPrint = function(obj, dietCd){
	$("#dietCd").val(dietCd);
	var $thisId = $(this).attr("id");
	var param = $("form[name=searchForm]").serialize();
	 
	 $.ajax({   
		type: "GET"  
		,url: "/user/diet/dietDetail.do"
		,data: param
		,success:function(data){
			$("#recomPop").html(data);
			jQuery.print('#'+obj+" .printBox");
		}
		,error:function(data){
			alert("recomPrint error");
		}
	});
};

var recomPrintDtl = function(obj){
	jQuery.print('#'+obj+" .printBox");
};

var mypagePrint = function(obj){
	jQuery.print('#'+obj+" .printBox");
};




/************************************************************
	 Nutrient Jacascript
	 Data : 2014.12.27
	 Developer : Sung Min Chang
************************************************************/
var untrFn = function(){
	var $obj = $(".nutrientCon");
	$obj.find(".listType .typeBtn a").each(function(idx){
		$(this).bind("click", function(){
			var nowCls = (idx == 1) ? "typeTxt" : "typeImg";
			$obj.find(".list").removeClass().addClass("list "+nowCls);
			$obj.find(".listType .typeBtn a").removeClass("on").eq(idx).addClass("on");			
			
			if(idx == 1){
				img.small();
			}else{
				img.big();
			}
		});
	});

	$(".brandBtn").bind("click",function(){
		if($(".brandNav").css("display") == "none"){
			$(".brandNav").show();
		}else{
			$(".brandNav").hide();
		}
	});
	
	$(".brandNav ul li").each(function(idx){
		$(this).bind({
			mouseenter : function(){
				$(this).find("img").stop().animate({"margin-left" : "-136px"},350);
			},
			mouseleave : function(){
				$(this).find("img").stop().animate({"margin-left" : "0"},250);
			}
		});
	});

	var $img = $obj.find(".list .box dl dd");
	
	$('.nutrientCon img').imgpreload
	({
	    each: function()
	    {
	        // this = dom image object
	        // check for success with: $(this).data('loaded')
	        // callback executes when each image loads
	    },
	    all: function()
	    {

			$img.css("opacity","1");
			img.big();
	        // this = array of dom image objects
	        // check for success with: $(this[i]).data('loaded')
	        // callback executes when all images are loaded
	    }
	});
	var img = {
		big : function(){
			
			var maxWid = $img.width(),
				maxHig = $img.height();
			
			$img.each(function(i){
				if(maxWid <= $(this).find("img").width()){
					$(this).find("img").addClass("hig").css("margin-top" , (maxHig/2)-($(this).find("img").height()/2) + "px");
				}
			});
		},
		small : function(){

			var maxWid = $img.width(),
				maxHig = $img.height();
		
			$img.each(function(i){
				if(maxWid <= $(this).find("img").width()){
					$(this).find("img").addClass("hig").css("margin-top" , (maxHig/2)-($(this).find("img").height()/2) + "px");
				}
			});
		}
	};
	
};

/************************************************************
	 Mypage Jacascript
	 Data : 2014.12.27
	 Developer : Sung Min Chang
************************************************************/
var mypageTbl = function(){

	mypage.clickEvt();

};
var mypage = {
	dietAdd : function(tr, td){
		/*var $pop = $("#foodPop");
		$pop.find("input[name=tr]").val(tr);
		$pop.find("input[name=td]").val(td);*/
		var $form = $("#myDietForm");
		$form.find("input[name=tr]").val(tr);
		$form.find("input[name=td]").val(td);

		$("#foodPop").load("/user/mydiet/foodSearchAsync.do", {
		}, function(data) {
			pop.open("foodPop");
		});
	},
	dietDel : function(inf, li){
		var txt = inf.split("|")[3];	//[3]=음식명

		$("#delPop .txt span").html(txt);
		$("#delPop, .popBg").fadeIn(300);
		$(".delBtn").unbind("click").bind("click",function(){
			mypage.dietDelProc(inf);
			li.parentNode.parentNode.removeChild(li.parentNode);
			mypage.altCancel();
		});
	},
	tdDel : function(i){
		var $tbl = $(".myTbl .list");
		$tbl.find("tbody tr").each(function(){
			
			var $inf = $(this).find("td").eq(i).find("input[name=inf]"),
				infLen = $inf.length 
				infVal = $inf.val();
			if(infLen == 1){
				mypage.dietDelProc(infVal);
			}
			
			$(this).find("td").eq(i).find("ul").remove();
		});
	},
	dietDelProc : function(inf) {
		inf = inf.split("|"); //음식정보 : [0]=순서, [1]=식단구분, [2]=음식코드, [3]=음식명, [4]=중량, [5]=칼로리
		
		for(var divIdx in mypage.arrChoesFood){
			if(divIdx == inf[1]){
				for(var foodIdx in mypage.arrChoesFood[divIdx]){
					if(mypage.arrChoesFood[divIdx][foodIdx][2] == inf[2]) {
						mypage.arrChoesFood[divIdx].splice(foodIdx, 1);
					}
				}
			}
		}
		mypage.calcKcalMinus();
	},
	pick : function(name, g, kcal){
		var $tbl = $(".myTbl .list");
		$tbl.find("tbody tr").eq(i).find("td").eq(o).append(trHtml);
		pop.close();
	},
	altAdd : function(obj, txt){
		obj.parentNode.style.backgroundPosition = "left bottom";
		$("#addPop .txt span").html(txt);
		$("#addPop").fadeIn(300);
	},
	altAlert : function(txt){
		$("#alertPop .txt span").html(txt);
		$("#alertPop").fadeIn(300);
	},
	sumEng : 0,			//총 열량
	breakfastEng : 0,	//아침 총 열량
	lunchEng : 0,		//점심 총 열량
	dinnerEng : 0,		//저녁 총 열량
	snackEng : 0,		//간식 총 열량
	arrChoesFood : [	//arrChoesFood[아침,점심,저녁,간식]
    	new Array(), //breakfast = {foodOrd(tr),foodDivCd(td),foodCd,foodNm,foodWt,foodEng}
    	new Array(), //lunch = {foodOrd(tr),foodDivCd(td),foodCd,foodNm,foodWt,foodEng}
    	new Array(), //dinner = {foodOrd(tr),foodDivCd(td),foodCd,foodNm,foodWt,foodEng}
    	new Array() //snack = {foodOrd(tr),foodDivCd(td),foodCd,foodNm,foodWt,foodEng}
    ],
	addChoes : function(){
		var $tbl = $(".myTbl .list"),
			$pop = $("#foodPop"),
			$form = $("#myDietForm"),
			$td = $tbl.find("tr").eq($form.find("input[name=tr]").val()).find("td").eq($form.find("input[name=td]").val()),
			txt = $pop.find("input[type=checkbox]:checked").val().split("|")[1],
			tr = $form.find("input[name=tr]").val(),
			td = $form.find("input[name=td]").val(),
			inf = tr+"|"+td+"|"+$pop.find("input[type=checkbox]:checked").val();

		if(mypage.addChoesProc(inf)) return;
		mypage.calcKcalPlus();
		
		if($td.find("ul").length == 0){
			$td.append("<ul></ul>");
		}

		$td.find("ul").html("<li><span>"+txt+"</span><input type='hidden' name='inf' value='"+inf+"' /><a href='#none' onclick='mypage.dietDel(\""+inf+"\", this);'><img src='../images/btn/btn_exclude.gif' alt='-' /></a></li>");

		pop.close();
		mypage.altCancel();

	},
	addChoesProc : function(inf) {
		inf = inf.split("|");
		
		//식단정보 체크
		for(var divIdx in mypage.arrChoesFood){
			if(divIdx == parseInt(inf[1])) {	//식단구분 : 0=아침, 1=점심, 2=저녁, 3=스낵
				for(var foodIdx in mypage.arrChoesFood[divIdx]){		//음식정보 : [0]=순서, [1]=식단구분, [2]=음식코드, [3]=음식명, [4]=중량, [5]=칼로리
					if(mypage.arrChoesFood[divIdx][foodIdx][0] == inf[0]) { //식단에 음식이 엎어쳐지면 기존 정보 삭제
						mypage.arrChoesFood[divIdx].splice(inf[0]-1,1);
					} else if(mypage.arrChoesFood[divIdx][foodIdx][2] == inf[2]) {	//식단에 음식이 중복인지 체크
						mypage.altAlert(inf[3]);
						return true;
					}
				}
			}
		}
		
		//선택한 음식정보를 arrChoesFood 에 추가
		for(var idx in mypage.arrChoesFood){
			//tr 순서대로 배열에 추가
			if(idx == parseInt(inf[1])) mypage.arrChoesFood[idx].splice(inf[0]-1,0,inf);
		}
	},
	calcKcalPlus : function(){
		this.sumEng = 0;
		this.breakfastEng = 0;
		this.lunchEng = 0;
		this.dinnerEng = 0;
		this.snackEng = 0;
		
		for(var divIdx in this.arrChoesFood){
			for(var foodIdx in this.arrChoesFood[divIdx]){
				this.sumEng += parseInt(this.arrChoesFood[divIdx][foodIdx][5]);
				
				if(divIdx == 0) this.breakfastEng += parseInt(this.arrChoesFood[divIdx][foodIdx][5]);
				else if(divIdx == 1) this.lunchEng += parseInt(this.arrChoesFood[divIdx][foodIdx][5]);
				else if(divIdx == 2) this.dinnerEng += parseInt(this.arrChoesFood[divIdx][foodIdx][5]);
				else if(divIdx == 3) this.snackEng += parseInt(this.arrChoesFood[divIdx][foodIdx][5]);
			}
		}
		$(".subContainer .subCon .mypageCon .myBox .total span").html(this.sumEng);
	},
	calcKcalMinus : function(){
		this.sumEng = 0;
		this.breakfastEng = 0;
		this.lunchEng = 0;
		this.dinnerEng = 0;
		this.snackEng = 0;
		
		for(var divIdx in this.arrChoesFood){
			for(var foodIdx in this.arrChoesFood[divIdx]){
				this.sumEng -= parseInt(this.arrChoesFood[divIdx][foodIdx][5]);
				
				if(divIdx == 0) this.breakfastEng -= parseInt(this.arrChoesFood[divIdx][foodIdx][5]);
				else if(divIdx == 1) this.lunchEng -= parseInt(this.arrChoesFood[divIdx][foodIdx][5]);
				else if(divIdx == 2) this.dinnerEng -= parseInt(this.arrChoesFood[divIdx][foodIdx][5]);
				else if(divIdx == 3) this.snackEng -= parseInt(this.arrChoesFood[divIdx][foodIdx][5]);
			}
		}
		
		this.sumEng = this.sumEng * -1;
		this.breakfastEng = this.breakfastEng * -1;
		this.lunchEng = this.lunchEng * -1;
		this.dinnerEng = this.dinnerEng * -1;
		this.snackEng = this.snackEng * -1;
		
		$(".subContainer .subCon .mypageCon .myBox .total span").html(this.sumEng);
	},
	addCancel : function(){
		$(".foodPop .list .tbl tbody tr td .ckBox").css("background-position","left top").find("input").prop("checked",false);
		$(".alertPop").fadeOut();
	},
	altCancel : function(){
		$(".alertPop, .popBg").fadeOut();
	},
	altConfirm : function(){
		$(".foodPop .list .tbl tbody tr td .ckBox").css("background-position","left top").find("input").prop("checked",false);
		$(".alertPop").fadeOut();
	},
	memuAdd : function(){
		var $tbl = $(".myTbl .list"),
			$tr = $tbl.find("tr"),
			max = $tr.length,
			trHtml = "<tr>" +
						"<td><a href='#none' class='addBtn'><img src='../images/btn/btn_add.gif' alt='+' /></a></td>" +
						"<td><a href='#none' class='addBtn'><img src='../images/btn/btn_add.gif' alt='+' /></a></td>" +
						"<td><a href='#none' class='addBtn'><img src='../images/btn/btn_add.gif' alt='+' /></a></td>" +
						"<td><a href='#none' class='addBtn'><img src='../images/btn/btn_add.gif' alt='+' /></a></td>" +
					"</tr>";

		$tbl.find("tbody").append(trHtml);

		mypage.clickEvt();

	},
	memuDel : function(){
		var $tbl = $(".myTbl .list"),
			$maxLen = $(".myTbl .list").find("tr").length-2;
		
		for(var divIdx in mypage.arrChoesFood){
			for(var foodIdx in mypage.arrChoesFood[divIdx]){		//음식정보 : [0]=순서, [1]=식단구분, [2]=음식코드, [3]=음식명, [4]=중량, [5]=칼로리
				if(mypage.arrChoesFood[divIdx][foodIdx][0] == $maxLen) {
					mypage.arrChoesFood[divIdx].splice(foodIdx, 1);
				}
			}
		}
		
		mypage.calcKcalMinus();
		
		$tbl.find("tbody tr:last").remove();
	},
	clickEvt : function(){
		var $tbl = $(".myTbl table.list"),
		$th = $tbl.find("thead tr th"),
		$tr = $tbl.find("tr");
	
		$th.each(function(i){
			$(this).find("a.del").unbind("click").bind("click", function(){
				mypage.tdDel(i);
			});
		});
		$tr.each(function(idx){
			$(this).find("td").each(function(t){

				$(this).find("a.addBtn").unbind("click").bind("click", function(){
					mypage.dietAdd(idx, t);
				});
				
			});
		});
	},
	//출처는 "내 몸이 건강해지는 866가지 칼로리수첩 -손정우"
	walkBurnKcal : 68,			//걷기 분당 운동시 소모 칼로리
	runBurnKcal : 191,			//뛰기 분당 운동시 소모 칼로리
	bicycleBurnKcal : 109		//자전거 분당 운동시 소모 칼로리
}

var StringBuffer = function() {
    this.buffer = new Array();
};
StringBuffer.prototype.append = function(str) {
    this.buffer.push(str);
};
StringBuffer.prototype.toString = function() {
    return this.buffer.join("");
};

/************************************************************
	 banner Jacascript
	 Data : 2014.10.29
	 Developer : Sung Min Chang
************************************************************/
var bner = {
	init : function(){
		bner.ac();
		bner.evt();
	},
	evt : function(){
		var $obj = $("#aside"),
			$li = $obj.find("ul li");
		
		$(window).bind("scroll",function(){
			bner.ac();
		});
		$(window).bind("resize",function(){
			bner.ac();
		});
	},
	ac : function(){
		var $obj = $("#aside"),
			$footer = $("#footer"),
			sclTop = $(window).scrollTop(),
			docHig  = $(document).height(),
			winHig = $(window).height(),
			winWid = $(window).width(),
			wid = 1020+((winWid-1000)/2),
			asideHig = $obj.find(".aside").outerHeight()+$obj.find(".aside2").outerHeight(),
			footTop = $(document).height() - ($footer.outerHeight() + asideHig),
			Top = posVal = null,
			pos = "top";
		if(sclTop > footTop){
			Top = $footer.outerHeight()+20,
			pos = "absolute",
			posVal = "bottom";
		}else{
			Top = (194 > $(window).scrollTop()) ? 214-$(window).scrollTop() : 20,
			pos = "fixed",
			posVal = "top";
		}
		
		$obj.attr("style","position:"+pos+";"+posVal+":"+Top+"px;left:"+wid+"px;");
	}

}

/************************************************************
	 Popup Jacascript
	 Data : 2014.10.29
	 Developer : Sung Min Chang
************************************************************/
var pop = {
	open : function(obj){
		$obj = $("#"+obj);
		$obj.css({
			"margin-left" : -1*($obj.outerWidth()/2) + "px"
		}).fadeIn(300);
		setTimeout(function(){
			
			var agt = navigator.userAgent.toLowerCase(),
				winHig = $(window).height(),
				docHig = $(document).height(),
				objHig = $obj.outerHeight(),
				sclTop = (agt.indexOf("trident") != -1) ? $("html, body").scrollTop() : $("body").scrollTop(),
				topCk = sclTop+((winHig-objHig)/2),
				marTop = (topCk > 0) ? topCk : 0;
				
			$obj.css({
				"margin-top" : marTop + "px"
			});
			
		},100);
		if(obj != "evtPop"){
			$(".popBg").fadeIn(300);	
		}
	},
	close : function(){
		var $obj = $(".LayPop"),
			$bg = $(".popBg");
		$obj.fadeOut(300);
		$bg.fadeOut(300);

	},
	altOpen : function(obj){
		var $obj = $("#"+obj),
			$bg = $(".popBg");
		$obj.fadeIn(300);
		$bg.fadeIn(300);
	},
	altCle : function(){
		var $obj = $(".alertPop"),
			$bg = $(".popBg");
		$obj.fadeOut(300);
		$bg.fadeOut(300);
	}
};

var chartPop = function(type){

	var $obj = $(".chartCon"),
		now = ("text" == type) ? 1 : 0,
		be = ("text" == type) ? 0 : 1;
	
	$obj.find(".btn a.btn").hide().eq(now).show();
	$obj.find(".box").eq(now).css({
		"display" : "block",
		"margin-left" : "-100px"
	}).stop().animate({
		"margin-left" : "0",
		"opacity" : 1
	});
	$obj.find(".box").eq(be).stop().animate({
		"opacity" : 0,		
		"margin-left" : "100px"
	},function(){
		$obj.find(".box").eq(be).css("display","none");
	});

}

var schDay = function(){
	$(".dayPop").fadeOut("300",function(){
		$(this).addClass("seeBox");
	});
};
