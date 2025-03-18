import axios, { AxiosResponse, AxiosError } from 'axios';

const app = document.getElementById('app');

if (app) {
    app.innerHTML = '<h1>Hello, Telegram WebApp!</h1>';

    axios.get('/api/data')
        .then((response: AxiosResponse) => {
            app.innerHTML += `<p>Data from backend: ${response.data.message}</p>`;
        })
        .catch((error: AxiosError) => {
            console.error('Error fetching data:', error.message);
        });
}