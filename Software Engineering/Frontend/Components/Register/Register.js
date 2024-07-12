import React, { useState } from "react";
import "@fontsource/inter";
import axios from "axios";
import "./Register.css";
import { Button } from "../Common/Button";
import { Container, Row, Col, Form, FormGroup } from "react-bootstrap";
import { Link } from "react-router-dom";
import NavBarSimple from "../Customers/NavBarSimple.js";
import { Navigate } from "react-router-dom";
import keys from "../../config/keys";

function Register() {
  const PASSWORD_REGEX =
    /^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%]).{8,24}$/;
  const EMAIL_REGEX = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;

  const [credentials, setCredentials] = useState({
    firstName: undefined,
    lastName: undefined,
    email: undefined,
    password: undefined,
    password2: undefined,
    mobile: undefined,
  });

  const [isValidPwd, setIsValidPwd] = useState(true);
  const [isValidEmail, setIsValidEmail] = useState(true);
  const [isValidConfirmPwd, setIsValidConfPwd] = useState(true);
  const [err, setErrMsg] = useState("");
  const [regSuccess, setRegSuccess] = useState(false);

  const handleClick = (e) => {
    e.preventDefault();
    axios
      .post(`http://${keys.localhost}:3000/api/users/register`, {
        first_name: credentials.firstName,
        last_name: credentials.lastName,
        password: credentials.password,
        email: credentials.email,
        password2: credentials.password2,
        mobile: credentials.mobile,
      })
      .then((response) => {
        setRegSuccess(true);
      })
      .catch((error) => {
        if (error.response.status !== 200) {
          setErrMsg(error.response.data);
        }
      });
    console.log(err[Object.keys(err)[0]]);
    setTimeout(() => {
      setErrMsg("");
    }, 3000);
  };

  const handleInputChange = (e) => {
    const id = e.target.id;
    if (id === "firstName") {
      setCredentials({
        firstName: e.target.value,
        lastName: credentials.lastName,
        email: credentials.email,
        password: credentials.password,
        password2: credentials.password2,
        mobile: credentials.mobile,
      });
    }
    if (id === "lastName") {
      setCredentials({
        firstName: credentials.firstName,
        lastName: e.target.value,
        email: credentials.email,
        password: credentials.password,
        password2: credentials.password2,
        mobile: credentials.mobile,
      });
    }
    if (id === "email") {
      const eml = EMAIL_REGEX.test(e.target.value);
      if (eml || e.target.value === "") {
        setCredentials({
          firstName: credentials.firstName,
          lastName: credentials.lastName,
          email: e.target.value,
          password: credentials.password,
          password2: credentials.password2,
          mobile: credentials.mobile,
        });
        setIsValidEmail(true);
      } else {
        setIsValidEmail(false);
      }
    }
    if (id === "password") {
      const pwd = PASSWORD_REGEX.test(e.target.value);
      if (pwd || e.target.value === "") {
        setCredentials({
          firstName: credentials.firstName,
          lastName: credentials.lastName,
          email: credentials.email,
          password: e.target.value,
          password2: credentials.password2,
          mobile: credentials.mobile,
        });
        setIsValidPwd(true);
      } else {
        setIsValidPwd(false);
      }
    }
    if (id === "confirmPassword") {
      if (e.target.value === credentials.password || e.target.value === "") {
        setCredentials({
          firstName: credentials.firstName,
          lastName: credentials.lastName,
          email: credentials.email,
          password: credentials.password,
          password2: e.target.value,
          mobile: credentials.mobile,
        });
        setIsValidConfPwd(true);
      } else {
        setIsValidConfPwd(false);
      }
    }
    if (id === "mobile") {
      setCredentials({
        firstName: credentials.firstName,
        lastName: credentials.lastName,
        email: credentials.email,
        password: credentials.password,
        password2: credentials.password2,
        mobile: e.target.value,
      });
    }
  };

  return (
    <>
      <main className="c-lg-main">
        {regSuccess ? (
          <>
            <Navigate replace to="/login" />
          </>
        ) : (
          <>
            <NavBarSimple />
            <div className="card-wrapper">
              <div className="card">
                <h1
                  className="text-2xl font-bold text-gray-800 sm:ml-3 ml-0 my-3"
                  style={{ color: "#F8BB16" }}
                >
                  Register
                </h1>
                <Form>
                  <p
                    className={
                      err[Object.keys(err)[0]] ? "errorMsg" : "offscreen"
                    }
                  >
                    {err[Object.keys(err)[0]]}
                  </p>
                  {/* <label htmlFor="firstname">First Name</label> */}
                  <input
                    type="text"
                    className="field"
                    placeholder="Enter First Name"
                    id="firstName"
                    autoComplete="off"
                    onChange={(e) => {
                      handleInputChange(e);
                    }}
                    required
                  />
                  {/* <label htmlFor="lastname">Last Name</label> */}
                  <input
                    type="text"
                    className="field"
                    placeholder="Enter Last Name"
                    id="lastName"
                    autoComplete="off"
                    onChange={(e) => {
                      handleInputChange(e);
                    }}
                    required
                  />

                  {/* <label htmlFor="email">Email</label> */}
                  <input
                    type="text"
                    className="field"
                    placeholder="Enter Email"
                    id="email"
                    autoComplete="off"
                    onChange={(e) => {
                      handleInputChange(e);
                    }}
                    required
                  />
                  <p
                    id="errNote"
                    className={isValidEmail ? "offscreen" : "instructions"}
                  >
                    INVALID EMAIL!!!
                  </p>

                  {/* <label htmlFor="password">Password</label> */}
                  <input
                    type="password"
                    className="field"
                    placeholder="Enter Password"
                    id="password"
                    autoComplete="off"
                    onChange={(e) => {
                      handleInputChange(e);
                    }}
                    onFocus={(e) => {
                      handleInputChange(e);
                    }}
                    required
                  />
                  <p
                    id="errNote"
                    className={isValidPwd ? "offscreen" : "instructions"}
                  >
                    8 to 24 characters.
                    <br />
                    Must include uppercase and lowercase letters, a number and a
                    special character.
                    <br />
                    Allowed special characters:{" "}
                    <span aria-label="exclamation mark">!</span>{" "}
                    <span aria-label="at symbol">@</span>{" "}
                    <span aria-label="hashtag">#</span>{" "}
                    <span aria-label="dollar sign">$</span>{" "}
                    <span aria-label="percent">%</span>
                  </p>

                  {/* <label htmlFor="confirmPassword">Confirm Password</label> */}
                  <input
                    type="password"
                    className="field"
                    placeholder="ReEnter Password"
                    id="confirmPassword"
                    autoComplete="off"
                    onChange={(e) => {
                      handleInputChange(e);
                    }}
                    onFocus={(e) => {
                      handleInputChange(e);
                    }}
                    required
                  />
                  <p
                    id="errNote"
                    className={isValidConfirmPwd ? "offscreen" : "instructions"}
                  >
                    PASSWORDS DON'T MATCH!!!
                  </p>

                  {/* <label htmlFor="mobile">Enter Mobile Number</label> */}
                  <input
                    type="text"
                    className="field"
                    placeholder="Mobile Number"
                    id="mobile"
                    autoComplete="off"
                    onChange={(e) => {
                      handleInputChange(e);
                    }}
                    required
                  />

                  <div
                    style={{
                      display: "flex",
                      justifyContent: "center",
                      alignItems: "center",
                    }}
                  >
                    <Button
                      className="btn secondary__btn auth__btn"
                      type="submit"
                      id="reg-submit"
                      buttonstyle="btn--outline"
                      buttonsize="btn--large"
                      onClick={handleClick}
                    >
                      Submit
                    </Button>
                  </div>
                </Form>
              </div>
            </div>
          </>
        )}
      </main>
    </>
  );
}

export default Register;
