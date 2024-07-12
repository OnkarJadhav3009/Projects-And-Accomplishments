import { useState } from "react";
import "./ForgotPassword.css"
import axios from "axios";
import { Button } from "react-bootstrap";
import { Link, Navigate } from "react-router-dom";
import PhoneInput from 'react-phone-number-input'
import 'react-phone-number-input/style.css'
import keys from "../../config/keys";



function ForgotPassword() {

    const [email, setEmail] = useState("");
    const [mobile, setMobile] = useState();
    const [isEmail, setIsEmail] = useState(true)
    const [success, setSuccess] = useState(false);
    const [message, setMessage] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (isEmail) {
            try {
                const response = await axios.post(`http://${keys.localhost}:3000/api/email/forgotpassword`, { email: email });
                setSuccess(true);
                setMessage(response.data.message);
                console.log(response.data.message);
            }
            catch (error) {
                console.log(error.data.message);
            }
        } else {
            // console.log(mobile);
            try {
                const response = await axios.post(`http://${keys.localhost}:3000/api/mobile/forgotpassword`, { mobile: mobile });
                setSuccess(true);
                setMessage(response.data.message);
                console.log(response.data.message);
            }
            catch (error) {
                console.log(error.data.message);
            }
        }

    }

    return (
        <main className="fp-main">
            <section className="fp-section">
                {
                    success ? (
                        <form className="fp-form">
                            <div className="fp-form-item">
                                <label htmlFor="text" className="fp-form-label">
                                    {message} <br></br>
                                    Please check your spam folder if not found in your inbox!
                                </label>
                                <br></br>
                                <a className="fp-link" href="../login">GO BACK TO LOGIN?</a>
                            </div>
                        </form>
                    ) : (
                        <>
                            {isEmail ?
                                (
                                    <form className="fp-form" onSubmit={handleSubmit}>
                                        <div className="fp-form-item">
                                            <label htmlFor="email" className="fp-form-label">Please enter your email id to recieve a link for resetting the password</label>
                                            <input className="fp-form-input" type="email" placeholder="Enter Email" onChange={(e) => { setEmail(e.target.value) }} required></input>
                                        </div>
                                        <div className="fp-form-item">
                                            <Link className="fp-link" onClick={() => { setIsEmail(false) }}><p >USE MOBILE?</p></Link>
                                        </div>
                                        <div className="fp-form-item">
                                            <input className="fp-submit" type="submit"></input>
                                        </div>
                                    </form>
                                ) : (
                                    <form className="fp-form" onSubmit={handleSubmit}>
                                        <div className="fp-form-item">
                                            <label htmlFor="email" className="fp-form-label">Please enter your mobile number to recieve a link for resetting the password</label>
                                            <PhoneInput placeholder="Enter phone number"
                                                value={mobile}
                                                onChange={setMobile} />
                                        </div>
                                        <div className="fp-form-item">
                                            <Link className="fp-link" onClick={() => { setIsEmail(true) }}><p >USE EMAIL?</p></Link>
                                        </div>
                                        <div className="fp-form-item">
                                            <input className="fp-submit" type="submit"></input>
                                        </div>
                                    </form>
                                )}
                        </>
                    )
                }

            </section>
        </main>
    );
}

export default ForgotPassword;