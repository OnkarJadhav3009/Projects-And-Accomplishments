import React, { useEffect, useState } from "react";
import "./styles/booking.css";
import MovieSelector from "./MovieSelector";
import SeatAvailability from "./SeatAvailability";
import SeatMatrix from "./SeatMatrix";
import PriceCalculator from "./PriceCalculator";
import GithubLogo from "./GithubLogo";
import axios from "axios";
import MovieContext from "./contexts/MovieContext";
import keys from "../../config/keys";
import NavBarSimple from "../Customers/NavBarSimple";

const Booking = () => {
  const movieID = localStorage.getItem("movieID");
  const location = localStorage.getItem("movieLocation");
  const [data, setData] = useState([]);

  useEffect(() => {
    axios
      .get(`http://${keys.localhost}:3000/api/shows/search/`, {
        params: {
          location: location,
        },
      })
      .then((response) => {
        setData(response.data.shows);
      });
  }, []);

  const filteredData = data.map((item) => {
    if (movieID === item.show_id) {
      return item;
    } else {
      return null;
    }
  });
  var movie = {};
  var rate = 0;
  var movieName = "";
  filteredData.forEach((element) => {
    if (element) {
      movie = element;
      rate = movie.show_rate;
      movieName = movie.show_movie[0].movie_name;
    }
  });

  const [movies, EditMovies] = useState({
    movieNames: {
      movieName: 10,
    },
    moviePrice: 10,
    totalSeats: 0,
    seatNumbers: [],
  });

  return (
    <>
      <NavBarSimple></NavBarSimple>
      <div className="main container">
        <MovieContext.Provider value={{ movies, changeState: EditMovies }}>
          <div>
            <p style={{ fontSize: "larger", fontStyle: "bold" }}>
              {movieName.toUpperCase()}
            </p>
          </div>
          <div>
            <GithubLogo />
          </div>
          <div>
            <SeatMatrix />
          </div>
          <div>
            <PriceCalculator />
          </div>
          <div>
            <SeatAvailability />
          </div>
        </MovieContext.Provider>
      </div>
    </>
  );
};

export default Booking;
