<template>
    <Teleport to="body">
      <div
        v-if="modelValue"
        class="fixed inset-0 bg-gray-200 bg-opacity-70 flex items-center justify-center z-50"
        @click="$emit('update:modelValue', false)"
      >
        <div class="bg-white rounded-xl p-6 w-[400px] shadow-lg" @click.stop>
          <h2 class="text-2xl font-bold mb-4 text-black">Remove Member</h2>
          <form @submit.prevent="handleSubmit" class="space-y-4">
            <div>
              <label
                for="member"
                class="block text-sm font-medium text-gray-700 mb-1"
              >
                Select Member
              </label>
              <select
                id="member"
                v-model="selectedMember"
                class="w-full px-4 py-2 border text-black border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent outline-none bg-white"
                required
              >
                <option value="" disabled selected>
                  Select a member to remove
                </option>
                <option
                  v-for="member in members"
                  :key="member.id"
                  :value="member.id"
                >
                  {{ member.username }}
                </option>
              </select>
            </div>
            <div class="flex justify-end gap-3 mt-6">
              <button
                type="button"
                class="px-4 py-2 text-white hover:bg-gray-100 rounded-lg transition-colors"
                @click="$emit('update:modelValue', false)"
              >
                Cancel
              </button>
              <button
                type="submit"
                class="px-4 py-2 bg-green-500 text-white rounded-lg hover:bg-green-600 transition-colors"
              >
                Remove Member
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
    members: {
      type: Array,
      required: true,
      default: () => [],
    },
  });
  
  const emit = defineEmits(["update:modelValue", "remove"]);
  
  const selectedMember = ref("");
  
  const handleSubmit = () => {
    if (selectedMember.value) {
      emit("remove", selectedMember.value);
      selectedMember.value = "";
      emit("update:modelValue", false);
    }
  };
  </script>
  