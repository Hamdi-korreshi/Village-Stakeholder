<template>
    <div clas="random-string-display"> 
        <button @click="fetchRandomString">Get Random String</button>
        <div v-if="testData">
            <p>Name: {{testData.name }}</p>
            <p>Value: {{ testData.value }}</p>
            <p>Created At: {{ testData.created_at }} </p>
        </div>
    </div>
</template>

<script>
import axios from "axios";
const API_URL = import.meta.env.VITE_API_URL;

export default {
    name: "RandomStringDisplay",
    data() {
        return {
            testData: null,
        };
    },
    methods: {
        async fetchRandonmString() {
            try {
                const response = await axios.get(`${API_URL}/village/v1/random-string`);
                this.testData = response.data;
            } catch (error) {
                console.error("Error fetching random string", error);
            }
        },
    },
};
</script>
