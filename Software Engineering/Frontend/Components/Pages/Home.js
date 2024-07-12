import React from 'react';
import '../../App.css';
import MainSection from "../Home/MainSection";
import Cards from "../Home/Cards";
import Header from "../Home/Header";
import Footer from "../Home/Footer";

function Home() {

return(
    <>
    <Header/>
    <MainSection />
    <Cards/>
    <Footer/>
  </>
);
   
}

export default Home