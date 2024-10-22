document.addEventListener('DOMContentLoaded', function() {
    fetch('/api/ipinfo')
        .then(response => response.json())
        .then(data => {
            const ipInfoDiv = document.getElementById('ip-info');
            if (data.error) {
                ipInfoDiv.textContent = `Error: ${data.error}`;
            } else {
                ipInfoDiv.innerHTML = `
                    <p><strong>IP Address:</strong> ${data.ip}</p>
                    <p><strong>City:</strong> ${data.city}</p>
                    <p><strong>Region:</strong> ${data.region}</p>
                    <p><strong>Country:</strong> ${data.country_name}</p>
                    <p><strong>ISP:</strong> ${data.org}</p>
                `;
            }
        })
        .catch(error => {
            const ipInfoDiv = document.getElementById('ip-info');
            ipInfoDiv.textContent = `Error fetching IP information: ${error}`;
        });
});