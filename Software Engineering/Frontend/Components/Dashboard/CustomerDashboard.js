import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import {
  Box,
  Card,
  CardContent,
  CardHeader,
  Typography,
  Divider,
  Button,
  Avatar,
  List,
  ListItem,
  ListItemText,
  ListItemIcon,
  AppBar,
  Toolbar,
  TextField,
  IconButton,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogContentText,
  DialogActions,
} from '@mui/material';
import FlightIcon from '@mui/icons-material/Flight'; // Import the Flight icon as the pigeon icon
import CloseIcon from '@mui/icons-material/Close'; // Import the Close icon for the remove button
import SlowMotionVideoIcon from '@mui/icons-material/SlowMotionVideo';
import SettingsIcon from '@mui/icons-material/Settings';


const CustomerDashboard = () => {

  const [userName, setUserName] = useState("");

  useEffect(() => {
    const savedUserName = localStorage.getItem('username');
    if (savedUserName) {
      setUserName(savedUserName);
      // console.log(userName);
    }
  }, []);

  // Add a state for booking status
  const [bookingStatus, setBookingStatus] = useState('Booked');

  // Function to handle canceling the booking
  const handleCancelBooking = () => {
    setBookingStatus('Cancelled');
  };

  // Add useNavigate hook from react-router-dom
  const navigate = useNavigate();

  // Add useEffect to fetch recentBooking data from API
  useEffect(() => {
  // Fetch recentBooking data from API here
  // Example: fetch('/api/recentBooking')
  //           .then((response) => response.json())
  //           .then((data) => setRecentBooking(data));
  }, []);

  // Navigation handlers for routes
  const handleLogout = () => {
  navigate('/login')
  };

  const handlePreferences = () => {
  // Navigate to the preferences route
  navigate('/preferences');;
  };

  const handleRecommendedMovies = () => {
  navigate('/customerMainHome')
  };

  const handleWatchAFlickLogo = () => {
  navigate('/customerMainHome')
  };


  const user = {
    name: userName,
    email: 'johndoe@gmail.com',
    membershipStatus: 'Premium',
    promoOffers: ['10% off your next booking', 'Buy 1 Get 1 Free'],
    rewardPoints: 1200,
  };

  const recentBooking = {
    movieTitle: 'Avengers End Game',
    movieTiming: 'April 24, 2023, 10:30 AM',
  };

  const [cardDetails, setCardDetails] = useState({
    cardNumber: '',
    expiryDate: '',
    cvv: '',
  });

  const [cardSaved, setCardSaved] = useState(false);

  const handleChange = (event) => {
    const { name, value } = event.target;
    setCardDetails((prevState) => ({ ...prevState, [name]: value }));
  };

  const handleSave = () => {
    console.log('Card details saved:', cardDetails);
    setCardSaved(true);
  };

    // Add a state to handle dialog open/close
    const [openDialog, setOpenDialog] = useState(false);

    // Function to handle dialog open
    const handleClickOpen = () => {
      setOpenDialog(true);
    };
  
    // Function to handle dialog close
    const handleClose = () => {
      setOpenDialog(false);
    };
  
    // Function to handle removing the card
    const handleRemove = () => {
      setCardDetails({ cardNumber: '', expiryDate: '', cvv: '' });
      setCardSaved(false);
      setOpenDialog(false);
    };  

    // console.log(user.name);

  const formatCardNumber = (cardNumber) => {
    return cardNumber.replace(/(\d{4})/g, '$1 ').trim();
  };

  return (
    <>
      <AppBar position="static" color="primary" elevation={0}>
        <Toolbar>
          <Typography variant="h4" sx={{ flexGrow: 1 }} color="secondary" onClick={handleWatchAFlickLogo}>
            WatchAFlick
          </Typography>
          <Avatar sx={{ bgcolor: 'secondary.500', mr: 2 }}>{user.name[0]}</Avatar>
          <Button variant="contained" color="primary" size="small" onClick={handleLogout}>
          <Typography variant="h6" sx={{ flexGrow: 1 }} color="secondary">
            Logout
          </Typography>
          </Button>
        </Toolbar>
      </AppBar>
      <Box sx={{ display: 'flex', bgcolor: 'primary.100', height: 'calc(100vh - 64px)', overflow: 'auto'}}>
        <Box sx={{ width: '20%', bgcolor: 'primary.200', height: '100%' }}>
          <List>
            <ListItem button onClick={handlePreferences}>
            <ListItemIcon>
                <SettingsIcon color="secondary" />
              </ListItemIcon>
              <ListItemText primary="Preferences" primaryTypographyProps={{ color: 'secondary.500' }} />
            </ListItem>
            <Divider />
            <ListItem button onClick={handleRecommendedMovies}>
            <ListItemIcon>
              <SlowMotionVideoIcon color="secondary" />
            </ListItemIcon>
              <ListItemText primary="Recommended Movies" primaryTypographyProps={{ color: 'secondary.500' }} />
            </ListItem>
            </List>
        </Box>
        <Box sx={{ flexGrow: 1, display: 'flex', flexDirection: 'column', alignItems: 'center', mt: 2, overflow: 'auto' }}>
          <Box sx={{ display: 'flex', flexDirection: 'row', justifyContent: 'space-between', flexWrap: 'wrap', width: '100%', maxWidth: 800, gap: 2 }}>
            <Card sx={{ flexGrow: 1, maxWidth: 'calc(50% - 8px)', mt: 2 }}>
            <CardHeader
              title="Recent Booking"
              sx={{ bgcolor: 'secondary.700' }}
              titleTypographyProps={{ variant: 'h5', color: 'grey.0' }}
              subheaderTypographyProps={{ variant: 'body1', color: 'grey.100' }}
            />
            <CardContent>
            {bookingStatus === 'Booked' ? (
              <>
                <Typography variant="h6" color="primary.500">
                  {recentBooking.movieTitle}
                </Typography>
                <Typography variant="body1" color="primary.300">
                  {recentBooking.movieTiming}
                </Typography>
                <Button
                  variant="contained"
                  color="primary"
                  sx={{ mt: 2 }}
                  onClick={handleCancelBooking}
                >
                  Cancel Booking
                </Button>
              </>
            ) : (
              <Typography variant="h6" color="error.main">
                Movie booking has been cancelled.
              </Typography>
            )}
          </CardContent>
            </Card>
            <Card sx={{ flexGrow: 1, maxWidth: 'calc(50% - 8px)', mt: 2 }}>
            <CardHeader
                title="Membership Status"
                sx={{ bgcolor: 'secondary.700' }}
                titleTypographyProps={{ variant: 'h5', color: 'grey.0' }}
              />
          <CardContent>
            <Typography variant="h6" color="primary.500">
              {user.membershipStatus}
            </Typography>
          </CardContent>
            </Card>
            <Card sx={{ flexGrow: 1, maxWidth: 'calc(50% - 8px)', mt: 2 }}>
              <CardHeader
              title="Promotional Offers"
              sx={{ bgcolor: 'secondary.700' }}
              titleTypographyProps={{ variant: 'h5', color: 'grey.0' }}
            />
            <CardContent>
              <List>
                {user.promoOffers.map((offer, index) => (
                  <ListItem key={index}>
                    <ListItemText primary={offer} />
                  </ListItem>
                ))}
              </List>
            </CardContent>
            </Card>
            <Card sx={{ flexGrow: 1, maxWidth: 'calc(50% - 8px)', mt: 2 }}>
                <CardHeader
                title="Reward Points"
                sx={{ bgcolor: 'secondary.700' }}
                titleTypographyProps={{ variant: 'h5', color: 'grey.0' }}
              />
              <CardContent>
                <Typography variant="h6" color="primary.500">
                  {user.rewardPoints} points
                </Typography>
              </CardContent>
            </Card>
          </Box>
          <Card sx={{ width: '100%', maxWidth: 800, mt: 2 }}>
          <CardHeader
            title="Payment Details"
            sx={{ bgcolor: 'secondary.700' }}
            titleTypographyProps={{ variant: 'h5', color: 'grey.0' }}
          />
          <CardContent>
            <TextField
              name="cardNumber"
              label="Credit/Debit Card Number"
              type="text"
              variant="outlined"
              fullWidth
              value={cardDetails.cardNumber}
              onChange={handleChange}
              sx={{ mb: 2 }}
            />
            <TextField
              name="expiryDate"
              label="Expiry Date"
              type="text"
              variant="outlined"
              fullWidth
              value={cardDetails.expiryDate}
              onChange={handleChange}
              sx={{ mb: 2 }}
            />
            <TextField
              name="cvv"
              label="CVV"
              type="password"
              variant="outlined"
              fullWidth
              value={cardDetails.cvv}
              onChange={handleChange}
              sx={{ mb: 2 }}
            />
            <Button
                variant="contained"
                color="primary"
                onClick={handleSave}
                  >
                Save Payment Details
             </Button>
          </CardContent>
          </Card>
          {cardSaved && (
            <Card sx={{ position: 'relative', width: '100%', maxWidth: 400, mt: 2, bgcolor: 'secondary.500', borderRadius: 2 }}>
              <CardContent>
                <Typography variant="h6" color="primary.main" sx={{ letterSpacing: 1 }}>
                  {formatCardNumber(cardDetails.cardNumber)}
                </Typography>
                <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mt: 2 }}>
                  <Typography variant="body1" color="primary.main">
                    {cardDetails.expiryDate}
                  </Typography>
                  <Typography variant="body1" color="primary.main">
                    CVV: {cardDetails.cvv}
                  </Typography>
                </Box>
                <Typography variant="subtitle2" color="primary.main" sx={{ mt: 1, letterSpacing: 1, textTransform: 'uppercase' }}>
                  {user.name}
                </Typography>
                <FlightIcon sx={{ position: 'absolute', bottom: 8, right: 8, fontSize: 40, color: 'grey.0' }} /> {/* Add flight icon */}
                <IconButton sx={{ position: 'absolute', top: 8, right: 8, color: 'grey.0' }} onClick={handleClickOpen}>
                  <CloseIcon /> {/* Add remove button */}
                </IconButton>
              </CardContent>
            </Card>
          )}
        </Box>
      </Box>
       {/* Add remove card confirmation dialog */}
       <Dialog
        open={openDialog}
        onClose={handleClose}
        aria-labelledby="alert-dialog-title"
        aria-describedby="alert-dialog-description"
      >
        <DialogTitle id="alert-dialog-title">{"Remove Saved Card"}</DialogTitle>
        <DialogContent>
          <DialogContentText id="alert-dialog-description">
            Are you sure you want to remove the saved card?
          </DialogContentText>
        </DialogContent>
        <DialogActions>
          <Button onClick={handleClose} color="primary">
            Cancel
          </Button>
          <Button onClick={handleRemove} color="primary" autoFocus>
            Yes
          </Button>
        </DialogActions>
      </Dialog>
    </>
  );
};

export default CustomerDashboard;
