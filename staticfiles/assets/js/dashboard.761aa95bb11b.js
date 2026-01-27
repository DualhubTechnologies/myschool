var chartEmployeeConfig = {
	series: [
		{
			name: 'Net Profit',
			data: [390, 115, 305, 250, 102, 40, 195, 235, 280]
		},
		{
			name: 'Revenue',
			data: [105, 205, 120, 380, 105, 205, 290, 310, 105]
		},
		{
			name: 'Free Cash Flow',
			data: [180, 200, 180, 250, 100, 400, 90	, 115, 195]
		}
	],
	colors: ['var(--bs-primary)', 'var(--bs-secondary)', 'var(--bs-info)'],
	chart: {
		type: 'bar',
		height: 320,
		
		toolbar: {
            show: false
        }
	},
	plotOptions: {
		bar: {
            horizontal: false,
            columnWidth: '55%',
            borderRadius: 3,
        },
	},
	dataLabels: {
		enabled: false
	},
	stroke: {
		show: true,
		width: 2,
		colors: ['transparent']
	},
	xaxis: {
		categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep'],
		axisBorder: {
			color: 'var(--bs-border-color)',
		},
		axisTicks: {
			show: false,
		},
		labels: {
			style: {
				colors: 'var(--bs-body-color)',
				fontSize: '13px',
				fontFamily: 'var(--bs-body-font-family)'
			}
		}
	},
	yaxis: {
		min: 0,
		max: 500,
		tickAmount: 5,
		labels: {
			formatter: function (value) {
				return value;
			},
			style: {
				colors: 'var(--bs-body-color)',
				fontSize: '13px',
				fontFamily: 'var(--bs-body-font-family)'
			}
		}
	},
	grid: {
		borderColor: 'var(--bs-border-color)',
		strokeDashArray: 5,
		xaxis: {
			lines: {
				show: false
			}
		},
		yaxis: {
			lines: {
				show: true,
			}
		}
	},
	fill: {
		opacity: 1
	},
	tooltip: {
		y: {
            formatter: function (val) {
				return "$ " + val + " thousands"
            }
		}
	},
	legend: {
        show: true,
        position: 'bottom',
        horizontalAlign: 'center',
        markers: {
			size: 5,
            shape: 'circle',
            radius: 10,
			width: 10,
			height: 10,
		},
		labels: {
			colors: 'var(--bs-heading-color)',
			fontFamily: 'var(--bs-body-font-family)',
			fontSize: '13px',
        }
    }
};
const chartEmployee = document.querySelector("#chartEmployee");
if (typeof chartEmployee !== undefined && chartEmployee !== null) {
    var chartInit = new ApexCharts(chartEmployee, chartEmployeeConfig);
	chartInit.render();
}


