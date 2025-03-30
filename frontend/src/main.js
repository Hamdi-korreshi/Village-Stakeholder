import { createApp } from 'vue'
import { createPinia } from "pinia"
import { createPersistedState } from 'pinia-plugin-persistedstate'
import './style.css'
import App from './App.vue'
import router from './router/index.js';
import axios from 'axios'
//import router from './router/index'
axios.defaults.withCredentials = true;
const pinia = createPinia();
pinia.use(createPersistedState())

const app = createApp(App);
app.use(router);
app.use(pinia)
app.mount('#app');
