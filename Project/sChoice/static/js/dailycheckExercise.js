$(function(){
    $.ajax({
        url:"/static/exercisetest.json",
        dataType:"json",
        success:function(data){
            let note = ''
            note+='<tr><td><progress  id="ex1B" value="'+ data[9].ex1 +'" max="100"></progress></td>'
            note+='<td><progress id="ex2B" value="'+ data[9].ex2 +'" max="100"></progress></td>'
            note+='<td><progress id="ex3B" value="'+ data[9].ex3 +'" max="100"></progress></td></tr>'
            note+='<tr><td>운동1 : '+ data[9].ex1+'kcal</td><td>운동2 : '+ data[9].ex2+'kcal</td><td>운동3 : '+data[9].ex3+'kcal</td></tr>'
            note+='<tr style="height:50px"><td></td><td></td><td></td></tr>'
            note+='<tr><td style="color:#ff0000">0분</td><td style="color:#419e46">0분</td><td style="color:#43419e">0분</td></tr>'
            note+='<tr><td>총 운동 시간</td><td>운동 횟수</td><td>1회 평균 운동 시간</td></tr>'

            $("#progressbars").html(note)

            const counter = {
                id: 'counter',
                beforeDraw(chart, args, options) {
                  const { ctx, chartArea: { top, right , bottom, left, width, height } } = chart;
                  ctx.save();
                  ctx.fillStyle = 'black';
                  ctx.fillRect(width / 2, top + (height / 2), 0, 0);
                  ctx.font = '45px sans-serif';
                  ctx.textAlign = 'center';     
                  // w 변동 h 변동  l 70 r 변동 t 0 b 변동
                  //console.log("width", width); 
                  ctx.fillText('태운 칼로리', width / 2 +(left), top + (height / 2));
                  ctx.fillText('680kcal', width / 2 +(left), top + (height / 2)+50);
                }
            };

            const ctx = document.getElementById('myChart').getContext('2d');
            const myChart = new Chart(ctx, {
                type: 'doughnut', 
                data: {
                    datasets: [{
                        label: '총 운동 칼로리',
                        data: [80,(100-80)],
                        backgroundColor: ['#7CCAAE','#eee'],
                        hoverOffset: 0,
                        cutout: "50%",
                    },
                    {
                        label: '운동1 이름',
                        data: [data[9].ex1,(100-data[9].ex1)],
                        backgroundColor: ['#ECEC84','#eee'],
                        hoverOffset: 0
                    },
                    {
                        label: '운동2 이름',
                        data: [data[9].ex2,(100-data[9].ex2)],
                        backgroundColor: ['#FFB69B','#eee'],
                        hoverOffset: 0
                    },
                    {
                        label: '운동3 이름',
                        data: [data[9].ex3,(100-data[9].ex3)],
                        backgroundColor: ['#A299CA','#eee']
                    },
                ],
                    labels: ['burned','remain']
                },//data.
                options: {
                    aspectRatio: 1,
                    layout: {
                        padding: {
                            left: 70,
                            right: 70,
                            top: 0,
                            bottom: 10,
                        }
                    },
                    responsive: true,
                    cutoutPercentage: 40,

                   // rotation: 1.5 * Math.PI,
                   // borderColor: false,
                   //borderRadius: 10,
                    plugins: {
                        legend: {
                            
                            display: false,
                        },
                        
                        title: {
                            display: false,
                        },
                        tooltips: {
                            enabled: false
                        },
                        rotation: 1.5 * Math.PI,
                        

                    },
                },
                plugins: [counter]
            });//chart
            
            
            
        },
                    
        error:function(){

        }
    })//ajax

})//function
