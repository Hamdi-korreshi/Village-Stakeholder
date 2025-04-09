<template>
  <div class="notifications-section">
    <div class="notifications-header">
      <h3>Notifications</h3>
      <button @click="markAllAsRead" class="mark-read-button">Mark All as Read</button>
    </div>
    <div class="notifications-list">
      <!-- If there are no notifications, show a message -->
      <div v-if="notifications.length === 0" class="no-notifications">
        No notifications.
      </div>
      <!-- Otherwise iterate through notifications -->
      <div v-else v-for="(notification, index) in notifications" 
           :key="notification.notification_id" 
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
          <div class="notification-time">{{ formatTime(notification.timestamp) }}</div>
        </div>
        <button @click="dismissNotification(index)" class="dismiss-button">×</button>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import apiClient from '../utils/axios.js';

export default {
  name: 'Notifications',
  setup() {
    const notifications = ref([]);

    const fetchNotifications = async () => {
      try {
        const response = await apiClient.get('/get_notifs/');
        // Assuming the backend returns a JSON object with a "notifications" key.
        console.log('Fetched notifications:', response.data.notifications);
        notifications.value = response.data.notifications || [];
      } catch (error) {
        console.error('Error fetching notifications:', error);
        notifications.value = [];
      }
    };

    // Formats a timestamp into a more readable format.
    const formatTime = (timestamp) => {
      const date = new Date(timestamp);
      return date.toLocaleString();
    };

    const markAllAsRead = () => {
      notifications.value = notifications.value.map(n => ({ ...n, read: true }));
      // Optionally, you might also update the status in the backend here.
    };

    const dismissNotification = (index) => {
      notifications.value.splice(index, 1);
    };

    onMounted(() => {
      fetchNotifications();
    });

    return {
      notifications
    };
  }
};
</script>

<style scoped>
/* Copy or import the notifications-specific styling from your Dashboard CSS */
.notifications-section {
  background-color: #1a1a1a;
  padding: 2em;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
  margin-bottom: 2rem;
}

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

.mark-read-button {
  background-color: #3a3a3a;
  color: rgba(255, 255, 255, 0.87);
}
</style>