var chartAttendanceRateConfig = {
	series: [
		{
			name: 'One Time',
			data: [35, 55, 41, 67, 22, 43, 21, 49, 49, 49, 49, 49]
		},
		{
			name: 'Late',
			data: [13, 23, 20, 8, 13, 27, 33, 12, 12, 12, 12, 12]
		},
		{
			name: 'Absent',
			data: [11, 17, 15, 15, 21, 14, 15, 13, 13, 13, 13, 13]
		}
	],
	colors: [
		'var(--bs-primary)',
		'var(--bs-secondary)',
		'var(--bs-gray)'
	],
	chart: {
		type: 'bar',
		height: 350,
		stacked: true,
		stackType: '100%',
		toolbar: { show: false }
	},
	stroke: {
		show: true,
		width: 1,
		colors: ['var(--bs-body-bg)']
	},
	grid: {
		borderColor: "var(--bs-border-color)",
		strokeDashArray: 5,
		yaxis: {
			lines: {
				show: true,
			},
		},
	},
	plotOptions: {
		bar: {
			horizontal: false,
			endingShape:'rounded',
			columnWidth: '25%',
			borderRadius: 6,
		}
	},
	dataLabels: {
		enabled: false
	},
	markers: {
		size: 0
	},
	legend: {
        show: true,
        position: 'bottom',
        horizontalAlign: 'center',
        markers: {
			size: 5,
            shape: 'circle',
            radius: 10,
			width: 8,
			height: 8,
		},
		labels: {
			colors: 'var(--bs-heading-color)',
			fontFamily: 'var(--bs-body-font-family)',
			fontSize: '13px',
        }
    },
	yaxis: {
		min: 0,
		max: 500,
		tickAmount: 5,
		labels: {
			formatter: function (value) {
				return value + '%';
			},
			style: {
				colors: 'var(--bs-body-color)',
				fontSize: '13px',
				fontFamily: 'var(--bs-body-font-family)'
			}
		}
	},
	xaxis: {
		type: "month",
		categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
		axisBorder: {
			color: 'var(--bs-border-color)',
			axisBorder: {
				show: true,
				color: 'var(--bs-light)',
				height: 0.5,
				width: '100%',
				offsetX: 0,
				offsetY: 0
			},
		},
		axisTicks: {
			show: false,
		},
		labels: {
			rotate: -90,
			style: {
				colors: 'var(--bs-body-color)',
				fontSize: '13px',
				fontFamily: 'var(--bs-body-font-family)'
			}
		},
	},
	fill: {
		opacity: 1
	},
	tooltip: {
		y: {
			formatter: function (val) {
				return val + '%';
			}
		}
	},
	grid: {
		show: false,
	}
};
const chartAttendanceRate = document.querySelector("#chartAttendanceRate");
if (typeof chartAttendanceRate !== undefined && chartAttendanceRate !== null) {
    var chartInit = new ApexCharts(chartAttendanceRate, chartAttendanceRateConfig);
	chartInit.render();
}



var chartPayrollSummaryConfig = {
	series: [
		{
			name: "Gross Salary",
			data: [55000, 60000, 68000, 52000, 69000, 73000, 71000, 74000, 70000, 75000, 72000, 77000]
		},
		{
			name: "Net Salary",
			data: [25000, 27000, 16000, 15500, 16500, 17200, 15800, 17000, 16200, 16800, 16000, 17500]
		},
		{
			name: "Tax Dedication",
			type: 'line',
			data: [25000, 50000, 40000, 20000, 52500, 45000, 55200, 47000, 25800, 58200, 36000, 59500]
		}
	],
	chart: {
		type: 'bar',
		height: 320,
		stacked: true,
		toolbar: {
			show: false
		},
		zoom: {
           enabled: true
		},
		dropShadow: {
           enabled: true,
           enabledOnSeries: undefined,
           top: 3,
           left: 0,
           blur: 4,
           color: "#000",
           opacity: 0.1,
		},
	},
	grid: {
		borderColor: 'var(--bs-border-color)',
		strokeDashArray: 3
	},
	yaxis: {
        min: 100000,
        max: 0,
        tickAmount: 5,
		labels: {
			formatter: function (value) {
				return (value / 1000) + "K";
			},
			style: {
				colors: 'var(--bs-body-color)',
				fontSize: '13px',
				fontFamily: 'var(--bs-body-font-family)'
			}
		}
    },
	xaxis: {
		type: "month",
		categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
		axisBorder: {
			color: 'var(--bs-border-color)',
			axisBorder: {
				show: true,
				color: 'var(--bs-light)',
				height: 0.5,
				width: '100%',
				offsetX: 0,
				offsetY: 0
			},
		},
		axisTicks: {
			show: false,
		},
		labels: {
			rotate: -90,
			style: {
				colors: 'var(--bs-body-color)',
				fontSize: '13px',
				fontFamily: 'var(--bs-body-font-family)'
			}
		},
	},
	colors: [
		"var(--bs-secondary)",
		"var(--bs-primary)",
		"var(--bs-info)"
	],
	legend: {
        show: true,
        position: 'bottom',
        horizontalAlign: 'center',
        markers: {
			size: 5,
            shape: 'circle',
            radius: 10,
			width: 8,
			height: 8,
		},
		labels: {
			colors: 'var(--bs-heading-color)',
			fontFamily: 'var(--bs-body-font-family)',
			fontSize: '13px',
        }
    },
	markers: {
		size: 4,
		colors: ['var(--bs-info)'], 
		strokeColors: '#ffffff',
		strokeWidth: 2,
		hover: {
			size: 4
		}
	},
	stroke: {
		curve: 'straight',
		width: [0, 0, 2.5],
	},
	plotOptions: {
		bar: {
			columnWidth: "40%",
			borderRadius: 0,
		}
	},
	dataLabels: {
		enabled: false
	},
	fill: {
		opacity: 1
	}
};
const chartPayrollSummary = document.querySelector("#chartPayrollSummary");
if (typeof chartPayrollSummary !== undefined && chartPayrollSummary !== null) {
    var chartInit = new ApexCharts(chartPayrollSummary, chartPayrollSummaryConfig);
	chartInit.render();
}


