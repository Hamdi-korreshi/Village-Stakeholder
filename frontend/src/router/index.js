import { createRouter, createWebHistory } from "vue-router"
import LoginPage from '../components/LoginPage.vue'
import Dashboard from '../components/Dashboard.vue'
import RegisterPage from '../components/RegisterPage.vue'
import TestAxios from '../components/TestAxios.vue'
import ChangePassword from '../components/ChangePassword.vue'
import { store_user_info } from "../utils/stores.js"

const routes = [
    {
        path: '/login',
        name: 'Login',
        component: LoginPage
    },
    {
        path: '/register',
        name: 'Register',
        component: RegisterPage,
        meta: { requiresGuest: true }
    },
    {
        path: '/dashboard',
        name: 'Dashboard',
        component: Dashboard,
        meta: { requiresAuth: true }
    },
    {
        path: '/test-axios',
        name: 'TestAxios',
        component: TestAxios,
    },
    {
        path: '/change-pass',
        name: 'Change-password',
        component: ChangePassword
    },
    {
        path: '/',
        redirect: '/login'
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

router.beforeEach((to, from, next) => {
    const user_store = store_user_info();
    if (to.matched.some(record => record.meta.requiresAuth)) {
      if (!user_store.user) {
        next({ name: 'Login' });
      } else {
        next();
      }
    } else {
      next();
    }
  });

export default router
