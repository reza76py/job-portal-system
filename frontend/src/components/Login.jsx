import React, { useState } from "react";
import axios from "axios";

const Login = ({ setAuthToken }) => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async () => {
    try {
      const response = await axios.post("http://127.0.0.1:8000/api/token/", {
        email,
        password
      });

      const token = response.data.access;
      localStorage.setItem("token", token);  // ✅ Save token in localStorage
      setAuthToken(token);  // ✅ Update token state in App.js (if applicable)
      alert("Login successful!");
      window.location.href = "/";  // Redirect to home/jobs page
    } catch (error) {
      console.error("Login error:", error);
      alert("Invalid credentials");
    }
  };

  return (
    <div>
      <h2>Login</h2>
      <input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} />
      <input type="password" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
      <button onClick={handleLogin}>Login</button>
    </div>
  );
};

export default Login;
