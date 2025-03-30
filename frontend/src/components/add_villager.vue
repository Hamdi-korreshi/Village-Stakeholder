<template>
  <button @click="addVillager" class="add-button">
    Add Villager
  </button>
</template>

<script>
import axios from 'axios';
import { get_my_village } from "../services/authServices.js";

export default {
  name: 'AddVillagerButton',
  props: {
    userId: {
      type: Number,
      required: true
    },
    associateId: {
      type: Number,
      required: true
    },
    relationId: {
      type: Number,
      required: true
    }
  },
  methods: {
    async addVillager() {
      try {
        const response = await axios.post('', {
          user: this.userId,
          associate: this.associateId,
          relation: this.relationId,
          status: 'pending'
        });
        console.log('Villager added successfully:', response.data);
        alert('Villager added!');
      } catch (error) {
        console.error('Error adding villager:', error);
        alert('Failed to add villager.');
      }
    }
  }
}
</script>

<style scoped>
.add-button {
  padding: 10px 20px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
}
.add-button:hover {
  background-color: #45a049;
}
</style>