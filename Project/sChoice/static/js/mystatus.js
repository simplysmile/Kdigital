

$(function(){
    $.ajax({
        url:"/static/test.json",
        dataType:"json",
        success:function(data){

            



            // 달성일, 몸무게 차트 
            const centerText={
                id:'centerTest',
                beforeDraw(chart,args,options){
                    const {ctx, chartArea:{left,right,top,bottom,width,height}} = chart;
                    ctx.save()
                    ctx.font='bolder 30px Arial';
                    ctx.fillStyle='#8C5A76'
                    ctx.fillText('TEXTESTES')
                    
                }
            }
            const ctx_goal = document.getElementById('goalchart').getContext('2d');
            const goalchart = new Chart(ctx_goal, {
                type: 'doughnut', 
                data: {
                    labels: ['done','remain'],
                    datasets: 
                    [
                        {
                            label: '날짜',
                            data: [10,(60-10),0,0],
                            backgroundColor: ['#8C5A76','#eee'],
                            cutout: "95%",
                            //hoverOffset: 5,    
                            rotation: -120,
                            circumference: 240,
                            
                        },
                        {
                            label: '몸무게',
                            data: [0,0,50,(60-50)],
                            backgroundColor: ['#6D80A6','#eee'],
                            cutout: "90%",
                            //hoverOffset: 5,    
                            rotation: -120,
                            circumference: 240,
                        },
                        
                    ],
                },//data.
                options: {
                    elements: {
                        center: {
                          text: 'Red is 2/3 the total numbers',
                          color: '#FF6384', // Default is #000000
                          fontStyle: 'Arial', // Default is Arial
                          sidePadding: 20, // Default is 20 (as a percentage)
                          minFontSize: 20, // Default is 20 (in px), set to false and text will not wrap.
                          lineHeight: 25 // Default is 25 (in px), used for when text wraps
                        }
                    },
                    plugins: {
                        
                    legend: {
                        display: false
                    },
                    tooltip: {
                        enabled: false
                    },
                }
                            
                   },
                   //plugins: [centerText]

            }); // 달성일, 몸무게 차트 
            

            // 몸무게 라인 그래프 

            const ctxW = document.getElementById('weightchange').getContext('2d');
            const labels_weight = ['월','화','수','목','금','토','일']
            const weightchange = new Chart(ctxW, {
                type: 'line', 
                data: {
                    labels: labels_weight,
                    datasets: [
                    {
                        label: '몸무게 변화추이',
                        data: [59, 58, 57.8, 58, 57.5, 57.5, 57.3],
                        borderColor: ['rgb(255, 99, 132)'],
                        backgroundColor:['rgba(255, 99, 132, 0.2)']
                    },
                    {
                        label: '목표몸무게',
                        data: [55,55,55,55,55,55,55],
                        borderColor: ['rgba(54, 162, 235)'],
                        backgroundColor:['rgba(54, 162, 235, 0.2)']
                    }
                
                ],
                },//data.
               
                options: {
                    responsive: true,
                    scales: {
                        y: {
                            max: 60,
                            min: 50,
                            ticks: {
                                stepSize: 1
                            }
                        }
                    }
                                       
                }
            }); // 몸무게 라인차트





        // --------------------------------------------------------------------------------------------------
        // --------------------------------------------------------------------------------------------------
        // --------------------------------------식단part----------------------------------------------------
        // --------------------------------------------------------------------------------------------------
        // --------------------------------------------------------------------------------------------------
         







       


            // doughnut chart 
            const ctx_meal = document.getElementById('mealChart').getContext('2d');
            const mealChart = new Chart(ctx_meal, {
                type: 'doughnut', 
                data: {
                    labels: ['done','remain'],
                    datasets: [{
                        label: '칼로리',
                        data: [80,(100-80),0,0,0],
                        backgroundColor: ['#7CCAAE','#eee'],
                        cutout: "80%",    
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
                        rotation: 1.5 * Math.PI,
                        
                        
                        
                        
                        
                       
                        
                    },
                    
                },
                
            }); // doughnut chart 
            




            const ctx_b_m = document.getElementById('weeklyBarChart_meal').getContext('2d');
            const labelsW = ['월','화','수','목','금','토','일']
            const mealWeekChart = new Chart(ctx_b_m, {
                type: 'bar', 
                data: {
                    labels: labelsW,
                    datasets: [
                    {
                        label: '달성현황',
                        data: [65, 59, 120, 81, 56, 100, 80],
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
                        data: [100, 100, 100, 100, 100, 100, 100],
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
                    }    



                    
                }
            }); // doughnut chart 


        // --------------------------------------------------------------------------------------------------
        // --------------------------------------------------------------------------------------------------
        // --------------------------------------운동part----------------------------------------------------
        // --------------------------------------------------------------------------------------------------
        // --------------------------------------------------------------------------------------------------

        // doughnut chart 
        const ctx_exer = document.getElementById('exerChart').getContext('2d');
        const exerChart = new Chart(ctx_exer, {
            type: 'doughnut', 
            data: {
                labels: ['done','remain'],
                datasets: [{
                    label: '칼로리',
                    data: [80,(100-80),0,0,0],
                    backgroundColor: ['#7CCAAE','#eee'],
                    cutout: "80%",    
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
            }
        }); // doughnut chart 
        




        const ctx1 = document.getElementById('weeklyBarChart_exer').getContext('2d');
        
        const myChart1 = new Chart(ctx1, {
            type: 'bar', 
            data: {
                labels: labelsW,
                datasets: [
                {
                    label: '달성현황',
                    data: [65, 59, 120, 81, 56, 100, 80],
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
                    data: [100, 100, 100, 100, 100, 100, 100],
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
                }    



                
            }
        }); // doughnut chart 



         


            
        },
                    
        error:function(){

        }
    })//ajax

})//function
