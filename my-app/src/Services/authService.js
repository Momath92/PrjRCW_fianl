// authService.js
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000'; // Remplacez par l'URL de votre API

// Inscription de l'utilisateur
const register = (nom, prenom, date_naissance, adresse, telephone, email, password) => {
    return axios.post(`${API_URL}/register`, {
        nom,
        prenom,
        date_naissance,
        adresse,
        telephone,
        email,
        password
    });
};

// Connexion de l'utilisateur
const login = (email, password) => {
    return axios.post(`${API_URL}/login`, {
        email,
        password
    }).then((response) => {
        if (response.data.accessToken) {
            localStorage.setItem('user', JSON.stringify(response.data));
        }
        return response.data;
    });
};

// Déconnexion de l'utilisateur
const logout = () => {
    localStorage.removeItem('user');
};

export default {
    register,
    login,
    logout
};
