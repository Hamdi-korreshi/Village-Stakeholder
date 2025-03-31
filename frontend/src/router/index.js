// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import Home from '../components/Home.vue';
import Login from '../components/login.vue';
import Registration from '../components/registration.vue';
import Profile from '../components/profile.vue';
import PasswordReset from '../components/passwordReset.vue';
import EmailVerification from '../components/emailVerification.vue';
import Calendar from '../components/CalendarPage/components/CalendarScheduling.vue';
import Dashboard from '../components/Dashboard.vue';
import { store_user_info } from "../utils/stores.js";


const routes = [
  { path: '/', 
    name: "Home",
    component: Home },
  { path: '/login', name: 'login', component: Login },
  { path: '/registration', 
    name: "Regstration",
    component: Registration, meta: { requiresGuest: true } },
  { path: '/profile', component: Profile, meta: { requiresAuth: true } },
  { path: '/passwordReset', component: PasswordReset },
  { path: '/emailVerification', component: EmailVerification },
  { path: '/calendar', component: Calendar, meta: { requiresAuth: true } },
  { path: '/dashboard', name: 'Dashboard', component: Dashboard, meta: { requiresAuth: true } },
]

const router = createRouter({ 
  history: createWebHistory(),
  routes,
})

router.beforeEach((to, from, next) => {
    const user_store = store_user_info();
    if (to.matched.some(record => record.meta.requiresAuth)) {
      if (!user_store.user) {
        next({ name: 'login' });
      } else {
        next();
      }
    } else {
      next();
    }
  });

export default router;