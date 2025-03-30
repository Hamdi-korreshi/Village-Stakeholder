<template>
  <button
    type="button"
    :style="{
      backgroundColor: modelValue ? '#22c55e' : '#ef4444',
    }"
    class="relative rounded-xl shadow-sm h-[28px] w-[52px]"
    role="switch"
    :aria-checked="modelValue"
    @click="$emit('update:modelValue', !modelValue)"
  >
    <span
      :class="[
        'absolute top-px w-6 h-6 bg-gray-100 rounded-xl shadow-sm transition-all duration-200',
        modelValue ? 'right-px' : 'left-px',
      ]"
    />
  </button>
</template>

<script setup>
defineProps({
  modelValue: {
    type: Boolean,
    required: true,
  },
});

defineEmits(["update:modelValue"]);
</script>
