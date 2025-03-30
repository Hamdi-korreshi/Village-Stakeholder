<template>
  <aside class="w-full text-white max-md:mt-8">
    <section
      class="flex flex-col h-[400px] text-black bg-gray-100 border border-solid shadow-sm border-black border-opacity-0"
    >
      <header
        class="px-16 py-3 text-sm text-center bg-gray-100 border border-solid border-black border-opacity-0 shadow-[0px_4px_4px_rgba(0,0,0,0.25)] max-md:px-5"
      >
        March {{ selectedDate }}
      </header>

      <div class="flex-1 overflow-y-auto px-0.5">
        <article
          v-for="event in dayEvents"
          :key="event.time"
          class="flex flex-col pt-2 pr-10 pb-4 pl-3.5 mt-2.5 mx-0.5 bg-green-100 rounded-xl border border-solid border-black border-opacity-0 shadow-[0px_4px_4px_rgba(0,0,0,0.25)] max-md:pr-5"
        >
          <time class="self-start text-sm">{{ event.time }}</time>
          <p class="mt-2 text-xs">
            {{ event.description }}
          </p>
        </article>
      </div>
    </section>

    <div class="mt-4 space-y-3.5">
      <button
        type="button"
        @click="showAddModal = true"
        class="flex justify-between items-center px-6 py-4 w-full h-[80px] bg-green-500 rounded-xl border border-solid border-black border-opacity-0 shadow-[0px_4px_4px_rgba(0,0,0,0.25)] max-md:px-5 max-md:mr-0.5 hover:bg-green-600 transition-colors duration-200"
        style="background-color: #22c55e"
      >
        <span class="text-lg font-bold whitespace-nowrap"
          >Add a Schedule Item</span
        >
        <span class="text-4xl">+</span>
      </button>

      <button
        type="button"
        @click="handleRemoveSchedule"
        class="flex justify-between items-center px-6 py-4 w-full h-[80px] bg-red-400 rounded-xl border border-solid border-black border-opacity-0 shadow-[0px_4px_4px_rgba(0,0,0,0.25)] max-md:px-5 max-md:mr-0.5 hover:bg-red-500 transition-colors duration-200"
        style="background-color: #ef4444"
      >
        <span class="text-lg font-bold whitespace-nowrap"
          >Remove a Schedule Item</span
        >
        <span class="text-4xl">-</span>
      </button>
    </div>

    <!-- Add Schedule Modal -->
    <div
      v-if="showAddModal"
      class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50"
      @click="showAddModal = false"
    >
      <div
        class="bg-white rounded-xl p-6 w-[500px] max-w-[90vw] shadow-lg text-black"
        @click.stop
      >
        <header class="flex justify-between items-center mb-6">
          <h2 class="text-2xl font-bold">Add Schedule Item</h2>
          <button
            @click="showAddModal = false"
            class="text-gray-500 hover:text-gray-700 transition-colors"
          >
            <span class="text-2xl">×</span>
          </button>
        </header>

        <form @submit.prevent="handleSubmitSchedule" class="space-y-4">
          <div class="space-y-2">
            <label for="title" class="block text-sm font-medium text-gray-700"
              >Title</label
            >
            <input
              id="title"
              v-model="newSchedule.title"
              type="text"
              class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500"
              required
            />
          </div>

          <div class="space-y-2">
            <label class="block text-sm font-medium text-gray-700"
              >Time Slot</label
            >
            <div class="flex items-center gap-4">
              <!-- Start Time -->
              <div class="flex items-center gap-1">
                <input
                  v-model="timeInput.startHour"
                  type="text"
                  maxlength="2"
                  placeholder="HH"
                  class="w-12 px-2 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500 text-center"
                  required
                />
                <span class="text-gray-500">:</span>
                <input
                  v-model="timeInput.startMinute"
                  type="text"
                  maxlength="2"
                  placeholder="MM"
                  class="w-12 px-2 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500 text-center"
                  required
                />
                <select
                  v-model="timeInput.startPeriod"
                  class="px-2 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500"
                  required
                >
                  <option value="am">AM</option>
                  <option value="pm">PM</option>
                </select>
              </div>

              <span class="text-gray-500">to</span>

              <!-- End Time -->
              <div class="flex items-center gap-1">
                <input
                  v-model="timeInput.endHour"
                  type="text"
                  maxlength="2"
                  placeholder="HH"
                  class="w-12 px-2 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500 text-center"
                  required
                />
                <span class="text-gray-500">:</span>
                <input
                  v-model="timeInput.endMinute"
                  type="text"
                  maxlength="2"
                  placeholder="MM"
                  class="w-12 px-2 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500 text-center"
                  required
                />
                <select
                  v-model="timeInput.endPeriod"
                  class="px-2 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500"
                  required
                >
                  <option value="am">AM</option>
                  <option value="pm">PM</option>
                </select>
              </div>
            </div>
          </div>

          <div class="space-y-2">
            <label
              for="location"
              class="block text-sm font-medium text-gray-700"
              >Location</label
            >
            <input
              id="location"
              v-model="newSchedule.location"
              type="text"
              class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500"
              required
            />
          </div>

          <div class="grid grid-cols-3 gap-4">
            <div class="space-y-2">
              <label for="month" class="block text-sm font-medium text-gray-700"
                >Month</label
              >
              <select
                id="month"
                v-model="newSchedule.month"
                class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500"
                required
              >
                <option v-for="month in months" :key="month" :value="month">
                  {{ month }}
                </option>
              </select>
            </div>

            <div class="space-y-2">
              <label for="date" class="block text-sm font-medium text-gray-700"
                >Date</label
              >
              <select
                id="date"
                v-model="newSchedule.date"
                class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500"
                required
              >
                <option
                  v-for="date in getDaysInMonth(
                    newSchedule.month,
                    newSchedule.year,
                  )"
                  :key="date"
                  :value="date"
                >
                  {{ date }}
                </option>
              </select>
            </div>

            <div class="space-y-2">
              <label for="year" class="block text-sm font-medium text-gray-700"
                >Year</label
              >
              <select
                id="year"
                v-model="newSchedule.year"
                class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-500"
                required
              >
                <option v-for="year in years" :key="year" :value="year">
                  {{ year }}
                </option>
              </select>
            </div>
          </div>

          <div class="flex justify-end gap-3 mt-6">
            <button
              type="button"
              @click="showAddModal = false"
              class="px-4 py-2 text-sm font-medium text-gray-700 bg-gray-100 rounded-md hover:bg-gray-200 focus:outline-none focus:ring-2 focus:ring-gray-500"
            >
              Cancel
            </button>
            <button
              type="submit"
              class="px-4 py-2 text-sm font-medium text-white bg-green-500 rounded-md hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-green-500"
            >
              Add Schedule
            </button>
          </div>
        </form>
      </div>
    </div>

    <!-- Remove Schedule Modal -->
    <div
      v-if="showRemoveModal"
      class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50"
      @click="showRemoveModal = false"
    >
      <div
        class="bg-white rounded-xl p-6 w-[500px] max-w-[90vw] shadow-lg text-black"
        @click.stop
      >
        <header class="flex justify-between items-center mb-6">
          <h2 class="text-2xl font-bold">Remove Schedule Item</h2>
          <button
            @click="showRemoveModal = false"
            class="text-gray-500 hover:text-gray-700 transition-colors"
          >
            <span class="text-2xl">×</span>
          </button>
        </header>

        <form @submit.prevent="handleConfirmRemove" class="space-y-4">
          <div class="grid grid-cols-3 gap-4">
            <div class="space-y-2">
              <label
                for="removeMonth"
                class="block text-sm font-medium text-gray-700"
                >Month</label
              >
              <select
                id="removeMonth"
                v-model="removeScheduleDate.month"
                class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-red-500"
                required
              >
                <option v-for="month in months" :key="month" :value="month">
                  {{ month }}
                </option>
              </select>
            </div>

            <div class="space-y-2">
              <label
                for="removeDate"
                class="block text-sm font-medium text-gray-700"
                >Date</label
              >
              <select
                id="removeDate"
                v-model="removeScheduleDate.date"
                class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-red-500"
                required
              >
                <option
                  v-for="date in getDaysInMonth(
                    removeScheduleDate.month,
                    removeScheduleDate.year,
                  )"
                  :key="date"
                  :value="date"
                >
                  {{ date }}
                </option>
              </select>
            </div>

            <div class="space-y-2">
              <label
                for="removeYear"
                class="block text-sm font-medium text-gray-700"
                >Year</label
              >
              <select
                id="removeYear"
                v-model="removeScheduleDate.year"
                class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-red-500"
                required
              >
                <option v-for="year in years" :key="year" :value="year">
                  {{ year }}
                </option>
              </select>
            </div>
          </div>

          <div class="space-y-2">
            <label for="event" class="block text-sm font-medium text-gray-700"
              >Select Event to Remove</label
            >
            <select
              id="event"
              v-model="selectedEvent"
              class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-red-500"
              required
            >
              <option value="">Select an event</option>
              <option
                v-for="event in availableEvents"
                :key="`${event.time}-${event.description}`"
                :value="event"
              >
                {{ event.time }} - {{ event.description }}
              </option>
            </select>
          </div>

          <div v-if="selectedEvent" class="mt-4 p-4 bg-red-50 rounded-lg">
            <h3 class="font-medium text-red-800 mb-2">
              Selected Event Details:
            </h3>
            <p class="text-sm text-red-700">Time: {{ selectedEvent.time }}</p>
            <p class="text-sm text-red-700">
              Description: {{ selectedEvent.description }}
            </p>
          </div>

          <div class="flex justify-end gap-3 mt-6">
            <button
              type="button"
              @click="showRemoveModal = false"
              class="px-4 py-2 text-sm font-medium text-gray-700 bg-gray-100 rounded-md hover:bg-gray-200 focus:outline-none focus:ring-2 focus:ring-gray-500"
            >
              Cancel
            </button>
            <button
              type="submit"
              :disabled="!selectedEvent"
              class="px-4 py-2 text-sm font-medium text-white bg-red-500 rounded-md hover:bg-red-600 focus:outline-none focus:ring-2 focus:ring-red-500 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              Remove Event
            </button>
          </div>
        </form>
      </div>
    </div>
  </aside>
