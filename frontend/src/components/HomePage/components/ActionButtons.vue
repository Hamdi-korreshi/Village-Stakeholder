<template>
  <aside class="flex flex-col gap-8 w-full min-w-[200px]">
    <button
      class="w-full text-xl font-bold text-white rounded-xl shadow-sm bg-slate-500 h-[59px] max-sm:text-base max-sm:h-[50px] hover:bg-slate-600 transition-colors"
      aria-label="Open Dashboard"
      style="background-color: #4472C4;"
    >
      Dashboard
    </button>
    <button
      class="w-full text-xl font-bold text-white rounded-xl shadow-sm bg-slate-500 h-[59px] max-sm:text-base max-sm:h-[50px] hover:bg-slate-600 transition-colors"
      aria-label="Open Calendar and Scheduling"
      style="background-color: #4472C4;"
    >
      Calendar / Scheduling
    </button>
    <button
      class="w-full text-xl font-bold text-white rounded-xl shadow-sm bg-slate-500 h-[59px] max-sm:text-base max-sm:h-[50px] hover:bg-slate-600 transition-colors"
      aria-label="Manage Members"
      style="background-color: #4472C4;"
    >
      Manage Members
    </button>
  </aside>
</template>

<script>
export default {
  name: "ActionButtons",
};
</script>
