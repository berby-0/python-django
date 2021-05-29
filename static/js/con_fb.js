
function fb1(list){
    var myChart = echarts.init(document.getElementById('fb1'));
    var data = list
    option = {
        title: [{
            text: '公司规模',
            top: '5%',
            left: '5%',
            textStyle: {
                //color: '#balck',
                fontSize: '16'
            }

        }],
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            }
        },
        legend: {
            data: [data['job01']['job_name'],data['job02']['job_name']]
        },
        toolbox: {
            show: true,
            orient: 'vertical',
            left: 'right',
            top: 'center',
            feature: {
                mark: {show: true},
                dataView: {show: true, readOnly: false},
                magicType: {show: true, type: ['line', 'bar', 'stack', 'tiled']},
                restore: {show: true},
                saveAsImage: {show: true}
            }
        },
        xAxis: [
            {
                type: 'category',
                axisTick: {show: false},
                data: data['job02']['companysize_text']['x_name'],
            }
        ],
        yAxis: [
            {
                type: 'value'
            }
        ],
        series: [
            {
                name:data['job01']['job_name'],
                type: 'bar',
                barGap: 0,
                emphasis: {
                    focus: 'series'
                },
                data: data['job01']['companysize_text']['data']
            },
            {
                name:data['job02']['job_name'],
                type: 'bar',
                emphasis: {
                    focus: 'series'
                },
                data: data['job02']['companysize_text']['data']
            },
        ]
    };

    myChart.setOption(option);
    window.addEventListener("resize", function () {
        myChart.resize();
    });
}

function fb2(list) {
    var myChart = echarts.init(document.getElementById('fb2'));
    var data = list
    option = {
        title: [{
            text: '学历要求',
            top: '5%',
            left: '5%',
            textStyle: {
                //color: '#balck',
                fontSize: '16'
            }

        }],
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            }
        },
        legend: {
            data: [data['job01']['job_name'],data['job02']['job_name']]
        },
        toolbox: {
            show: true,
            orient: 'vertical',
            left: 'right',
            top: 'center',
            feature: {
                mark: {show: true},
                dataView: {show: true, readOnly: false},
                magicType: {show: true, type: ['line', 'bar', 'stack', 'tiled']},
                restore: {show: true},
                saveAsImage: {show: true}
            }
        },
        xAxis: [
            {
                type: 'category',
                axisTick: {show: false},
                data: data['job02']['degreefrom']['x_name'],
            }
        ],
        yAxis: [
            {
                type: 'value'
            }
        ],
        series: [
            {
                name:data['job01']['job_name'],
                type: 'bar',
                barGap: 0,
                emphasis: {
                    focus: 'series'
                },
                data: data['job01']['degreefrom']['data']
            },
            {
                name:data['job02']['job_name'],
                type: 'bar',
                emphasis: {
                    focus: 'series'
                },
                data: data['job02']['degreefrom']['data']
            },
        ]
    };
    myChart.setOption(option);
    window.addEventListener("resize", function () {
        myChart.resize();
    });
}

function fb3(list) {
    var myChart = echarts.init(document.getElementById('fb3'));
    var data = list

    option = {
        title: [{
            text: '公司类型',
            top: '5%',
            left: '5%',
            textStyle: {
                //color: '#balck',
                fontSize: '16'
            }

        }],
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            }
        },
        legend: {
            data: [data['job01']['job_name'],data['job02']['job_name']]
        },
        toolbox: {
            show: true,
            orient: 'vertical',
            left: 'right',
            top: 'center',
            feature: {
                mark: {show: true},
                dataView: {show: true, readOnly: false},
                magicType: {show: true, type: ['line', 'bar', 'stack', 'tiled']},
                restore: {show: true},
                saveAsImage: {show: true}
            }
        },
        xAxis: [
            {
                type: 'category',
                axisTick: {show: false},
                data: data['job02']['companytype_text']['x_name'],
            }
        ],
        yAxis: [
            {
                type: 'value'
            }
        ],
        series: [
            {
                name:data['job01']['job_name'],
                type: 'bar',
                barGap: 0,
                emphasis: {
                    focus: 'series'
                },
                data: data['job01']['companytype_text']['data']
            },
            {
                name:data['job02']['job_name'],
                type: 'bar',
                emphasis: {
                    focus: 'series'
                },
                data: data['job02']['companytype_text']['data']
            },
        ]
    };
    myChart.setOption(option);
    window.addEventListener("resize", function () {
        myChart.resize();
    });
}