var employeeScore1Config = {
	series: [83],
	chart: {
		type: 'radialBar',
		height: 60,
		width: 60,
		sparkline: {
			enabled: true
		}
	},
	plotOptions: {
		radialBar: {
			hollow: {
				margin: 0,
				size: '80%'
			},
			track: {
				background: 'rgba(var(--bs-primary-rgb), 0.1)',
				strokeWidth: '100%',
				margin: -2
			},
			dataLabels: {
				show: true,
				name: {
					show: false
				},
				value: {
					fontSize: '14px',
					fontWeight: '500',
					fontFamily: 'var(--bs-body-font-family)',
					color: 'var(--bs-heading-color)',
					show: true,
					offsetY: 5
				}
			},
		}
	},
	stroke: {
		lineCap: 'round'
	},
	colors: ['var(--bs-primary)'],
}
const employeeScore1 = document.querySelector("#employeeScore1");
if (typeof employeeScore1 !== undefined && employeeScore1 !== null) {
    var chartInit = new ApexCharts(employeeScore1, employeeScore1Config);
	chartInit.render();
}



var averageTeamKPIConfig = {
	series: [
		{
			data: [300, 200, 190, 100, 250, 300, 350, 500]
		}
	],
	chart: {
		height: 280,
		type: 'area',
		toolbar:{
			show: false
		},
	},
	colors:[
		"var(--bs-secondary)",
	],
	dataLabels: {
		enabled: false
	},
	stroke: {
		curve: 'smooth',
		width: 2,
	},
	legend:{
		show: false,
	},
	grid:{
		show: true,
		strokeDashArray: 3,
		borderColor: 'var(--bs-border-color)',
	},
	yaxis: {
		min: 0,
		max: 500,
		tickAmount: 5,
		labels: {
			style: {
				colors: 'var(--bs-body-color)',
				fontSize: '14px',
			},
			formatter: function (value) {
				return value;
			}
		},
	},
	xaxis: {
		categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug'],
		labels:{
			style: {
				colors: 'var(--bs-body-color)',
				fontSize: '12px',
			},
		},
		axisTicks : {
			show : false
		},
		axisBorder : {
			show : false
		},
	},
	fill:{
		type:'gradient',
		gradient: {
			colorStops:[ 
				[
					{
						offset: 0,
						color: 'var(--bs-secondary)',
						opacity: 0.2
					},
					{
						offset: 50,
						color: 'var(--bs-secondary)',
						opacity: 0.1
					},
					{
						offset: 80,
						color: 'var(--bs-secondary)',
						opacity: 0
					}
				]
			]
		},				
	},
	tooltip: {
		x: {
			show: true,
		},
		y: {
			formatter: function (val) {
				return val.toLocaleString();
			}
		},
		theme: "light"
	},
	responsive: [{
		breakpoint: 575,
		options: {
			chart : {
				height:200,
			},
			yaxis: {
				labels:{
					style: {
						fontSize: '11px',
					},
				},
			},
			xaxis: {
				labels:{
					style: {
						fontSize: '11px',
					},
				},
			},
		},
	}]
}
const averageTeamKPI = document.querySelector("#averageTeamKPI");
if (typeof averageTeamKPI !== undefined && averageTeamKPI !== null) {
    var chartInit = new ApexCharts(averageTeamKPI, averageTeamKPIConfig);
	chartInit.render();
}



