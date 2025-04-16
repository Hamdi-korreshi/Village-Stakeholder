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
              :events="scheduledEvents.filter(event => event.date === selectedDate)"
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
import { ref, onMounted } from "vue";
import CalendarGrid from "./CalendarGrid.vue";
import SchedulePanel from "./SchedulePanel.vue";

import {
  getCalendarEvents,
  makeCalendarEvent,
  updateCalendarEvent,
  deleteCalendarEvent
} from "../../../services/calendarServices.js";

export interface ScheduleItem {
  id?: number;
  date: number;
  time: string;
  description: string;
  month: number;
  year: number;   
}


export interface DayCell {
  date: number;
  isCurrentMonth: boolean;
  hasSchedule?: boolean;
  scheduleType?: "blue" | "green" | "default";
}

const selectedDate = ref<number>(7); // Default to March 7
const scheduledEvents = ref<ScheduleItem[]>([]);

const parseTime = (timeStr: string) => {
  const [time, period] = timeStr.split(/(?:am|pm)/i);
  const [hours, minutes] = time.trim().split(":").map(Number);
  const isPM = period.trim().toLowerCase() === "pm";

  return {
    hours: hours === 12 ? 0 : hours,
    minutes,
    isPM,
  };
};

const sortScheduleEvents = () => {
  scheduledEvents.value.sort((a, b) => {
    const timeA = parseTime(a.time.split(" - ")[0]);
    const timeB = parseTime(b.time.split(" - ")[0]);

    if (timeA.isPM !== timeB.isPM) {
      return timeA.isPM ? 1 : -1;
    }

    if (timeA.hours !== timeB.hours) {
      return timeA.hours - timeB.hours;
    }

    return timeA.minutes - timeB.minutes;
  });
}; 



const formatTimeAMPM = (date: Date) => {
  return date.toLocaleTimeString("en-US", {
    hour: "numeric",
    minute: "2-digit",
    hour12: true,
    timeZone: "America/New_York", // Or your desired timezone
  });
};

onMounted(async () => {
  try {
    const response = await getCalendarEvents();
    scheduledEvents.value = (response.events || []).map((event: any) => {
      const start = new Date(event.start_time);
      const end = new Date(event.end_time);

      return {
        id: event.event_id,
        date: start.getUTCDate(),
        time: `${formatTimeAMPM(start)} - ${formatTimeAMPM(end)}`,
        description: event.description,
        month: start.getUTCMonth() + 1,
        year: start.getUTCFullYear(),
      };
    });

    console.log("Scheduled Events:", scheduledEvents.value);
    sortScheduleEvents();
  } catch (error) {
    console.error("Failed to load events:", error);
    scheduledEvents.value = [];
  }
});





const addScheduleItem = async (item: ScheduleItem) => {
  try {
    const [start_time, end_time] = item.time.split(" - ");
    const formattedDate = `${item.year}-${String(item.month).padStart(2, '0')}-${String(item.date).padStart(2, '0')}`;
    
    const eventData = {
      event_name: item.description.split(" - ")[0],
      start_time: `${formattedDate}T${start_time}`,
      end_time: `${formattedDate}T${end_time}`,
      description: item.description,
      reminder: false
    };

    const created = await makeCalendarEvent(eventData);// JUST BACKEND CALL
  } catch (error) {
    console.error("Error adding event:", error);
  }
};



const removeScheduleItem = async (item: ScheduleItem) => {
  if (!item.id) return;
  try {
    await deleteCalendarEvent(item.id);
  } catch (error) {
    console.error("Error removing event:", error);
  }
};


const handleDateSelect = (date: number) => {
  selectedDate.value = date;
};

const months = [
  "January", "February", "March", "April", "May", "June",
  "July", "August", "September", "October", "November", "December"
];
const years = [2024, 2025, 2026];
</script>