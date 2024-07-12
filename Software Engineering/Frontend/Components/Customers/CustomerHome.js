import React from 'react'
import NavCustomerBar from './NavCustomerBar';
import CustomerMainSection from './CustomerMainSection';
import Chat from "../ChatBot/Chat"

function CustomerHome() {
  return (
    <>
   <NavCustomerBar/>
   <CustomerMainSection/>
   <Chat/>
   
   
  
  </>
  );
}

export default CustomerHome