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
    name: "Dashbaord",
    components: {RandomStringDisplay},
    methods: {
        async signoutUser() {
            try {
                const result = await signout();
                console.log(result.message)
                //this.$router.push({'name':"login"})
                toast.success("Logout Success. Goodbye!", {
                  autoClose: 5000, // 5 seconds
                });
                setTimeout(() => {
                  this.$router.push({ name: "login" });
                }, 2000);
            }
            catch (error) {
                console.error("Sign out error", error);
            }
        }
    }
  };
  </script>
  
  <style scoped>
  /* Overall layout */
  .dashboard-container {
    max-width: 1280px;
    margin: 0 auto;
    padding: 2rem;
  }
  
  .dashboard-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 2rem;
  }
  
  h2, h3 {
    color: rgba(255, 255, 255, 0.87);
    line-height: 1.1;
  }
  
  h2 {
    font-size: 2em;
  }
  
  h3 {
    font-size: 1.5em;
    margin-bottom: 1rem;
  }
  
  .dashboard-content {
    display: flex;
    flex-direction: column;
    gap: 2rem;
  }
  
  /* Sections */
  .analytics-section,
  .notifications-section,
  .user-management-section,
  .random-string-section {
    background-color: #1a1a1a;
    padding: 2em;
    border-radius: 8px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
  }
  
  /* Analytics Section */
  .stats-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1.5rem;
    margin-bottom: 2rem;
  }
  
  .stat-card {
    background-color: #242424;
    padding: 1.5rem;
    border-radius: 8px;
    text-align: center;
    border-left: 4px solid #4472C4;
  }
  
  .stat-value {
    font-size: 2em;
    font-weight: bold;
    color: rgba(255, 255, 255, 0.87);
    margin-bottom: 0.5rem;
  }
  
  .stat-label {
    color: rgba(255, 255, 255, 0.6);
    font-size: 0.9em;
  }
  
  .chart-container {
    background-color: #242424;
    border-radius: 8px;
    padding: 1.5rem;
    height: 300px;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  .chart-placeholder {
    color: rgba(255, 255, 255, 0.6);
  }
  
  /* Notifications Section */
  .notifications-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1rem;
  }
  
  .notifications-list {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
  }
  
  .notification-item {
    display: flex;
    align-items: center;
    padding: 1rem;
    background-color: #242424;
    border-radius: 8px;
    transition: background-color 0.2s;
  }
  
  .notification-item.unread {
    background-color: #2a2a4a;
    border-left: 3px solid #4472C4;
  }
  
  .notification-icon {
    font-size: 1.5em;
    margin-right: 1rem;
    width: 40px;
    text-align: center;
  }
  
  .notification-content {
    flex: 1;
  }
  
  .notification-title {
    font-weight: bold;
    color: rgba(255, 255, 255, 0.87);
    margin-bottom: 0.2rem;
  }
  
  .notification-message {
    color: rgba(255, 255, 255, 0.7);
    font-size: 0.9em;
    margin-bottom: 0.2rem;
  }
  
  .notification-time {
    color: rgba(255, 255, 255, 0.5);
    font-size: 0.8em;
  }
  
  .dismiss-button {
    background: none;
    border: none;
    color: rgba(255, 255, 255, 0.5);
    font-size: 1.5em;
    cursor: pointer;
    padding: 0 0.5rem;
  }
  
  .dismiss-button:hover {
    color: rgba(255, 255, 255, 0.87);
  }
  
  /* User Management Section */
  .management-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 1rem;
  }
  
  .users-table {
    display: flex;
    flex-direction: column;
  }
  
  .table-header, .table-row {
    display: grid;
    grid-template-columns: 80px 1fr 1fr 120px 150px;
    gap: 1rem;
    padding: 1rem;
    align-items: center;
  }
  
  .table-header {
    font-weight: bold;
    border-bottom: 1px solid #3a3a3a;
  }
  
  .table-row {
    transition: background-color 0.2s;
  }
  
  .table-row:hover {
    background-color: #242424;
  }
  
  .actions-cell {
    display: flex;
    gap: 0.5rem;
  }
  
  /* Buttons */
  button {
    border-radius: 8px;
    border: 1px solid transparent;
    padding: 0.6em 1.2em;
    font-size: 1em;
    font-weight: 500;
    font-family: inherit;
    background-color: #1a1a1a;
    cursor: pointer;
    transition: border-color 0.25s;
  }
  
  .signout-button {
    background-color: #ff4444;
    color: white;
  }
  
  .signout-button:hover {
    background-color: #cc0000;
  }
  
  .mark-read-button {
    background-color: #3a3a3a;
    color: rgba(255, 255, 255, 0.87);
  }
  
  .mark-read-button:hover {
    border-color: #4472C4;
  }
  
  .add-user-button {
    background-color: #4472C4;
    color: white;
  }
  
  .add-user-button:hover {
    background-color: #4472C4;
  }
  
  .edit-button {
    background-color: #4472C4;
    color: white;
    padding: 0.4em 0.8em;
    font-size: 0.9em;
  }
  
  .delete-button {
    background-color: #ff4444;
    color: white;
    padding: 0.4em 0.8em;
    font-size: 0.9em;
  }
  
  .save-button {
    background-color: #4472C4;
    color: white;
  }
  
  .cancel-button {
    background-color: #3a3a3a;
    color: rgba(255, 255, 255, 0.87);
  }
  
  .confirm-delete-button {
    background-color: #ff4444;
    color: white;
  }
  
  .cancel-delete-button {
    background-color: #3a3a3a;
    color: rgba(255, 255, 255, 0.87);
  }
  
  /* Form elements */
  .form-group {
    margin-bottom: 1.5rem;
  }
  
  .form-group label {
    display: block;
    margin-bottom: 0.5rem;
    color: rgba(255, 255, 255, 0.87);
  }
  
  .form-group input,
  .form-group select {
    width: 100%;
    padding: 0.6em;
    border-radius: 8px;
    border: 1px solid #4472C4;
    background-color: #242424;
    color: rgba(255, 255, 255, 0.87);
    font-family: inherit;
    transition: border-color 0.25s;
  }
  
  .form-group input:focus,
  .form-group select:focus {
    border-color: #4472C4;
    outline: none;
  }
  
  /* Random String Section */
  .random-string-section {
    margin-top: 2rem;
  }
  
  /* Light mode adaptation */
  @media (prefers-color-scheme: light) {
    h2, h3 {
      color: #213547;
    }
  
    .analytics-section,
    .notifications-section,
    .user-management-section,
    .random-string-section {
      background-color: #f9f9f9;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }
  
    .stat-card {
      background-color: #ffffff;
      border-left-color: #4472C4;
    }
  
    .stat-value {
      color: #213547;
    }
  
    .stat-label {
      color: #666;
    }
  
    .chart-container {
      background-color: #ffffff;
    }
  
    .chart-placeholder {
      color: #666;
    }
  
    .notification-item {
      background-color: #ffffff;
    }
  
    .notification-item.unread {
      background-color: #f0f7ff;
      border-left-color: #4472C4;
    }
  
    .notification-title {
      color: #213547;
    }
  
    .notification-message {
      color: #555;
    }
  
    .notification-time {
      color: #777;
    }
  
    .dismiss-button {
      color: #999;
    }
  
    .dismiss-button:hover {
      color: #333;
    }
  
    .table-header {
      border-bottom-color: #ddd;
    }
  
    .table-row:hover {
      background-color: #f5f5f5;
    }
  
    .signout-button {
      background-color: #ff4444;
    }
  
    .mark-read-button {
      background-color: #e0e0e0;
      color: #333;
    }
  
    .add-user-button {
      background-color: #4472C4;
    }
  
    .edit-button {
      background-color: #4472C4;
    }
  
    .delete-button {
      background-color: #ff4444;
    }
  
    .form-group label {
      color: #213547;
    }
  
    .form-group input,
    .form-group select {
      background-color: #ffffff;
      color: #213547;
      border-color: #4472C4;
    }
  }
  </style>