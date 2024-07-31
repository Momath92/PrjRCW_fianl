# try:
#     import snowflake.connector
#     print("Importation réussie de snowflake.connector")

#     # Remplacez ces valeurs par vos informations de connexion Snowflake
#     conn = snowflake.connector.connect(
#         user='MOMATH92',          # Vérifiez votre nom d'utilisateur
#         password='Rassoulle92', # Assurez-vous que le mot de passe est correct
#         account='mtjxohy-wp28902'
#     )

#     cursor = conn.cursor()
    
#     # Lister les entrepôts disponibles
#     cursor.execute("SHOW WAREHOUSES")
#     warehouses = cursor.fetchall()
#     print("Liste des entrepôts disponibles:")
#     for warehouse in warehouses:
#         print(warehouse[0])

#     # Utiliser le premier entrepôt de la liste (ou un autre de votre choix)
#     if warehouses:
#         selected_warehouse = warehouses[0][0]  # Sélectionner le premier entrepôt de la liste
#         cursor.execute(f"USE WAREHOUSE {selected_warehouse}")
#         print(f"Entrepôt '{selected_warehouse}' sélectionné.")
#     else:
#         print("Aucun entrepôt disponible.")

#     # Sélectionner la base de données et le schéma
#     cursor.execute("USE DATABASE DATARCW")
#     cursor.execute("USE SCHEMA PATIENTS")

#     # Vérifiez l'existence de la table 'patients'
#     cursor.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'PATIENTS'")
#     table_exists = cursor.fetchone()

#     if table_exists:
#         print("La table 'patients' existe.")
#         # Sélectionnez les données de la table 'patients'
#         cursor.execute("SELECT * FROM PATIENTS")
#         patients = cursor.fetchall()
#         for patient in patients:
#             print(patient)
#     else:
#         print("La table 'patients' n'existe pas.")

#     cursor.close()
#     conn.close()

# except snowflake.connector.errors.Error as e:
#     print(f"Erreur de connexion: {e}")
# except ModuleNotFoundError as e:
#     print(f"Erreur d'importation: {e}")
# except Exception as e:
#     print(f"Erreur: {e}")
try:
    import snowflake.connector
    print("Importation réussie de snowflake.connector")

    # Remplacez ces valeurs par vos informations de connexion Snowflake
    conn = snowflake.connector.connect(
        user='MOMATH92',          # Vérifiez votre nom d'utilisateur
        password='Rassoulle92', # Assurez-vous que le mot de passe est correct
        account='mtjxohy-wp28902'
    )

    cursor = conn.cursor()
    
    # Lister les entrepôts disponibles
    cursor.execute("SHOW WAREHOUSES")
    warehouses = cursor.fetchall()
    print("Liste des entrepôts disponibles:")
    for warehouse in warehouses:
        print(warehouse[0])

    # Utiliser le premier entrepôt de la liste (ou un autre de votre choix)
    if warehouses:
        selected_warehouse = warehouses[0][0]  # Sélectionner le premier entrepôt de la liste
        cursor.execute(f"USE WAREHOUSE {selected_warehouse}")
        print(f"Entrepôt '{selected_warehouse}' sélectionné.")
    else:
        print("Aucun entrepôt disponible.")

    # Sélectionner la base de données et le schéma
    cursor.execute("USE DATABASE DATARCW")
    cursor.execute("USE SCHEMA PATIENTS")

    # Vérifiez l'existence de la table 'patients'
    cursor.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'PATIENTS'")
    table_exists = cursor.fetchone()

    if table_exists:
        print("La table 'patients' existe.")
        
        # Insérer des données dans la table 'patients'
        try:
            cursor.execute(
                """
                INSERT INTO patients (nom, prenom, date_naissance, adresse, telephone, email) 
                VALUES 
                ('Doe', 'John', '1990-01-01', '123 Main St', '1234567890', 'john.doe@example.com'),
                ('Smith', 'Jane', '1985-05-15', '456 Elm St', '0987654321', 'jane.smith@example.com')
                """
            )
            conn.commit()
            print("Données insérées avec succès.")
        except snowflake.connector.errors.ProgrammingError as e:
            print(f"Erreur lors de l'insertion des données : {e}")

        # Sélectionnez les données de la table 'patients'
        cursor.execute("SELECT * FROM PATIENTS")
        patients = cursor.fetchall()
        print("Données de la table 'patients':")
        for patient in patients:
            print(patient)
    else:
        print("La table 'patients' n'existe pas.")

    cursor.close()
    conn.close()

except snowflake.connector.errors.Error as e:
    print(f"Erreur de connexion: {e}")
except ModuleNotFoundError as e:
    print(f"Erreur d'importation: {e}")
except Exception as e:
    print(f"Erreur: {e}")
