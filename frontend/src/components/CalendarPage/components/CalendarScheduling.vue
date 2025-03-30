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
              :scheduled-events="scheduledEvents"
              @select-date="handleDateSelect"
            />
          </section>

          <section class="w-[300px] flex-shrink-0">
            <SchedulePanel
              :selected-date="selectedDate"
              :events="scheduledEvents"
              @new-schedule="addScheduleItem"
              @remove-schedule="removeScheduleItem"
              :months="months"
              :years="years"
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

const parseTime = (timeStr: string) => {
  // Extract time and period from the start time
  const [time, period] = timeStr.split(/(?:am|pm)/i);
  const [hours, minutes] = time.trim().split(":").map(Number);
  const isPM = period.trim().toLowerCase() === "pm";

  return {
    hours: hours === 12 ? 0 : hours, // Convert 12 to 0 for proper sorting
    minutes,
    isPM,
  };
};

const sortScheduleEvents = () => {
  scheduledEvents.value.sort((a, b) => {
    const timeA = parseTime(a.time.split(" - ")[0]);
    const timeB = parseTime(b.time.split(" - ")[0]);

    // First sort by AM/PM
    if (timeA.isPM !== timeB.isPM) {
      return timeA.isPM ? 1 : -1;
    }

    // Then sort by hours
    if (timeA.hours !== timeB.hours) {
      return timeA.hours - timeB.hours;
    }

    // Finally sort by minutes
    return timeA.minutes - timeB.minutes;
  });
};

const handleDateSelect = (date: number) => {
  selectedDate.value = date;
};

const addScheduleItem = (item: ScheduleItem) => {
  scheduledEvents.value.push(item);
  sortScheduleEvents();
};

const months = [
  "January",
  "February",
  "March",
  "April",
  "May",
  "June",
  "July",
  "August",
  "September",
  "October",
  "November",
  "December",
];

const currentYear = new Date().getFullYear();
const years = Array.from({ length: 5 }, (_, i) => currentYear + i);

const removeScheduleItem = (itemToRemove: ScheduleItem) => {
  scheduledEvents.value = scheduledEvents.value.filter(
    (item) =>
      !(
        item.date === itemToRemove.date &&
        item.time === itemToRemove.time &&
        item.description === itemToRemove.description
      ),
  );
};
</script>
