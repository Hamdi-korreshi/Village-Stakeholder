import { createRouter, createWebHistory } from "vue-router"
import Home from '../components/Home.vue'
import Login from '../components/login.vue'
import Dashboard from '../components/Dashboard.vue'
import Registration from '../components/registration.vue'
import TestAxios from '../components/TestAxios.vue'
import CalendarScheduling from '../components/CalendarPage/components/CalendarScheduling.vue'
import Profile from '../components/profile.vue'
import PasswordReset from "../components/passwordReset.vue"
import TutorialPage from '../components/TutorialPage/components/MainLayout.vue'
import EmailVerification from "../components/emailVerification.vue"
import SettingsPage from '../components/SettingsPage/components/MainLayout.vue'
import HomePage from '../components/Home.vue'
import ManageMembersPage from '../components/ManageMembers/components/ManageMembers.vue'
import ChangePassword from '../components/ChangePassword.vue'
import Village from '../components/HomePage/components/UserVillage.vue'
import { store_user_info } from "../utils/stores.js"
import DeleteProfile from '../components/DeleteProfile.vue'

const routes = [
    {
        path: '/login',
        name: 'Login',
        component: Login
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
        path: '/manage',
        name: 'ManageMembers',
        component: ManageMembersPage,
    },
    {
      path: '/passwordReset',
      name: 'PasswordReset',
      component: PasswordReset,
    },
    {
      path: '/emailVerification',
      name: 'EmailVerification',
      component: EmailVerification,
    },
    {
        path: '/registration',
        name: 'Registration',
        component: Registration,
        meta: { requiresGuest: true }
    },
    {
        path: '/dashboard',
        name: 'Dashboard',
        component: Dashboard,
        meta: { requiresAuth: true }
    },
    {
      path: '/profile',
      name: 'Profile',
      component: Profile,
      meta: { requiresAuth: true }
    },
    {
      path: '/village',
      name: 'Village',
      component: Village,
      meta: { requiresAuth: true }
    },
    {
        path: '/change-pass',
        name: 'Change-password',
        component: ChangePassword,
        meta: { requiresAuth: true }    
    },
    {
        path: '/delete-profile',
        name: 'Delete-profile',
        component: DeleteProfile,
        meta: { requiresAuth: true } 
    },
    {
        path: '/Home',
        name: 'Home', 
        component: Home,
    }
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