# # # # from fastapi import FastAPI, Depends, HTTPException
# # # # from sqlalchemy.orm import Session
# # # # from . import models, schemas, dependencies
# # # # from .database import engine

# # # # models.Base.metadata.create_all(bind=engine)

# # # # app = FastAPI()

# # # # @app.post("/patients/", response_model=schemas.Patient)
# # # # def create_patient(patient: schemas.PatientCreate, db: Session = Depends(dependencies.get_db)):
# # # #     db_patient = models.Patient(**patient.dict())
# # # #     db.add(db_patient)
# # # #     db.commit()
# # # #     db.refresh(db_patient)
# # # #     return db_patient

# # # # @app.get("/patients/{patient_id}", response_model=schemas.Patient)
# # # # def read_patient(patient_id: int, db: Session = Depends(dependencies.get_db)):
# # # #     db_patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
# # # #     if db_patient is None:
# # # #         raise HTTPException(status_code=404, detail="Patient not found")
# # # #     return db_patient

# # # from fastapi import FastAPI, HTTPException, Depends
# # # from sqlalchemy.orm import Session
# # # from typing import List
# # # from .database import SessionLocal, engine
# # # from . import models, schemas

# # # app = FastAPI()

# # # # Create the database tables
# # # models.Base.metadata.create_all(bind=engine)

# # # # Dependency to get the database session
# # # def get_db():
# # #     db = SessionLocal()
# # #     try:
# # #         yield db
# # #     finally:
# # #         db.close()

# # # @app.post("/patients/", response_model=schemas.Patient)
# # # def create_patient(patient: schemas.PatientCreate, db: Session = Depends(get_db)):
# # #     db_patient = models.Patient(**patient.dict())
# # #     db.add(db_patient)
# # #     db.commit()
# # #     db.refresh(db_patient)
# # #     return db_patient

# # # @app.get("/patients/{patient_id}", response_model=schemas.Patient)
# # # def read_patient(patient_id: int, db: Session = Depends(get_db)):
# # #     db_patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
# # #     if db_patient is None:
# # #         raise HTTPException(status_code=404, detail="Patient not found")
# # #     return db_patient

# # # @app.get("/patients/", response_model=List[schemas.Patient])
# # # def read_patients(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
# # #     patients = db.query(models.Patient).offset(skip).limit(limit).all()
# # #     return patients

# # # @app.put("/patients/{patient_id}", response_model=schemas.Patient)
# # # def update_patient(patient_id: int, patient: schemas.PatientCreate, db: Session = Depends(get_db)):
# # #     db_patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
# # #     if db_patient is None:
# # #         raise HTTPException(status_code=404, detail="Patient not found")
# # #     for key, value in patient.dict().items():
# # #         setattr(db_patient, key, value)
# # #     db.commit()
# # #     db.refresh(db_patient)
# # #     return db_patient

# # # @app.delete("/patients/{patient_id}", response_model=schemas.Patient)
# # # def delete_patient(patient_id: int, db: Session = Depends(get_db)):
# # #     db_patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
# # #     if db_patient is None:
# # #         raise HTTPException(status_code=404, detail="Patient not found")
# # #     db.delete(db_patient)
# # #     db.commit()
# # #     return db_patient
# # from fastapi import FastAPI, HTTPException
# # from typing import List
# # from pydantic import BaseModel
# # from datetime import date
# # from .database import get_connection

# # app = FastAPI()

# # class Patient(BaseModel):
# #     id: int = None
# #     nom: str
# #     prenom: str
# #     date_naissance: date
# #     adresse: str
# #     telephone: str
# #     email: str

# # @app.post("/patients/", response_model=Patient)
# # def create_patient(patient: Patient):
# #     conn = get_connection()
# #     cur = conn.cursor()
# #     try:
# #         cur.execute("""
# #         INSERT INTO PATIENTS (NOM, PRENOM, DATE_NAISSANCE, ADRESSE, TELEPHONE, EMAIL) 
# #         VALUES (%s, %s, %s, %s, %s, %s)
# #         """, (patient.nom, patient.prenom, patient.date_naissance, patient.adresse, patient.telephone, patient.email))
# #         conn.commit()
# #         cur.execute("SELECT LAST_INSERT_ID()")
# #         patient_id = cur.fetchone()[0]
# #         patient.id = patient_id
# #         return patient
# #     except Exception as e:
# #         raise HTTPException(status_code=400, detail=str(e))
# #     finally:
# #         cur.close()
# #         conn.close()

