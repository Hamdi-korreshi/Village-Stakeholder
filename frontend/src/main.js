import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
<<<<<<< HEAD
import router from './components/router/index.js';

const app = createApp(App);
app.use(router);  // Enable Vue Router
app.mount('#app');
=======
import axios from 'axios'
import router from './router/index'
axios.defaults.withCredentials = true;

createApp(App).use(router).mount('#app')
>>>>>>> origin
