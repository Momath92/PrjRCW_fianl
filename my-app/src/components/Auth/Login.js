// Login.js
import React, { useState } from 'react';
import authService from '../Services/authService';

const Login = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleLogin = async (e) => {
        e.preventDefault();
        try {
            await authService.login(email, password);
            // Redirigez ou affichez un message de succès
        } catch (error) {
            console.error('Erreur lors de la connexion:', error);
        }
    };

    return (
        <form onSubmit={handleLogin}>
            <input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} />
            <input type="password" placeholder="Mot de passe" value={password} onChange={(e) => setPassword(e.target.value)} />
            <button type="submit">Se connecter</button>
        </form>
    );
};

export default Login;
