import React from 'react';
import { styled } from '@mui/system';
import { Card, CardContent, Typography, Button } from '@mui/material';
import ThumbUpIcon from '@mui/icons-material/ThumbUp';
import { useNavigate } from 'react-router-dom';

const Root = styled('div')(({ theme }) => ({
  backgroundColor: theme.palette.primary.main,
  height: '100vh',
  display: 'flex',
  justifyContent: 'center',
  alignItems: 'center',
  flexDirection: 'column',
}));

const BookingConfirmed = () => {
  const navigate = useNavigate();

  return (
    <Root>
      <Card sx={{ maxWidth: 800, padding: 5 }}>
        <CardContent>
          <Typography gutterBottom variant="h1" component="div" align="center">
            Booking Confirmed!
          </Typography>
          <Typography variant="body2" color="text.secondary" align="center">
            Your booking has been successfully confirmed!
            Enjoy the movie!
          </Typography>
          <ThumbUpIcon
            sx={{
              fontSize: '950px',
              width: '100%',
              height: 'auto',
              display: 'block',
              margin: '24px auto',
              color:"#F8BB16"
            }}
          />
          <Typography variant="body2" color="text.secondary" align="center">
            We have sent the booking information to your registerd Email/Mobile number
          </Typography>

          <Button
            variant="contained"
            color="secondary"
            onClick={() => navigate('/customerMainHome')}
            sx={{
              display: 'block',
              marginLeft: 'auto',
              marginRight: 'auto',
              marginTop:'24px'
            }}
          >
            Back to Home
          </Button>
        </CardContent>
      </Card>
    </Root>
  );
};

export default BookingConfirmed;
