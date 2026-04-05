import React, { useEffect } from "react";
import { useNavigate } from "react-router-dom";

export const Private = () => {
    const navigate = useNavigate();

    useEffect(() => {
        const token = sessionStorage.getItem("token");
        // Si no hay token, lo mandamos al login de vuelta 
        if (!token) {
            navigate("/login");
        }
    }, []);

    return (
        <div>
            <h1>Área Privada 🕵️‍♂️</h1>
            <p>Si estás viendo esto, es porque tienes un token válido.</p>
        </div>
    );
};