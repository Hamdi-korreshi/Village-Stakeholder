<template>
    <div class="register-page">
        <h2>Register</h2>
        <RegisterForm @registration-success="onRegisterSuccess"/>
        <p>
            Already have an account?
            <router-link to="/login">Login here</router-link>
        </p>
    </div>
</template>

<script>
import RegisterForm from './RegisterForm.vue';
console.log("API_URL:", import.meta.env.VITE_API_URL)
export default {
    name: "RegisterPage",
    components: { RegisterForm },
    methods: {
        // makes the user go to login after successful registration
        onRegisterSuccess() {
            this.$router.push({name: 'Login'})
        },
    },
};
</script>
