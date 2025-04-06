document.getElementById('upload-form').addEventListener('submit', function(event) {
  event.preventDefault();
  const formData = new FormData();
  const fileInput = document.getElementById('file-input');
  formData.append('file', fileInput.files[0]);

  fetch('/upload', {
      method: 'POST',
      body: formData
  })
  .then(response => response.json())
  .then(data => {
      const resultDiv = document.getElementById('upload-result');
      if (data.error) {
          resultDiv.textContent = data.error;
      } else {
          resultDiv.textContent = 'Extracted Text: ' + data.text;
      }
  })
  .catch(error => {
      console.error('Error:', error);
  });
});

document.getElementById('search-button').addEventListener('click', function() {
  const query = document.getElementById('search-input').value;
  fetch(`/search?query=${query}`)
  .then(response => response.json())
  .then(data => {
      const resultsDiv = document.getElementById('search-results');
      resultsDiv.innerHTML = '';
      data.results.forEach(result => {
          const li = document.createElement('li');
          li.textContent = result;
          resultsDiv.appendChild(li);
      });
  })
  .catch(error => {
      console.error('Error:', error);
  });
});