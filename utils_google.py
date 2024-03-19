from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials

def authenticate():
    key_path = "reciperecommender-417613-a00264eae2d6.json"

    # Create credentials based on key from service account
    # Make sure your account has the roles listed in the Google Cloud Setup section
    credentials = Credentials.from_service_account_file(
        key_path,
        scopes=['https://www.googleapis.com/auth/cloud-platform'])
    
    if credentials.expired:
        credentials.refresh(Request())
        
    PROJECT_ID = "reciperecommender-417613"
    service_account = "reciperecommender@reciperecommender-417613.iam.gserviceaccount.com"
    with open("Pinecone_API_KEY.txt") as f:
        pinecone_API_KEY = f.read()
        
    return credentials, PROJECT_ID, service_account, pinecone_API_KEY