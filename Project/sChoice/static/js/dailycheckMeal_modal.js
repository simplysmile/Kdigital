





// 모달
function addMeal(sdate,num){
    modal.style.display = "block";
    
    modifyMeal(sdate,num)
}
// Get the modal
var modal = document.getElementById("myModal");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];
// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
    location.reload();
}
// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
        location.reload();
    }
}




document.getElementById('serDB').addEventListener('keydown',function(e){
    if(e.code === 'Enter'){
         
        searchDB()
    }
})

var DBlist_data={} // 사용자가 검색한 db 전체 데이터 저장
var userdata=[] // 사용자가 식단으로 추가한 데이터를 저장
// db에 있는 
function searchDB()
{
    // 검색어
    var kword = document.getElementById('serDB').value;

    if($("#serDB").val().length<1){
        Swal.fire({
            title: '',
            text: '1글자 이상 입력하셔야 검색이 가능합니다.',
            icon: 'info',
            confirmButtonColor: '#87CEEB', 
            confirmButtonText: 'OK', 
        })
        .then(function(){
            //alert('1글자 이상 입력하셔야 검색이 가능합니다.')
        })
        $("#serDB").focus()
        return false 
    }
    
    $.ajax({
        type: "GET",
        url:"/dailycheck/searchMeal/",
        data: {"keyword":kword},
        dataType:"json",   
        success: function (data) {
            DBlist_data = data
            var dblist = ''
            for (var i = 0; i < data.data.length ; i++) {
                dblist += '<tr><td>'+ data.data[i].f_name + '</td>'
                dblist += '<td>'+ data.data[i].f_weight + '</td>'
                dblist += '<td>'+ data.data[i].f_cal + '</td>'
                dblist += '<td><img width=20 height=20 src="/static/img/basic/plus_data.png" onclick="add_meal('+data.data[i].f_id+')"></td></tr>'
            }
            if (dblist == ''){
                dblist += '<tr><td colspan=3> 검색하신 내용이 없습니다 </td></tr>'
                dblist += '<tr><td colspan=3> 검색어를 바꿔서 다시 검색해주세요 :) </td></tr>'
            }
            $('#mealdb_tbody').html(dblist)
        },
        error: function () {
            console.log('error');
        }
     });
}

// 식단 등록 테이블에서 해당 row 삭제
function del_meal(num)
{   
    //rmtxt = '.foodid'+num
    rmtxt = '.'+num
    $(rmtxt).remove()
}

function deltefromdb(num, mealSel, mealdate){


    Swal.fire({
        title: '정말로 삭제 하시겠습니까?',
        text: "다시 되돌릴 수 없습니다. 신중하세요.",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#87CEEB',
        cancelButtonColor: '#eee',
        confirmButtonText: '확인',
        cancelButtonText: '취소'
    }).then((result) => {
        if (result.isConfirmed) {
            rmtxt = '.'+num
            $(rmtxt).remove()

            $.ajax({
                type: "GET",
                url:"/dailycheck/delDailyMealData/",
                data: {"f_id":num, 'sdate':mealdate, 'mealtime':mealSel},
                dataType:"json",   
                success: function (data) {
                    console.log('성공');
                },
                error: function () {
                    console.log('error');
                }
            });
        }
    })


/*
    if (confirm('정말로 삭제 하시겠습니까?')){
        rmtxt = '.'+num
        $(rmtxt).remove()

        $.ajax({
            type: "GET",
            url:"/dailycheck/delDailyMealData/",
            data: {"f_id":num, 'sdate':mealdate, 'mealtime':mealSel},
            dataType:"json",   
            success: function (data) {
                console.log('성공');
            },
            error: function () {
                console.log('error');
            }
        });
    }*/


}