# # @app.get("/patients/{patient_id}", response_model=Patient)
# # def read_patient(patient_id: int):
# #     conn = get_connection()
# #     cur = conn.cursor()
# #     try:
# #         cur.execute("SELECT * FROM PATIENTS WHERE ID = %s", (patient_id,))
# #         row = cur.fetchone()
# #         if row:
# #             return Patient(id=row[0], nom=row[1], prenom=row[2], date_naissance=row[3], adresse=row[4], telephone=row[5], email=row[6])
# #         else:
# #             raise HTTPException(status_code=404, detail="Patient not found")
# #     except Exception as e:
# #         raise HTTPException(status_code=400, detail=str(e))
# #     finally:
# #         cur.close()
# #         conn.close()

# # @app.get("/patients/", response_model=List[Patient])
# # def read_patients(skip: int = 0, limit: int = 10):
# #     conn = get_connection()
# #     cur = conn.cursor()
# #     try:
# #         cur.execute("SELECT * FROM PATIENTS LIMIT %s OFFSET %s", (limit, skip))
# #         rows = cur.fetchall()
# #         patients = [Patient(id=row[0], nom=row[1], prenom=row[2], date_naissance=row[3], adresse=row[4], telephone=row[5], email=row[6]) for row in rows]
# #         return patients
# #     except Exception as e:
# #         raise HTTPException(status_code=400, detail=str(e))
# #     finally:
# #         cur.close()
# #         conn.close()

# # @app.put("/patients/{patient_id}", response_model=Patient)
# # def update_patient(patient_id: int, patient: Patient):
# #     conn = get_connection()
# #     cur = conn.cursor()
# #     try:
# #         cur.execute("""
# #         UPDATE PATIENTS SET NOM = %s, PRENOM = %s, DATE_NAISSANCE = %s, ADRESSE = %s, TELEPHONE = %s, EMAIL = %s 
# #         WHERE ID = %s
# #         """, (patient.nom, patient.prenom, patient.date_naissance, patient.adresse, patient.telephone, patient.email, patient_id))
# #         conn.commit()
# #         patient.id = patient_id
# #         return patient
# #     except Exception as e:
# #         raise HTTPException(status_code=400, detail=str(e))
# #     finally:
# #         cur.close()
# #         conn.close()

# # @app.delete("/patients/{patient_id}", response_model=Patient)
# # def delete_patient(patient_id: int):
# #     conn = get_connection()
# #     cur = conn.cursor()
# #     try:
# #         cur.execute("SELECT * FROM PATIENTS WHERE ID = %s", (patient_id,))
# #         row = cur.fetchone()
# #         if row:
# #             cur.execute("DELETE FROM PATIENTS WHERE ID = %s", (patient_id,))
# #             conn.commit()
# #             return Patient(id=row[0], nom=row[1], prenom=row[2], date_naissance=row[3], adresse=row[4], telephone=row[5], email=row[6])
# #         else:
# #             raise HTTPException(status_code=404, detail="Patient not found")
# #     except Exception as e:
# #         raise HTTPException(status_code=400, detail=str(e))
# #     finally:
# #         cur.close()
# #         conn.close()
# from fastapi import FastAPI, HTTPException
# from typing import List
# from pydantic import BaseModel
# from datetime import date
# from .database import get_connection

# app = FastAPI()

# class Patient(BaseModel):
#     id: int = None
#     nom: str
#     prenom: str
#     date_naissance: date
#     adresse: str
#     telephone: str
#     email: str

# @app.post("/patients/", response_model=Patient)
# def create_patient(patient: Patient):
#     conn = get_connection()
#     cur = conn.cursor()
#     try:
#         cur.execute("""
#         INSERT INTO PATIENTS (NOM, PRENOM, DATE_NAISSANCE, ADRESSE, TELEPHONE, EMAIL) 
#         VALUES (%s, %s, %s, %s, %s, %s)
#         """, (patient.nom, patient.prenom, patient.date_naissance, patient.adresse, patient.telephone, patient.email))
#         conn.commit()
#         cur.execute("SELECT LAST_INSERT_ID()")
#         patient_id = cur.fetchone()[0]
#         patient.id = patient_id
#         return patient
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))
#     finally:
#         cur.close()
#         conn.close()

