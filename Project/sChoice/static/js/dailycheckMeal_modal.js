// 모달
function addMeal(){
    modal.style.display = "block";
}
// Get the modal
var modal = document.getElementById("myModal");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];
// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
}
// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

var dummydata=[]
//document.addEventListener('keydown',function(e){

document.getElementById('serDB').addEventListener('keydown',function(e){
    if(e.code === 'Enter'){
         
        searchDB()
    }
})



dummydata1=[
{'id':1,'name':'사과','weight':100,'kcal':57,'carb':14.4,'prot':0.2, 'fat':0},
{'id':2,'name':'사과즙','weight':120,'kcal':59,'carb':14.5,'prot':0.1, 'fat':0.1},
{'id':3,'name':'사과식초','weight':10,'kcal':2,'carb':0.2,'prot':0, 'fat':0}
]
dummydata2=[
{'id':4,'name':'고구마','weight':75,'kcal':98,'carb':23.4,'prot':1.0, 'fat':0.2},
{'id':5,'name':'고구마말랭이','weight':60,'kcal':172,'carb':38.0,'prot':4.0, 'fat':0.4},
{'id':6,'name':'고구마맛탕','weight':100,'kcal':245,'carb':47.3,'prot':1.6, 'fat':5.5}
]

function searchDB()
{
    //if($("#serDB").val().length<=1){
    //    alert('2글자 이상 입력하셔야 검색이 가능합니다.')
    //    $("#serDB").focus()
    //    return false
    //}

    var kword = document.getElementById('serDB').value;
    $.ajax({
        type: "GET",
        //url:"/static/js/oracle.py",
        url:"/dailycheck/searchMeal/",
        data: {"keyword":kword},
        dataType:"json",
        
        success: function (data) {
            console.log(typeof(data));
            console.log(data.data.length);

            var dblist = ''

            for (var i = 0; i < 3; i++) {
                dblist += '<tr><td>'+ data.data[i].f_name + '</td>'
                dblist += '<td>'+ data.data[i].f_weight + '</td>'
                dblist += '<td>'+ data.data[i].f_cal + '</td>'
                dblist += '<td><img width=20 height=20 src="/static/img/basic/plus_data.png" onclick="add_meal('+data.data[i].f_id+')"></td></tr>'
            }
            $('#mealdb_tbody').html(dblist)





        },
        error: function () {
            console.log('error');
        }
     });
 
    

    //document.search.submit()

    // const searchname = document.getElementById('serDB').value;

    //if(searchname=='사과'){ dummydata=dummydata1 }
    //else if(searchname=='고구마'){dummydata=dummydata2 }
    
    



    //dblist = ''

    //for (var i = 0; i < dummydata.length; i++) {

    //    dblist += '<tr><td>'+ dummydata[i].name + '</td>'
    //    dblist += '<td>'+ dummydata[i].weight + '</td>'
    //    dblist += '<td>'+ dummydata[i].kcal + '</td>'
    //    dblist += '<td><img width=20 height=20 src="/static/img/basic/plus_data.png" onclick="add_meal('+dummydata[i].id+')"></td></tr>'
   // }

    //$('#mealdb_tbody').html(dblist)

}

function del_meal(num)
{
    //var rmtxt = 5
    rmtxt = '.foodid'+num
    $(rmtxt).remove()
    
    
    

}
function add_meal(num)
{
    
    for (var i = 0; i < dummydata.length; i++) {
        if (num == dummydata[i].id){

            var adddata = dummydata[i]
        }

    }

    var insertdata=''

    insertdata += '<tr class="foodid'+adddata.id+'"><td>'+adddata.name +'</td>'
    insertdata += '<td><input id="foodweight'+adddata.id+'" class="foodweight" type="text" name="foodweight" size="5" value="'+adddata.weight +'" style="text-align:center;"><img width=20 height=20 src="/static/img/basic/chevron.png" onclick="modi_meal('+adddata.id+')"></td>'
    insertdata += '<td id="eat_cal'+adddata.id+'">'+adddata.kcal+'</td>'
    insertdata += '<td id="eat_carb'+adddata.id+'">'+adddata.carb+'</td>'
    insertdata += '<td id="eat_prot'+adddata.id+'">'+adddata.prot+'</td>'
    insertdata += '<td id="eat_fat'+adddata.id+'">'+adddata.fat+'</td>'
    insertdata += '<td><img width=20 height=20 src="/static/img/basic/minus_data.png" onclick="del_meal('+adddata.id+')"></td></tr>'



    


    
    $('#meal_input_tbody').append(insertdata)

    document.getElementById('foodweight').addEventListener('keydown',function(e){
        if(e.code === 'Enter'){
            
            testtest(adddata.id)
        }
    })



    

}

function modi_meal(num){
    
    // 수정 전 데이터 저장  
    for (var i = 0; i < dummydata1.length; i++) {
        if (num == dummydata1[i].id){
            
            var modidata = dummydata1[i]
        }
        
    }
    
    
    rmtxt = '.foodid'+num
    
    //alert(modidata.name)
    
    
    var change_gram = document.getElementById('foodweight'+ modidata.id ).value;
    var new_ratio = change_gram/Number(modidata.weight)
    new_ratio=new_ratio.toFixed(2)
    
    
    
    
    var modi_cal =Number(modidata.kcal)*new_ratio
    var modi_carb =Number(modidata.carb)*new_ratio
    var modi_prot =Number(modidata.prot)*new_ratio
    var modi_fat =Number(modidata.fat)*new_ratio
    
    
    
    var updated_data = ''
    updated_data += '<tr class="foodid'+modidata.id+'"><td class="foodid'+modidata.id+'">'+ modidata.name +'</td>'
    updated_data += '<td><input id="foodweight'+modidata.id+'" class="foodweight" type="text" name="foodweight" size="5" value="'+change_gram +'" style="text-align:center;"><img width=20 height=20 src="/static/img/basic/chevron.png" onclick="modi_meal('+modidata.id+')"></td>'
    
    var updated_data_cal = '<td id="eat_cal'+modidata.id+'">'+modi_cal+'</td>'
    var updated_data_carb = '<td id="eat_carb'+modidata.id+'">'+modi_carb+'</td>'
    var updated_data_prot = '<td id="eat_prot'+modidata.id+'">'+modi_prot+'</td>'
    var updated_data_fat = '<td id="eat_fat'+modidata.id+'">'+modi_fat+'</td>'

    var txt1 = '#eat_cal'+modidata.id
    var txt2 = '#eat_carb'+modidata.id
    var txt3 = '#eat_prot'+modidata.id
    var txt4 = '#eat_fat'+modidata.id

    $(txt1).html(updated_data_cal)
    $(txt2).html(updated_data_carb)
    $(txt3).html(updated_data_prot)
    $(txt4).html(updated_data_fat)
    
    
    //updated_data += '<td id="eat_cal'+modidata.id+'">'+modi_cal+'</td>'
    //updated_data += '<td id="eat_carb'+modidata.id+'">'+modi_carb+'</td>'
    //updated_data += '<td id="eat_prot'+modidata.id+'">'+modi_prot+'</td>'
    //updated_data += '<td id="eat_fat'+modidata.id+'">'+modi_fat+'</td>'
    //updated_data += '<td><img width=20 height=20 src="/static/img/basic/minus_data.png" onclick="del_meal('+modidata.id+')"></td></tr>'

    // $(rmtxt).remove()
    // $('#meal_input_tbody').append(updated_data)
    
  



        

    

}
