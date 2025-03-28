import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import axios from 'axios'
import router from './router/index'
axios.defaults.withCredentials = true;

createApp(App).use(router).mount('#app')
