<template>
  <div class="min-h-screen bg-gray-100 flex flex-col items-center justify-center p-4">
    <h1 class="text-4xl font-bold text-blue-600 mb-4">
      Welcome to My Vue + Django App
    </h1>
    <p class="text-lg text-gray-700">
      {{ message }}
    </p>
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