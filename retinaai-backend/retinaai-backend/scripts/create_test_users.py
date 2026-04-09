import requests
import json

BASE_URL = "http://localhost:8000"

def register_and_verify(user_data):
    print(f"Registering {user_data['full_name']} ({user_data['role']})...")
    reg_response = requests.post(f"{BASE_URL}/auth/register", json=user_data)
    
    if reg_response.status_code == 200 or reg_response.status_code == 400 and "already registered" in reg_response.text:
        if reg_response.status_code == 200:
            print("Registration successful (OTP sent).")
        else:
            print("User already exists, proceeding to verification check.")
        
        print(f"Verifying {user_data['email']} with special OTP 000000...")
        verify_data = {
            "email": user_data["email"],
            "otp": "000000"
        }
        ver_response = requests.post(f"{BASE_URL}/auth/verify-otp", json=verify_data)
        
        if ver_response.status_code == 200:
            print("Verification successful.")
            return True
        else:
            print(f"Verification failed: {ver_response.text}")
            return False
    else:
        print(f"Registration failed: {reg_response.text}")
        return False

# Test Patient
patient = {
    "full_name": "Test Patient",
    "email": "testpatient@example.com",
    "phone": "1234567890",
    "password": "Password123",
    "role": "Patient"
}

# Test Doctor
doctor = {
    "full_name": "Test Doctor",
    "email": "testdoctor@example.com",
    "phone": "0987654321",
    "password": "Password123",
    "role": "Doctor",
    "medical_license_id": "MD12345",
    "specialization": "Retina Specialist",
    "hospital_name": "General Hospital",
    "experience": "10 years"
}

if __name__ == "__main__":
    try:
        # Check if server is running
        requests.get(BASE_URL)
        
        register_and_verify(patient)
        print("-" * 20)
        register_and_verify(doctor)
        
    except requests.exceptions.ConnectionError:
        print("Error: Backend server is not running on http://localhost:8000")
        print("Please start the backend server and run this script again.")
