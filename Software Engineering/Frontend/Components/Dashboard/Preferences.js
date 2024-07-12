import React, { useState } from 'react';
import {
  Box,
  Card,
  CardContent,
  CardHeader,
  Typography,
  Divider,
  IconButton,
  TextField,
  Button,
} from '@mui/material';
import EditIcon from '@mui/icons-material/Edit';
import SaveIcon from '@mui/icons-material/Save';
import CancelIcon from '@mui/icons-material/Cancel';
import { useNavigate } from 'react-router-dom';

const Preferences = () => {
  const [phoneNumber, setPhoneNumber] = useState('123-456-7890');
  const [emailAddress, setEmailAddress] = useState('johndoe@gmail.com');
  const [editMode, setEditMode] = useState(false);

  const navigate = useNavigate();

  const toggleEditMode = () => {
    setEditMode(!editMode);
  };

  const handleSave = () => {
    // Save the changes to the backend and update the user's preferences
    setEditMode(false);
  };

  const handleCancel = () => {
    // Reset the fields to their initial values
    setEditMode(false);
  };

  const handleReturnHome = () => {
    navigate('/customer-dashboard');
  };

  return (
    <Box
      sx={{
        width: '100vw',
        height: '100vh',
        backgroundColor: 'primary.300',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
      }}
    >
      <Card
        sx={{
          width: { xs: '90%', sm: '60%', md: '40%', lg: '30%' },
        }}
      >
        <CardHeader
          title="Preferences"
          subheader="Update your preferences"
          action={
            <IconButton onClick={toggleEditMode}>
              <EditIcon />
            </IconButton>
          }
        />
        <Divider />
        <CardContent>
          <Typography variant="h6">Phone Number</Typography>
          <TextField
            value={phoneNumber}
            onChange={(e) => setPhoneNumber(e.target.value)}
            disabled={!editMode}
            fullWidth
          />
          <Typography variant="h6" style={{ marginTop: 16 }}>
            Email Address
          </Typography>
          <TextField
            value={emailAddress}
            onChange={(e) => setEmailAddress(e.target.value)}
            disabled={!editMode}
            fullWidth
          />
          {editMode && (
            <Box mt={2} display="flex" justifyContent="flex-end">
              <Button onClick={handleCancel} color="secondary">
                <CancelIcon />
                Cancel
              </Button>
              <Button onClick={handleSave} color="primary">
                <SaveIcon />
                Save
              </Button>
            </Box>
          )}
          <Button
        variant="contained"
        color="primary"
        onClick={handleReturnHome}
        style={{ marginTop: 16 }}
      >
        Return to profile
      </Button>
        </CardContent>
      </Card>
    </Box>
  );
};

export default Preferences;