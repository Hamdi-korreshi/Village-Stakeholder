<template>
    <section class="shadow-sm bg-zinc-300 h-[431px] max-md:w-full">
      <header class="p-1.5 text-sm text-center text-black bg-white shadow-sm">
        Members
      </header>
      <div class="h-[calc(100%_-_28px)] overflow-auto" role="list" aria-label="Members list">
        <ul class="p-2">
          <li v-for="(member, index) in members" :key="index" class="py-1 border-b border-gray-400">
            {{ member.name }}
          </li>
        </ul>
        <div v-if="errorMessage" class="text-red-500 text-center p-2">
          {{ errorMessage }}
        </div>
      </div>
    </section>
  </template>
  
  <script>
  import { get_my_village } from '../../../services/villageServices.js';
  
  export default {
    name: "MembersList",
    data() {
      return {
        members: [],
        errorMessage: "",
      };
    },
    methods: {
      async displayMember() {
        this.errorMessage = "";
        try {
          const data = await get_my_village(); // directly gets JSON data
          this.members = data.members;
        } catch (error) {
          console.error('Fetch error:', error);
          this.errorMessage = error.message;
        }
      }
    },
    created() {
      this.displayMember();
    }
  };
  </script>
  
  