<template>
  <div>
    <h1>Welcome to My Vue + Django App</h1>
    <p>{{ message }}</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const message = ref('')

onMounted(async () => {
  try {
    const response = await axios.get('/api/hello/')
    message.value = response.data.message
  } catch (error) {
    console.error(error)
  }
})
</script>