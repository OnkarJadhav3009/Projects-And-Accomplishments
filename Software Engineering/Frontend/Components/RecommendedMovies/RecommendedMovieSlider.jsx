import React from "react";
import Slider from "react-slick";
import Modal from '@mui/material/Modal';
import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import keys from "../../config/keys.js";
import { Typography, Button } from '@mui/material';
import Box from '@mui/material/Box';
import {
  CardActions,
  Card,
  CardContent,
  Rating,
  Paper,
} from "@mui/material";

const style = {
  position: 'absolute' ,
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: 400,
  bgcolor: 'background.paper',
  border: '2px solid #000',
  boxShadow: 24,
  p: 4,
};


const RecommendedMovieCard = (props) => {
  return (
    <>
      <div className="w-full h-30 px-2" >
        <img
          className="w-full h-full rounded-lg"
          src={props.src}
          alt="entertainment"
        />
      </div>
    </>
  );
};

const RecommendedMovieSlider = () => {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [movies, setMovies] = useState([]);
  const [movieLength, setMovieLength] = useState([]);
  const [movieRating, setMovieRating] = useState([]);
  const [movieGenre, setMovieGenre] = useState([]);
  const [movieReleaseDate, setReleaseDate] = useState([])
  const [movieName,setMovieName] = useState([]);
  const [value, setValue] = useState(0);
  const [ratingValue, setRatingValue] = useState(0);

  const handleRatingChange = (event, newValue) => {
    setRatingValue(newValue);
  };

  const handleCloseModal = () => {
    setIsModalOpen(false);
  };

  const handleImageClick = (index) => {
    setValue(index);
    setIsModalOpen(true);
  };

  const handleSliderChange = (event, newValue) => {
    setValue(newValue);
  };

  const handleSliderChangeCommitted = (event, newValue) => {
    console.log("Selected index:", newValue);
  };
  
  useEffect(() => {
    axios.get(`http://${keys.localhost}:3000/api/movies/movie?enddate=2023-04-26&startdate=2023-04-23`)
      .then(response => {
        const movies = response.data;
        const movieImages = movies.movies.map(movie => movie.movie_image);
        const movieTitles = movies.movies.map(movie => movie.movie_name);
        const movieLength = movies.movies.map(movie => movie.movie_length);
        const movieRating = movies.movies.map(movie => movie.movie_rating.map(rate => rate.rating_name));
        const movieGenre = movies.movies.map(movie => movie.movie_genres.map(genre => genre.genre_name).join(", "));
        const releaseDate = movies.movies.map(movie => movie.movie_release_date);
        const updated_dates = releaseDate.map((date) => {
          const d = new Date(date);
          const month = d.toLocaleString('default', { month: 'short' });
          const day = d.getDate();
          const year = d.getFullYear();
          return `${month} ${day}, ${year}`;
        });

        setMovies(movieImages);
        setMovieName(movieTitles);
        setMovieLength(movieLength);
        setMovieRating(movieRating);
        setMovieGenre(movieGenre);
        setReleaseDate(updated_dates);
      })
      .catch(error => {
        console.error(error);
      });
  },[]);

  const settings = {
    infinite: false,
    autoplay: false,
    slidesToShow: 5,
    slidesToScroll: 4,
    initialSlide: 0,
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 2,
        },
      },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 1,
          initialSlide: 1,
        },
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 1,
        },
      },
    ],
  };

  return (
    <>
    <Slider
  {...settings}
  value={value}
  onChange={handleSliderChange}
  onChangeCommitted={handleSliderChangeCommitted}
  min={0}
  max={movies.length - 1}
  step={1}
  marks={true}
>

  {movies.map((image, index) => (
    <div key={index} onClick={() => handleImageClick(index)}>
      <RecommendedMovieCard src={image} alt={`movies ${index + 1}`} width={"30%"}
          height={"50%"}
          objectFit="cover"/>
    </div>
  ))}
  {
    <Modal open={isModalOpen} onClose={handleCloseModal}>
      <div>
      <Paper
  sx={{
    position: "absolute",
    top: "50%",
    left: "50%",
    transform: "translate(-50%, -50%)",
    width: "70%",
    bgcolor: "#F8BB16",
    color: "#606060",
    boxShadow: 24,
    p: 4,
  }}
>
  <Card
    raised
    sx={{
      display: "flex",
      padding: "5px",
      alignItems: "center",
      bgcolor: "#1E1E1E",
      color: "#FFFF00",
    }}
  >
   <CardContent sx={{ display: 'flex', alignItems: 'center', bgcolor: '#1E1E1E', padding: '24px' }}>
  <img src={movies[value]} alt={`movies ${value + 1}`} style={{ maxWidth: '200px', maxHeight: '300px', objectFit: 'contain' }} />

  <Box sx={{ display: 'flex', flexDirection: 'column', ml: 3, flexGrow: 1 }}>
    <Box sx={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
      <Typography variant="h4" component="h2" gutterBottom style={{ color: '#F8BB16', fontWeight: 'bold' }}>
        {movieName[value]}
      </Typography>

    </Box>
    <Typography variant="h6" component="h6" gutterBottom style={{ color: '#F8BB16', fontWeight: 'bold', display: 'flex', alignItems: 'center' }}>
  <span style={{ marginRight: '1rem' }}>{movieReleaseDate[value]}</span>
  <Rating 
    name="movie-rating"
    value={ratingValue}
    onChange={handleRatingChange}
  />
</Typography>

    
    <Typography variant="h6" gutterBottom style={{ color: 'white', marginTop: '12px' }}>
      {movieLength[value]} | {movieRating[value]} | {movieGenre[value]}
    </Typography>

    <Button size="small" variant="contained" color="error" sx={{ mt: 3, width: '200px', alignSelf: 'flex-start', fontWeight:'bold' }} component={Link}
  to="/book-tickets">
     Book Tickets
    </Button>

  </Box>
</CardContent>


  </Card>
</Paper>

    
    
    </div>
  </Modal>
  }
</Slider>
      
    </>
  );
};
export default RecommendedMovieSlider;