function fb4(list) {
    var myChart = echarts.init(document.getElementById('fb4'));
    var data = list

    option = {
        title: [{
            text: '工作年限',
            top: '5%',
            left: '5%',
            textStyle: {
                //color: '#balck',
                fontSize: '16'
            }

        }],
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            }
        },
        legend: {
            data: [data['job01']['job_name'],data['job02']['job_name']]
        },
        toolbox: {
            show: true,
            orient: 'vertical',
            left: 'right',
            top: 'center',
            feature: {
                mark: {show: true},
                dataView: {show: true, readOnly: false},
                magicType: {show: true, type: ['line', 'bar', 'stack', 'tiled']},
                restore: {show: true},
                saveAsImage: {show: true}
            }
        },
        xAxis: [
            {
                type: 'category',
                axisTick: {show: false},
                data: data['job02']['workyear']['x_name'],
            }
        ],
        yAxis: [
            {
                type: 'value'
            }
        ],
        series: [
            {
                name:data['job01']['job_name'],
                type: 'bar',
                barGap: 0,
                emphasis: {
                    focus: 'series'
                },
                data: data['job01']['workyear']['data']
            },
            {
                name:data['job02']['job_name'],
                type: 'bar',
                emphasis: {
                    focus: 'series'
                },
                data: data['job02']['workyear']['data']
            },
        ]
    };

    myChart.setOption(option);
    window.addEventListener("resize", function () {
        myChart.resize();
    });
}

function fb5(list) {
    var myChart = echarts.init(document.getElementById('fb5'));
    var data = list


    option = {
        // backgroundColor: "#0f375f",
        tooltip: {
            trigger: "axis",
            axisPointer: {
                type: 'cross',
                label: {
                    backgroundColor: '#6a7985'
                }
            }
        },
        grid: {
            left: '8%',
            right: '5%',
            bottom: '0',
            top:'16%',
            containLabel: true
        },
        //图片保存
        toolbox: {
            feature: {
                saveAsImage: {}
            }
        },
        legend: {

            top: "2%",
            left: 'center',
            textStyle: {
                color: "#000",
                fontSize: "12"
            },

        },

        xAxis: {
            color: "#000",
            name: "行业",
            type: 'category',
            data: data['job01']['companyind_text']['x_name'],
            nameTextStyle: {
                color: "#000",
                fontSize: 14
            },
            axisLine: {
                show: true, //隐藏X轴轴线
                lineStyle: {
                    color: '#fff',
                    width: 2
                }
            },
            axisTick: {
                show: true //隐藏X轴刻度
            },
            axisLabel: {
                show: true,
                textStyle: {
                    color: "#000", //X轴文字颜色
                    fontSize: 16
                }
            },

        },
        yAxis: [{
                color: "#000",
                type: "value",
                name: "岗位数量",

                nameTextStyle: {
                    color: "#000",
                    fontSize: 16
                },
                splitLine: {
                    show: false
                },
                axisTick: {
                    show: true
                },
                axisLine: {
                    show: true,
                    lineStyle: {
                        color: '#fff',
                        width: 2
                    }
                },
                axisLabel: {
                    show: true,
                    textStyle: {
                        color: "#000",
                        fontSize: 16
                    }
                },

            },
            {
            show:false

            }
        ],
        series: [{
                name: data['job01']['job_name']+"行业分布",
                type: "line",
                yAxisIndex: 1, //使用的 y 轴的 index，在单个图表实例中存在多个 y轴的时候有用
                smooth: true, //平滑曲线显示
                showAllSymbol: true, //显示所有图形。
                symbol: "circle", //标记的图形为实心圆
                symbolSize: 8, //标记的大小
                itemStyle: {
                    //折线拐点标志的样式
                    color: "#eb2bd1",
                    borderColor: "#3D7EEB",
                    width: 2,
                    shadowColor: "#3D7EEB",
                    shadowBlur: 4
                },
                lineStyle: {
                    color: "#c1ff38",
                    width: 2,
                    shadowColor: "#3D7EEB",
                    shadowBlur: 4
                },
                areaStyle: {
                    color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                            offset: 0,
                            color: "rgba(61,126,235, 0.5)"
                        },
                        {
                            offset: 1,
                            color: "rgba(61,126,235, 0)"
                        }
                    ])
                },
                // data: [200, 300, 300, 900, 1500, 1200, 600]
                data: data['job01']['companyind_text']['data'],

        },{
                name: data['job02']['job_name']+"行业分布",
                type: "line",
                yAxisIndex: 1, //使用的 y 轴的 index，在单个图表实例中存在多个 y轴的时候有用
                smooth: true, //平滑曲线显示
                showAllSymbol: true, //显示所有图形。
                symbol: "circle", //标记的图形为实心圆
                symbolSize: 8, //标记的大小
                itemStyle: {
                    //折线拐点标志的样式
                    color: "#47cab7",
                    borderColor: "#3D7EEB",
                    width: 2,
                    shadowColor: "#3D7EEB",
                    shadowBlur: 4
                },
                lineStyle: {
                    color: "#000",
                    width: 2,
                    shadowColor: "#3D7EEB",
                    shadowBlur: 4
                },
                areaStyle: {
                    color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                            offset: 0,
                            color: "rgba(61,126,235, 0.5)"
                        },
                        {
                            offset: 1,
                            color: "rgba(61,126,235, 0)"
                        }
                    ])
                },
                // data: [200, 300, 300, 900, 1500, 1200, 600]
                data: data['job02']['companyind_text']['data'],

        }


        ]
    };

    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
    window.addEventListener("resize", function () {
        myChart.resize();
    });

}

