<template>
  <article
    class="flex flex-col justify-center items-center px-px bg-stone-300 h-[89px] shadow-[0px_4px_4px_rgba(0,0,0,0.25)] w-[89px] cursor-pointer"
    @click="$emit('click')"
  >
    <div
      :class="[
        'px-1 pt-1 pb-20 h-[88px] shadow-[0px_4px_4px_rgba(0,0,0,0.25)] w-[88px] max-md:pr-5',
        getCellBackground,
      ]"
    >
      {{ day.date }}
    </div>
  </article>
</template>

<script setup lang="ts">
import { computed } from "vue";

export interface DayCell {
  date: number;
  isCurrentMonth: boolean;
  hasSchedule?: boolean;
  scheduleType?: "blue" | "green" | "default";
}
const props = defineProps<{
  day: DayCell;
  isSelected?: boolean;
}>();

const getCellBackground = computed(() => {
  if (!props.day.isCurrentMonth) return "bg-zinc-500";
  if (props.isSelected) return "bg-blue-100";
  if (props.day.scheduleType === "blue") return "bg-blue-100";
  if (props.day.scheduleType === "green") return "bg-green-100";
  return "bg-neutral-50";
});
</script>
