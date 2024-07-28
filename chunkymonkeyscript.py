import pandas as pd

# Read the CSV file
file_path = 'swe.csv'  # Change this to the path of your CSV file
df = pd.read_csv(file_path)

# Define CSS styles (unchanged)
css = '''
<style>
    :root {
        --primary-color: #3498db;
        --secondary-color: #2c3e50;
        --background-color: #ecf0f1;
        --text-color: #34495e;
    }

    body {
        font-family: 'Arial', sans-serif;
        line-height: 1.6;
        margin: 0;
        padding: 0;
        background-color: var(--background-color);
        color: var(--text-color);
    }

    .container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 20px;
    }

    h1, h2 {
        color: var(--secondary-color);
        text-align: center;
    }

    #filters {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        margin-bottom: 20px;
        background-color: #fff;
        padding: 15px;
        border-radius: 5px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    #filters input, #filters select {
        padding: 10px;
        border: 1px solid #ddd;
        border-radius: 4px;
        font-size: 16px;
    }

    #filters button {
        padding: 10px 20px;
        background-color: var(--primary-color);
        color: white;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        transition: background-color 0.3s;
    }

    #filters button:hover {
        background-color: #2980b9;
    }

    #job-container {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
        gap: 20px;
    }

    .job-listing {
        background-color: #fff;
        border-radius: 5px;
        padding: 20px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        transition: transform 0.3s;
    }

    .job-listing:hover {
        transform: translateY(-5px);
    }

    .job-title {
        font-size: 1.2em;
        color: var(--primary-color);
        margin-bottom: 10px;
    }

    .company {
        font-weight: bold;
        color: var(--secondary-color);
    }

    .location, .salary {
        color: #7f8c8d;
        font-size: 0.9em;
    }

    .description {
        margin-top: 10px;
        font-size: 0.9em;
    }

    #chatbot {
        background-color: #fff;
        border-radius: 5px;
        padding: 20px;
        margin-top: 30px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    #chatbotOutput {
        height: 300px;
        overflow-y: auto;
        border: 1px solid #ddd;
        padding: 10px;
        margin-bottom: 10px;
        background-color: #f9f9f9;
        border-radius: 4px;
    }

    #userInput {
        width: calc(100% - 22px);
        padding: 10px;
        margin-bottom: 10px;
        border: 1px solid #ddd;
        border-radius: 4px;
    }

    #resumeUpload, #apiKeyInput {
        margin-top: 10px;
    }

    .button {
        padding: 10px 20px;
        background-color: var(--primary-color);
        color: white;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        transition: background-color 0.3s;
    }

    .button:hover {
        background-color: #2980b9;
    }
</style>
'''

# Create HTML content
html_content = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Job Listings</title>
    {css}
    <script>
        function applyFilters() {{
            var searchInput = document.getElementById('searchInput').value.toLowerCase();
            var industryFilter = document.getElementById('industryFilter').value.toLowerCase();
            var roleFilter = document.getElementById('roleFilter').value.toLowerCase();
            var locationFilter = document.getElementById('locationFilter').value.toLowerCase();
            var jobListings = document.getElementsByClassName('job-listing');

            for (var i = 0; i < jobListings.length; i++) {{
                var jobListing = jobListings[i];
                var titleElement = jobListing.getElementsByClassName('job-title')[0];
                var companyElement = jobListing.getElementsByClassName('company')[0];
                var locationElement = jobListing.getElementsByClassName('location')[0];
                var descriptionElement = jobListing.getElementsByClassName('description')[0];

                var title = titleElement ? titleElement.innerText.toLowerCase() : '';
                var company = companyElement ? companyElement.innerText.toLowerCase() : '';
                var location = locationElement ? locationElement.innerText.toLowerCase() : '';
                var description = descriptionElement ? descriptionElement.innerText.toLowerCase() : '';

                var matchesSearch = title.includes(searchInput) || company.includes(searchInput) || description.includes(searchInput);
                var matchesIndustry = industryFilter === "" || description.includes(industryFilter);
                var matchesRole = roleFilter === "" || title.includes(roleFilter);
                var matchesLocation = locationFilter === "" || location.includes(locationFilter);

                if (matchesSearch && matchesIndustry && matchesRole && matchesLocation) {{
                    jobListing.style.display = "";
                }} else {{
                    jobListing.style.display = "none";
                }}
            }}
        }}
    </script>
</head>
<body>
    <div class="container">
    <h1>AI-Powered Job Finder</h1>
    <div id="filters">
        <input type="text" id="searchInput" placeholder="Search jobs..." oninput="applyFilters()"/>
        <select id="industryFilter" onchange="applyFilters()">
            <option value="">All Industries</option>
            <option value="healthcare">Healthcare</option>
            <option value="finance">Finance</option>
            <option value="education">Education</option>
            <option value="technology">Technology</option>
            <option value="hospitality">Hospitality</option>
            <option value="manufacturing">Manufacturing</option>
            <option value="retail">Retail</option>
            <option value="government">Government</option>
            <option value="entertainment">Entertainment</option>
            <option value="energy">Energy</option>
        </select>
        <select id="roleFilter" onchange="applyFilters()">
            <option value="">All Roles</option>
            <option value="software engineer">Software Engineering</option>
            <option value="data scientist">Data Science</option>
            <option value="product manager">Product Management</option>
            <option value="designer">Design</option>
            <option value="marketing">Marketing</option>
        </select>
        <select id="locationFilter" onchange="applyFilters()">
            <option value="">All Locations</option>
            <option value="new york">New York, USA</option>
            <option value="london">London, UK</option>
            <option value="tokyo">Tokyo, Japan</option>
            <option value="sydney">Sydney, Australia</option>
            <option value="toronto">Toronto, Canada</option>
            <option value="berlin">Berlin, Germany</option>
            <option value="sao paulo">São Paulo, Brazil</option>
            <option value="mumbai">Mumbai, India</option>
            <option value="beijing">Beijing, China</option>
            <option value="cape town">Cape Town, South Africa</option>
        </select>
    </div>
</div>

        <div id="job-container">
'''


# Function to add a job listing field
def add_job_field(column, value):
    if column.lower() == 'title':
        return f'<div class="job-title">{value}</div>'
    elif column.lower() == 'company':
        return f'<div class="company">{value}</div>'
    elif column.lower() == 'location':
        return f'<div class="location">{value}</div>'
    elif column.lower() == 'apply':
        return f'<div class="apply"><a href="{value}" target="_blank">Apply Now</a></div>'
    elif column.lower() == 'description':
        return f'<div class="description">{value}</div>'
    else:
        return f'<div>{column}: {value}</div>'


# Add job listings dynamically
for _, job in df.iterrows():
    html_content += '<div class="job-listing">'
    for column in df.columns:
        html_content += add_job_field(column, job[column])
    html_content += '</div>'

html_content += '''
        </div>
        <div id="chatbot">
            <h2>AI Chatbot</h2>
            <div id="chatbotOutput"></div>
            <input type="text" id="userInput" placeholder="Tell me about your experience..." />
            <button onclick="sendToChatbot()" class="button">Send</button>
            <input type="file" id="resumeUpload" accept=".pdf,.doc,.docx" />
            <button onclick="uploadResume()" class="button">Upload Resume</button>
        </div>
    </div>
</body>
</html>
'''

# Save the HTML to a file
with open('index.html', 'w') as f:
    f.write(html_content)

print("HTML file with styled job listings has been created: index.html")