var taskStatusChartConfig = {
	series: [65.7],
	chart: {
		type: 'radialBar',
		offsetY: -15,
		height: 380,
		sparkline: { enabled: true }
	},
	plotOptions: {
		radialBar: {
			startAngle: -90,
			endAngle: 90,
			track: {
				background: "#fff",
				strokeWidth: '100%',
				margin: 25,
				dropShadow: {
					enabled: true,
					top: 10,
					left: 0,
					blur: 15,
					color: 'rgba(2, 180, 250, 1)',
					opacity: 0.25
				}
			},
			dataLabels: {
				name: { show: false },
				value: {
					show: true,
					offsetY: -30,
					fontSize: '30px',
					fontFamily: 'var(--bs-body-font-family)',
					fontWeight: 800,
					color: 'var(--bs-dark)',
				},
			}
		}
	},
	grid: {
		padding: {
			top: 0,
			bottom: 0,
			left: 0,
			right: 0
		}
	},
	fill: {
		colors: ['var(--bs-info)']
	},	
}
const taskStatusChart = document.querySelector("#taskStatusChart");
if (typeof taskStatusChart !== undefined && taskStatusChart !== null) {
    var chartInit = new ApexCharts(taskStatusChart, taskStatusChartConfig);
	chartInit.render();
}



var employeeScore2Config = {
	series: [37],
	chart: {
		type: 'radialBar',
		height: 60,
		width: 60,
		sparkline: {
			enabled: true
		}
	},
	plotOptions: {
		radialBar: {
			hollow: {
				margin: 0,
				size: '80%'
			},
			track: {
				background: 'rgba(var(--bs-danger-rgb), 0.1)',
				strokeWidth: '100%',
				margin: -2
			},
			dataLabels: {
				show: true,
				name: {
					show: false
				},
				value: {
					fontSize: '14px',
					fontWeight: '500',
					fontFamily: 'var(--bs-body-font-family)',
					color: 'var(--bs-heading-color)',
					show: true,
					offsetY: 5
				}
			},
		}
	},
	stroke: {
		lineCap: 'round'
	},
	colors: ['var(--bs-danger)'],
}
const employeeScore2 = document.querySelector("#employeeScore2");
if (typeof employeeScore2 !== undefined && employeeScore2 !== null) {
    var chartInit = new ApexCharts(employeeScore2, employeeScore2Config);
	chartInit.render();
}


var employeeScore3Config = {
	series: [46],
	chart: {
		type: 'radialBar',
		height: 60,
		width: 60,
		sparkline: {
			enabled: true
		}
	},
	plotOptions: {
		radialBar: {
			hollow: {
				margin: 0,
				size: '80%'
			},
			track: {
				background: 'rgba(var(--bs-warning-rgb), 0.1)',
				strokeWidth: '100%',
				margin: -2
			},
			dataLabels: {
				show: true,
				name: {
					show: false
				},
				value: {
					fontSize: '14px',
					fontWeight: '500',
					fontFamily: 'var(--bs-body-font-family)',
					color: 'var(--bs-heading-color)',
					show: true,
					offsetY: 5
				}
			},
		}
	},
	stroke: {
		lineCap: 'round'
	},
	colors: ['var(--bs-warning)'],
}
const employeeScore3 = document.querySelector("#employeeScore3");
if (typeof employeeScore3 !== undefined && employeeScore3 !== null) {
    var chartInit = new ApexCharts(employeeScore3, employeeScore3Config);
	chartInit.render();
}


