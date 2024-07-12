import axios from "axios";
import { useState } from "react";
import { Navigate } from "react-router-dom";
import keys from "../../config/keys";

function ForgotPasswordMain() {

    const [newPassword, setNewPassword] = useState("");
    const [success, setSuccess] = useState(false);
    const [message, setMessage] = useState("");

    const handleSubmit = async (e) => {
        e.preventDefault();
        const params = new Proxy(new URLSearchParams(window.location.search), {
            get: (searchParams, prop) => searchParams.get(prop),
        });

        const token = params.token;

        try {
            const response = await axios.post(`http://${keys.localhost}:3000/api/resetPassword/`, { token: token, password: newPassword });
            setSuccess(true);
            setMessage(response.data.message);
            console.log(response.data.message);
        }
        catch (error) {
            console.log(error.data.message);
        }
    }

    return (
        <main className="fp-main">
            <section className="fp-section">
                {success ? (
                    <div className="fp-form-item">
                        <label className="fp-form-label">
                            {message}
                        </label>
                    </div>
                ) : (
                    <form className="fp-form" onSubmit={handleSubmit}>
                        <div className="fp-form-item">
                            <input className="fp-form-input" type="password" placeholder="Enter new password" onChange={(e) => { setNewPassword(e.target.value) }} required></input>
                        </div>
                        <div className="fp-form-item">
                            <input type="submit"></input>
                        </div>

                    </form>
                )}

            </section>
        </main>
    );

};

export default ForgotPasswordMain;