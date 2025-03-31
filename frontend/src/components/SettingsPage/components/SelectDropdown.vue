<template>
    <select
      :value="modelValue"
      @change="$emit('update:modelValue', $event.target.value)"
      class="text-base font-light shadow-sm bg-zinc-300 h-[29px] w-[156px] px-2 rounded"
    >
      <option disabled value="">Select Item</option>
      <slot></slot>
    </select>
  </template>
  
  <script setup>
  defineProps({
    modelValue: {
      type: String,
      required: true,
    },
  });
  
  defineEmits(["update:modelValue"]);
  </script>
  