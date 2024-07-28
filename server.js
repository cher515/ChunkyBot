// Sample internship data (replace with your CSV data)
const internships = [
  {
      title: "Software Engineering Intern",
      company: "Tech Solutions Inc.",
      industry: "Technology",
      role: "software_engineering",
      salary: "$25-$35 /h",
      location: "San Francisco, CA"
  },
  {
      title: "Data Science Intern",
      company: "Data Insights Co.",
      industry: "Data Analytics",
      role: "data_science",
      salary: "$22-$30 /h",
      location: "New York, NY"
  },
  {
      title: "Product Management Intern",
      company: "ProductPro",
      industry: "Software",
      role: "product_management",
      salary: "$20-$28 /h",
      location: "Seattle, WA"
  },
  // Add more internship objects here
];

function displayInternships(internshipsToShow) {
  const internshipList = document.getElementById('internshipList');
  internshipList.innerHTML = '';
  internshipsToShow.forEach(internship => {
      const internshipElement = document.createElement('div');
      internshipElement.className = 'internship';
      internshipElement.innerHTML = `
          <h3>${internship.title}</h3>
          <p><strong>Company:</strong> ${internship.company}</p>
          <p><strong>Industry:</strong> ${internship.industry}</p>
          <p><strong>Role:</strong> ${internship.role.replace('_', ' ')}</p>
          <p><strong>Salary:</strong> ${internship.salary}</p>
          <p><strong>Location:</strong> ${internship.location}</p>
      `;
      internshipList.appendChild(internshipElement);
  });
}

function init() {
  displayInternships(internships);
  populateFilters();
}

function populateFilters() {
  const industryFilter = document.getElementById('industryFilter');
  const locationFilter = document.getElementById('locationFilter');

  const industries = [...new Set(internships.map(internship => internship.industry))];
  const locations = [...new Set(internships.map(internship => internship.location))];

  populateSelect(industryFilter, industries);
  populateSelect(locationFilter, locations);
}

function populateSelect(selectElement, options) {
  options.forEach(option => {
      const optionElement = document.createElement('option');
      optionElement.value = option;
      optionElement.textContent = option;
      selectElement.appendChild(optionElement);
  });
}

function applyFilters() {
  const searchTerm = document.getElementById('searchInput').value.toLowerCase();
  const selectedIndustry = document.getElementById('industryFilter').value;
  const selectedRole = document.getElementById('roleFilter').value;
  const selectedLocation = document.getElementById('locationFilter').value;

  const filteredInternships = internships.filter(internship => 
      internship.title.toLowerCase().includes(searchTerm) &&
      (selectedIndustry === '' || internship.industry === selectedIndustry) &&
      (selectedRole === '' || internship.role === selectedRole) &&
      (selectedLocation === '' || internship.location === selectedLocation)
  );

  displayInternships(filteredInternships);
}

async function sendToChatbot() {
  const userInput = document.getElementById('userInput').value;
  const chatbotOutput = document.getElementById('chatbotOutput');
  const apiKey = document.getElementById('apiKeyInput').value;

  if (!apiKey) {
      alert('Please enter your OpenAI API key.');
      return;
  }

  chatbotOutput.innerHTML += `<p><strong>You:</strong> ${userInput}</p>`;

  try {
      const response = await fetch('https://api.openai.com/v1/chat/completions', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
              'Authorization': `Bearer ${apiKey}`
          },
          body: JSON.stringify({
              model: "gpt-3.5-turbo",
              messages: [{role: "user", content: userInput}]
          })
      });

      const data = await response.json();
      const aiResponse = data.choices[0].message.content;

      chatbotOutput.innerHTML += `<p><strong>AI:</strong> ${aiResponse}</p>`;
  } catch (error) {
      console.error('Error:', error);
      chatbotOutput.innerHTML += `<p><strong>AI:</strong> Sorry, I encountered an error. Please check your API key and try again.</p>`;
  }

  document.getElementById('userInput').value = '';
  chatbotOutput.scrollTop = chatbotOutput.scrollHeight;
}

async function uploadResume() {
  const resumeUpload = document.getElementById('resumeUpload');
  const chatbotOutput = document.getElementById('chatbotOutput');
  const apiKey = document.getElementById('apiKeyInput').value;

  if (!apiKey) {
      alert('Please enter your OpenAI API key.');
      return;
  }

  if (resumeUpload.files.length > 0) {
      const file = resumeUpload.files[0];
      const reader = new FileReader();

      reader.onload = async function(e) {
          const resumeText = e.target.result;
          chatbotOutput.innerHTML += `<p><strong>AI:</strong> Analyzing your resume...</p>`;

          try {
              const response = await fetch('https://api.openai.com/v1/chat/completions', {
                  method: 'POST',
                  headers: {
                      'Content-Type': 'application/json',
                      'Authorization': `Bearer ${apiKey}`
                  },
                  body: JSON.stringify({
                      model: "gpt-3.5-turbo",
                      messages: [{
                          role: "user", 
                          content: `Analyze this resume and suggest suitable internships based on the candidate's skills and experience: ${resumeText}`
                      }]
                  })
              });

              const data = await response.json();
              const aiResponse = data.choices[0].message.content;

              chatbotOutput.innerHTML += `<p><strong>AI:</strong> ${aiResponse}</p>`;
          } catch (error) {
              console.error('Error:', error);
              chatbotOutput.innerHTML += `<p><strong>AI:</strong> Sorry, I encountered an error while analyzing your resume. Please try again later.</p>`;
          }

          chatbotOutput.scrollTop = chatbotOutput.scrollHeight;
      };

      reader.readAsText(file);
  } else {
      alert('Please select a file to upload.');
  }
}

window.onload = init;


function applyFilters() {
  const searchInput = document.getElementById('searchInput').value;
  const industry = document.getElementById('industryFilter').value;
  const role = document.getElementById('roleFilter').value;
  const location = document.getElementById('locationFilter').value;

  fetch('/api/data', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
      },
      body: JSON.stringify({
          searchInput: searchInput,
          industry: industry,
          role: role,
          location: location
      })
  })
  .then(response => response.json())
  .then(data => {
      console.log('Data:', data);
      // Process and display data here
  })
  .catch(error => console.error('Error:', error));
}

function sendToChatbot() {
  const userInput = document.getElementById('userInput').value;

  fetch('/api/chatbot', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message: userInput })
  })
  .then(response => response.json())
  .then(data => {
      document.getElementById('chatbotOutput').textContent = data.reply;
  })
  .catch(error => console.error('Error:', error));
}