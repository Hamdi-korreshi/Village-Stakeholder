<template>
  <main class="bg-white">
    <div class="pb-10 min-w-screen min-h-screen bg-gray-100">
      <CalendarHeader />

      <div class="flex flex-col items-center px-14 mt-5 w-full max-md:px-5">
        <h1 class="text-4xl text-black mb-4">March 2025</h1>

        <div class="flex gap-5 justify-center w-full max-w-[1024px]">
          <section class="w-[647px] flex-shrink-0">
            <CalendarGrid
              :selected-date="selectedDate"
              @select-date="handleDateSelect"
            />
          </section>

          <section class="w-[300px] flex-shrink-0">
            <SchedulePanel
              :selected-date="selectedDate"
              :events="scheduledEvents"
            />
          </section>
        </div>
      </div>
    </div>
  </main>
</template>

<script setup lang="ts">
import { ref } from "vue";
import CalendarHeader from "./CalendarHeader.vue";
import CalendarGrid from "./CalendarGrid.vue";
import SchedulePanel from "./SchedulePanel.vue";
import type { DayCell, ScheduleItem } from "./types";

const selectedDate = ref<number>(7); // Default to March 7

const scheduledEvents = ref<ScheduleItem[]>([
  {
    date: 7,
    time: "8:30am - 9:00am",
    description: "Doctor's Appointment - 123 Central Ave. Newark, NJ",
  },
  {
    date: 7,
    time: "10:00am - 10:30am",
    description: "Doctor's Appointment - 456 Main St. Newark, NJ",
  },
  {
    date: 7,
    time: "11:30am - 12:00pm",
    description: "Doctor's Appointment - 789 Park Ave. Newark, NJ",
  },
  {
    date: 7,
    time: "2:00pm - 2:30pm",
    description: "Doctor's Appointment - 321 Oak St. Newark, NJ",
  },
  {
    date: 7,
    time: "3:30pm - 4:00pm",
    description: "Doctor's Appointment - 654 Pine St. Newark, NJ",
  },
  {
    date: 7,
    time: "4:30pm - 5:00pm",
    description: "Doctor's Appointment - 987 Elm St. Newark, NJ",
  },
]);

const handleDateSelect = (date: number) => {
  selectedDate.value = date;
};
</script>