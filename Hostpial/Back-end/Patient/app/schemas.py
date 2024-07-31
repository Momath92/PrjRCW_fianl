from pydantic import BaseModel
from datetime import date

class PatientCreate(BaseModel):
    nom: str
    prenom: str
    date_naissance: date
    adresse: str
    telephone: str
    email: str
