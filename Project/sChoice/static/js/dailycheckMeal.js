$(function(){
    $.ajax({
        url:"/static/mealjson.json",
        dataType:"json",
        success:function(data){

            var carbgram = Math.round(data.goalCal * 0.5 * 0.25)
            var protgram =  Math.round(data.goalCal * 0.3 * 0.25)
            var fatgram =  Math.round(data.goalCal * 0.2 * 0.11)
            let note = ''
            note+='<tr><td><progress  id="carbB" value="'+ data.carb +'" max="'+carbgram+'"></progress></td>'
            note+='<td><progress id="proteinB" value="'+ data.prot +'" max="'+protgram+'"></progress></td>'
            note+='<td><progress id="fatB" value="'+ data.fat +'" max="'+fatgram+'"></progress></td></tr>'
            note+='<tr><td>탄수화물 : '+ data.carb +'g/'+carbgram+'g</td><td>단백질 : '+ data.prot+'g/'+protgram+'g</td><td>지방 : '+data.fat+'g/'+fatgram+'g</td></tr>'
            

            $("#progressbars").html(note)

            // console.log(data)
            var remaincal = data.goalCal - data.totalCal
            var gcal = 0
            var tcal = 0
            if (remaincal<0) {
                gcal = 0
                tcal = 100
            }
            else{
                gcal = remaincal
                tcal = data.totalCal

            }

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
                  ctx.fillText('Intake: '+data.totalCal+' kcal', width / 2 +(left), top + (height / 2));
                  ctx.fillText('Remain: '+remaincal+' kcal', width / 2 +(left), top + (height / 2)+50);
                  //ctx.fillText('남았습니다', width / 2 +(left), top + (height / 2)+100);
                }
            };


            const ctx = document.getElementById('myChart').getContext('2d');
            const myChart = new Chart(ctx, {
                type: 'doughnut', 
                data: {
                    
                    datasets: [{
                        label: '칼로리',
                        data: [tcal,gcal,0,0,0],
                        backgroundColor: ['#7CCAAE','#eee'],
                        hoverOffset: 0,
                        cutout: "80%",
                    },
                    {
                        label: '탄단지',
                        data: [0,0,data.carb, data.prot, data.fat],
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



