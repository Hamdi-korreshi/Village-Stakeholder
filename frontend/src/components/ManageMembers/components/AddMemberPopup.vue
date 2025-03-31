<template>
    <Teleport to="body">
      <div
        v-if="modelValue"
        class="fixed inset-0 bg-gray-200 bg-opacity-70 flex items-center justify-center z-50"
        @click="$emit('update:modelValue', false)"
      >
        <div class="bg-white rounded-xl p-6 w-[400px] shadow-lg" @click.stop>
          <h2 class="text-2xl font-bold mb-4 text-black">Add New Member</h2>
          <form @submit.prevent="handleSubmit" class="space-y-4 ">
            <div>
              <label
                for="username"
                class="block text-sm font-medium text-gray-700 mb-1"
              >
                Username
              </label>
              <input
                id="username"
                type="text"
                v-model="username"
                class="w-full px-4 py-2 border text-black border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent outline-none"
                placeholder="Enter username"
                required
              />
            </div>
            <div>
              <label
                for="role"
                class="block text-sm font-medium text-gray-700 mb-1"
              >
                Role
              </label>
              <select
                id="role"
                v-model="selectedRole"
                class="w-full text-black px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent outline-none bg-white"
                required
              >
                <option value="" disabled>Select a role</option>
                <option v-for="role in roles" :key="role" :value="role">
                  {{ role }}
                </option>
              </select>
            </div>
            <div class="flex justify-end gap-3 mt-6">
              <button
                type="button"
                class="px-4 py-2 text-white hover:bg-gray-100 rounded-lg transition-colors"
                @click="$emit('update:modelValue', false)"
                style="background-color: #ef4444;"
              >
                Cancel
              </button>
              <button
                type="submit"
                class="px-4 py-2 bg-green-500 text-white rounded-lg hover:bg-green-600 transition-colors"
                style="background-color: #4472C4;"
              >
                Add Member
              </button>
            </div>
          </form>
        </div>
      </div>
    </Teleport>
  </template>
  
  <script setup>
  import { ref } from "vue";
  
  const props = defineProps({
    modelValue: {
      type: Boolean,
      required: true,
    },
  });
  
  const emit = defineEmits(["update:modelValue", "add"]);
  
  const username = ref("");
  const selectedRole = ref("");
//   const roles = ["Admin", "Editor", "Viewer", "Contributor"];
const roles = [
        ("academic", "Academic"),
        ("family", "Family"),
        ("college", "College"),
        ("trade_school", "Trade School"),
        ("workforce_recruiter", "Workforce Recruiter"),
        ("health_advisor", "Health Advisor"),
        ("religion_advisor", "Religion Advisor"),
        ("close_friend", "Close Friend"),
        ("mentor", "Mentor"),
    ]
  
  const handleSubmit = () => {
    if (username.value.trim() && selectedRole.value) {
      emit("add", {
        username: username.value.trim(),
        // role: selectedRole.value,
        role: selectedRole.value,
      });
      username.value = "";
      selectedRole.value = "";
      emit("update:modelValue", false);
    }
  };
  </script>
  