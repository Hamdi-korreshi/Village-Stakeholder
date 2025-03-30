<template>
  <button @click="createVillage" class="create-button">
    Create Village
  </button>
</template>

<script>
import axios from 'axios'

export default {
  name: 'MakeVillageButton',
  props: {
    ownerId: {
      type: Number,
      required: true
    },
    description: {
      type: String,
      default: "This is your village."
    }
  },
  methods: {
    async createVillage() {
      try {
        const response = await axios.post('http://localhost:8000/village/v1/create-village/', {
          owner: this.ownerId,
          description: this.description
        });
        console.log('Village created successfully:', response.data);
        alert('Village created!');
      } catch (error) {
        console.error('Error creating village:', error);
        alert('Failed to create village.');
      }
    }
  }
}
</script>

<style scoped>
.create-button {
  padding: 10px 20px;
  background-color: #2196F3;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
}
.create-button:hover {
  background-color: #1976D2;
}
</style>