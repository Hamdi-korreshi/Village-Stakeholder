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
const routes = [
    {
        path: '/login',
        name: 'Login',
        component: LoginPage,
        meta: { requiresGuest: true }
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
        path: '/test-axios',
        name: 'TestAxios',
        component: TestAxios,
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

// router.beforeEach((to,form,next) => {
//     const isLoggedIn = false;

//     if (to.meta.requiresAuth && !isLoggedIn) {
//         next({ name: 'Login' });
//       } else if (to.meta.requiresGuest && isLoggedIn) {
//         next({ name: 'Dashboard' });
//       } else {
//         next();
//       }
// });

export default router
