<template>
  <button @click="testRequest">Test Axios</button>
</template>

<script setup>
import apiClient from "../utils/axios";

async function testRequest() {
  try {
    const res = await apiClient.get("village/v1/csrf/");
    console.log("Test response:", res.data);
  } catch (err) {
    console.error("Axios Test Error:", err);
  }
}
</script>