import { Alert, Snackbar } from "@mui/material"
import React from "react"

export const Toast = ({ open, setOpen, message, severity }) => {
	return (
		<Snackbar
			open={open}
			onClose={() => setOpen(false)}
			autoHideDuration={2000}
		>
			<Alert
				onClose={() => setOpen(false)}
				severity={severity || "success"}
				variant='filled'
				sx={{ width: "100%" }}
			>
				{message}
			</Alert>
		</Snackbar>
	)
}
