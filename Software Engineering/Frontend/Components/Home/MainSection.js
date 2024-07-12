import React from 'react';
import '../../App.css';
import { Button } from '../Common/Button';
import './MainSection.css';
import { Link } from 'react-router-dom';
import SupportEngine from "../SupportEngine"

function MainSection() {
  return (

    <div className='hero-container'>
      <video src='/videos/video2.mp4' autoPlay loop muted />
      <h2>ADVENTURE OF THE BIG SCREEN AWAITS</h2>
      <p>What are you waiting for?</p>
      <div className='hero-btns'>
        <Button type = 'button'
          className='btns'
          buttonStyle='btn--outline'
          buttonSize='btn--large'
          url = "./register"
          >
          GET STARTED
        </Button>
        <Button type = 'button'
          className='btns'
          buttonStyle='btn--primary'
          buttonSize='btn--large'
          url = "./login"
        >
           BOOK TICKETS 
          
        </Button>
      </div>
    </div>
  );
}

export default MainSection