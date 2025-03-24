<template>
  <div class="container">
    <header>
<!--      <img src="logo.png" alt="B the Cause logo" class="logo"> -->
      <nav>
        <ul>
          <li><a href="#">Home</a></li>
          <li><a href="#">About</a></li>
          <li><a href="#">Contact</a></li>
        </ul>
      </nav>
    </header>

    <main>
      <section class="calendar-section">
        <div class="calendar">
          <h2>March 2025</h2>
          <div class="calendar-grid">
            <!-- Calendar days and scheduling item will be populated dynamically by Vue.js -->
          </div>
        </div>

        <div class="flex flex-col gap-5">
          <h3>March 7</h3>
          <div class="schedule-item">
            <p>8:30am - 9:00am</p>
            <p>Doctor's Appointment - 123 Central Ave. Newark, NJ</p>
          </div>
          <button class="bg-green-700 text-white px-4 py-2 rounded-xl font-bold hover:bg-blue-700 mt-4" @click="addScheduleItem">Add a Schedule Item</button>
          <button class="bg-btc-green" @click="removeScheduleItem">Remove a Schedule Item</button>
        </div>
      </section>
    </main>
  </div>
</template>

<script setup>
    import {ref} from 'vue'
      const schedule = ref({
        date: 'March 7',
        time: '8:30am - 9:00am',
        description: "Doctor's Appointment - 123 Central Ave. Newark, NJ"
      })
    function addScheduleItem() {
      // Add a new schedule item
    }
    function removeScheduleItem() {
      // Remove the current schedule item
    }

</script>
