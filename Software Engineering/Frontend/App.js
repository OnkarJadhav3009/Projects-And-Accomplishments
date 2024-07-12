import { React, useEffect } from "react";
import "./App.css";
import Home from "./Components/Pages/Home";
import Login from "./Components/Login/Login";
import Register from "./Components/Register/Register";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import CustomerHome from "./Components/Customers/CustomerHome";
import CustomerHomeLanding from "./Components/Customers/CustomerHomeLanding";
import { gapi } from "gapi-script";
import CustomerDashboard from "./Components/Dashboard/CustomerDashboard";
import Preferences from "./Components/Dashboard/Preferences";
import { ThemeProvider, createTheme } from "@mui/material/styles";
import CssBaseline from "@mui/material/CssBaseline";
import OnsiteHome from "./Components/OnsiteManagement/onsiteHome";
import SupportAdmin from "./Components/SupportAdmin";
import Booking from "./Components/Booking/booking";
import BookingConfirmed from "./Components/Pages/BookingConfirmed";

// React slick css
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import "@fontsource/inter";
import ForgotPassword from "./Components/Login/ForgotPassword";
import ForgotPasswordMain from "./Components/Login/ForgotPasswordMain";
import MoviePage from "./Components/MoviePages/MoviePage";

const clientId =
  "973282407747-5e4l7ut9st7c6aqace5d1avdjcjp8o3s.apps.googleusercontent.com";

//Theme code
const theme = createTheme({
  palette: {
    grey: {
      0: "#ffffff",
      10: "#f6f6f6",
      50: "#f0f0f0",
      100: "#e0e0e0",
      200: "#c2c2c2",
      300: "#a3a3a3",
      400: "#858585",
      500: "#666666",
      600: "#525252",
      700: "#3d3d3d",
      800: "#292929",
      900: "#141414",
      1000: "#000000",
    },
    primary: {
      100: "#606060",
      200: "#474747",
      300: "#444444",
      400: "#333333",
      500: "#2D2D2D",
      600: "#1E1E1E",
      700: "#1C1C1C",
      800: "#161616",
      900: "#000000",
    },
    secondary: {
      main: "#F8BB16",
      100: "#FBE9A7",
      200: "#F8E08B",
      300: "#F5D16D",
      400: "#F2C250",
      500: "#F8BB16",
      600: "#D89F13",
      700: "#B18210",
      800: "#8E6610",
      900: "#6B490D",
    },
  },
  typography: {
    fontFamily: ["Inter", "sans-serif"].join(","),
    fontSize: 12,
    h1: {
      fontFamily: ["Inter", "sans-serif"].join(","),
      fontSize: 40,
    },
    h2: {
      fontFamily: ["Inter", "sans-serif"].join(","),
      fontSize: 32,
    },
    h3: {
      fontFamily: ["Inter", "sans-serif"].join(","),
      fontSize: 24,
    },
    h4: {
      fontFamily: ["Inter", "sans-serif"].join(","),
      fontSize: 20,
    },
    h5: {
      fontFamily: ["Inter", "sans-serif"].join(","),
      fontSize: 16,
    },
    h6: {
      fontFamily: ["Inter", "sans-serif"].join(","),
      fontSize: 14,
    },
  },
});

// Theme code

function App() {
  useEffect(() => {
    function start() {
      gapi.client.init({
        clientId: clientId,
        scope: "",
      });
    }
    gapi.load("client:auth2", start);
  });

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Router>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/customerHome" element={<CustomerHome />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/customerMainHome" element={<CustomerHomeLanding />} />
          <Route path="/forgotPassword" element={<ForgotPassword />} />
          <Route path="/customerSupport" element={<SupportAdmin />} />
          <Route path="/api/reset-password" element={<ForgotPasswordMain />} />
          <Route path="/book-tickets" element={<Booking />} />
          <Route path="/onsiteManagement" element={<OnsiteHome />} />
          <Route path="/customer-dashboard" element={<CustomerDashboard />} />
          <Route path="/preferences" element={<Preferences />} />
          <Route path="/moviePage" element={<MoviePage />} />
          <Route path="/booking" element={<Booking />} />
          <Route path="/bookingConfirmed" element={<BookingConfirmed />} />
        </Routes>
      </Router>
    </ThemeProvider>
  );
}

export default App;