// 검색한 db 데이터를 식단 등록 테이블에 추가 
function add_meal(num)
{
    
    for (var i = 0; i < DBlist_data.data.length; i++) {
        if (num == DBlist_data.data[i].f_id){

            var adddata = DBlist_data.data[i]
        }

    }
    userdata.push(adddata)
    
    var insertdata=''

    insertdata += '<tr class="'+adddata.f_id+'"><td>'+adddata.f_name +'</td>'
    insertdata += '<td><input id="foodweight'+adddata.f_id+'" class="foodweight" type="text" name="foodweight" size="5" value="'+adddata.f_weight +'" style="text-align:center;"><img width=20 height=20 src="/static/img/basic/chevron.png" onclick="modi_meal('+adddata.f_id+')"></td>'
    insertdata += '<td id="eat_cal'+adddata.f_id+'">'+adddata.f_cal+'</td>'
    insertdata += '<td id="eat_carb'+adddata.f_id+'">'+adddata.f_carb+'</td>'
    insertdata += '<td id="eat_prot'+adddata.f_id+'">'+adddata.f_prot+'</td>'
    insertdata += '<td id="eat_fat'+adddata.f_id+'">'+adddata.f_fat+'</td>'
    insertdata += '<td><img width=20 height=20 src="/static/img/basic/minus_data.png" onclick="del_meal('+adddata.f_id+')"></td></tr>'
 
    if (userdata.length ==1){

        $('#meal_input_tbody').html('')
    }
    $('#meal_input_tbody').append(insertdata)
    document.getElementById('foodweight').addEventListener('keydown',function(e){
        if(e.code === 'Enter'){
            testtest(adddata.id)
        }
    })
}

