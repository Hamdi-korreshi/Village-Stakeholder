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
import apiClient from "../utils/axios.js";

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
                const response = await apiClient.get(`/village/v1/random-string`);
                this.testData = response.data;
            } catch (error) {
                console.error("Error fetching random string", error);
            }
        },
    },
};
</script>