var employeeScore4Config = {
	series: [64],
	chart: {
		type: 'radialBar',
		height: 60,
		width: 60,
		sparkline: {
			enabled: true
		}
	},
	plotOptions: {
		radialBar: {
			hollow: {
				margin: 0,
				size: '80%'
			},
			track: {
				background: 'rgba(var(--bs-secondary-rgb), 0.1)',
				strokeWidth: '100%',
				margin: -2
			},
			dataLabels: {
				show: true,
				name: {
					show: false
				},
				value: {
					fontSize: '14px',
					fontWeight: '500',
					fontFamily: 'var(--bs-body-font-family)',
					color: 'var(--bs-heading-color)',
					show: true,
					offsetY: 5
				}
			},
		}
	},
	stroke: {
		lineCap: 'round'
	},
	colors: ['var(--bs-secondary)'],
}
const employeeScore4 = document.querySelector("#employeeScore4");
if (typeof employeeScore4 !== undefined && employeeScore4 !== null) {
    var chartInit = new ApexCharts(employeeScore4, employeeScore4Config);
	chartInit.render();
}



var leavesPresentsScoreConfig = {
	series: [80],
	chart: {
		type: 'radialBar',
		height: 90,
		width: 90,
		sparkline: {
			enabled: true
		}
	},
	plotOptions: {
		radialBar: {
			hollow: {
				margin: 0,
				size: '75%'
			},
			track: {
				background: 'rgba(var(--bs-primary-rgb), 0.1)',
				strokeWidth: '100%',
				margin: -2
			},
			dataLabels: {
				show: true,
				name: {
					show: false
				},
				value: {
					fontSize: '15px',
					fontWeight: '600',
					fontFamily: 'var(--bs-body-font-family)',
					color: 'var(--bs-heading-color)',
					show: true,
					offsetY: 5
				}
			},
		}
	},
	stroke: {
		lineCap: 'round'
	},
	colors: ['var(--bs-primary)'],
}
const leavesPresentsScore = document.querySelector("#leavesPresentsScore");
if (typeof leavesPresentsScore !== undefined && leavesPresentsScore !== null) {
    var chartInit = new ApexCharts(leavesPresentsScore, leavesPresentsScoreConfig);
	chartInit.render();
}



var leavesPlannedScoreConfig = {
	series: [20],
	chart: {
		type: 'radialBar',
		height: 90,
		width: 90,
		sparkline: {
			enabled: true
		}
	},
	plotOptions: {
		radialBar: {
			hollow: {
				margin: 0,
				size: '75%'
			},
			track: {
				background: 'rgba(var(--bs-danger-rgb), 0.1)',
				strokeWidth: '100%',
				margin: -2
			},
			dataLabels: {
				show: true,
				name: {
					show: false
				},
				value: {
					fontSize: '15px',
					fontWeight: '600',
					fontFamily: 'var(--bs-body-font-family)',
					color: 'var(--bs-heading-color)',
					show: true,
					offsetY: 5
				}
			},
		}
	},
	stroke: {
		lineCap: 'round'
	},
	colors: ['var(--bs-danger)'],
}
const leavesPlannedScore = document.querySelector("#leavesPlannedScore");
if (typeof leavesPlannedScore !== undefined && leavesPlannedScore !== null) {
    var chartInit = new ApexCharts(leavesPlannedScore, leavesPlannedScoreConfig);
	chartInit.render();
}