// 식단에 저장한 데이터의 무게를 조절 
function modi_meal(num){
    
    // 수정 전 데이터 저장  
    // 사용자가 식단리스트에 추가한 데이터 중에서 수정하고싶은 데이터를 찾아 modidata에 저장
    for (var i = 0; i < userdata.length; i++) {
        if (num == userdata[i].f_id){
            
            var modidata = userdata[i]
        }
        
    }

    // 무게를 통해 칼로리 및 탄단지 수정을 위한 비율 계산
    var change_gram = document.getElementById('foodweight'+ modidata.f_id ).value;
    var new_ratio = change_gram/Number(modidata.f_weight)
    new_ratio=new_ratio.toFixed(2)
        
    
    var modi_cal =Number(modidata.f_cal)*new_ratio
    var modi_carb =Number(modidata.f_carb)*new_ratio
    var modi_prot =Number(modidata.f_prot)*new_ratio
    var modi_fat =Number(modidata.f_fat)*new_ratio
    
    
    
    var updated_data = ''
    updated_data += '<tr class="'+modidata.f_id+'"><td class="'+modidata.f_id+'">'+ modidata.f_name +'</td>'
    updated_data += '<td><input id="foodweight'+modidata.f_id+'" class="foodweight" type="text" name="foodweight" size="5" value="'+change_gram +'" style="text-align:center;"><img width=20 height=20 src="/static/img/basic/chevron.png" onclick="modi_meal('+modidata.f_id+')"></td>'
    
    var updated_data_cal = '<td id="eat_cal'+modidata.f_id+'">'+modi_cal.toFixed(2)+'</td>'
    var updated_data_carb = '<td id="eat_carb'+modidata.f_id+'">'+modi_carb.toFixed(2)+'</td>'
    var updated_data_prot = '<td id="eat_prot'+modidata.f_id+'">'+modi_prot.toFixed(2)+'</td>'
    var updated_data_fat = '<td id="eat_fat'+modidata.f_id+'">'+modi_fat.toFixed(2)+'</td>'

    var txt1 = '#eat_cal'+modidata.f_id
    var txt2 = '#eat_carb'+modidata.f_id
    var txt3 = '#eat_prot'+modidata.f_id
    var txt4 = '#eat_fat'+modidata.f_id

    $(txt1).html(updated_data_cal)
    $(txt2).html(updated_data_carb)
    $(txt3).html(updated_data_prot)
    $(txt4).html(updated_data_fat)
    


}
function canceldBtnb()
{
    Swal.fire({
        title: '등록을 취소하시겠습니까 ?',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#87CEEB',
        cancelButtonColor: '#eee',
        confirmButtonText: '확인',
        cancelButtonText: '취소'
    }).then((result) => {
        if (result.isConfirmed) {
            modal.style.display = "none";   
            location.reload();
        }
    })


    /*
    if (confirm('등록을 취소하시겠습니까?')){
        modal.style.display = "none";   
        location.reload();
    }*/
}
var mealtimesel = ''
function modifyMeal(sdate,num)
{
    var mealSel = ''
    // 아침, 점심, 저녁, 간식
    if (num ==1){
        
        mealSel='B'

    }
    else if (num ==2){
        mealSel='L'
    }
    else if (num ==3){
        mealSel='D'
    }
    else if (num ==4){
        mealSel='S'
    }
    mealtimesel = mealSel
    
    
    // 만약에 데이터가 있을 경우... 보여주기 . 
    mymeallistDic = {'len':6,'mealSel':mealSel}

    $.ajax({
        type: "GET",
        url:"/dailycheck/"+ sdate +"/addMealData/",
        data: mymeallistDic,
        dataType:"json",   
        success: function (data) {
            
            var msel= document.querySelector('#m_select').options[1].value 
            document.querySelector('#m_select').options[num].selected = true

            if (mealtimesel=='B'){
                $('#selbox').prepend('<p style="text-align:center; width:100px; font-size:30px;  font-weight: bold;background-color:#A0DDE0;">아침</p>')
            }

            else if (mealtimesel=='L'){
                $('#selbox').prepend('<p style="text-align:center; width:100px; font-size:30px;  font-weight: bold;background-color:#A0DDE0;">점심</p>')
            }

            else if (mealtimesel=='D'){
                $('#selbox').prepend('<p style="text-align:center; width:100px; font-size:30px;  font-weight: bold;background-color:#A0DDE0;">저녁</p>')
            }

            else if (mealtimesel=='S'){
                $('#selbox').prepend('<p style="text-align:center; width:100px; font-size:30px;  font-weight: bold;background-color:#A0DDE0;">간식</p>')
            }
            

            var insertdata=''
            for(var i = 0 ; i < data.indata.length; i++){
                
                var adddata = data.indata[i]
               
            
                insertdata += '<tr class="'+adddata.f_id+'"><td>'+adddata.f_name +'</td>'
                insertdata += '<td><input id="foodweight'+adddata.f_id+'" class="foodweight" type="text" name="foodweight" size="5" value="'+adddata.f_weight +'" style="text-align:center;"></td>'
                insertdata += '<td id="eat_cal'+adddata.f_id+'">'+adddata.f_cal+'</td>'
                insertdata += '<td id="eat_carb'+adddata.f_id+'">'+adddata.f_carb+'</td>'
                insertdata += '<td id="eat_prot'+adddata.f_id+'">'+adddata.f_prot+'</td>'
                insertdata += '<td id="eat_fat'+adddata.f_id+'">'+adddata.f_fat+'</td>'
                insertdata += '<td><img width=20 height=20 src="/static/img/basic/minus_data.png" onclick="deltefromdb('+adddata.f_id+',\'' +mealtimesel+ '\'' +',\'' +data.mealdate+'\')"></td></tr>'
                
                
            }
            if ( insertdata !=''){

                $('#meal_input_tbody').html(insertdata)
            }
            

            

        
            
        },
        error: function () {
            console.log('error');
        }
    });
}
function registerdbBtn(sdate)
{
    if($("#m_select").val()==''){
        alert('식사 시간을 선택하셔야 입력이 가능합니다.')
        $("#m_select").focus()
        return false
    }

    var mealtime=$("#m_select").val()
    

    
    




    var mtbody = document.getElementById('meal_input_tbody');

    console.log(mtbody)
  
    console.log(mtbody.rows[0].cells[0].innerText)

   
    var realwet = document.getElementById('foodweight'+mtbody.rows[0].className).value;
    console.log(realwet)
    

    
    // alert(mtbody.rows[0].className)


    var mymeallist=[]
    for (var i = 0 ;i < mtbody.rows.length; i++){
        var mymeal = {'f_id':mtbody.rows[i].className,'f_name':mtbody.rows[i].cells[0].innerText,
        'f_weight': document.getElementById('foodweight'+mtbody.rows[i].className).value,
        'f_cal': Math.round(mtbody.rows[i].cells[2].innerText),
        'f_carb': mtbody.rows[i].cells[3].innerText,
        'f_prot': mtbody.rows[i].cells[4].innerText,
        'f_fat': mtbody.rows[i].cells[5].innerText}

        mymeallist.push(mymeal);
        

    }

    //console.log(mymeallist)

    mymeallistDic = {'d':mymeallist, 'len': mymeallist.length,'mealtime':mealtime }

    // data: JSON.stringify(mymeallistDic),

    // alert(sdate)
    

    $.ajax({
        type: "POST",
        url:"/dailycheck/"+ sdate +"/addMealData/",
        data: mymeallistDic,
        dataType:"json",   
        success: function (data) {
            Swal.fire({
                title: '',
                text: data.msg,
                icon: 'info',
                confirmButtonColor: '#87CEEB', // confrim 버튼 색깔 지정
                confirmButtonText: 'OK', // confirm 버튼 텍스트 지정
                //"로그인을 하셔야 달력 상세보기가 가능합니다.",'','success'
            })
            .then(function(){
                window.location.reload()
            })


            //alert(data.msg)
            //window.location.reload()

           
            
        },
        error: function () {
            console.log('error');
        }
     });


}
