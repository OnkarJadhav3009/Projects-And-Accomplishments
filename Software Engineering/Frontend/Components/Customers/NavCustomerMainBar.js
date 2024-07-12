import React, { useState, useEffect } from "react";
import AppBar from "@mui/material/AppBar";
import Box from "@mui/material/Box";
import Toolbar from "@mui/material/Toolbar";
import IconButton from "@mui/material/IconButton";
import InputBase from "@mui/material/InputBase";
import Typography from "@mui/material/Typography";
import Menu from "@mui/material/Menu";
import { styled, alpha } from "@mui/material/styles";
import Container from "@mui/material/Container";
import Avatar from "@mui/material/Avatar";
import Button from "@mui/material/Button";
import Tooltip from "@mui/material/Tooltip";
import MenuItem from "@mui/material/MenuItem";
import useSearchBar from "../SearchBar/useSearchBar";

const Search = styled("div")(({ theme }) => ({
  position: "relative",
  borderRadius: theme.shape.borderRadius,
  backgroundColor: alpha(theme.palette.common.white, 0.15),
  "&:hover": {
    backgroundColor: alpha(theme.palette.common.white, 0.25),
  },
  marginLeft: "60px",
  width: "100%",
  [theme.breakpoints.up("sm")]: {
    marginLeft: theme.spacing(1),
    width: "auto",
  },
}));

const SearchIconWrapper = styled("div")(({ theme }) => ({
  padding: theme.spacing(0, 2),
  height: "100%",
  position: "absolute",
  pointerEvents: "none",
  display: "flex",
  alignItems: "center",
  justifyContent: "center",
}));

const StyledInputBase = styled(InputBase)(({ theme }) => ({
  color: "inherit",
  "& .MuiInputBase-input": {
    padding: theme.spacing(1, 1, 1, 0),
    // vertical padding + font size from searchIcon
    paddingLeft: `calc(1em + ${theme.spacing(4)})`,
    transition: theme.transitions.create("width"),
    width: "100%",
    [theme.breakpoints.up("sm")]: {
      width: "12ch",
      "&:focus": {
        width: "50ch",
      },
    },
  },
}));

const setting = ["Dashboard", "Logout"];
const locations = ["Chicago", "Indianapolis", "New York"];

