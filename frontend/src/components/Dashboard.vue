<template>
    <div class="dashboard"> 
        <h2>Dashboard</h2>
        <button @click="signoutUser">Sign Out</button>
        <RandomStringDisplay />
    </div>
</template>

<script>
    import { signout } from "../services/authServices"
    import RandomStringDisplay from "./RandomStringDisplay.vue"

export default {
    name: "Dashbaord",
    components: {RandomStringDisplay},
    methods: {
        async signoutUser() {
            try {
                const result = await signout();
                console.log(result.message)
                this.$router.push({'name':"Login"})
            }
            catch (error) {
                console.error("Sign out error", error);
            }
        }
    }
};
</script>