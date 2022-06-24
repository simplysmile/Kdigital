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
            var alist=[]
            var bColor=['#ECEC84','#FFB69B','#A299CA']
            
            ex_count=data.length
            
            for(let j=0;j<data.length;j++){
                total_kcal+=data[j].burned_kcal
                total_time+=data[j].ex_time
            }
            avg_time= total_time/ex_count

            let remain_kcal=Math.round(100-(total_kcal/data[0].total_burn_kcal)*100)
            var cont1=''
            var cont2=''
            var remain_per=0
            if(remain_kcal<0){
                cont1='달성성공!'
                cont2='goal : '+String(data[0].total_burn_kcal)+'kcal'
                remain_per=0
            }else{
                cont1='burned : '+String(total_kcal)+'kcal'
                cont2='goal : '+String(data[0].total_burn_kcal)+'kcal'
                remain_per=remain_kcal
  
            }
            console.log(remain_kcal)
            
            var strlist={label: '총 운동 칼로리', data: [100-remain_per,remain_per], backgroundColor: ['#7CCAAE','#eee'], hoverOffset: 0,  cutout: "70%" }
            alist.push(strlist)
            if(data.length>3){
                for(let i=0;i<3;i++){
                    note+='<td><progress  id="exB'+(i+1)+'" value="'+ data[i].kcal_per +'" max="100"></progress></td>'
                    var strlist1 = {
                        label: '칼로리',
                        data: [data[i].kcal_per,(100-data[i].kcal_per)],
                        backgroundColor: [bColor[i],'#eee'],
                        hoverOffset: 0,
                        cutout: "60%",
                    }
                    alist.push(strlist1)
                }
                note+='</tr>'
                note+='<tr>'
                for(let i=1;i<4;i++){
                    note+='<td>'+data[i-1].ex_name+' : '+ data[i-1].burned_kcal+'kcal / '+data[i-1].goal_kcal+'kcal<br>('+Math.round(data[i-1].kcal_per)+'% 달성)</td>'
                }
            }
            else{
                for(let i=0;i<data.length;i++){
                    note+='<td><progress  id="exB'+(i+1)+'" value="'+ data[i].kcal_per +'" max="100"></progress></td>'
                    
                    var strlist1 = {
                        label: '칼로리',
                        data: [data[i].kcal_per,(100-data[i].kcal_per)],
                        backgroundColor: [bColor[i],'#eee'],
                        hoverOffset: 0,
                        cutout: "60%",
                    }
                    alist.push(strlist1)
                }
                note+='</tr>'
                note+='<tr>'
                for(let i=1;i<(data.length)+1;i++){
                    note+='<td>'+data[i-1].ex_name+' : '+ data[i-1].burned_kcal+'kcal / '+data[i-1].goal_kcal+'kcal<br>('+Math.round(data[i-1].kcal_per)+'% 달성)</td>'
                }
            }

            note+='</tr>'
            note+='<tr style="height:50px"><td></td><td></td><td></td></tr>'
            note+='<tr><td style="color:#ff0000">'+total_time+'분</td><td style="color:#419e46">'+ex_count+'번</td><td style="color:#43419e">'+avg_time+'분</td></tr>'
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
                  ctx.fillText(cont2, width / 2 +(left), top + (height / 2));
                  ctx.fillText(cont1, width / 2 +(left), top + (height / 2)+50);
                }
            };

            const ctx = document.getElementById('myChart').getContext('2d');
            const myChart = new Chart(ctx, {
                type: 'doughnut', 
                data: {
                    datasets: alist,
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
