const dateFormat = (date) => {
    return date.toLocaleDateString().replace(/\./g, "").split(" ");
}
const dateFormat_send = (date) => {
    return date.toISOString().slice(0,10);
    //return date.toLocaleDateString().replace(/\D/g , "");
}


// 달력 생성
const makeCalendar = (date) => {

    
    
    // 현재의 년도와 월 받아오기
    const [nowYear, nowMonth, nowDay] = dateFormat(date);
    
    // 지난달의 마지막 요일
    const prevDay = new Date(nowYear, nowMonth - 1, 1).getDay();
    
    // 현재 월의 마지막 날 구하기
    const lastDay = dateFormat(new Date(nowYear, nowMonth, 0)).pop() * 1;
    
    let htmlDummy = '';
    


    $.ajax({
        type: "GET",
        url:"/dailycheck/calendarData/",
        dataType:"json",   
        success: function (data) {
            var meal_keys = Object.keys(data.body_json.meal.m_cal)
            var exer_keys = Object.keys(data.body_json.exer.ex_cal)
            var user_keys = Object.keys(data.body_json.user.u_date)
            
            console.log((data.body_json.user))
            console.log(( data.body_json.user.u_date.length))
            console.log(( data.body_json.user.u_date[0]))
            console.log(( data.body_json.user.u_w[0]))

            var str = ''
            var str_ex = ''
            var str_user_w = ''
            var str_user_im = ''

            for (let i = 1; i <= lastDay; i++) {    

                for (let j = 0 ; j < meal_keys.length; j++){
                    var m_date = new Date(parseInt(meal_keys[j]));
                    if ( m_date.getDate() == i ){
                        
                        
                        if (data.goaleatcal >= data.body_json.meal.m_cal[meal_keys[j]]){
                            str = '<li style="font-size:11px;">식단: '+ data.body_json.meal.m_cal[meal_keys[j]] +'kcal<img width="10" src="/static/img/face_icon/smile.png"></li>'

                        }
                        else{

                            str = '<li style="font-size:11px;">식단: '+ data.body_json.meal.m_cal[meal_keys[j]] +'kcal<img width="10" src="/static/img/face_icon/angry.png"></li>'
                        }
                        
                        
                        
                        $("#"+nowMonth+"m"+i).append(str)
                    }
                }

                for (let k = 0 ; k < exer_keys.length; k++){
                    var ex_date = new Date(parseInt(exer_keys[k]));
                    if ( ex_date.getDate() == i ){
                        if (data.goalburncal < data.body_json.exer.ex_cal[exer_keys[k]] ){

                            str_ex = '<li style="font-size:11px;">운동: '+ data.body_json.exer.ex_cal[exer_keys[k]] +'kcal<img width="10" src="/static/img/face_icon/smile.png"></li>'
                        }
                        else{

                            str_ex = '<li style="font-size:11px;">운동: '+ data.body_json.exer.ex_cal[exer_keys[k]] +'kcal<img width="10" src="/static/img/face_icon/angry.png"></li>'
                        }
                        $("#"+nowMonth+"m"+i).append(str_ex)
                    }
                }

                for (let l = 0 ; l < user_keys.length; l++){
                    var usr_date = new Date(parseInt(data.body_json.user.u_date[l]));
                    if ( usr_date.getDate() == i ){
                        if (data.body_json.user.u_w[l]!= null ){
                            str_user_w = '<li style="font-size:11px; color:#36aeb3;">'+ data.body_json.user.u_w[l] +'kg </li>'
                            $("#"+nowMonth+"m"+i).append(str_user_w)
                        }
                        
                        if (data.body_json.user.u_im[l]!= null ){
                            str_user_im = '<li><img width="15" src="/static/img/nav_icon/image.png"></li>'
                            $("#"+nowMonth+"m"+i).append(str_user_im)
                        }
                    }
                }


            }
            


            
           


        },
        error: function () {
            console.log('error');
            // 전달 날짜 표시하기
            
        }
        
        
    }); // ajax 
    
    
for (let i = 0; i < prevDay; i++) {
    htmlDummy += `<div class="noColor"></div>`;
}

// 현재 날짜 표시하기
for (let i = 1; i <= lastDay; i++) {    
    htmlDummy += `<div id="`+ nowMonth +`m`+ i +`" class="abc" onclick="selectD('`+ [nowYear,nowMonth,i] +`')">${i}</div>`;
}





   

// 지금까지 추가한 날짜 박스
const maxDay = prevDay + lastDay;

// 마지막날이 들어있는 열에 남은 박스 채우기
const nextDay = (Math.ceil(maxDay / 7) * 7) - maxDay;

// 다음달 날짜
for (let i = 0; i < nextDay; i++) {
    htmlDummy += `<div class="noColor"></div>`;
}

document.querySelector(`.dateBoard`).innerHTML = htmlDummy;
document.querySelector(`.dateTitle`).innerText = `${nowYear}년 ${nowMonth}월`;
}
    
const date = new Date();

// Date 객체를 보내서 달력 생성
makeCalendar(date);

date.setMonth(date.getMonth() - 1);

// 이전달 이동
document.querySelector(`.prevDay`).onclick = () => {
    makeCalendar(new Date(date.setMonth(date.getMonth() - 1)));
}

// 다음달 이동
document.querySelector(`.nextDay`).onclick = () => {
    makeCalendar(new Date(date.setMonth(date.getMonth() + 1)));
}


