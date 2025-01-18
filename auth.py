import requests

# Your LinkedIn App credentials
CLIENT_ID = 'your_client_id'
CLIENT_SECRET = 'your_client_secret'
REDIRECT_URI = 'your_redirect_uri'

# Step 1: Get authorization URL
auth_url = f"https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope=r_liteprofile"
print("Go to the following URL to authorize the app:", auth_url)

# Step 2: After authorization, LinkedIn redirects to your REDIRECT_URI with a 'code' parameter
authorization_code = input("Enter the authorization code: ")

# Step 3: Exchange the authorization code for an access token
token_url = "https://www.linkedin.com/oauth/v2/accessToken"
data = {
    'grant_type': 'authorization_code',
    'code': authorization_code,
    'redirect_uri': REDIRECT_URI,
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET
}

response = requests.post(token_url, data=data)
access_token = response.json().get('access_token')
print("Access Token:", access_token)

# Step 4: Use the access token to retrieve profile information
profile_url = "https://api.linkedin.com/v2/me"
headers = {'Authorization': f'Bearer {access_token}'}
profile_data = requests.get(profile_url, headers=headers).json()

print("Profile Data:", profile_data)
