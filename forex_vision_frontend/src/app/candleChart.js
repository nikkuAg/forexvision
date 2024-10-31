import CanvasJSReact from "@canvasjs/react-charts"

var CanvasJSChart = CanvasJSReact.CanvasJSChart
export const CandleChart = ({ data }) => {
	const dataPoints = data.map((d) => ({
		x: new Date(d.date),
		y: [d.open, d.high, d.low, d.close],
	}))
	console.log(dataPoints)
	const options = {
		theme: "light3",
		animationEnabled: false,
		exportEnabled: false,
		zoomEnabled: true,
		height: "400",
		axisX: {
			title: "Date",
			valueFormatString: "YYYY-MM-DD",
			gridThickness: 0.5,
			gridColor: "#d7d7d7",
			lineColor: "#d7d7d7",
			lineThickness: 1,
			labelFontColor: "#a0a0a0",
			titleFontColor: "#a0a0a0",
			labelFontSize: "12",
			titleFontSize: "12",
			tickLength: 0,
		},
		axisY: {
			title: "Prices",
			gridThickness: 0.5,
			gridColor: "#d7d7d7",
			lineColor: "#d7d7d7",
			lineThickness: 1,
			labelFontColor: "#a0a0a0",
			titleFontColor: "#a0a0a0",
			labelFontSize: "12",
			titleFontSize: "12",
			tickLength: 0,
		},
		data: [
			{
				type: "candlestick",
				color: "#707070",
				fillOpacity: 0.7,
				risingColor: "red",
				fallingColor: "green",
				yValueFormatString: "0.000",
				xValueFormatString: "MMM DD, YYYY",
				dataPoints: dataPoints,
			},
		],
	}
	return <CanvasJSChart options={options} />
}