function NavCustomerMainBar() {
  const [anchorElNav, setAnchorElNav] = useState("");
  const [anchorElUser, setAnchorElUser] = useState("");
  const [anchorElLocation, setAnchorElLocation] = useState("");
  const [userName, setUserName] = useState("");
  const [location, setLocation] = useState("");
  const [displayLocation, setDisplayLocation] = useState("");
  // const userName = localStorage.getItem("username");

  useEffect(() => {
    const savedUserName = localStorage.getItem('username');
    if (savedUserName) {
      setUserName(savedUserName);
    }
  }, []);

  const { render, searchText, prev } = useSearchBar();

  const handleMenuClick = (setting) => {
    if (setting === "Dashboard") {
      window.location.href = "/customer-dashboard";
    } else if (setting === "Logout") {
      handleLogout();
    } else {
      handleCloseUserMenu();
    }
  };

  const handleOpenLocationMenu = (event) => {
    setAnchorElLocation(event.currentTarget);
  };

  const handleCloseLocationMenu = () => {
    setAnchorElLocation(null);
  };

  const handleOpenUserMenu = (event) => {
    setAnchorElUser(event.currentTarget);
  };

  const handleCloseUserMenu = () => {
    setAnchorElUser(null);
  };

  const handleLogout = () => {
      localStorage.removeItem('username');
      localStorage.removeItem('accessToken');
      localStorage.removeItem('refreshToken');
      window.location.href='/customerHome'
         
  };

  useEffect(() => {
    if (location) {
      setDisplayLocation(location);
    } else {
      setDisplayLocation("CHOOSE LOCATION");
    }
  }, [location]);

    // useEffect(() => {
    //   setUserName(username);
    // }, [userName]);

  return {
    searchText,
    location,
    render: (
      <>
        <AppBar position="fixed" sx={{ backgroundColor: "black" }}>
          <Container maxWidth="xl">
            <Toolbar disableGutters>
              <Typography
                variant="h3"
                noWrap
                component="a"
                href="/"
                sx={{
                  mr: 2,
                  display: { xs: "none", md: "flex" },
                  fontFamily:
                    "https://fonts.googleapis.com/css2?family=Nunito&display=swap",
                  fontWeight: 700,
                  letterSpacing: ".3rem",
                  color: "inherit",
                  textDecoration: "none",
                }}
              >
                WatchaFlick
              </Typography>
              <Box
                component="img"
                sx={{ width: 45, height: 50 }}
                alt="Logo"
                src="/images/logo.png"
              />
              
              <>
                <Box
                  sx={{
                    flexGrow: 1,
                    display: { xs: "none", md: "flex" },
                    color: "black",
                    padding: "0rem 5rem 0rem 5rem",
                  }}
                >
                  {render}
                </Box>
                <Box
                  sx={{
                    flexGrow: 1,
                    display: { xs: "none", md: "flex" },
                    color: "white",
                  }}
                >
                  <Tooltip title="Choose location">
  <Button
    style={{ 
      color: "white",
      fontSize: "15px", // increase the font size
      fontWeight: "bold", // add bold font weight
      textTransform: "uppercase", // convert to uppercase 
    }}
    onClick={handleOpenLocationMenu}
  >
    {displayLocation}
  </Button>
</Tooltip>

                  <Menu
                    sx={{ mt: "45px" }}
                    id="menu-appbar"
                    anchorEl={anchorElLocation}
                    anchorOrigin={{
                      vertical: "top",
                      horizontal: "right",
                    }}
                    keepMounted
                    transformOrigin={{
                      vertical: "top",
                      horizontal: "right",
                    }}
                    open={Boolean(anchorElLocation)}
                    onClose={handleCloseLocationMenu}
                  >
                    {locations.map((l, index) => (
                      <MenuItem
                        key={index}
                        onClick={() => {
                          setLocation(locations[index]);
                          handleCloseLocationMenu();
                        }}
                      >
                        <Typography textAlign="center">{l}</Typography>
                      </MenuItem>
                    ))}
                  </Menu>
                </Box>
              </>

              <Typography
                variant="h5"
                noWrap
                component="a"
                href=""
                sx={{
                  mr: 2,
                  display: { xs: "flex", md: "none" },
                  flexGrow: 1,
                  fontFamily:
                    "https://fonts.googleapis.com/css2?family=Nunito&display=swap",
                  fontWeight: 700,
                  letterSpacing: ".3rem",
                  color: "inherit",
                  textDecoration: "none",
                }}
              >
                WatchaFlick
              </Typography>
              <div>Welcome {userName}!</div>
              <Box sx={{ flexGrow: 0 }}>
                <Tooltip title="Open settings">
                  <IconButton onClick={handleOpenUserMenu} sx={{ p: 0 }}>
                    <Avatar alt="Remy Sharp" src="images/user2.png" />
                  </IconButton>
                </Tooltip>
                <Menu
                  sx={{ mt: "45px" }}
                  id="menu-appbar"
                  anchorEl={anchorElUser}
                  anchorOrigin={{
                    vertical: "top",
                    horizontal: "right",
                  }}
                  keepMounted
                  transformOrigin={{
                    vertical: "top",
                    horizontal: "right",
                  }}
                  open={Boolean(anchorElUser)}
                  onClose={handleCloseUserMenu}
                >
                  {setting.map((setting, index) => (
                    <MenuItem
                      key={index}
                      onClick={() => handleMenuClick(setting)}
                    >
                      <Typography textAlign="center">{setting}</Typography>
                    </MenuItem>
                  ))}
                </Menu>
              </Box>
            </Toolbar>
          </Container>
        </AppBar>
      </>
    ),
  };
}
export default NavCustomerMainBar;
