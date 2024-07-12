import axios from "axios";
import { useEffect, useState } from "react";
import { Box, Button } from "@mui/material";
import keys from "../../config/keys";
import {
  Card,
  CardContent,
  CardMedia,
  Chip,
  Grid,
  Typography,
} from "@mui/material";

function MoviePage() {
  const [data, setData] = useState([]);
  const movieID = localStorage.getItem("movieID");
  const location = localStorage.getItem("movieLocation");

  var m;
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

  const handleBooking = () =>{
    window.location.href='/booking'
  }

  return (
    <Box
      sx={{
        backgroundColor: "primary.900",
        minHeight: "100vh",
        py: 2,
        color: "black",
      }}
    >
      {data.map((item) => {
        if (item.show_id == movieID) {
          const name = item.show_movie[0].movie_name;
          const image = item.show_movie[0].movie_image;
          const rating = item.show_movie[0].movie_rating;
          const length = item.show_movie[0].movie_length;
          const cost = item.show_rate;
          const characters = item.show_movie[0].movie_cast.map(
            (e) => e.cast_name
          );
          const genres = item.show_movie[0].movie_genres.map(
            (e) => e.genre_name
          );
          const languages = item.show_movie[0].movie_languages.map(
            (e) => e.language_name
          );
          const cast = item.show_movie[0].cast_actor.map((e) => e.actor_name);
          const cast_about = item.show_movie[0].cast_actor.map(
            (e) => e.actor_about
          );
          const theatre_name = item.show_movietheater[0].movietheater_name;
          const theatre_address =
            item.show_movietheater[0].movietheater_address;
          const screen_name = item.show_theaterscreen[0].theaterscreen_name;
          const screen_type = item.show_theaterscreen[0].theaterscreen_type;

          // return (
          //   <div key={item.show_id}>
          //     <div>{name}</div>
          //     <img src={image} alt={"NONE"} />
          //     <div>{theatre_name}</div>
          //     <div>{rating}</div>
          //     <div>{cost}</div>
          //     <div>{theatre_address}</div>
          //     <div>{screen_name}</div>
          //     <div>{screen_type}</div>
          //     <div>{characters.join(", ")}</div>
          //     <div>{genres.join(", ")}</div>
          //     <div>{languages.join(", ")}</div>
          //     <div>{cast.join(", ")}</div>
          //     <div>{cast_about.join(", ")}</div>
          //   </div>
          // );
          return (
            <Box key={item.show_id} mt={2} mx="auto" maxWidth="95%">
              <Grid container spacing={2}>
                <Grid item xs={12} md={4}>
                  <Card>
                    <CardMedia
                      component="img"
                      height="400"
                      image={image}
                      alt="Movie poster"
                    />
                    <Button
                      sx={{
                        color: "primary",
                        backgroundColor: "secondary.500",
                        width: "100%",
                        fontSize: "larger", 
                        fontStyle: "bold"
                      }}
                      onClick={handleBooking}
                    >
                      {" "}
                      BOOK TICKETS{" "}
                    </Button>
                  </Card>
                </Grid>
                <Grid item xs={12} md={8}>
                  <CardContent>
                    <Typography
                      variant="h3"
                      mb={1}
                      sx={{ color: "secondary.main", fontStyle: "bold" }}
                    >
                      {name.toUpperCase()}
                    </Typography>
                    <Typography
                      variant="h5"
                      sx={{ color: "secondary.500", fontStyle: "bold" }}
                    >
                      Rating: {rating}
                    </Typography>
                    <Typography
                      variant="h5"
                      sx={{ color: "secondary.500", fontStyle: "bold" }}
                    >
                      Duration: {length}
                    </Typography>
                    <Typography
                      variant="h5"
                      sx={{ color: "secondary.500", fontStyle: "bold" }}
                    >
                      Cost: {cost}
                    </Typography>
                    <Typography
                      variant="h5"
                      sx={{ color: "secondary.500", fontStyle: "bold" }}
                    >
                      Theatre Name: {theatre_name}
                    </Typography>
                    <Typography
                      variant="h5"
                      sx={{ color: "secondary.500", fontStyle: "bold" }}
                    >
                      Theatre Address: {theatre_address}
                    </Typography>
                    <Typography
                      variant="h5"
                      sx={{ color: "secondary.500", fontStyle: "bold" }}
                    >
                      Screen Name: {screen_name}
                    </Typography>
                    <Typography
                      variant="h5"
                      sx={{ color: "secondary.500", fontStyle: "bold" }}
                    >
                      Screen Type: {screen_type}
                    </Typography>

                    <Box
                      mt={2}
                      sx={{
                        backgroundColor: "grey.900",
                        padding: "1rem",
                        borderRadius: "0.5rem",
                      }}
                    >
                      <Typography variant="h5" sx={{ color: "secondary.500" }}>
                        Characters:
                      </Typography>
                      {characters.map((character) => (
                        <Chip
                          key={character}
                          label={character}
                          mr={1}
                          mb={1}
                          color="secondary"
                        />
                      ))}
                    </Box>

                    {/* <Box mt={2}>
                      <Typography variant="h5">Characters:</Typography>
                      {characters.map((character) => (
                        <Chip key={character} label={character} mr={1} mb={1} />
                      ))}
                    </Box> */}

                    <Box
                      mt={2}
                      sx={{
                        backgroundColor: "grey.900",
                        padding: "1rem",
                        borderRadius: "0.5rem",
                      }}
                    >
                      <Typography variant="h5" sx={{ color: "secondary.500" }}>
                        Genres:
                      </Typography>
                      {genres.map((genre) => (
                        <Chip
                          key={genre}
                          label={genre}
                          mr={1}
                          mb={1}
                          color="secondary"
                        />
                      ))}
                    </Box>
                    {/* <Box mt={2}>
                      <Typography variant="h5">Genres:</Typography>
                      {genres.map((genre) => (
                        <Chip key={genre} label={genre} mr={1} mb={1} />
                      ))}
                    </Box> */}

                    <Box
                      mt={2}
                      sx={{
                        backgroundColor: "grey.900",
                        padding: "1rem",
                        borderRadius: "0.5rem",
                      }}
                    >
                      <Typography variant="h5" sx={{ color: "secondary.500" }}>
                        Languages:
                      </Typography>
                      {languages.map((language) => (
                        <Chip
                          key={language}
                          label={language}
                          mr={1}
                          mb={1}
                          color="secondary"
                        />
                      ))}
                    </Box>

                    {/* <Box mt={2}>
                      <Typography variant="h5">Languages:</Typography>
                      {languages.map((language) => (
                        <Chip key={language} label={language} mr={1} mb={1} />
                      ))}
                    </Box> */}
                    <Box
                      mt={2}
                      sx={{
                        backgroundColor: "grey.900",
                        padding: "1rem",
                        borderRadius: "0.5rem",
                      }}
                    >
                      <Typography variant="h5" sx={{ color: "secondary.500" }}>
                        Cast:
                      </Typography>
                      {cast.map((actor, index) => (
                        <Box key={actor} mb={1}>
                          <Typography
                            variant="h6"
                            sx={{ color: "secondary.500" }}
                          >
                            {actor}: {cast_about[index]}
                          </Typography>
                        </Box>
                      ))}
                    </Box>
                  </CardContent>
                </Grid>
              </Grid>
            </Box>
          );
        }
      })}
    </Box>
  );
}
export default MoviePage;
