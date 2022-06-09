$(function(){
    $.ajax({
        url:"/static/test.json",
        dataType:"json",
        success:function(data){
            let note = ''
            note+='<tr><td><progress  id="carbB" value="'+ data[9].carb +'" max="100"></progress></td>'
            note+='<td><progress id="proteinB" value="'+ data[9].protien +'" max="100"></progress></td>'
            note+='<td><progress id="fatB" value="'+ data[9].fat +'" max="100"></progress></td></tr>'
            note+='<tr><td>탄수화물 : '+ data[9].carb+'g</td><td>단백질 : '+ data[9].protien+'g</td><td>지방 : '+data[9].fat+'g</td></tr>'
            

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
                  ctx.fillText('1200kcal', width / 2 +(left), top + (height / 2));
                  ctx.fillText('remains', width / 2 +(left), top + (height / 2)+50);
                }
            };


            const ctx = document.getElementById('myChart').getContext('2d');
            const myChart = new Chart(ctx, {
                type: 'doughnut', 
                data: {
                    
                    datasets: [{
                        label: '칼로리',
                        data: [80,(100-80),0,0,0],
                        backgroundColor: ['#7CCAAE','#eee'],
                        hoverOffset: 0,
                        cutout: "80%",
                    },
                    {
                        label: '탄단지',
                        data: [0,0,data[9].carb, data[9].protien, data[9].fat],
                        backgroundColor: ['white','white','#ECEC84','#FFB69B','#A299CA'],
                        label: 'Doughnut 2',
                        cutout: "80%",
                    },
                    
                    
                ],
                    labels: ['intake','remain','Carbonate','Protein', 'Fat']
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