</template>

<script setup lang="ts">
import { computed, ref } from "vue";

export interface ScheduleItem {
  date: number;
  time: string;
  description: string;
}

const props = defineProps<{
  selectedDate: number;
  events: ScheduleItem[];
  months: string[];
  years: number[];
}>();

const emit = defineEmits<{
  (e: "new-schedule", item: ScheduleItem): void;
  (e: "remove-schedule", item: ScheduleItem): void;
}>();

const showAddModal = ref(false);
const showRemoveModal = ref(false);
const selectedEvent = ref<ScheduleItem | null>(null);

const removeScheduleDate = ref({
  month: "March",
  date: props.selectedDate,
  year: 2025,
});

const dayEvents = computed(() => {
  return props.events.filter((event) => event.date === props.selectedDate);
});

const availableEvents = computed(() => {
  return props.events.filter(
    (event) => event.date === removeScheduleDate.value.date,
  );
});

const getDaysInMonth = (month: string, year: number) => {
  const monthIndex = props.months.indexOf(month);
  return new Date(year, monthIndex + 1, 0).getDate();
};

const handleRemoveSchedule = () => {
  showRemoveModal.value = true;
  removeScheduleDate.value = {
    month: "March",
    date: props.selectedDate,
    year: 2025,
  };
};

const handleConfirmRemove = () => {
  if (selectedEvent.value) {
    emit("remove-schedule", selectedEvent.value);
    showRemoveModal.value = false;
    selectedEvent.value = null;
  }
};

