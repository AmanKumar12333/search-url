// script.js
document.getElementById('fetch-btn').addEventListener('click', () => {
    const url = document.getElementById('url-input').value;
    fetch('http://127.0.0.1:5000/fetch-product', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ url })
        })
        .then(response => response.json())
        .then(data => {
            const productDetails = document.getElementById('product-details');
            productDetails.innerHTML = '';
            if (data.error) {
                productDetails.innerHTML = `<p>Error: ${data.error}</p>`;
            } else {
                productDetails.innerHTML = `
                <h2>${data.title}</h2>
                <p><strong>Price:</strong> ${data.price}</p>
                <p><strong>Description:</strong> ${data.description}</p>
            `;
            }
        })
        .catch(error => {
            const productDetails = document.getElementById('product-details');
            productDetails.innerHTML = `<p>Error: ${error}</p>`;
        });
});