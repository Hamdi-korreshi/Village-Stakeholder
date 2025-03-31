<template>
    <link
      href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&family=Raleway:wght@400&display=swap"
      rel="stylesheet"
    />
    <div class="min-w-screen min-h-screen bg-gray-100">
      <TheHeader />
      <main class="px-14 py-8">
        <h1 class="mb-9 text-5xl text-center text-black max-sm:text-3xl">
          User's Village
        </h1>
        <DashboardGrid />
      </main>
    </div>
  </template>
  
  <script>
  import TheHeader from "./TheHeader.vue";
  import DashboardGrid from "./DashboardGrid.vue";
  
  export default {
    name: "UserVillage",
    components: {
      TheHeader,
      DashboardGrid,
    },
  };
  </script>
  