var leavesUnplannedScoreConfig = {
	series: [49],
	chart: {
		type: 'radialBar',
		height: 90,
		width: 90,
		sparkline: {
			enabled: true
		}
	},
	plotOptions: {
		radialBar: {
			hollow: {
				margin: 0,
				size: '75%'
			},
			track: {
				background: 'rgba(var(--bs-info-rgb), 0.1)',
				strokeWidth: '100%',
				margin: -2
			},
			dataLabels: {
				show: true,
				name: {
					show: false
				},
				value: {
					fontSize: '15px',
					fontWeight: '600',
					fontFamily: 'var(--bs-body-font-family)',
					color: 'var(--bs-heading-color)',
					show: true,
					offsetY: 5
				}
			},
		}
	},
	stroke: {
		lineCap: 'round'
	},
	colors: ['var(--bs-info)'],
}
const leavesUnplannedScore = document.querySelector("#leavesUnplannedScore");
if (typeof leavesUnplannedScore !== undefined && leavesUnplannedScore !== null) {
    var chartInit = new ApexCharts(leavesUnplannedScore, leavesUnplannedScoreConfig);
	chartInit.render();
}



var leavesPendingScoreConfig = {
	series: [68],
	chart: {
		type: 'radialBar',
		height: 90,
		width: 90,
		sparkline: {
			enabled: true
		}
	},
	plotOptions: {
		radialBar: {
			hollow: {
				margin: 0,
				size: '75%'
			},
			track: {
				background: 'rgba(var(--bs-secondary-rgb), 0.1)',
				strokeWidth: '100%',
				margin: -2
			},
			dataLabels: {
				show: true,
				name: {
					show: false
				},
				value: {
					fontSize: '15px',
					fontWeight: '600',
					fontFamily: 'var(--bs-body-font-family)',
					color: 'var(--bs-heading-color)',
					show: true,
					offsetY: 5
				}
			},
		}
	},
	stroke: {
		lineCap: 'round'
	},
	colors: ['var(--bs-secondary)'],
}
const leavesPendingScore = document.querySelector("#leavesPendingScore");
if (typeof leavesPendingScore !== undefined && leavesPendingScore !== null) {
    var chartInit = new ApexCharts(leavesPendingScore, leavesPendingScoreConfig);
	chartInit.render();
}





const bsBodyBG = getComputedStyle(document.documentElement).getPropertyValue('--bs-body-bg').trim();
const bsPrimary = getComputedStyle(document.documentElement).getPropertyValue('--bs-primary').trim();
const bsSecondary = getComputedStyle(document.documentElement).getPropertyValue('--bs-secondary').trim();
const bsBodyColor = getComputedStyle(document.documentElement).getPropertyValue('--bs-body-color').trim();
const bsBorderColor = getComputedStyle(document.documentElement).getPropertyValue('--bs-border-color').trim();
const bsHeadingColor = getComputedStyle(document.documentElement).getPropertyValue('--bs-heading-color').trim();
const bsFontFamily = getComputedStyle(document.documentElement).getPropertyValue('--bs-body-font-family').trim();

function employeeTypeChartConfig() {
	const centerTextPlugin = {
		afterDraw(chart) {
			const { ctx, chartArea: { left, right, top, bottom } } = chart;
			const centerX = (left + right) / 2;
			const centerY = (top + bottom) / 2;

			// Calculate total dynamically
			const dataset = chart.data.datasets[0];
			const total = dataset.data.reduce((acc, val) => acc + val, 0);

			ctx.save();
			ctx.textAlign = 'center';
			ctx.textBaseline = 'middle';

			// Total value
			ctx.font = 'bold 26px sans-serif';
			ctx.fillStyle = '#000';
			ctx.fillText(total, centerX, centerY - 5);

			// Label below
			ctx.font = '14px sans-serif';
			ctx.fillStyle = '#999';
			ctx.fillText('Employee', centerX, centerY + 18);

			ctx.restore();
		}
	};
	
	const canvas = document.getElementById('employeeTypeChart');
    if (!canvas) return;
	const ctx = canvas.getContext('2d');
	
	new Chart(ctx, {
		type: 'doughnut',
		data: {
			labels: ['Onsite', 'Remote', 'Hybrid'],
			datasets: [{
				data: [600, 200, 200],
				backgroundColor: ['#316AFF', '#FF8110', '#FDBB1F'],
				borderRadius: 10,
				spacing: 0, 
				hoverOffset: 5,
				borderWidth: 5,
				borderColor: bsBodyBG,
				hoverBorderColor: bsBodyBG
			}]
		},
		options: {
			cutout: '65%',
			devicePixelRatio: 2,
			layout: {
				padding: 20
			},
			plugins: {
				legend: {
					display: false
				},
				tooltip: {
					callbacks: {
						label: context => `${context.label}: ${context.formattedValue}`
					}
				}
			}
		},
		plugins: [centerTextPlugin]

	});
}
document.addEventListener('DOMContentLoaded', employeeTypeChartConfig);


