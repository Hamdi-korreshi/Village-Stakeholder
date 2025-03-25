// utils/axios.js
import axios from 'axios';

const apiClient = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  withCredentials: true,
  headers: {
    'Content-Type': 'application/json'
  },
});

// Axios interceptor to automatically set CSRF Token
apiClient.interceptors.request.use(
  async (config) => {
    // Ensure you have the CSRF token cookie from Django
    const csrfToken = getCookie('csrftoken');
    if (!csrfToken) {
      // Fetch CSRF token explicitly from Django backend
      await axios.get(`${import.meta.env.VITE_API_URL}/csrf/`, {
        withCredentials: true
      });
      config.headers['X-CSRFToken'] = getCookie('csrftoken');
    } else {
      config.headers['X-CSRFToken'] = csrfToken;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// Utility function to read cookies
function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}

export default apiClient;
