

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
                  var kgstr = '목표까지 '+String(Math.round(data.weight[0]-data.goal_weight,2))+'kg!!'
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

            var mealtxt = ''
            mealtxt +='<div style="font-size:23px;">'+data.username +'님 지금까지 식단목표를 <span style="color:red; ">'+mealpercentage+'</span>% 달성중입니다.'
            if (mealpercentage > 80){
                mealtxt +='<br>지금처럼 계속 꾸준히 해주시면 원하시는 목표를 금방 이루실거에요 :) </div>'
            }
            else if (mealpercentage > 50){
                mealtxt +='<br>원하시는 목표위해서 조금만 더 분발해주세요 :) 화이팅 ! </div>'
            }
            else{
                mealtxt +='<br>혹시 너무 무리한 목표설정이 아니신가요? 회원정보 수정에서 목표일을 변경하실 수 있습니다-. :) </div>'

            }
            mealtxt+='<li>평균적으로 아침, 점심, 저녁, 간식을 <span style="color:red; ">'+ data.minfo.blds_ratio +'</span>의 비율로 섭취하고 있으며,</li>'
            mealtxt+='<li>하루평균 <span style="color:red; ">'+ data.minfo.avgDCal +'</span>칼로리를 섭취하고 있어요</li>'
            if (data.minfo.avgDCal<1000){
                mealtxt +='<ul  style="font-size:12px; text-align:left;"> 너무 적은 칼로리를 섭취하고 계시네요. 이렇게 계속 섭취하시면 건강을 잃을 수 있어요. <br>혹시 너무 무리한 목표설정이 아니신가요? 회원정보 수정에서 목표일을 변경하실 수 있습니다-. :) 천천히 건강하게 살을빼세요 </ul>'
            }
            mealtxt+='<li>또한 평균적으로 탄단지를 <span style="color:red; ">'+ data.minfo.cpf_ratio +'</span>의 비율로 섭취하고 있어요.</li>'
            mealtxt+='<li>건강한 다이어트를 위한 탄단지의 비율은 5:3:2, 혹은 4:4:2 비율이에요.</li>'
            mealtxt+='<li>하루평균 탄수화물 <span style="color:red; ">'+Math.round(data.minfo.avgCarb,2) +'</span>g, 단백질 <span style="color:red; ">' +Math.round(data.minfo.avgProt)+ '</span>g, 지방 <span style="color:red; ">'+ Math.round(data.minfo.avgFat)+'</span>g을 섭취하고 있어요.</li>'
            if (data.minfo.avgProt<data.weight[0]*1){
                mealtxt+='<li>건강한 다이어트를 위해서 단백질은 하루에 <span style="color:red; ">'+ data.weight[0]*1 +'</span>g 이상을 섭취하셔야 해요. 단백질 섭취량을 조금 늘려주세요'
            }
            if (data.minfo.avgCarb<100){
                mealtxt+='<li>건강한 다이어트를 위해서 탄수화물은 하루에 100g 이상을 섭취하셔야 해요. 안그러면 탈모와 같은 부작용이 올 수 있어요. 탄수화물 섭취를 좀 늘려주세요'
            }
            var exertxt = ''
            exertxt +='<div style="font-size:23px;">'+ data.username +'님 지금까지 운동목표를 <span style="color:red; ">'+exerpercentage+'</span>% 달성중입니다.'
            if (exerpercentage > 80){
                exertxt +='<br>지금처럼 계속 꾸준히 해주시면 원하시는 목표를 금방 이루실거에요 :) </div>'
            }
            else if (exerpercentage > 50){
                exertxt +='<br>원하시는 목표위해서 조금만 더 분발해주세요 :) 화이팅 ! </div>'
            }
            else{
                exertxt +='<br>혹시 너무 무리한 목표설정이 아니신가요? 회원정보 수정에서 목표일을 변경하실 수 있습니다.  :) </div>'

            }

            exertxt +='<li>현재까지 유산소 운동 <span style="color:red; ">'+ data.einfo.aerobic[1]+'</span>분, 근력운동 <span style="color:red; ">'+data.einfo.aerobic[3] +'</span>분 하셨어요. </li>'
            exertxt +='<li>그 결과 유산소 운동으로 <span style="color:red; ">'+ data.einfo.aerobic[4]+'</span>칼로리를 소모하시고 근력운동으로 <span style="color:red; ">'+data.einfo.aerobic[5] +'</span> 칼로리를 소모하셨어요. </li>'
            if (data.einfo.aerobic[0]>data.einfo.aerobic[2]){ // 유산소를 더 많이할 경우

                exertxt +='<ul style="font-size:12px; text-align:left;"> 무산소 운동은 근육의 크기와 힘을 키우고 순발력을 증가켜줘요. 또한 몸을 탄탄하게 하며 탄력적으로 보일 수 있게 해주며 근육량 증가에 의한 기초대사량의 유지,증가로 다이어트시의 정체기극복과 빠진 체중을 유지하는데도 도움을 주기때문에 근력 운동을 더 해주는게 어떨까요?</ul>'
            }
            else{ // 근력운동을 더 많이할 경우
                exertxt +='<ul style="font-size:12px; text-align:left;"> 유산소 운동은 장시간 지속할 수 있고 체지방을 감소시키고 폐와 심장의 기능이 개선되요. 또한 무산소운동에 비해 비교적 안전성이 높아 운동초보자, 고령자도 가볍게 시작할 수 있으며, 꾸준히 시행시 운동부족과 관련된 각종 성인병의 예방과 개선에 도움이 되는 유산소 운동을 추가적으로 해주는게 어떨까요?.</ul>'

            }
            
            exertxt +='<li>가장 많이하신 운동은 <span style="color:red; ">'+data.einfo.mostexer+'</span>이네요. 좋아하는 운동을 자주해보세요 :)</li>'
            exertxt +='<li>오늘 까지 <span style="color:red; ">'+data.workoutday+'</span>일 중에 <span style="color:red; ">'+ data.einfo.exerwk.reduce((a, b) => a + b, 0)+'</span>일을 운동하셨어요.</li>'
            exertxt +='<li>요일별 운동현황은 월: <span style="color:red; ">'+data.einfo.exerwk[0]+'</span>회, 화: <span style="color:red; ">'+data.einfo.exerwk[1]+'</span>회, 수: <span style="color:red; ">'+data.einfo.exerwk[2]+'</span>회, 목: <span style="color:red; ">'+data.einfo.exerwk[3]+'</span>회, 금: <span style="color:red; ">'+data.einfo.exerwk[4]+'</span>회, 토: <span style="color:red; ">'+data.einfo.exerwk[5]+'</span>회, 일: <span style="color:red; ">'+data.einfo.exerwk[6]+'</span>회 하셨네요 :)</li>'
            exertxt +='<li>간단한 걷기, 스트레칭이라도 매일 꾸준히 해주시는것이 좋아요 :) 앞으로도 힘내서 꾸준히 운동해주세요.</li>'

            








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
