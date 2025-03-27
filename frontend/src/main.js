import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './components/router/index.js';

const app = createApp(App);
app.use(router);  // Enable Vue Router
app.mount('#app');
