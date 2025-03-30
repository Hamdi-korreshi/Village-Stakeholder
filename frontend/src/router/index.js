import { createRouter, createWebHistory } from "vue-router"
import LoginPage from '../components/LoginPage.vue'
import Dashboard from '../components/Dashboard.vue'
import RegisterPage from '../components/RegisterPage.vue'
import TestAxios from '../components/TestAxios.vue'
import CalendarScheduling from '../components/CalendarPage/components/CalendarScheduling.vue'
import TutorialPage from '../components/TutorialPage/components/MainLayout.vue'
import SettingsPage from '../components/SettingsPage/components/MainLayout.vue'
import HomePage from '../components/HomePage/components/UserVillage.vue'
import ManageMembersPage from '../components/ManageMembers/components/ManageMembers.vue'
import ChangePassword from '../components/ChangePassword.vue'
import { store_user_info } from "../utils/stores.js"

const routes = [
    {
        path: '/login',
        name: 'Login',
        component: LoginPage
    },
    {
        path: '/calendar',
        name: 'Calendar',
        component: CalendarScheduling,
    },
    {
        path: '/tutorial',
        name: 'Tutorial',
        component: TutorialPage,
    },
    {
        path: '/settings',
        name: 'Settings',
        component: SettingsPage,
    },
    {
        path: '/home',
        name: 'Home',
        component: HomePage,
    },
    {
        path: '/manage',
        name: 'Manage Members',
        component: ManageMembersPage,
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
        path: '/change-pass',
        name: 'Change-password',
        component: ChangePassword,
        meta: { requiresAuth: true }    
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
