$(function () {
    // 请求数据
    $.ajax({
        type: 'get',
        url: '/get_echart_data',
        dataType: 'json',
        success: function (returnData) {
            // console.log(returnData['data']);
            // 调用echarts
            echarts_31(returnData);
        }
    });


    function echarts_31(data) {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('fb1'));

        option = {
            title: [{
                        text: '融资情况',
                        left: 'center',
                        textStyle: {
                            color: '#fff',
                            fontSize: '16'
                        }

                    }],
             tooltip: {
                        trigger: 'item',
                        formatter: "{a} <br/>{b}: {c} ({d}%)",
                        position: function (p) {   //其中p为当前鼠标的位置
                            return [p[0] + 10, p[1] - 10];
                        }
                    },
            //图片保存
            toolbox: {
                feature: {
                    saveAsImage: {}
                }
            },
            legend: {
                        top: '62%',
                        itemWidth: 10,
                        itemHeight: 10,
                        // data:['2D线','3D线','资源类','采集类','宝宝大全','2D视频','3D视频'],
                        data: data['companysize_text']['x_name'],
                        textStyle: {
                            color: 'rgba(255,255,255,0.75)',
                            fontSize: '10'
                        }
                    },
            series: [
                {
                    name:'融资情况',
                    type:'pie',
                    center: ['50%', '38%'],
                    radius: ['40%', '60%'],
                    color:['#2640f5', '#fe566c', '#65db99', '#d30afd', '#78f4f5', '#fcba61', '#f5d978', '#c8f578'],
                    data: data['companysize_text']['data'],
                    itemStyle:{
                        normal:{
                            label:{
                                show:false,
                                position:'inner',
                                textstyle:{
                                    fontWeight:50,
                                    fontSize:1
                                }
                            },
                            labelLine:{
                                show:false,
                            }

                        }
                    },

                }
            ]
        };
        myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }

})
;