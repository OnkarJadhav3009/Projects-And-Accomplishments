import { useState, useEffect } from "react";
import { GoogleLogin } from "react-google-login";
import FacebookLogin from "react-facebook-login";
import NavBarSimple from "../Customers/NavBarSimple.js";
import { Form, FormGroup } from "react-bootstrap";
import { Navigate } from "react-router-dom";
import CustomerHomeLanding from "../Customers/CustomerHomeLanding";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import { Link } from "react-router-dom";
import keys from "../../config/keys.js";
import "./Login.css";
import { FaGoogle } from "react-icons/fa";
import { Button } from "../Common/Button";
import "@fontsource/inter";

const Login = () => {
  const [user, setUser] = useState("");
  const [pwd, setPwd] = useState("");
  const [errMsg, setErrMsg] = useState("");
  const [success, setSuccess] = useState(false);
  const [userName, setUserName] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    console.log(userName);
    localStorage.setItem("username", userName);
  }, [userName]);

  const handleUsernameChange = (event) => {
    setUser(event.target.value);
  };

  const handlePasswordChange = (event) => {
    setPwd(event.target.value);
  };

  const clientId =
    "973282407747-5e4l7ut9st7c6aqace5d1avdjcjp8o3s.apps.googleusercontent.com";

  const onSuccess = async (res) => {
    console.log(res);
    try {
      const google_response = await axios.post(
        `http://${keys.localhost}:3000/api/users/google_login`,
        {
          idToken: res.tokenObj.id_token,
        }
      );
      setSuccess(true);
      console.log("Login Success! User:", res.profileObj.name);
      setUserName(res.profileObj.name);
      console.log(google_response);
    } catch (error) {
      setErrMsg(error.data.mesage);
      setTimeout(() => {
        setErrMsg("");
      }, 3000);
      console.log("Login Failed! res=", error);
    }
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    console.log("Got in the server");
    try {
      const response = await axios.post(
        `http://${keys.localhost}:3000/api/users/login`,
        {
          emailormobile: user,
          password: pwd,
        }
      );
      setSuccess(true);
      console.log(response.data.token);
      console.log(response.data.user._id);
      setUserName(response.data.user.first_name);
    } catch (error) {
      setErrMsg(error.response.data);
      setTimeout(() => {
        setErrMsg("");
      }, 3000);
      console.log(error.response.data);
    }
  };

  // async function responseFacebook(response) {
  //   try {
  //     const facebook_response = await axios.post("/api/users/facebook_login", {
  //       access_token: response.accessToken,
  //     });
  //     console.log(facebook_response);
  //   } catch (error) {
  //     setErrMsg(error.data.mesage);
  //     setTimeout(() => {
  //       setErrMsg("");
  //     }, 3000);
  //     console.log(error.response);
  //   }
  // }

  const handleFacebookLogin = async () => {
    try {
      // Redirect to the Facebook Login page
      console.log("checkkk: ", keys.localhost);
      window.location.href = `http://${keys.localhost}:3000/facebook_login`;
    } catch (error) {
      console.log(error);
    }

    try {
      const response = await axios.post(
        `http://${keys.localhost}:3000/facebook_login`,
        {
          access_token: "FACEBOOK_ACCESS_TOKEN",
        }
      );
      setUser(response.data);
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <>
      {/* <NavCustomerBar/> */}

      <main className="c-lg-main">
        {success ? (
          <>
            <Navigate to="../customerMainHome"></Navigate>
          </>
        ) : (
          <>
            <NavBarSimple />

            <div className="card-wrapper" sx={{ bgcolor: "black" }}>
              <div className="card">
                <h1
                  className="text-2xl font-bold text-gray-800 sm:ml-3 ml-0 my-3"
                  style={{ color: "#F8BB16" }}
                >
                  Login
                </h1>

                <Form onSubmit={handleSubmit}>
                  <p className="error" htmlFor="error">
                    {errMsg[Object.keys(errMsg)[0]]}
                  </p>

                  {/* <label className='lg-label' htmlFor="email">Email</label> */}
                  <input
                    type="text"
                    className="field"
                    placeholder="Enter email"
                    id="username"
                    autoComplete="off"
                    onChange={handleUsernameChange}
                    value={user}
                    required
                  />

                  {/* <label className='lg-label' htmlFor="password">Password</label> */}
                  <input
                    type="password"
                    className="field"
                    placeholder="Enter password"
                    id="password"
                    onChange={handlePasswordChange}
                    value={pwd}
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
                      buttonstyle="btn--outline"
                      buttonsize="btn--large"
                      onClick={handleSubmit}
                    >
                      Login
                    </Button>
                  </div>
                </Form>
                <p>
                  Don't have an account? <Link to="/register"> Create</Link>
                </p>
                <Link to="../forgotPassword">
                  <p>Forgot Password ?</p>
                </Link>
                <FormGroup>
                  <div className="btn_secondary__btn_auth__btn">
                    <GoogleLogin
                      clientId={clientId}
                      buttonText="Login with Google"
                      onSuccess={onSuccess}
                      cookiePolicy={"single_host_origin"}
                      isSignedIn={true}
                    ></GoogleLogin>

                    {/* <FacebookLogin
                      appId="1829736540733671"
                      buttonText="Login with FB"
                      autoLoad={false}
                      fields="name,email,picture"
                      callback={responseFacebook}
                    /> */}
                    <div
                      style={{
                        color: "lightblue",
                        background: "darkblue",
                        width: "100%",
                        height: "100%",
                        textAlign: "centre",
                        display: "flex",
                        flexDirection: "column",
                        padding: "1rem",
                      }}
                    >
                      <button onClick={handleFacebookLogin}>
                        Login with Facebook
                      </button>
                    </div>
                  </div>
                </FormGroup>
              </div>
            </div>
          </>
        )}
      </main>
    </>
  );
};

export default Login;
