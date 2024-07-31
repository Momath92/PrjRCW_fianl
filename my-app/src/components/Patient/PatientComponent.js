import React, { useState, useEffect } from 'react';
import { createPatient, getPatient } from '../../services/patientService';

const PatientComponent = () => {
  const [patient, setPatient] = useState(null);
  const [newPatient, setNewPatient] = useState({
    nom: 'Doe',
    prénom: 'John',
    date_naissance: '1990-01-01',
    adresse: '123 Main St',
    téléphone: '1234567890',
    email: 'john.doe@example.com'
  });

  useEffect(() => {
    getPatient(1).then(data => setPatient(data));
  }, []);

  const handleCreatePatient = () => {
    createPatient(newPatient).then(data => setPatient(data));
  };

  return (
    <div>
      <h1>Patient Information</h1>
      {patient && (
        <div>
          <p>Name: {patient.nom} {patient.prénom}</p>
          <p>Birthdate: {patient.date_naissance}</p>
          <p>Address: {patient.adresse}</p>
          <p>Phone: {patient.téléphone}</p>
          <p>Email: {patient.email}</p>
        </div>
      )}
      <button onClick={handleCreatePatient}>Create New Patient</button>
    </div>
  );
};

export default PatientComponent;
