$(function(){
    $.ajax({
        url:"/static/exercisetest.json",
        dataType:"json",
        success:function(data){
            let note = ''
            note+='<tr>'
            let total_kcal=0
            let total_time=0
            let avg_time=0

            ex_count=data.length
            if(data.length>3){
                for(let i=0;i<3;i++){
                    note+='<td><progress  id="'+data[i].ex_no+'" value="'+ data[i].kcal_per +'" max="100"></progress></td>'

                }
                note+='</tr>'
                note+='<tr>'
                for(let i=1;i<4;i++){
                    note+='<td>'+data[i-1].ex_name+' : '+ data[i-1].burned_kcal+'kcal</td>'
                    total_kcal+=data[i-1].burned_kcal
                    total_time+=data[i-1].ex_time
                    
                }
            }
            else{
                for(let i=0;i<data.length;i++){
                    note+='<td><progress  id="'+data[i].ex_no+'" value="'+ data[i].kcal_per +'" max="100"></progress></td>'
                }
                note+='</tr>'
                note+='<tr>'
                for(let i=1;i<(data.length)+1;i++){
                    note+='<td>'+data[i-1].ex_name+' : '+ data[i-1].burned_kcal+'kcal</td>'
                    total_kcal+=data[i-1].burned_kcal
                    total_time+=data[i-1].ex_time
                }
            }
            avg_time= parseInt(total_time/data.length)

            note+='</tr>'
            note+='<tr style="height:50px"><td></td><td></td><td></td></tr>'
            note+='<tr><td style="color:#ff0000">'+total_time+'분</td><td style="color:#419e46">'+ex_count+'회</td><td style="color:#43419e">'+avg_time+'분</td></tr>'
            note+='<tr><td>총 운동 시간</td><td>운동 개수</td><td>평균 운동 시간</td></tr>'

            $("#progressbars").html(note)
            
            const counter = {
                id: 'counter',
                beforeDraw(chart, args, options) {
                  const { ctx, chartArea: { top, right , bottom, left, width, height } } = chart;
                  ctx.save();
                  ctx.fillStyle = 'black';
                  ctx.fillRect(width / 2, top + (height / 2), 0, 0);
                  ctx.font = '30px sans-serif';
                  ctx.textAlign = 'center';     
                  // w 변동 h 변동  l 70 r 변동 t 0 b 변동
                  //console.log("width", width); 
                  ctx.fillText('태운 칼로리', width / 2 +(left), top + (height / 2));
                  ctx.fillText((total_kcal)+'kcal', width / 2 +(left), top + (height / 2)+50);
                }
            };

            const ctx = document.getElementById('myChart').getContext('2d');
            const myChart = new Chart(ctx, {
                type: 'doughnut', 
                data: {
                    datasets: [{
                        label: '총 운동 칼로리',
                        data: [data[0].goal_burn_kcal,(100-80)],
                        backgroundColor: ['#7CCAAE','#eee'],
                        hoverOffset: 0,
                        cutout: "60%",
                    },
                    {
                        label: data[0].ex_name,
                        data: [data[0].burned_kcal,(100-data[0].burned_kcal)],
                        backgroundColor: ['#ECEC84','#eee'],
                        hoverOffset: 0
                    },
                    {
                        label: data[1].ex_name,
                        data: [data[1].burned_kcal,(100-data[1].burned_kcal)],
                        backgroundColor: ['#FFB69B','#eee'],
                        hoverOffset: 0
                    },
                    // {
                    //     label: '운동3 이름',
                    //     data: [data[3].kcal,(100-data[3].kcal)],
                    //     backgroundColor: ['#A299CA','#eee']
                    // },
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
                    cutoutPercentage: 60,

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
