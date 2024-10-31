"use client"
import { CURRENCIES_QUOTE, PERIOD } from "@/constants/constants"
import { ThemeProvider } from "@emotion/react"
import { DatePicker, LocalizationProvider } from "@mui/x-date-pickers"
import { AdapterDayjs } from "@mui/x-date-pickers/AdapterDayjs"
import dayjs from "dayjs"
import { useState, useEffect } from "react"
import { theme } from "./theme"
import {
	AppBar,
	Box,
	Divider,
	FormControl,
	FormControlLabel,
	InputLabel,
	MenuItem,
	Select,
	Stack,
	Switch,
	Typography,
} from "@mui/material"
import axios from "axios"
import { FOREX_DATA_API } from "@/constants/apis"
import { Chart } from "./chart"
import { Toast } from "./snackbar"
import { CandleChart } from "./candleChart"

export default function Home() {
	const [exchangeData, setExchangeData] = useState([])
	const [showLineChart, setShowLineChart] = useState(true)
	const [quote, setQuote] = useState(Object.keys(CURRENCIES_QUOTE)[0])
	const [period, setPeriod] = useState(Object.keys(PERIOD)[0])
	const [date, setDate] = useState({
		startDate: null,
		endDate: null,
	})
	const [openToast, setOpenToast] = useState(false)
	const [message, setMessage] = useState("")
	const [severity, setSeverity] = useState("info")

	const handlePeriodChange = (event) => {
		setPeriod(event.target.value)
		if (event.target.value != "")
			setDate({
				startDate: null,
				endDate: null,
			})
	}

	const handleStartDateChange = (value) => {
		setDate({
			...date,
			startDate: value,
		})
		setPeriod("")
	}

	const handleEndDateChange = (value) => {
		setDate({
			...date,
			endDate: value,
		})
		setPeriod("")
	}

	useEffect(() => {
		const data = {
			quote,
		}
		if (period) {
			data["period"] = period
		} else if (date.startDate && date.endDate) {
			data["start_date"] = dayjs(date.startDate).format("YYYY-MM-DD")
			data["end_date"] = dayjs(date.endDate).format("YYYY-MM-DD")
		}

		if (data["period"] || (data["start_date"] && data["end_date"])) {
			axios
				.post(FOREX_DATA_API, data)
				.then((response) => {
					setExchangeData(response.data)
					if (response.data.length == 0) {
						setMessage("No data found for the given period")
						setOpenToast(true)
						setSeverity("info")
					}
				})
				.catch((error) => {
					setMessage(error.response.data.message)
					setOpenToast(true)
					setSeverity("error")
				})
		}
	}, [quote, period, date])

	return (
		<div>
			<ThemeProvider theme={theme}>
				<AppBar position='static'>
					<Box sx={{ p: 2 }}>
						<Typography variant='h5'>Forex Vision</Typography>
					</Box>
				</AppBar>
				<Box sx={{ p: 2 }}>
					<Stack gap={2}>
						<FormControl fullWidth>
							<Stack spacing={2}>
								<FormControl sx={{ width: "50%" }}>
									<InputLabel id='quote-label'>Exchange Quote</InputLabel>
									<Select
										labelId='quote-label'
										label='Exchange Quote'
										onChange={(e) => setQuote(e.target.value)}
										defaultValue={quote}
										value={quote}
									>
										{Object.keys(CURRENCIES_QUOTE).map((key) => (
											<MenuItem key={key} value={key}>
												{CURRENCIES_QUOTE[key]}
											</MenuItem>
										))}
									</Select>
								</FormControl>
								<Stack direction={"row"} spacing={2} alignItems={"center"}>
									<FormControl sx={{ width: "10%" }}>
										<InputLabel id='quote-label'>Period</InputLabel>
										<Select
											labelId='quote-label'
											label='Period'
											onChange={handlePeriodChange}
											defaultValue={period}
											value={period}
										>
											{Object.keys(PERIOD).map((key) => (
												<MenuItem key={key} value={key}>
													{PERIOD[key]}
												</MenuItem>
											))}
										</Select>
									</FormControl>
									<Divider>OR</Divider>
									<LocalizationProvider dateAdapter={AdapterDayjs}>
										<FormControl>
											<Stack direction={"row"} spacing={2}>
												<DatePicker
													value={date.startDate}
													label={"Start Date"}
													format='YYYY-MM-DD'
													onChange={(newValue) =>
														handleStartDateChange(newValue)
													}
												/>
												<DatePicker
													value={date.endDate}
													label={"End Date"}
													format='YYYY-MM-DD'
													onChange={(newValue) => handleEndDateChange(newValue)}
												/>
											</Stack>
										</FormControl>
									</LocalizationProvider>
									<FormControl>
										<FormControlLabel
											control={<Switch defaultChecked />}
											onChange={() => setShowLineChart(!showLineChart)}
											label='Line Chart'
										/>
									</FormControl>
								</Stack>
							</Stack>
						</FormControl>
						<Box>
							{exchangeData && exchangeData.length > 0 && (
								<>
									{showLineChart ? (
										<Chart data={exchangeData} />
									) : (
										<CandleChart data={exchangeData} />
									)}
								</>
							)}
						</Box>
					</Stack>
				</Box>
				<Toast
					open={openToast}
					setOpen={setOpenToast}
					message={message}
					severity={severity}
				/>
			</ThemeProvider>
		</div>
	)
}
