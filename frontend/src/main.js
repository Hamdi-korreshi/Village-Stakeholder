import { createApp } from 'vue'
import { createPinia } from 'pinia'
import './style.css'
import App from './App.vue'
import axios from 'axios'
import router from './router/index'
axios.defaults.withCredentials = true;
const pinia = createPinia();

createApp(App).use(router).use(pinia).mount('#app')
