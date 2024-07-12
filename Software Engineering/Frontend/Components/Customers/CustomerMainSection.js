import { useEffect, useState } from "react";
import Box from "@mui/material/Box";
import axios from "axios";
import { Hidden, ThemeProvider } from "@mui/material";
import { Slider, Checkbox, FormControlLabel, Button } from "@mui/material";
import HeroCarousel from "./HeroCarousel";
import EntertainmentCardSlider from "../Entertainment/EntertainmentCardSlider";
import RecommendedMovieSlider from "../RecommendedMovies/RecommendedMovieSlider";
import "./CustomerMainSection.css";
import keys from "../../config/keys";

function CustomerMainSection({ searchText, location }) {
  const [dataSuccess, setDataSuccess] = useState(false);
  const [data, setData] = useState(null);

  const today = "04-05-2023";
  const tomorrow = "04-17-2023";

  const [startDate, setStartDate] = useState(null);
  const [endDate, setEndDate] = useState(null);

  useEffect(() => {
    axios
      .get(`http://${keys.localhost}:3000/api/shows/search/`, {
        params: {
          location: location,
          startdate: startDate,
          enddate: endDate,
          minprice: range[0],
          maxprice: range[1],
        },
      })
      .then((response) => {
        setData(response.data.shows);
        setDataSuccess(true);
      });
  }, [searchText]);

  const [range, setRange] = useState([0, 10]);

  const handleChange = async (e) => {
    setRange(e.target.value);
  };

  const [checked1, setChecked1] = useState(false);

  const handleCheckbox1Change = async () => {
    setChecked1(!checked1);
  };

  const [checked2, setChecked2] = useState(false);

  const handleCheckbox2Change = async () => {
    setChecked2(!checked2);
  };

  const handleApply = () => {
    if (checked1 && !checked2) {
      setStartDate(today);
      setEndDate(today);
    } else if (!checked1 && checked2) {
      setStartDate(tomorrow);
      setEndDate(tomorrow);
    } else {
      setStartDate(today);
      setEndDate(tomorrow);
    }
    const response = axios.get(
      `http://${keys.localhost}/api/shows/search/`,
      {
        params: {
          location: location,
          startdate: startDate,
          enddate: endDate,
          minprice: range[0],
          maxprice: range[1],
        },
      }
    );

    setData(response.data.shows);
  };

  return (
    <div className="mainsection">
      {dataSuccess && searchText && location ? (
        <div className="search-results">
          <div className="search-filters">
            <div style={{ backgroundColor: "primary", padding: "1rem" }}>
              <FormControlLabel
                control={
                  <Checkbox
                    checked={checked1}
                    onChange={handleCheckbox1Change}
                    sx={{
                      "& .MuiSvgIcon-root": { fontSize: 28, color: "yellow" },
                    }}
                  />
                }
                label="TODAY"
              />
            </div>
            <div style={{ backgroundColor: "primary", padding: "1rem" }}>
              <FormControlLabel
                control={
                  <Checkbox
                    checked={checked2}
                    onChange={handleCheckbox2Change}
                    sx={{
                      "& .MuiSvgIcon-root": { fontSize: 28, color: "yellow" },
                    }}
                  />
                }
                label="TOMORROW"
              />
            </div>
            <div style={{ backgroundColor: "primary", padding: "1rem" }}>
              <p style={{ fontSize: "large" }}>PRICE</p>
              <Slider
                value={range}
                onChange={handleChange}
                valueLabelDisplay="auto"
                marks
                min={0}
                max={30}
                step={5}
                disableSwap
                color="secondary"
              />
            </div>
            <div style={{ backgroundColor: "primary", padding: "1rem" }}>
              <button
                style={{
                  color: "black",
                  background: "#F8BB16",
                  width: "200px",
                  height: "50px",
                }}
                onClick={handleApply}
              >
                APPLY
              </button>
            </div>
          </div>
          <br></br>
          <br></br>
          {data.map((item) => {
            return (
              <Box
                className="movie-info"
                sx={{
                  backgroundColor: "primary",
                  padding: "1rem",
                  "&:hover": {
                    backgroundColor: "#F8BB16",
                    color: "#303030",
                    cursor: "pointer",
                    overflow: "hidden",
                    overflowY: "auto"
                  },
                }}
                key={item.show_id}
              >
                {item.show_movie[0].movie_name
                  .toLowerCase()
                  .includes(searchText.toLowerCase()) ? (
                  <a
                    href="../moviePage"
                    onClick={() => {
                      localStorage.setItem("movieID", item.show_id);
                      localStorage.setItem("movieLocation", location);
                    }}
                    key={item.show_id}
                  >
                    <div key={item.show_id} style={{ display: "flex", backgroud: "white" }}>
                      <p key={item.show_id} style={{ fontStyle: "oblique", fontWeight: "bold" }}>
                        {item.show_movie[0].movie_name.toUpperCase()}
                      </p>
                    </div>
                    <br></br>
                  </a>
                ) : (
                  <div  style={{ color: "primary" }}></div>
                )}
              </Box>
            );
          })}
        </div>
      ) : (
        <>
          <HeroCarousel />
          <div className="container">
            <h1
              align="left"
              className="text-2xl font-bold text-gray-800 sm:ml-3 ml-0 my-3"
              style={{ color: "#F8BB16" }}
            >
              THE BEST OF ENTERTAINMENT
            </h1>
            <EntertainmentCardSlider />
          </div>

          <div className="container">
            <h1
              align="left"
              className="text-2xl font-bold text-gray-800 sm:ml-3 ml-0 my-3"
              style={{ color: "#F8BB16" }}
            >
              RECOMMENDED MOVIES
            </h1>
            <RecommendedMovieSlider/>
          </div>
        </>
      )}
    </div>
  );
}

export default CustomerMainSection;