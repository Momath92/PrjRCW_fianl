# from sqlalchemy import Column, Integer, String, Date
# from .database import Base

# class Patient(Base):
#     __tablename__ = "patients"

#     id = Column(Integer, primary_key=True, index=True, autoincrement=True)
#     nom = Column(String, index=True)
#     prenom = Column(String, index=True)
#     date_naissance = Column(Date)
#     adresse = Column(String)
#     telephone = Column(String)
#     email = Column(String, unique=True, index=True)
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from contextlib import contextmanager
import snowflake.connector

app = FastAPI()

# Configuration de la connexion Snowflake
SNOWFLAKE_USER = 'MOMATH92'
SNOWFLAKE_PASSWORD = 'Rassoulle92'
SNOWFLAKE_ACCOUNT = 'mtjxohy-wp28902'
SNOWFLAKE_WAREHOUSE = 'COMPUTE_WH'
SNOWFLAKE_DATABASE = 'DATARCW'
SNOWFLAKE_SCHEMA = 'PATIENTS'

class Patient(BaseModel):
    NOM: str
    PRENOM: str
    DATE_NAISSANCE: str
    ADRESSE: str
    TELEPHONE: str
    EMAIL: str

@contextmanager
def get_snowflake_conn():
    conn = snowflake.connector.connect(
        user=SNOWFLAKE_USER,
        password=SNOWFLAKE_PASSWORD,
        account=SNOWFLAKE_ACCOUNT,
        warehouse=SNOWFLAKE_WAREHOUSE,
        database=SNOWFLAKE_DATABASE,
        schema=SNOWFLAKE_SCHEMA
    )
    try:
        yield conn
    finally:
        conn.close()

@app.post("/patients/")
def create_patient(patient: Patient):
    try:
        with get_snowflake_conn() as conn:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO patients (NOM, PRENOM, DATE_NAISSANCE, ADRESSE, TELEPHONE, EMAIL) VALUES (%s, %s, %s, %s, %s, %s)",
                (patient.NOM, patient.PRENOM, patient.DATE_NAISSANCE, patient.ADRESSE, patient.TELEPHONE, patient.EMAIL)
            )
            return {"message": "Patient created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/patients/")
def read_patients():
    try:
        with get_snowflake_conn() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM patients")
            results = cur.fetchall()
            patients = []
            for row in results:
                patient = {
                    "ID": row[0],
                    "NOM": row[1],
                    "PRENOM": row[2],
                    "DATE_NAISSANCE": row[3],
                    "ADRESSE": row[4],
                    "TELEPHONE": row[5],
                    "EMAIL": row[6]
                }
                patients.append(patient)
            return patients
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/patients/{patient_id}")
def read_patient(patient_id: int):
    try:
        with get_snowflake_conn() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM patients WHERE ID = %s", (patient_id,))
            result = cur.fetchone()
            if result:
                patient = {
                    "ID": result[0],
                    "NOM": result[1],
                    "PRENOM": result[2],
                    "DATE_NAISSANCE": result[3],
                    "ADRESSE": result[4],
                    "TELEPHONE": result[5],
                    "EMAIL": result[6]
                }
                return patient
            else:
                raise HTTPException(status_code=404, detail="Patient not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/patients/{patient_id}")
def update_patient(patient_id: int, patient: Patient):
    try:
        with get_snowflake_conn() as conn:
            cur = conn.cursor()
            cur.execute(
                "UPDATE patients SET NOM = %s, PRENOM = %s, DATE_NAISSANCE = %s, ADRESSE = %s, TELEPHONE = %s, EMAIL = %s WHERE ID = %s",
                (patient.NOM, patient.PRENOM, patient.DATE_NAISSANCE, patient.ADRESSE, patient.TELEPHONE, patient.EMAIL, patient_id)
            )
            return {"message": "Patient updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/patients/{patient_id}")
def delete_patient(patient_id: int):
    try:
        with get_snowflake_conn() as conn:
            cur = conn.cursor()
            cur.execute("DELETE FROM patients WHERE ID = %s", (patient_id,))
            return {"message": "Patient deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)

