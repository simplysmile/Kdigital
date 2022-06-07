const dateFormat = (date) => {
    return date.toLocaleDateString().replace(/\./g, "").split(" ");
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

// 전달 날짜 표시하기
for (let i = 0; i < prevDay; i++) {
    htmlDummy += `<div class="noColor"></div>`;
 }

// 현재 날짜 표시하기
for (let i = 1; i <= lastDay; i++) {    
    if (i == nowDay){
        htmlDummy += `<div id="`+ nowMonth +`m`+ i +`" class="colToday" onclick="selectD()">${i}`
        htmlDummy += `<li>식단</li>`
        htmlDummy += `<li>운동</li>`
        htmlDummy += `<li>`+dateFormat(date)+`</li>`
        
        
        
        htmlDummy += `</div>`;


    }
    else{

        htmlDummy += `<div id="`+ nowMonth +`m`+ i +`" class="abc" onclick="selectD()">${i}</div>`;
    }
    
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