function fb6(list) {
    var myChart = echarts.init(document.getElementById('fb6'));
    var data = list
    option = {
        // backgroundColor:"#0f375f",
        grid: {
            left: '8%',
            right: '5%',
            top: '5%',
            containLabel: false
        },
        legend: {
            top: "2%",
            right: 'center',
            textStyle: {
                color: '#2640f5',
                fontSize: "12"
            },
        },
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'cross',
            }
        },
        //图片保存
        toolbox: {
            feature: {
                saveAsImage: {}
            }
        },
        xAxis: {
            type: 'category',
            // boundaryGap: false,
            data: data['job01']['providesalary_text']['x_name'],
            triggerEvent: true,
            splitLine: {
                show: false
            },
            axisLine: {
                show: true,
                lineStyle: {
                    width: 2,
                    color: '#fff',
                }
            },
            axisTick: {
                show: false
            },
            axisLabel: {
                //     textStyle: {
                //     color: "rgba(250,250,250,0.6)", //X轴文字颜色
                //     fontSize: 16
                // },
                color: '#000',
                fontSize: 16,
                fontWeight: 'bold',
                textShadowOffsetY: 2
            }
        },
        yAxis: {
            nameTextStyle: {
                color: '#fff',
                fontSize: 16,
                textShadowColor: '#000',
                textShadowOffsetY: 2
            },
            type: 'value',
            splitLine: {
                show: true,
                lineStyle: {
                    color: 'rgba(255,255,255,.2)'
                }
            },
            axisLine: {
                show: true,
                lineStyle: {
                    width: 2,
                    color: 'rgba(255,255,255,.6)'
                }
            },
            axisTick: {
                show: true
            },
            axisLabel: {
                textStyle: {
                    color: "#000", //X轴文字颜色
                    fontSize: 16
                },
                color: '#000',
                fontSize: 16,
                textShadowColor: '#fff',
                textShadowOffsetY: 2
            }
        },
        dataZoom: [{
            type: 'inside',
            start: 0,
            end: 10
        }, {
            start: 0,
            end: 10,
            handleIcon: 'M10.7,11.9v-1.3H9.3v1.3c-4.9,0.3-8.8,4.4-8.8,9.4c0,5,3.9,9.1,8.8,9.4v1.3h1.3v-1.3c4.9-0.3,8.8-4.4,8.8-9.4C19.5,16.3,15.6,12.2,10.7,11.9z M13.3,24.4H6.7V23h6.6V24.4z M13.3,19.6H6.7v-1.4h6.6V19.6z',
            handleSize: '80%',
            height: 16,
            handleStyle: {
                color: '#fff',
                shadowBlur: 3,
                shadowColor: 'rgba(0, 0, 0, 0.6)',
                shadowOffsetX: 2,
                shadowOffsetY: 2
            }
        }],
        series: [
            {
                name: data['job01']['job_name'],
                type: 'line',
                data: data['job01']['providesalary_text']['avg'],
                symbol: 'none',
                symbolSize: 12,
                color: '#888888',
                label: {
                    show: false,
                    position: 'top',
                    textStyle: {
                        fontSize: 18,
                        fontWeight: 'bold'
                    }
                },
            },
            {
                name: data['job02']['job_name'],
                type: 'line',
                data: data['job02']['providesalary_text']['avg'],
                symbol: 'none',
                symbolSize: 12,
                color: '#3D7EEB',
                label: {
                    show: false,
                    position: 'top',
                    textStyle: {
                        fontSize: 18,
                        fontWeight: 'bold'
                    }
                },
            },
             {
                name: data['job01']['job_name']+'_avg',
                type: 'line',
                markLine: {
                    data: [{
                        yAxis: data['job01']['providesalary_text']['salary']['avg']
                    }]
                }
            },
            {
                name: data['job02']['job_name']+'_avg',
                type: 'line',
                markLine: {
                    data: [{
                        yAxis: data['job02']['providesalary_text']['salary']['avg']
                    }]
                }
            }
        ]
    };


    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
    window.addEventListener("resize", function () {
        myChart.resize();
    });
}

