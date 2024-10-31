"use client"
import { Line } from "react-chartjs-2"
import {
	Chart as ChartJS,
	LineElement,
	CategoryScale,
	LinearScale,
	PointElement,
	Legend,
	Tooltip,
} from "chart.js"
import { Box } from "@mui/material"

ChartJS.register(
	LineElement,
	CategoryScale,
	LinearScale,
	PointElement,
	Legend,
	Tooltip
)

export const Chart = ({ data }) => {
	const dates = data.map((d) => d.date)
	const openPrices = data.map((d) => d.open)
	const highPrices = data.map((d) => d.high)
	const lowPrices = data.map((d) => d.low)
	const closePrices = data.map((d) => d.close)

	const chartData = {
		labels: dates,
		datasets: [
			{
				label: "Open Prices",
				data: openPrices,
				borderColor: "#ff5722",
				fill: false,
			},
			{
				label: "Low Prices",
				data: lowPrices,
				borderColor: "#8bc34a",
				fill: false,
			},
			{
				label: "High Prices",
				data: highPrices,
				borderColor: "#2196f3",
				fill: false,
			},
			{
				label: "Close Prices",
				data: closePrices,
				borderColor: "#6d1b7b",
				fill: false,
			},
		],
	}

	const options = {
		responsive: true,
		plugins: {
			legend: {
				position: "top",
			},
			tooltip: {
				mode: "index",
				intersect: false,
			},
		},
		scales: {
			x: {
				title: {
					display: true,
					text: "Dates",
				},
			},
			y: {
				title: {
					display: true,
					text: "Prices",
				},
			},
		},
	}

	return <Line data={chartData} options={options} />
}
