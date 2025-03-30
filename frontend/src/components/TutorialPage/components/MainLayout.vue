<template>
    <main class="min-w-screen min-h-screen bg-gray-100">
      <Header />
      <WelcomeSection />
    </main>
  </template>
  
  <script>
  import Header from "./Header.vue";
  import WelcomeSection from "./WelcomeSection.vue";
  
  export default {
    name: "MainLayout",
    components: {
      Header,
      WelcomeSection,
    },
  };
  </script>
  