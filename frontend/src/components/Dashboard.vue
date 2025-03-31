<template>
    <div class="dashboard-container">
      <div class="dashboard-header">
        <h2>Dashboard</h2>
        <button @click="signoutUser" class="signout-button">Sign Out</button>
      </div>
  
      <div class="dashboard-content">
        <!-- User Analytics Section -->
        <div class="analytics-section">
          <h3>User Analytics</h3>
          <div class="stats-grid">
            <div class="stat-card">
              <div class="stat-value">1,254</div>
              <div class="stat-label">Total Users</div>
            </div>
            <div class="stat-card">
              <div class="stat-value">342</div>
              <div class="stat-label">Active Today</div>
            </div>
            <div class="stat-card">
              <div class="stat-value">87%</div>
              <div class="stat-label">Engagement Rate</div>
            </div>
            <div class="stat-card">
              <div class="stat-value">2.5m</div>
              <div class="stat-label">Total Sessions</div>
            </div>
          </div>
          
          <div class="chart-container">
            <div class="chart-placeholder">User Growth Chart</div>
          </div>
        </div>
  
        <!-- Notifications Section -->
        <div class="notifications-section">
          <div class="notifications-header">
            <h3>Notifications</h3>
            <button @click="markAllAsRead" class="mark-read-button">Mark All as Read</button>
          </div>
          
          <div class="notifications-list">
            <div v-for="(notification, index) in notifications" :key="index" 
                 class="notification-item" 
                 :class="{ 'unread': !notification.read }">
              <div class="notification-icon">
                <span v-if="notification.type === 'alert'">⚠️</span>
                <span v-else-if="notification.type === 'info'">ℹ️</span>
                <span v-else>🔔</span>
              </div>
              <div class="notification-content">
                <div class="notification-title">{{ notification.title }}</div>
                <div class="notification-message">{{ notification.message }}</div>
                <div class="notification-time">{{ notification.time }}</div>
              </div>
              <button @click="dismissNotification(index)" class="dismiss-button">×</button>
            </div>
          </div>
        </div>
      </div>
  </div>    
</template>

<script>
    import { signout } from "../services/authServices"
    import RandomStringDisplay from "./RandomStringDisplay.vue"
    import { toast } from "vue3-toastify";
    import "vue3-toastify/dist/index.css";

export default {
  name: "Dashboard",
  components: {
    RandomStringDisplay,
    AddVillagerButton,
    MakeVillageButton
  },
  data() {
    return {
      currentUserId: 1,        // Replace with logic to get logged in user ID
      targetVillagerId: 2,     // Replace with selected villager/user to add
      selectedRelationId: 3    // Replace with selected relation ID
    }
  },
  methods: {
    async signoutUser() {
      try {
        const result = await signout();
        console.log(result.message)
        this.$router.push({ name: "Login" })
      } catch (error) {
        console.error("Sign out error", error);
      }
    }
  }
};
</script>