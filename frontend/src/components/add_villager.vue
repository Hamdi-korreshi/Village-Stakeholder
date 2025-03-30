<template>
  <button @click="addVillager" class="add-button">
    Add Villager
  </button>
</template>

<script>
import { addVillagerToVillage } from "../services/villageServices.js";

export default {
  name: "AddVillagerButton",
  props: {
    userId: {
      type: Number,
      required: true,
    },
    associateId: {
      type: Number,
      required: true,
    },
    relationId: {
      type: Number,
      required: true,
    },
  },
  methods: {
    async addVillager() {
      try {
        const response = await addVillagerToVillage(this.userId, this.associateId, this.relationId);
        console.log("Villager added successfully:", response);
        alert("Villager added!");
      } catch (error) {
        console.error("Error adding villager:", error);
        alert("Failed to add villager.");
      }
    },
  },
};
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
