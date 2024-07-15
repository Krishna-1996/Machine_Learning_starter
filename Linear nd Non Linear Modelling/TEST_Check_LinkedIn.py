import pandas as pd
from linkedin_api import Linkedin

# Initialize LinkedIn API with your credentials
api = Linkedin('1904krishna@gmail.com', 'J@iShriKrishn@1996')

# Data to be searched
data = {
    "Company Name": ["Global Logic", "Global Logic", "DAIKIN AIRCONDITIONING INDIA", ...],
    "Person's Name": ["Vineet Yadav", "Harpreet Singh", "Kamal Nagar", ...],
    "Designation": ["Architect - Technical", "Manager", "Senior Product Manager", ...]
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Function to search for a LinkedIn profile
def search_linkedin_profile(name, company):
    profiles = api.search_people(keywords=name, company=company)
    if profiles:
        profile = profiles[0]  # Take the first result
        profile_url = f"https://www.linkedin.com/in/{profile['public_identifier']}"
        return "Yes", profile_url
    else:
        return "No", ""

# Apply the function to each row in the DataFrame
df[['LinkedIn Available', 'LinkedIn Profile Link']] = df.apply(
    lambda row: pd.Series(search_linkedin_profile(row["Person's Name"], row["Company Name"])),
    axis=1
)

# Save results to a new CSV file
df.to_csv('linkedin_profiles.csv', index=False)

print("LinkedIn profile search completed and results saved to linkedin_profiles.csv")