function companyPayChartConfig() {
	const centerTextPlugin = {
		id: 'centerTextPlugin',
		afterDraw(chart) {
			const { ctx, chartArea: { left, right, top, bottom } } = chart;
			const centerX = (left + right) / 2;
			const centerY = (top + bottom) / 2;

			const dataset = chart.data.datasets[0];
			const total = dataset.data.reduce((acc, val) => acc + val, 0);

			let displayValue = total;
			let displayLabel = 'Total Data';

			// Check if hovering
			const activeElements = chart.getActiveElements();
			if (activeElements.length > 0) {
				const firstPoint = activeElements[0];
				displayValue = dataset.data[firstPoint.index];
				displayLabel = chart.data.labels[firstPoint.index];
			}

			ctx.save();
			ctx.textAlign = 'center';
			ctx.textBaseline = 'middle';

			// Dynamic value
			ctx.font = 'bold 26px sans-serif';
			ctx.fillStyle = bsHeadingColor;
			ctx.fillText(displayValue, centerX, centerY - 8);

			// Dynamic label
			ctx.font = '14px sans-serif';
			ctx.fillStyle = bsBodyColor;
			ctx.fillText(displayLabel, centerX, centerY + 14);

			ctx.restore();
		}
	};
	
	const canvas = document.getElementById('companyPayChart');
    if (!canvas) return;
	const ctx = canvas.getContext('2d');
	
	new Chart(ctx, {
		type: 'doughnut',
		data: {
			labels: ['Salary', 'Bonus', 'Commission', 'Overtime', 'Reimbursement',  'Benefits'],
			datasets: [{
				data: [600, 643, 1608, 884, 2251, 1447],
				backgroundColor: ['#FF401C', '#22B07E', '#02B4FA', '#FF8110', '#316AFF', '#FDBB1F'],
				borderRadius: 30,
				spacing: 0, 
				hoverOffset: 5,
				borderWidth: 2,
				borderColor: bsBodyBG,
				hoverBorderColor: bsBodyBG
			}]
		},
		options: {
			cutout: '85%',
			devicePixelRatio: 2,
			layout: {
				padding: 10
			},
			plugins: {
				legend: {
					display: false
				},
				tooltip: {
					enabled: false,
					callbacks: {
						label: context => `${context.label}: ${context.formattedValue}`
					}
				}
			}
		},
		plugins: [centerTextPlugin]

	});
}
document.addEventListener('DOMContentLoaded', companyPayChartConfig);


if ($('#dt_EmployeeLeave').length) {
	const dt_EmployeeLeave = $('#dt_EmployeeLeave').DataTable({
		searching: true,
		pageLength: 6,
		select: false,
		lengthChange: false,
		info: false,
		paging: false,
		scrollCollapse: true,
		scrollY: '300px',
		language: {
			search: "",
			searchPlaceholder: 'Search'
		},
		initComplete: function() {
			var dtSearch = $('#dt_EmployeeLeave_wrapper .dt-search').detach();
			$('#dt_EmployeeLeave_Search').append(dtSearch);
			$('#dt_EmployeeLeave_Search .dt-search').prepend('<i class="fi fi-rr-search"></i>');
			$('#dt_EmployeeLeave_Search .dt-search label').remove();
			$('#dt_EmployeeLeave_wrapper > .row.mt-2.justify-content-between').first().remove();
		},
	});
}

