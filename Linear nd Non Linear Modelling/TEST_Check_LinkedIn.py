import pandas as pd
from linkedin_api import Linkedin

# Initialize LinkedIn API with your credentials
api = Linkedin('1904krishna@gmail.com', 'J@iShriKrishn@1996')

# Data to be searched
data = {
    "Company Name": [
        "Global Logic", "Global Logic", "DAIKIN AIRCONDITIONING INDIA", "USHA INTERNATIONAL", 
        "IRIS SOFTWARE", "SAREGAMA INDIA", "HEALTHCARE GLOBAL VIJAY ONCOLOGY", 
        "R SYSTEMS INTERNATION", "ABBOTT LABORATORIES INDIA", "QUALITYKIOSK", 
        "Macmillan Publishers India", "DLF Brands", "Sasken Communication Technologies", 
        "Global Logic", "THERMAX", "BRIGADE ENTERPRISES", "CARBORUNDUM UNIVERSAL", 
        "AVENUES INTEGRATION SYSTEMS", "DAINIK SURFACE CHEMICALS", "EXIDE INDUSTRIES", 
        "ALLIED NIPPON COMPONENTS", "FUJITSU CONSULTING", "Goldi Solar", "IBM", 
        "AMERICAN BREW CRAFTS", "DHARAMPAL SATYAPAL  DS GROUP", "XCEEDANCE INFOTECH", 
        "ANAND RATHI WEALTH ADVISORS", "COFORGE", "BERGER PAINTS INDIA", "Oracle", 
        "MEDLIFE INTERNATIONAL", "QUICK HEAL HEALTHCARE AND SURGICALS", "WINJIT TECHNOLOGIES", 
        "Quovantis Technologies", "", "", "", "HDFC LIFE INSURANCE COMPANY", "RILOGIX TECHNOLOGIES INDIA", 
        "DATAMATICS GLOBAL SERVICES", "MCAFEE", "TATA CLASSEDGE", "Wipro Infrastructure", "Self 2024 Accounts", 
        "Self 2024 Accounts", "Self 2024 Accounts", "Digiplug Technologies", "ACCENTURE SOLUTIONS", "Self 2024 Accounts", 
        "AVERY Weight Tronix", "RELIANCE ENERGY", "Reliance Jio", "Reliance Jio", "RELIANCE HOME", 
        "Reliance Jio", "AMERICAN BREW CRAFTS", "RELIANCE COMMERCIAL FINANCE", "RELIANCE COMMERCIAL FINANCE", 
        "RELIANCE CAPITAL VENTURES", "Reliance Jio", "", "HDFC BANK", "Self 2024 Accounts", "Ingram Micro India", 
        "FEDERAL CHEMICAL WORKS", "NIIT Technologies", "HCL Infosystem", "BANNARI AMMAN APPAREL", "Infosys Bpo", 
        "Anoosmar Technologies", "ARYAKA NETWORKS INDIA", "ABC CONSULTANTS", "AMBIK HARMONIC FILTERS", "YOKOGAWA INDIA", 
        "KALPATARU POWER TRANSMISSION", "C G INTERNATIONAL", "PHILIPS INDIA", "NIryas Food Products", "MAWANA SUGARS", 
        "SONA PROCESSORS INDIA", "Weir Minerals (India)", "ADEEP LIFE SCIENCES", "FUTURE GENERALI INDIA INSURANCE COMPANY", 
        "JYOTI RUBBER UDYOG INDIA", "SAP", "IBM INDIA", "VISA", "IBM INDIA", "Fedelity", "TATA CONSULTANCY SERVICES", 
        "Infosys Bpo", "Info Gain India", "AUTOMOTIVE MANUFACTURERS", "ANGEL BROKING", "DBS BANK", "BANK OF INDIA", 
        "J P MORGAN SECURITIES INDIA", "ANGEL ONE WEALTH MANAGEMENT", "Self 2024 Accounts", "ICICI BANK", "HDFC BANK", 
        "DEWAN TYRES", "HDFC BANK", "Cineom Broadcast India", "Mahindra & Mahindra", "DXC Technology", "GINGER REALTORS", 
        "", "STELCO", "INDIVAR SOFTWARE SOLUTIONS", "The Lalit Hotel", "STARTUP INDIA ADVISERS", "CYBERTHINK INFOTECH", 
        "JAQUAR AND COMPANY", "ALLENGERS MEDICAL SYSTEMS", "BURSYS INFOTECH INDIA", "J C T", "EMINENCE TECHNOLOGY", 
        "Wipro Infrastructure", "Sungard AS", "RED HAT", "AMTEX SYSTEMS", "KURTOSYS SYSTEMS INDIA", "IMARTICUS", 
        "IDS Software Solutions", "COFORGE", "ACCENTURE SOLUTIONS", "RADHEYA SOCIAL WELFARE FOUNDATION", "ABBOTT INDIA", 
        "ADDRESSHEALTH SOLUTIONS INDIA", "Map Systems", "VERIZON", "ACCELTOP LEARNING", "ELGI ULTRA APPLIANCES", "EDC", 
        "PETROFAC ENGINEERING INDIA", "PETROFAC ENGINEERING INDIA", "FORGE 2000", "EXPLEO SOLUTIONS", "", 
        "Mahindra & Mahindra", "MARICO", "ICICI LOMBARD GENERAL INSURANCE COMPANY", "RELIANCE ENERGY", "MAGMA", 
        "RELIANCE INDIA", "DCB BANK", "UTKARSH INDIA", "Ebex (Esselgroup)", "CONCENTRIX", "RELIANCE CAPITAL VENTURES", 
        "RELIANCE INFOCOMM", "SHAPOORJI PALLONJI & COMPANY", "MAHINDRA AND MAHINDRA", "ESSEL MINING & INDUSTRIES", 
        "COFORGE", "TATA CONSULTANCY SERVICES", "L&T INFRASTRUCTURE DEVELOPMENT PROJECTS", "LARSEN AND TOUBRO", 
        "LARSEN AND TOUBRO", "HCL TECHNOLOGIES", "SELF EMPLOYED", "MCCORMICK FOODS INDIA", "NISC EXPORT SERVICES"
    ],
    "Person's Name": [
        "Vineet Yadav", "Harpreet Singh", "Kamal Nagar", "Tamal Banerjee", "Mallika Chaturvedi", "Pratha Ghosh", 
        "Hasan Bakhtawar", "Paras Khonde", "Ravisankar Yakkanti", "Sushant Shivaji", "Ravi Bhushan", "Vipin Sharma", 
        "Ravisankar K", "Aditya Mehta", "Shivashankar G", "Raj Subramanya", "Siddhartha Roy", "Swapnil Chavhan", 
        "Ankur Kapruwan", "Gauttam Dutta", "Akhilesh Singh", "Anurag Singh", "Shirish Arvind Gheware", "DV Nagagrajesh", 
        "Soumarghya Mukherjee", "Vivek Namdev", "Priyanka Dhuliya", "Pawan Burde", "Mohammed Burhanuddin", "Subir Saha", 
        "Kavya Srinivasan", "Shashank Shekhar", "Vishwajeet Chauhan", "Muddassar Shaikh", "Ravi Kumar", "Anindya Khare", 
        "Vyomkesh Tiwari", "Hemachandra M S", "Mahesh Bk", "Aditya Gondane", "Manisha Jadhav", "Hemlata Soni", "Ajeeth Rajesh", 
        "Anupam Kumar", "Amit Shah", "Chander Madan", "Ashish Gattewar", "Gaurav Mishra", "Purvang Pandya", "Garima", 
        "Avinash Kumar", "Milind Kadam", "Mudeer Khan", "Nisha Upadhyay", "Harshal Harbak", "Saurabh Shah", "Pramod Jangid", 
        "Titto Natarajan", "Anuj Anurag", "Sanjeev Bhatia", "Satyadeep Mishra", "Amit Kumar Yadav", "Venus Dsouza", 
        "Pk Ramesh", "Ajit G Joshi", "George Joseph", "Manisha Kharod", "Prerna Koul", "Arumugam Sellamuthu", "Murali Doss", 
        "Ankur Panchbudhe", "Aseem Sethi", "Parth Sharma", "Chandrakant Khadilkar", "Manoj Nair", "D Gandhi", 
        "Aparna Sundareshwaran", "Ananda Ananda", "Jayesh Morvadiya", "S Sharma", "Dinesh Vora", "Vinoth Kumar", "Dinesh Sharma", 
        "Ashok Thiagarajan", "Kalki Mangukiya", "Nitin Gupta", "Ashok Bhardwaj", "Harinder Singh", "Amit Kumar", "Nehal Hande", 
        "Amandeep Singh", "Nelson Thomas", "Naini Ghai", "Dilip Parulekar", "Rajbeer Kataria", "Ramesh Mallya", "Ganesh Chittoor", 
        "Shubham Salani", "Mukesh Prasad", "Preethi Nair", "Vidya Sagar", "Mahesh Malkar", "Sachin Konkar", "Ajit Singh", 
        "Kiran Karad", "Sachin Gupta", "Aruldoss Ganesan", "Hozefa Muchhala", "Sourav Dutta", "G L Koli", "Raghav Bhandari", 
        "Bheshaz Bedi", "Susheel Kumar", "Faisal Alam", "Harpreet Bhasin", "Rishabh Sharma", "Abhinav Kaushik", "H K Chopra", 
        "Priya Kaundal", "Sachin", "Raj Shivaram", "Bhargav Meka", "Natarajan Ramasamy", "Richajain Duma", "Gurprasath K", 
        "BS Prakash", "Sreenivas M", "Pradeep Kumar Kalva", "A Joshi", "Yatinder Mahindroo", "Nima Nair", "Satish P P", 
        "Ritesh Kadam", "Divya Anjali", "Shankar N", "Aanchal Jaiswal", "Sohan Pal", "Anoj Verma", "Selva Kumar", "Manoj Kumar", 
        "Ved Gupta", "Ammu Venkatesh", "Manish Kedia", "Manish Gulati", "Indranil Chatterjee", "Gaurav Ganguly", "Rahul Dighe", 
        "Shashank Shekhar", "Manoj Vachhani", "Balaji Vankala", "Chinmay Patra", "Prince Sharma", "Ajoy Rajani", "Jeslin George", 
        "Ashok Asawale", "Mahendra Paul", "Tarun Malik", "Naresh Gupta", "M Ramesh", "Sunil Haridas", "Ghouse Mohideen", 
        "Sachin Saini", "Sushil Sethia", "Santoshchadalavada", "Sharada Kulkarni"
    ],
    "Designation": [
        "Architect - Technical", "Manager", "Senior Product Manager", "Sr Manager Information Technology - Group Infra Head", 
        "Consultant, IT", "Manager - IT & Systems", "Deputy General Manager Marketi", "Technical Manager", 
        "Senior Manager - Quality", "Test Engineer", "Software Programmer", "Deputy General Manager (HR)", "Senior Software Engineer", 
        "DevOps Engineer", "Head - Unit", "Deputy General Manager - IT", "Self Employed", "Manager - Software", "Manager", 
        "General Manager  IT", "Manager  HR  Administration", "Application Devloper Trainee", "Software Engineer", "Director - IT", 
        "Manager - HR, Telecom & Power", "Assistant Manager - Quality Assurance", "Assistant Manager", "Vice President - IT", 
        "Architect", "Vice President - IT (retired)", "Engineer", "Lead", "Manager - IT", "Software Engineer", "Developer", 
        "Head - Marketing", "Manager - Software", "SQL DBA and Database Application Support", "Manager - IT Security", 
        "SDE2", "Consultant", "Data Engineer", "Product - Data Analyst 2", "Manager", "Assistant Vice President - Operation", 
        "GRC/Archer Consultant", "Data Engineer", "Assistant General Manager Technology", "Senior Manager - IT", "STUDENT", 
        "Senior Sales Manager", "Manager", "Software Developer", "Assistant Manager IT", "Chief Information Security Officer", 
        "Network Engineer", "RF planning engineer", "Head  Procurement", "Assistant General Manager Sales", 
        "National Risk Manager - Vehicles", "Head HR", "Regional Manager", "Assistant Manager", "Assistant Manager - Procurement", 
        "Head - Solution Architect", "Assistant General Manager - IT", "associate datacenter services", "Lead IT", 
        "Deputy General Manager  IT", "Senior Cloud Engineer", "Chief Technology Officer", "Senior Director", 
        "Business Acquisition Head Honchos", "Director", "Manager  IT", "Senior Vice President - IT", "Director", 
        "Vice President - IT", "Associate Vice President", "Deputy General Manager - IT", "Associate Vice President, IT", 
        "Manager  IT", "Head - IT", "Assistant Vice President - IT", "Chief Technology Officer", "Head - IT", "DevOps Engineer", 
        "Senior Software Engineer", "Software Engineer", "System Engineer", "Software Engineer", "Test Engineer", 
        "Consultant", "General Manager - Information Technology", "ManagerIT", "Head - Technology, India", "Manager  Information Technology", 
        "Infrastructure Architect", "Manager IT", "Analyst", "Chief Manager", "Senior Manager - IT", "Assistant General Manager - IT", 
        "IT Manager", "Manager - IT", "Head - Security", "Head- IT", "Founder & CEO", "Executive Director & Head IT", "Manager", 
        "Cloud Administrator", "Manager  HR", "Manager - IT", "Manager", "Deputy Manager - IT", "Manager - IT", "Product Manager", 
        "Sr. Vice President", "Web Developer", "SAP Consultant", "Solution Architect", "Senior Solution Architect", "Lead Technical architect", 
        "Devops Engineer", "Consultant IT", "Solution Architect", "Principal Architect", "Architect", "General Manager", "REGIONAL MANAGER", 
        "Offering Manager", "Head Of Product Management and Project Management", "Software Development Engineer", "Test Engineer", 
        "Senior Executive Systems", "Director Business Development", "Engineer Piping Layout", "Senior Engineer", "Technology Associate", 
        "Business Analyst", "Senior Manager - IT", "Deputy General Manager", "Senior Vice President - Corporate Communications", 
        "Vice President", "Assistant Vice President - Engineering", "General Manager - Lead Litigation", "VP - Marketing", 
        "Vice President - IT", "Chief Information Officer", "Head - Program", "Director Sales", "Head - Analytics GTM", 
        "Senior Vice President - IT", "Head Sales", "Vice President - IT", "Head - IT", "Senior Vice President", "Head - Presales & Product Propositions", 
        "Head - IT", "Head - Projects & Technical Services", "Head - Project", "Head - Marketing", "Head ­ IT", "IT QA - Global Solution Delivery", 
        "Manager - IT"
    ]
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
