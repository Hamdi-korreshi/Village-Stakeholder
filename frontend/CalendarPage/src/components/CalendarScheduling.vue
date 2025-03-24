<template>
  <main class="overflow-hidden bg-white">
    <div class="pb-10 w-full bg-gray-100 max-md:max-w-full">
      <CalendarHeader />

      <div
        class="flex flex-col items-start px-14 mt-5 w-full max-md:px-5 max-md:max-w-full"
      >
        <h1 class="ml-24 text-4xl text-black max-md:ml-2.5">March 2025</h1>

        <div class="flex gap-5 max-md:flex-col">
          <section class="w-[66%] max-md:ml-0 max-md:w-full">
            <CalendarGrid />
          </section>

          <section class="ml-5 w-[34%] max-md:ml-0 max-md:w-full">
            <SchedulePanel />
          </section>
        </div>
      </div>
    </div>
  </main>
</template>

<script setup lang="ts">
import CalendarHeader from "./CalendarHeader.vue";
import CalendarGrid from "./CalendarGrid.vue";
import SchedulePanel from "./SchedulePanel.vue";
</script>
