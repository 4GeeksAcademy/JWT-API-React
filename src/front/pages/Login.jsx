import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

export const Login = () => {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        const resp = await fetch(import.meta.env.VITE_BACKEND_URL + "/api/login", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ email, password })
        });

        if (resp.ok) {
            const data = await resp.json();
            sessionStorage.setItem("token", data.access_token); // Guardar el token
            navigate("/private"); // Redirigir a la vista privada
        } else {
            alert("Credenciales inválidas");
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="email" onChange={(e) => setEmail(e.target.value)} placeholder="Email" />
            <input type="password" onChange={(e) => setPassword(e.target.value)} placeholder="Contraseña" />
            <button type="submit">Iniciar Sesión</button>
        </form>
    );
};