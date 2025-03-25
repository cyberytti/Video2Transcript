// static/script.js
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('upload-form');
    const progressBarContainer = document.querySelector('.progress-container');
    const progressBar = document.querySelector('.progress-bar');
    const progressText = document.querySelector('.progress-text');
    const resultsDiv = document.getElementById('results');
    const messageP = document.getElementById('message');
    const downloadLink = document.getElementById('download-link');
    const errorMessageDiv = document.getElementById('error-message');

    form.addEventListener('submit', function(e) {
        e.preventDefault();

        // Reset UI
        progressBar.style.width = '0%';
        progressText.textContent = 'Processing...';
        progressBarContainer.style.display = 'block';
        resultsDiv.style.display = 'none';
        downloadLink.style.display = 'none';
        errorMessageDiv.style.display = 'none';


        const formData = new FormData(form);

        fetch('/process', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            // Simulate progress (replace with actual progress if possible)
            let progress = 0;
            const interval = setInterval(() => {
                progress += 10;
                progressBar.style.width = `${progress}%`;
                if (progress >= 100) {
                    clearInterval(interval);
                    //progressText.textContent = 'Complete!'; // Don't set to complete here, wait for the actual response
                }
            }, 200); // Adjust interval as needed

            return response.json();
        })
        .then(data => {
            progressBarContainer.style.display = 'none'; // Hide progress bar
            progressText.textContent = 'Complete!';

            if (data.success) {
                resultsDiv.style.display = 'block';
                messageP.textContent = 'Processing complete!';
                downloadLink.href = data.download_url;
                downloadLink.style.display = 'inline-block';
            } else {
                errorMessageDiv.textContent = data.error || 'An unknown error occurred.';
                errorMessageDiv.style.display = 'block';
            }
        })
        .catch(error => {
            progressBarContainer.style.display = 'none';
            errorMessageDiv.textContent = 'An error occurred: ' + error;
            errorMessageDiv.style.display = 'block';
            console.error('Error:', error);
        });
    });
});