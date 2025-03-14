import { createRouter, createWebHistory } from "vue-router"
import LoginPage from '../components/LoginPage.vue'
import Dashboard from '../components/Dashboard.vue'

const routes = [
    {
        path: '/login',
        name: 'Login',
        component: LoginPage
    },
    {
        path: '/dashboard',
        name: 'Dashboard',
        component: Dashboard
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

export default router
