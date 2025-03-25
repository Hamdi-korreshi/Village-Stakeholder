<template>
    <form @submit.prevent="submitRegistration" class="register-form">
        <div>
            <label for="email">Email:</label>
            <input type="email" id="email" v-model="email" required/>
        </div>
        <div>
            <label for="username">Username:</label>
            <input type="username" id="username" v-model="username" required />
        </div>
        <div>
            <label for="password">Password:</label>
            <input type="password" id="password" v-model="password" required />
        </div>
        <button type="submit">Register</button>
        <p v-if="errorMessage" class="error">{{errorMessage}}</p>
    </form> 
</template>

<script>
import { register } from '../services/authServices.js'

export default {
    name: "RegisterForm",
    data() {
        return {
            email: "",
            username: "",
            password: "",
            errorMessage: ""  
        };
    },
    methods: {
        async submitRegistration() {
            try {
                const result = await register(this.email, this.username, this.password);
                if (result.message === "User registered successfully") {
                    this.$emit("registration-success");
                } 
                else {
                    this.errorMessage = result.error || "Registration failed.";
                }
            }
            catch (error) {
                this.errorMessage = "Registration failed please check your input";
                console.error("Registration error:", error);
            }
        }
    }
}
</script>
