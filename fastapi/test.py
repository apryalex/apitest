# Import des librairies
from unittest import TestCase, main
from fastapi.testclient import TestClient
from api import app
import os



# Tests unitaire de l'environnement de développement
class TestDev(TestCase):

    # Vérifie que les fichiers sont présents
    def test_files(self):

        required_files = ["model_1.pkl", "labelencoder.pkl", "model_2.pkl", "api.py"]
        for file in required_files:
            self.assertIn(file, os.listdir())

    # Vérifie que les requirements sont présents
    def test_requirements(self):
        self.assertIn("requirements.txt", os.listdir())
    
    # Vérifie que le gitignore est présent
    def test_gitignore(self):
        self.assertIn(".gitignore", os.listdir())

# Création du client de test



# Tests unitaire de l'API
class TestAPI(TestCase):

    def setUp(self):
        self.client = TestClient(app)
    
    # Vérifie que l'API est bien lancée
    def test_api_is_running(self):
        response = self.client.get("/hello")
        self.assertEqual(response.status_code, 200)

    # Vérifie l'endpoint Hello
    def test_hello_endpoint(self):
        response = self.client.get("/hello")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Hello World"})

    # Vérifie l'endpoint predict
    def test_predict_endpoint(self):
        payload = {
            "Gender": "Male",
            "Age": 30,
            "Physical_Activity_Level": 3,
            "Heart_Rate": 80,
            "Daily_Steps": 8000,
            "BloodPressure_high": 120,
            "BloodPressure_low": 80
        }
        response = self.client.post("/predict", json=payload)
        self.assertEqual(response.status_code, 200)
    
    # Vérifie l'endpoint predict2
    def test_predict_endpoint(self):
        payload = {
        "Physical_Activity_Level": 42,
        "Heart_Rate": 77,
        "Daily_Steps": 4200
        }
        response = self.client.post("/predict2", json=payload)
        self.assertEqual(response.status_code, 200)

# Démarrage des tests
if __name__== "__main__" :
    main(
        verbosity=2,
    )
