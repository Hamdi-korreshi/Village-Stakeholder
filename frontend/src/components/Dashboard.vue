<template>
  <div class="dashboard-container">
    <div class="dashboard-header">
      <h2>Dashboard</h2>
      <div class="header-actions">
        <button @click="goToVillage" class="village-button">Village</button>
        <button @click="goToSettings" class="settings-button">Settings</button>
        <button @click="signoutUser" class="signout-button">Sign Out</button>
      </div>
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

      <!-- User Management Section -->
      <div class="user-management-section">
        <div class="management-header">
          <h3>User Management</h3>
          <button @click="showAddUserModal = true" class="add-user-button">+ Add User</button>
        </div>
        
        <div class="users-table">
          <div class="table-header">
            <div class="table-cell">ID</div>
            <div class="table-cell">Username</div>
            <div class="table-cell">Email</div>
            <div class="table-cell">Role</div>
            <div class="table-cell">Actions</div>
          </div>
          <div v-for="user in users" :key="user.id" class="table-row">
            <div class="table-cell">{{ user.id }}</div>
            <div class="table-cell">{{ user.username }}</div>
            <div class="table-cell">{{ user.email }}</div>
            <div class="table-cell">{{ user.role }}</div>
            <div class="table-cell actions-cell">
              <button @click="editUser(user)" class="edit-button">Edit</button>
              <button @click="confirmDeleteUser(user)" class="delete-button">Delete</button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Random String Display -->
    <div class="random-string-section">
      <RandomStringDisplay />
    </div>

    <!-- Add User Modal -->
    <modal v-if="showAddUserModal" @close="showAddUserModal = false">
      <h3 slot="header">Add New User</h3>
      <div slot="body">
        <div class="form-group">
          <label for="newUsername">Username</label>
          <input id="newUsername" type="text" v-model="newUser.username" required />
        </div>
        <div class="form-group">
          <label for="newEmail">Email</label>
          <input id="newEmail" type="email" v-model="newUser.email" required />
        </div>
        <div class="form-group">
          <label for="newPassword">Password</label>
          <input id="newPassword" type="password" v-model="newUser.password" required />
        </div>
        <div class="form-group">
          <label for="newRole">Role</label>
          <select id="newRole" v-model="newUser.role">
            <option value="user">User</option>
            <option value="admin">Admin</option>
            <option value="editor">Editor</option>
          </select>
        </div>
      </div>
      <div slot="footer">
        <button @click="addUser" class="save-button">Save User</button>
        <button @click="showAddUserModal = false" class="cancel-button">Cancel</button>
      </div>
    </modal>

    <!-- Delete Confirmation Modal -->
    <modal v-if="showDeleteModal" @close="showDeleteModal = false">
      <h3 slot="header">Confirm User Deletion</h3>
      <div slot="body">
        <p>Are you sure you want to delete user "{{ userToDelete.username }}"?</p>
        <p>This action cannot be undone.</p>
      </div>
      <div slot="footer">
        <button @click="deleteUser" class="confirm-delete-button">Delete</button>
        <button @click="showDeleteModal = false" class="cancel-delete-button">Cancel</button>
      </div>
    </modal>
  </div>
</template>

<script>
import { signout } from "../services/authServices";
import RandomStringDisplay from "./RandomStringDisplay.vue";
import { ref } from 'vue';
import { useRouter } from 'vue-router';

export default {
  name: "Dashboard",
  components: { RandomStringDisplay },
  setup() {
    const router = useRouter();
    
    const notifications = ref([
      { id: 1, title: 'System Update', message: 'New version 2.3.0 is available', time: '2 hours ago', type: 'info', read: false },
      { id: 2, title: 'New User', message: 'John Doe has registered', time: '5 hours ago', type: 'info', read: true },
      { id: 3, title: 'Alert', message: 'High traffic detected', time: '1 day ago', type: 'alert', read: false },
      { id: 4, title: 'Maintenance', message: 'Scheduled maintenance tonight at 2 AM', time: '2 days ago', type: 'info', read: true }
    ]);
    
    const users = ref([
      { id: 1, username: 'admin', email: 'admin@example.com', role: 'admin' },
      { id: 2, username: 'johndoe', email: 'john@example.com', role: 'user' },
      { id: 3, username: 'janedoe', email: 'jane@example.com', role: 'editor' },
      { id: 4, username: 'bobsmith', email: 'bob@example.com', role: 'user' }
    ]);
    
    const showAddUserModal = ref(false);
    const showDeleteModal = ref(false);
    const userToDelete = ref(null);
    
    const newUser = ref({
      username: '',
      email: '',
      password: '',
      role: 'user'
    });
    
    const signoutUser = async () => {
      try {
        const result = await signout();
        console.log(result.message);
        router.push({ name: "Login" });
      } catch (error) {
        console.error("Sign out error", error);
      }
    };
    
    const goToSettings = () => {
      router.push({ name: "Settings" });
    };
    
    const goToVillage = () => {
      router.push({ name: "Village" });
    };
    
    const markAllAsRead = () => {
      notifications.value = notifications.value.map(n => ({ ...n, read: true }));
    };
    
    const dismissNotification = (index) => {
      notifications.value.splice(index, 1);
    };
    
    const addUser = () => {
      const newId = Math.max(...users.value.map(u => u.id)) + 1;
      users.value.push({
        id: newId,
        ...newUser.value
      });
      showAddUserModal.value = false;
      resetNewUser();
    };
    
    const resetNewUser = () => {
      newUser.value = {
        username: '',
        email: '',
        password: '',
        role: 'user'
      };
    };
    
    const editUser = (user) => {
      console.log('Edit user:', user);
      // Implement edit functionality
    };
    
    const confirmDeleteUser = (user) => {
      userToDelete.value = user;
      showDeleteModal.value = true;
    };
    
    const deleteUser = () => {
      users.value = users.value.filter(u => u.id !== userToDelete.value.id);
      showDeleteModal.value = false;
      userToDelete.value = null;
    };
    
    return {
      notifications,
      users,
      newUser,
      showAddUserModal,
      showDeleteModal,
      userToDelete,
      signoutUser,
      goToSettings,
      goToVillage,
      markAllAsRead,
      dismissNotification,
      addUser,
      editUser,
      confirmDeleteUser,
      deleteUser
    };
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

.header-actions {
  display: flex;
  gap: 1rem;
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

.village-button {
  background-color: #4CAF50;
  color: white;
}

.village-button:hover {
  background-color: #3e8e41;
}

.settings-button {
  background-color: #3a3a3a;
  color: rgba(255, 255, 255, 0.87);
}

.settings-button:hover {
  background-color: #4472C4;
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

  .village-button {
    background-color: #4CAF50;
    color: white;
  }
  
  .village-button:hover {
    background-color: #3e8e41;
  }

  .settings-button {
    background-color: #e0e0e0;
    color: #333;
  }
  
  .settings-button:hover {
    background-color: #4472C4;
    color: white;
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