const timeInput = ref({
  startHour: "",
  startMinute: "",
  startPeriod: "am",
  endHour: "",
  endMinute: "",
  endPeriod: "am",
});

const newSchedule = ref({
  title: "",
  location: "",
  month: "March",
  date: props.selectedDate,
  year: 2025,
});

const validateTime = () => {
  // Validate hours (1-12)
  const startHour = parseInt(timeInput.value.startHour);
  const endHour = parseInt(timeInput.value.endHour);
  if (isNaN(startHour) || startHour < 1 || startHour > 12) {
    alert("Start hour must be between 1 and 12");
    return false;
  }
  if (isNaN(endHour) || endHour < 1 || endHour > 12) {
    alert("End hour must be between 1 and 12");
    return false;
  }

  // Validate minutes (00-59)
  const startMinute = parseInt(timeInput.value.startMinute);
  const endMinute = parseInt(timeInput.value.endMinute);
  if (isNaN(startMinute) || startMinute < 0 || startMinute > 59) {
    alert("Start minute must be between 00 and 59");
    return false;
  }
  if (isNaN(endMinute) || endMinute < 0 || endMinute > 59) {
    alert("End minute must be between 00 and 59");
    return false;
  }

  // Format minutes to always have two digits
  timeInput.value.startMinute = startMinute.toString().padStart(2, "0");
  timeInput.value.endMinute = endMinute.toString().padStart(2, "0");

  return true;
};

const formatTimeString = () => {
  const startTime = `${timeInput.value.startHour}:${timeInput.value.startMinute}${timeInput.value.startPeriod}`;
  const endTime = `${timeInput.value.endHour}:${timeInput.value.endMinute}${timeInput.value.endPeriod}`;
  return `${startTime} - ${endTime}`;
};

const handleSubmitSchedule = () => {
  if (!validateTime()) {
    return;
  }

  const scheduleItem = {
    ...newSchedule.value,
    time: formatTimeString(),
  };

  emit("new-schedule", {
    date: scheduleItem.date,
    time: scheduleItem.time,
    description: `${scheduleItem.title} - ${scheduleItem.location}`,
  });

  showAddModal.value = false;

  // Reset form
  newSchedule.value = {
    title: "",
    location: "",
    month: "March",
    date: props.selectedDate,
    year: 2025,
  };

  timeInput.value = {
    startHour: "",
    startMinute: "",
    startPeriod: "am",
    endHour: "",
    endMinute: "",
    endPeriod: "am",
  };
};
</script>

<style scoped>
.overflow-y-auto {
  scrollbar-width: thin;
  scrollbar-color: rgba(0, 0, 0, 0.2) transparent;
}

.overflow-y-auto::-webkit-scrollbar {
  width: 6px;
}

.overflow-y-auto::-webkit-scrollbar-track {
  background: transparent;
}

.overflow-y-auto::-webkit-scrollbar-thumb {
  background-color: rgba(0, 0, 0, 0.2);
  border-radius: 3px;
}
</style>
