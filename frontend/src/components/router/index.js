// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import Home from '../Home.vue';
import Login from '../login.vue';
import Registration from '../registration.vue';
import Profile from '../profile.vue';
import PasswordReset from '../passwordReset.vue';
import EmailVerification from '../emailVerification.vue';
import Calendar from '../CalendarPage/components/CalendarScheduling.vue';
import Dashboard from '../Dashboard.vue';

const routes = [
  { path: '/', component: Home },
  { path: '/login', name: 'login', component: Login },
  { path: '/registration', component: Registration },
  { path: '/profile', component: Profile },
  { path: '/passwordReset', component: PasswordReset },
  { path: '/emailVerification', component: EmailVerification },
  { path: '/calendar', component: Calendar },
  { path: '/Dashboard', name: 'Dashboard', component: Dashboard },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;