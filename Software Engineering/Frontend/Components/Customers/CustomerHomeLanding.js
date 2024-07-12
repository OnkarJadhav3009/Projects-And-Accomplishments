import React from "react";
import CustomerMainSection from "./CustomerMainSection";
import NavCustomerMainBar from "./NavCustomerMainBar";
import SupportEngine from "../SupportEngine";

function CustomerHomeLanding({ userName }) {
  const { render, searchText, location } = NavCustomerMainBar(userName);

  return (
    <div>
      <div>{render}</div>
      <div>
        <CustomerMainSection searchText={searchText} location={location}/>
        <SupportEngine/>
      </div>
    </div>
  );
}

export default CustomerHomeLanding;