if ($('#dt_PageEmployeeLeave').length) {
	const dt_PageEmployeeLeave = $('#dt_PageEmployeeLeave').DataTable({
		searching: true,
		pageLength: 10,
		select: false,
		lengthChange: false,
		info: true,
		paging: true,
		language: {
			search: "",
			searchPlaceholder: 'Search',
			paginate: {
				previous: "<i class='fi fi-rr-angle-left'></i>",
				next: "<i class='fi fi-rr-angle-right'></i>",
				first: "<i class='fi fi-rr-angle-double-left'></i>",
				last: "<i class='fi fi-rr-angle-double-right'></i>"
			},
		},
		initComplete: function() {
			var dtSearch = $('#dt_PageEmployeeLeave_wrapper .dt-search').detach();
			$('#dt_PageEmployeeLeave_Search').append(dtSearch);
			$('#dt_PageEmployeeLeave_Search .dt-search').prepend('<i class="fi fi-rr-search"></i>');
			$('#dt_PageEmployeeLeave_Search .dt-search label').remove();
			$('#dt_PageEmployeeLeave_wrapper > .row.mt-2.justify-content-between').first().remove();
		},
	});
}

if ($('#dt_EmployeeAttendance').length) {	
	const dt_EmployeeAttendance = $('#dt_EmployeeAttendance').DataTable({
		searching: true,
		pageLength: 9,
		select: false,
		lengthChange: false,
		info: true,
		paging: true,
		language: {
			search: "",
			searchPlaceholder: 'Search',
			paginate: {
				previous: "<i class='fi fi-rr-angle-left'></i>",
				next: "<i class='fi fi-rr-angle-right'></i>",
				first: "<i class='fi fi-rr-angle-double-left'></i>",
				last: "<i class='fi fi-rr-angle-double-right'></i>"
			},
		},
		initComplete: function() {
			var dtSearch = $('#dt_EmployeeAttendance_wrapper .dt-search').detach();
			$('#dt_EmployeeAttendance_Search').append(dtSearch);
			$('#dt_EmployeeAttendance_Search .dt-search').prepend('<i class="fi fi-rr-search"></i>');
			$('#dt_EmployeeAttendance_Search .dt-search label').remove();
			$('#dt_EmployeeAttendance_wrapper > .row.mt-2.justify-content-between').first().remove();
		},
		columnDefs: [{ 
			targets: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32],
			orderable: false,
		}]
	});
}

if ($('#dt_PayrollList').length) {
	const dt_PayrollList = $('#dt_PayrollList').DataTable({
		searching: true,
		pageLength: 10,
		select: false,
		lengthChange: false,
		info: true,
		paging: true,
		language: {
			search: "",
			searchPlaceholder: 'Search',
			paginate: {
				previous: "<i class='fi fi-rr-angle-left'></i>",
				next: "<i class='fi fi-rr-angle-right'></i>",
				first: "<i class='fi fi-rr-angle-double-left'></i>",
				last: "<i class='fi fi-rr-angle-double-right'></i>"
			},
		},
		initComplete: function() {
			var dtSearch = $('#dt_PayrollList_wrapper .dt-search').detach();
			$('#dt_PayrollList_Search').append(dtSearch);
			$('#dt_PayrollList_Search .dt-search').prepend('<i class="fi fi-rr-search"></i>');
			$('#dt_PayrollList_Search .dt-search label').remove();
			$('#dt_PayrollList_wrapper > .row.mt-2.justify-content-between').first().remove();
		},
		columnDefs: [{ 
			targets: [0],
			orderable: false,
		}]
	});
}

if(jQuery('#dateTimeFlatpickr').length > 0 ){
	$("#dateTimeFlatpickr").flatpickr({
		enableTime: false,
		dateFormat: "Y-m-d H:i",
		inline: true,
	});
}

if(jQuery('.flatpickr-date').length > 0 ){
	$(".flatpickr-date").flatpickr({
		enableTime: false,
		dateFormat: "Y-m-d H:i",
	});
}