import { createTheme } from "@mui/material/styles"

export const theme = (theme) =>
	createTheme({
		...theme,
		components: {
			MuiPickersToolbar: {
				styleOverrides: {
					root: {
						color: "#a6adbb33",
						borderRadius: "2px",
						borderWidth: "1px",
						borderColor: "#a6adbb33",
						border: "1px solid",
						backgroundColor: "#a6adbb33",
					},
				},
			},
		},
	})
