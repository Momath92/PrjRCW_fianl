import React, { createContext, useContext, useState } from 'react';
import axios from 'axios';

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const auth = useProvideAuth();
  return <AuthContext.Provider value={auth}>{children}</AuthContext.Provider>;
};

export const useAuth = () => {
  return useContext(AuthContext);
};

const useProvideAuth = () => {
  const [user, setUser] = useState(null);

  const login = async (username, password) => {
    const response = await axios.post('http://localhost:8000/auth/login', {
      username,
      password,
    });
    const { access_token } = response.data;
    localStorage.setItem('token', access_token);
    const user = await getUser();
    setUser(user);
  };

  const signup = async (userData) => {
    await axios.post('http://localhost:8000/auth/signup', userData);
  };

  const logout = () => {
    localStorage.removeItem('token');
    setUser(null);
  };

  const getUser = async () => {
    const token = localStorage.getItem('token');
    if (token) {
      const response = await axios.get('http://localhost:8000/auth/me', {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
      return response.data;
    }
    return null;
  };

  return {
    user,
    login,
    signup,
    logout,
  };
};
