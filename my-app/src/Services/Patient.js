import axios from 'axios';

const API_URL = 'http://localhost:8000';

export const createPatient = async (patientData) => {
  const response = await axios.post(`${API_URL}/patients`, patientData);
  return response.data;
};

export const getPatient = async (patientId) => {
  const response = await axios.get(`${API_URL}/patients/${patientId}`);
  return response.data;
};
