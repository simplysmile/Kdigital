

$(function(){
    $.ajax({
        url:"/dailycheck/myStatusData",
        dataType:"json",
        success:function(data){

            console.log(data)


            // 달성일, 몸무게 차트 
            const goal_txt = {
                id: 'goal_txt',
                beforeDraw(chart, args, options) {
                  const { ctx, chartArea: { top, right , bottom, left, width, height } } = chart;
                  ctx.save();
                  ctx.fillStyle = 'black';
                  ctx.fillRect(width / 2, top + (height / 2), 0, 0);
                  ctx.font = '30px sans-serif';
                  ctx.textAlign = 'center';     
                  var daystr = String(data.workoutday)+'/'+String(data.goal_period) +' 일'
                  var kgstr = '목표까지 '+String(data.weight[0]-data.goal_weight)+'kg!!'
                  ctx.fillText(daystr, width / 2 +(left), top + (height / 2)+70);
                  ctx.fillText(kgstr, width / 2 +(left), top + (height / 2)+120);
                }

            };

           

            const ctx_goal = document.getElementById('goalchart').getContext('2d');
            const goalchart = new Chart(ctx_goal, {
                type: 'doughnut', 
                data: {
                    labels: ['done','remain'],
                    datasets: 
                    [
                        {
                            label: '날짜',
                            data: [data.workoutday,(data.goal_period-data.workoutday),0,0],
                            backgroundColor: ['#8C5A76','#eee'],
                            cutout: "95%",
                            //hoverOffset: 5,    
                            rotation: -120,
                            circumference: 240,
                            
                        },
                        {
                            label: '몸무게',
                            data: [0,0,(data.firstweight-data.goal_weight)-(data.weight[0]-data.goal_weight),(data.weight[0]-data.goal_weight)],
                            backgroundColor: ['#6D80A6','#eee'],
                            cutout: "90%",
                            //hoverOffset: 5,    
                            rotation: -120,
                            circumference: 240,
                        },
                        
                    ],
                },//data.
                options: {
                
                    plugins: {
                        
                    legend: {
                        display: false
                    },
                    tooltip: {
                        enabled: false
                    },
                }
                            
                },
                  
               plugins: [goal_txt],

            }); // 달성일, 몸무게 차트 
            

            // 몸무게 라인 그래프 
            var lenw = data.weight.length
            var goalw = []
            var currw=[]
            var currdays=[]
            for (var i = 0 ; i<lenw ; i++)
            {
                goalw.push(data.goal_weight)
                currw.push(data.weight[lenw-i-1])
                currdays.push(data.alldays[lenw-i-1])

            }

            const ctxW = document.getElementById('weightchange').getContext('2d');
            const labels_weight = currdays
            const weightchange = new Chart(ctxW, {
                type: 'line', 
                data: {
                    labels: labels_weight,
                    datasets: [
                    {
                        label: '몸무게 변화추이',
                        data: currw,
                        borderColor: ['rgb(255, 99, 132)'],
                        backgroundColor:['rgba(255, 99, 132, 0.2)']
                    },
                    {
                        label: '목표몸무게',
                        data: goalw,
                        borderColor: ['rgba(54, 162, 235)'],
                        backgroundColor:['rgba(54, 162, 235, 0.2)']
                    }
                
                ],
                },//data.
               
                options: {
                    responsive: true,
                    scales: {
                        y: {
                            max: data.firstweight + 1 ,
                            min: data.goal_weight -5,
                            ticks: {
                                stepSize: 1
                            }
                        }
                    }
                                       
                }
            }); // 몸무게 라인차트



            var meal_keys = Object.keys(data.mealweak.m_cal)
            var exer_keys = Object.keys(data.exerweak.m_cal)
            var eatweek=[]
            var exerweek=[]
            var exergoalweek=[]
            var goalweek=[]
            var week = new Array('일','월','화','수','목','금','토','일','월','화','수','목','금','토')
            var d = new Date();
            //alert(week[d.getDay()])
            var titleweek = []

            for (var i = 0; i<meal_keys.length;i++){
                eatweek.push(data.mealweak.m_cal[meal_keys[i]])
                goalweek.push(data.goalMeal)
                
                titleweek.push(week[(d.getDay())+1+i])
                
            }

            for (var i = 0; i<exer_keys.length;i++){
                exerweek.push(data.exerweak.m_cal[exer_keys[i]])
                exergoalweek.push(data.goalEx)                
            }
            
            
            
            var mealpercentage = (data.mealpercent)
            var exerpercentage = (data.exerpercent)
            var totalpercentage = Math.round((mealpercentage + exerpercentage)/2)

            

            var statstr = '<h2>' + data.username +'님 '
            if (totalpercentage == 100){
                statstr += '<img width="50" src="/static/img/face_icon/love.png"> <h4>총'+totalpercentage+'%의 달성률이십니다 ! AMAZING !!</h4> '
            }
            else if(totalpercentage >= 80){
                statstr += '<img width="50" src="/static/img/face_icon/smile.png"><h4>총'+ totalpercentage+'%의 달성률이십니다 ! 지금처럼 꾸준히 진행해주세요</h4>'
            }
            else if(totalpercentage >= 60){
                statstr += '<img width="50" src="/static/img/face_icon/neutral.png"><h4>총'+ totalpercentage+'%의 달성률이십니다. 조금만 분발해주세요 </h4>'
            }
            else if(totalpercentage >= 40){
                statstr += '<img width="50" src="/static/img/face_icon/disbelief.png"><h4>총'+totalpercentage+'%의 달성률이십니다. 힘내주세요! </h4>'
            }
            else if(totalpercentage >= 20){
                statstr += '<img width="50" src="/static/img/face_icon/sad.png"><h4>총'+ totalpercentage+'%의 달성률이십니다. 다시 시작하실 수 있습니다 ! 힘내세요! </h4>'
            }
            else {
                statstr += '<img width="50" src="/static/img/face_icon/crying.png"><h4>총'+ totalpercentage+'%의 달성률이십니다. 새로운 마음으로 다시 시작해보세요 :) 목표하시는 몸무게를 달성하실 수 있을거에요  </h4>'
            }
            statstr += '</h2>'

            $('#usertotalstatus').html(statstr)

            var mealtxt = '현재까지 식단목표 '+mealpercentage+'% 달성중 !!'
            mealtxt+='<br>평균적으로 아침, 점심, 저녁, 간식을 2:2:6:0의 비율로 섭취하고 계십니다'
            mealtxt+='<br>총 20일 중 간식을 5일 섭취하셨습니다. 건강한 다이어트를 위해 간식의 섭취를 줄여주세요'
            mealtxt+='<br>평균적으로 탄단지를 4:4:2의 비율로 섭취하고 계십니다 건강한 비율은 5:3:2 입니다'
            mealtxt+='<br>하루평균 탄단지섭취량은 10g, 20g, 5g 입니다.'
            mealtxt+='<br>하루 단백질은 '+ data.weight[0]*1 +'g을 섭취하셔야 합니다. '

            var exertxt = '현재까지 운동목표 '+exerpercentage+'% 달성중 !!'
            $('#mealtxt').html(mealtxt)
            $('#exertxt').html(exertxt)





        // --------------------------------------------------------------------------------------------------
        // --------------------------------------------------------------------------------------------------
        // --------------------------------------식단part----------------------------------------------------
        // --------------------------------------------------------------------------------------------------
        // --------------------------------------------------------------------------------------------------
         

        
        
        const textinsert = {
            id: 'textinsert',
            beforeDraw(chart, args, options) {
              const { ctx, chartArea: { top, right , bottom, left, width, height } } = chart;
              ctx.save();
              ctx.fillStyle = 'black';
              ctx.fillRect(width / 2, top + (height / 2), 0, 0);
              ctx.font = '20px sans-serif';
              ctx.textAlign = 'center';     
              
              ctx.fillText(mealpercentage +"%", width / 2 +(left), top + (height / 2));
            }
        };
            // doughnut chart 
            const ctx_meal = document.getElementById('mealChart').getContext('2d');
            const mealChart = new Chart(ctx_meal, {
                type: 'doughnut', 
                data: {
                    labels: ['done','remain'],
                    datasets: [{
                        label: '칼로리',
                        data: [mealpercentage,(100-mealpercentage),0,0,0],
                        backgroundColor: ['#7CCAAE','#eee'],
                        cutout: "60%",    
                    }],
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
                    }, 
                },
                plugins: [textinsert],
                
            }); // doughnut chart 
            
            




            const ctx_b_m = document.getElementById('weeklyBarChart_meal').getContext('2d');
            const labelsW = titleweek
            const mealWeekChart = new Chart(ctx_b_m, {
                type: 'bar', 
                data: {
                    labels: labelsW,
                    datasets: [
                    {
                        label: '달성현황',
                        data: eatweek,
                        backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(255, 159, 64, 0.2)',
                        'rgba(255, 205, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(153, 102, 255, 0.2)',
                        'rgba(201, 203, 207, 0.2)'
                        ],
                        borderColor: [
                        'rgb(255, 99, 132)',
                        'rgb(255, 159, 64)',
                        'rgb(255, 205, 86)',
                        'rgb(75, 192, 192)',
                        'rgb(54, 162, 235)',
                        'rgb(153, 102, 255)',
                        'rgb(201, 203, 207)'
                        ],
                        borderWidth: 5,
                        borderSkipped: false,
                        borderRadius: {
                            topLeft: 100,
                            topRight: 100,
                            bottomRight: 25,
                            bottomLeft: 25,
                        },
                        

                    },
                    {
                        label: '목표',
                        data: goalweek,
                        backgroundColor: ['#eee','#eee','#eee','#eee','#eee','#eee','#eee'],
                        borderWidth: 5,
                        borderSkipped: false,
                        borderRadius: {
                            topLeft: 100,
                            topRight: 100,
                            bottomRight: 25,
                            bottomLeft: 25,
                        },


                    }


                    
                    
                    ],
                },//data.
               
                options: {
                    responsive: true,
                    scales: {
                        x: {
                            
                            stacked: true
                         },
                        
                         y: {
                            display: false,
                            
                         },

                        xAxes: [{
                            gridLines: {
                                color: "rgba(0, 0, 0, 0)",
                            },
                            display:false
                        }],
                        yAxes:[{
                            ticks:{
                                min:0,
                                max:100,
                                stepSize:10,
                                display: false
                            },
                            scaleLabel:{
                                display: false
                            },
                            gridLines: {
                                color: "rgba(0, 0, 0, 0)",
                            },
                            display:false
                        }]

                    },
                    plugins: {
                        legend: {
                           
                            display: false,
                        },
                        title: {
                            display: true,
                            text: '지난 일주일간 섭취 칼로리'
                        }
                    }    



                    
                },
                
            }); // doughnut chart 


        // --------------------------------------------------------------------------------------------------
        // --------------------------------------------------------------------------------------------------
        // --------------------------------------운동part----------------------------------------------------
        // --------------------------------------------------------------------------------------------------
        // --------------------------------------------------------------------------------------------------

        const textinsert_exer = {
            id: 'textinsert_exer',
            beforeDraw(chart, args, options) {
              const { ctx, chartArea: { top, right , bottom, left, width, height } } = chart;
              ctx.save();
              ctx.fillStyle = 'black';
              ctx.fillRect(width / 2, top + (height / 2), 0, 0);
              ctx.font = '20px sans-serif';
              ctx.textAlign = 'center';     
              
              ctx.fillText(exerpercentage+'%', width / 2 +(left), top + (height / 2));
            }
        };

        // doughnut chart 
        const ctx_exer = document.getElementById('exerChart').getContext('2d');
        const exerChart = new Chart(ctx_exer, {
            type: 'doughnut', 
            data: {
                labels: ['done','remain'],
                datasets: [{
                    label: '칼로리',
                    data: [exerpercentage,(100-exerpercentage),0,0,0],
                    backgroundColor: ['#7CCAAE','#eee'],
                    cutout: "60%",    
                }],
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
                rotation: 1.5 * Math.PI
            }
            },
            plugins: [textinsert_exer],
        }); // doughnut chart 
        




        const ctx1 = document.getElementById('weeklyBarChart_exer').getContext('2d');
        
        const myChart1 = new Chart(ctx1, {
            type: 'bar', 
            data: {
                labels: labelsW,
                datasets: [
                {
                    label: '달성현황',
                    data: exerweek,
                    backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(255, 159, 64, 0.2)',
                    'rgba(255, 205, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(201, 203, 207, 0.2)'
                    ],
                    borderColor: [
                    'rgb(255, 99, 132)',
                    'rgb(255, 159, 64)',
                    'rgb(255, 205, 86)',
                    'rgb(75, 192, 192)',
                    'rgb(54, 162, 235)',
                    'rgb(153, 102, 255)',
                    'rgb(201, 203, 207)'
                    ],
                    borderWidth: 5,
                    borderSkipped: false,
                    borderRadius: {
                        topLeft: 100,
                        topRight: 100,
                        bottomRight: 25,
                        bottomLeft: 25,
                    },
                    

                },
                {
                    label: '목표',
                    data: exergoalweek,
                    backgroundColor: ['#eee','#eee','#eee','#eee','#eee','#eee','#eee'],
                    borderWidth: 5,
                    borderSkipped: false,
                    borderRadius: {
                        topLeft: 100,
                        topRight: 100,
                        bottomRight: 25,
                        bottomLeft: 25,
                    },


                }


                
                
                ],
            },//data.
           
            options: {
                responsive: true,
                scales: {
                    x: {
                        
                        stacked: true
                     },
                    
                     y: {
                        display: false,
                        
                     },

                    xAxes: [{
                        gridLines: {
                            color: "rgba(0, 0, 0, 0)",
                        },
                        display:false
                    }],
                    yAxes:[{
                        ticks:{
                            min:0,
                            max:100,
                            stepSize:10,
                            display: false
                        },
                        scaleLabel:{
                            display: false
                        },
                        gridLines: {
                            color: "rgba(0, 0, 0, 0)",
                        },
                        display:false
                    }]

                },
                plugins: {
                    legend: {
                       
                        display: false,
                    },
                    title: {
                        display: true,
                        text: '지난 일주일간 운동 칼로리'
                    }
                }    



                
            }
        }); // doughnut chart 



         


            
        },
                    
        error:function(){

        }
    })//ajax

})//function
