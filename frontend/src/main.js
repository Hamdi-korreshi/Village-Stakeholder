import { createApp } from 'vue'
import { createPinia } from "pinia"
import { createPinia } from 'pinia'
import { createPersistedState } from 'pinia-plugin-persistedstate'
import './style.css'
import App from './App.vue'
import router from './components/router/index.js';
import axios from 'axios'
import router from './router/index'
axios.defaults.withCredentials = true;
const pinia = createPinia();
pinia.use(createPersistedState())

const app = createApp(App);
app.use(createPinia());
app.use(router);  // Enable Vue Router
app.mount('#app');
createApp(App).use(router).use(pinia).mount('#app')
