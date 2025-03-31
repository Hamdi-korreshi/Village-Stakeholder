<template>
    <div class="bg-gray-100 min-h-screen min-w-screen">
      <Header />
      <SettingsPage />
    </div>
  </template>
  
  <script setup>
  //import Header from "./Header.vue";
  import SettingsPage from "./SettingsPage.vue";
  </script>
  
  <script>
  export default {
    name: "MainLayout",
  };
  </script>
  