# @app.get("/patients/{patient_id}", response_model=Patient)
# def read_patient(patient_id: int):
#     conn = get_connection()
#     cur = conn.cursor()
#     try:
#         cur.execute("SELECT * FROM PATIENTS WHERE ID = %s", (patient_id,))
#         row = cur.fetchone()
#         if row:
#             return Patient(id=row[0], nom=row[1], prenom=row[2], date_naissance=row[3], adresse=row[4], telephone=row[5], email=row[6])
#         else:
#             raise HTTPException(status_code=404, detail="Patient not found")
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))
#     finally:
#         cur.close()
#         conn.close()

# @app.get("/patients/", response_model=List[Patient])
# def read_patients(skip: int = 0, limit: int = 10):
#     conn = get_connection()
#     cur = conn.cursor()
#     try:
#         cur.execute("SELECT * FROM PATIENTS LIMIT %s OFFSET %s", (limit, skip))
#         rows = cur.fetchall()
#         patients = [Patient(id=row[0], nom=row[1], prenom=row[2], date_naissance=row[3], adresse=row[4], telephone=row[5], email=row[6]) for row in rows]
#         return patients
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))
#     finally:
#         cur.close()
#         conn.close()

# @app.put("/patients/{patient_id}", response_model=Patient)
# def update_patient(patient_id: int, patient: Patient):
#     conn = get_connection()
#     cur = conn.cursor()
#     try:
#         cur.execute("""
#         UPDATE PATIENTS SET NOM = %s, PRENOM = %s, DATE_NAISSANCE = %s, ADRESSE = %s, TELEPHONE = %s, EMAIL = %s 
#         WHERE ID = %s
#         """, (patient.nom, patient.prenom, patient.date_naissance, patient.adresse, patient.telephone, patient.email, patient_id))
#         conn.commit()
#         patient.id = patient_id
#         return patient
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))
#     finally:
#         cur.close()
#         conn.close()

# @app.delete("/patients/{patient_id}", response_model=Patient)
# def delete_patient(patient_id: int):
#     conn = get_connection()
#     cur = conn.cursor()
#     try:
#         cur.execute("SELECT * FROM PATIENTS WHERE ID = %s", (patient_id,))
#         row = cur.fetchone()
#         if row:
#             cur.execute("DELETE FROM PATIENTS WHERE ID = %s", (patient_id,))
#             conn.commit()
#             return Patient(id=row[0], nom=row[1], prenom=row[2], date_naissance=row[3], adresse=row[4], telephone=row[5], email=row[6])
#         else:
#             raise HTTPException(status_code=404, detail="Patient not found")
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))
#     finally:
#         cur.close()
#         conn.close()
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import date
import snowflake.connector

app = FastAPI()

# Schéma Pydantic pour la création d'un patient
class PatientCreate(BaseModel):
    nom: str
    prenom: str
    date_naissance: date
    adresse: str
    telephone: str
    email: str

# Configuration de la connexion à Snowflake
def get_connection():
    return snowflake.connector.connect(
        user='MOMATH92',
        password='Rassoulle92',
        account='mtjxohy-wp28902',
        warehouse='COMPUTE_WH',
        database='DATARCW',
        schema='PATIENTS'
    )

@app.post("/patients/")
async def create_patient(patient: PatientCreate):
    conn = get_connection()
    cur = conn.cursor()
    
    try:
        cur.execute("""
            INSERT INTO patients (NOM, PRENOM, DATE_NAISSANCE, ADRESSE, TELEPHONE, EMAIL)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (patient.nom, patient.prenom, patient.date_naissance, patient.adresse, patient.telephone, patient.email))
        conn.commit()
        return {"message": "Patient créé avec succès"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        conn.close()

@app.get("/patients/")
async def read_patients():
    conn = get_connection()
    cur = conn.cursor()
    
    try:
        cur.execute("SELECT * FROM patients")
        rows = cur.fetchall()
        patients = [
            {
                "id": row[0],
                "nom": row[1],
                "prenom": row[2],
                "date_naissance": row[3],
                "adresse": row[4],
                "telephone": row[5],
                "email": row[6]
            }
            for row in rows
        ]
        return patients
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        conn.close()

