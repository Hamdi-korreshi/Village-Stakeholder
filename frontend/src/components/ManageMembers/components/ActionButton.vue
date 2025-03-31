<template>
  <button
    class="flex justify-between items-center px-5 py-0 text-xl font-bold text-white rounded-xl shadow-sm cursor-pointer h-[59px] w-[302px] max-md:w-full transition-colors duration-200"
    :style="{ backgroundColor: buttonColor }"
    @click="$emit('click')"
  >
    <span>{{ text }}</span>
    <span class="text-5xl">{{ variant === "add" ? "+" : "-" }}</span>
  </button>
</template>

<script setup>
import { computed } from "vue";

const props = defineProps({
  text: {
    type: String,
    required: true,
  },
  variant: {
    type: String,
    validator: (value) => ["add", "remove"].includes(value),
    required: true,
  },
});

const buttonColor = computed(() => {
  console.log("Button variant:", props.variant); // Debug log
  return props.variant === "add" ? "#22c55e" : "#ef4444";
});

defineEmits(["click"]);
</script>
