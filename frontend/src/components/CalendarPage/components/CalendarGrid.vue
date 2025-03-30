<template>
  <section class="flex flex-col items-center w-[647px]">
    <div class="grid grid-cols-7 gap-x-[24px] w-full text-xs text-black mb-4">
      <div v-for="day in weekDays" :key="day" class="text-center w-[89px]">
        {{ day }}
      </div>
    </div>

    <div class="grid grid-cols-7 gap-1 w-full text-black">
      <CalendarCell
        v-for="day in calendarDays"
        :key="`${day.date}-${day.isCurrentMonth}`"
        :day="day"
        :is-selected="selectedDate === day.date && day.isCurrentMonth"
        @click="() => handleCellClick(day)"
      />
    </div>
  </section>
</template>

<script setup lang="ts">
import { ref } from "vue";
import CalendarCell from "./CalendarCell.vue";
export interface ScheduleItem {
  date: number;
  time: string;
  description: string;
}

export interface DayCell {
  date: number;
  isCurrentMonth: boolean;
  hasSchedule?: boolean;
  scheduleType?: "blue" | "green" | "default";
}


const props = defineProps<{
  selectedDate: number;
}>();

const emit = defineEmits<{
  (e: "select-date", date: number): void;
}>();

const weekDays = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"];

const calendarDays = ref<DayCell[]>([
  // Previous month
  ...[23, 24, 25, 26, 27, 28].map((date) => ({
    date,
    isCurrentMonth: false,
  })),
  // Current month
  ...Array.from({ length: 31 }, (_, i) => ({
    date: i + 1,
    isCurrentMonth: true,
    scheduleType: i + 1 === 7 ? "green" : "default", // Only keep green for day 7
  })),
  // Next month
  ...[1, 2, 3, 4, 5].map((date) => ({
    date,
    isCurrentMonth: false,
  })),
]);

const handleCellClick = (day: DayCell) => {
  if (day.isCurrentMonth) {
    emit("select-date", day.date);
  }
};
</script>
