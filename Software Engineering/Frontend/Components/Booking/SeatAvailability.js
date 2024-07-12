import React from "react";
import Seat from "./Seat";
import './styles/seatAvailability.css'


const SeatAvailability = () => {
  return (
    <div className="seatAvailability-container">
      <div className="seatAvailability-header">Seat Availability</div>
      <div className="row mb-3">
        Unoccupied: <Seat seatColor="seat-red" />{" "}
        <span className="ml-3">Occupied: </span>
        <Seat seatColor="seat-white" />
      </div>
    </div>
  );
};

export default SeatAvailability;
