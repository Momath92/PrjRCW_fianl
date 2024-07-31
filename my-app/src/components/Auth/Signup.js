// Signup.js
import React, { useState } from 'react';
import authService from '../Services/authService';

const Signup = () => {
    const [nom, setNom] = useState('');
    const [prenom, setPrenom] = useState('');
    const [date_naissance, setDateNaissance] = useState('');
    const [adresse, setAdresse] = useState('');
    const [telephone, setTelephone] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleSignup = async (e) => {
        e.preventDefault();
        try {
            await authService.register(nom, prenom, date_naissance, adresse, telephone, email, password);
            // Redirigez ou affichez un message de succès
        } catch (error) {
            console.error('Erreur lors de l\'inscription:', error);
        }
    };

    return (
        <form onSubmit={handleSignup}>
            <input type="text" placeholder="Nom" value={nom} onChange={(e) => setNom(e.target.value)} />
            <input type="text" placeholder="Prénom" value={prenom} onChange={(e) => setPrenom(e.target.value)} />
            <input type="date" placeholder="Date de Naissance" value={date_naissance} onChange={(e) => setDateNaissance(e.target.value)} />
            <input type="text" placeholder="Adresse" value={adresse} onChange={(e) => setAdresse(e.target.value)} />
            <input type="text" placeholder="Téléphone" value={telephone} onChange={(e) => setTelephone(e.target.value)} />
            <input type="email" placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} />
            <input type="password" placeholder="Mot de passe" value={password} onChange={(e) => setPassword(e.target.value)} />
            <button type="submit">S'inscrire</button>
        </form>
    );
};

export default Signup;
