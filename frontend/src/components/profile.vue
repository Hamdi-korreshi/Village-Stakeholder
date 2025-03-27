<template>
  <div class="profile-container">
    <div class="profile-header">
      <h2>User Profile</h2>
      <button @click="toggleEditMode" class="edit-button">
        {{ editMode ? 'Cancel' : 'Edit Profile' }}
      </button>
    </div>

    <div class="profile-content">
      <!-- User Avatar Section -->
      <div class="avatar-section">
        <div class="avatar-container">
          <img 
            :src="user.avatar || 'https://via.placeholder.com/150'" 
            alt="Profile Picture" 
            class="avatar"
          />
          <button v-if="editMode" class="avatar-upload-button" @click="triggerFileInput">
            Change Photo
          </button>
          <input 
            type="file" 
            ref="fileInput" 
            @change="handleAvatarUpload" 
            accept="image/*" 
            style="display: none"
          />
        </div>
      </div>

      <!-- User Details Section -->
      <div class="details-section">
        <form @submit.prevent="saveProfile" class="profile-form">
          <div class="form-group">
            <label for="username">Username</label>
            <input 
              id="username" 
              type="text" 
              v-model="user.username" 
              :disabled="!editMode"
              required
            />
          </div>

          <div class="form-group">
            <label for="email">Email</label>
            <input 
              id="email" 
              type="email" 
              v-model="user.email" 
              :disabled="!editMode"
              required
            />
          </div>

          <div class="form-group">
            <label for="fullName">Full Name</label>
            <input 
              id="fullName" 
              type="text" 
              v-model="user.fullName" 
              :disabled="!editMode"
            />
          </div>

          <div class="form-group">
            <label for="bio">Bio</label>
            <textarea 
              id="bio" 
              v-model="user.bio" 
              :disabled="!editMode"
              rows="3"
            ></textarea>
          </div>

          <!-- Only show password fields in edit mode -->
          <div v-if="editMode" class="password-section">
            <h3>Change Password</h3>
            <div class="form-group">
              <label for="currentPassword">Current Password</label>
              <input 
                id="currentPassword" 
                type="password" 
                v-model="password.current"
              />
            </div>
            <div class="form-group">
              <label for="newPassword">New Password</label>
              <input 
                id="newPassword" 
                type="password" 
                v-model="password.new"
              />
            </div>
            <div class="form-group">
              <label for="confirmPassword">Confirm New Password</label>
              <input 
                id="confirmPassword" 
                type="password" 
                v-model="password.confirm"
              />
            </div>
          </div>

          <div v-if="editMode" class="form-actions">
            <button type="submit" class="save-button">Save Changes</button>
            <button type="button" @click="resetForm" class="cancel-button">Reset</button>
          </div>
        </form>
      </div>

      <!-- Settings Section -->
      <div class="settings-section">
        <h3>Account Settings</h3>
        <div class="settings-options">
          <div class="setting-item">
            <span>Email Notifications</span>
            <toggle-switch v-model="settings.emailNotifications" />
          </div>
          <div class="setting-item">
            <span>Dark Mode</span>
            <toggle-switch v-model="settings.darkMode" />
          </div>
          <div class="setting-item">
            <span>Two-Factor Authentication</span>
            <toggle-switch v-model="settings.twoFactorAuth" />
          </div>
        </div>
        
        <div class="danger-zone">
          <h4>Danger Zone</h4>
          <button @click="confirmDeletion" class="delete-account-button">
            Delete Account
          </button>
        </div>
      </div>
    </div>

    <!-- Confirmation Modal -->
    <modal v-if="showDeleteModal" @close="showDeleteModal = false">
      <h3 slot="header">Confirm Account Deletion</h3>
      <div slot="body">
        <p>Are you sure you want to delete your account? This action cannot be undone.</p>
        <p>All your data will be permanently removed.</p>
      </div>
      <div slot="footer">
        <button @click="deleteAccount" class="confirm-delete-button">Delete Account</button>
        <button @click="showDeleteModal = false" class="cancel-delete-button">Cancel</button>
      </div>
    </modal>

    <p class="message">{{ message }}</p>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

export default {
  name: 'ProfilePage',
  setup() {
    const router = useRouter();
    const fileInput = ref(null);
    const editMode = ref(false);
    const showDeleteModal = ref(false);
    const message = ref('');
    const originalUserData = ref({});
    
    const user = ref({
      username: '',
      email: '',
      fullName: '',
      bio: '',
      avatar: ''
    });

    const password = ref({
      current: '',
      new: '',
      confirm: ''
    });

    const settings = ref({
      emailNotifications: true,
      darkMode: false,
      twoFactorAuth: false
    });

    // Fetch user data when component mounts
    onMounted(async () => {
      try {
        const token = localStorage.getItem('access_token');
        const response = await fetch('http://127.0.0.1:8000/api/user/profile', {
          headers: {
            'Authorization': `Bearer ${token}`
          }
        });

        if (response.ok) {
          const data = await response.json();
          user.value = data;
          originalUserData.value = {...data};
          
          // Fetch settings if available
          if (data.settings) {
            settings.value = data.settings;
          }
        } else {
          throw new Error('Failed to fetch user data');
        }
      } catch (error) {
        message.value = 'Error loading profile: ' + error.message;
      }
    });

    const toggleEditMode = () => {
      editMode.value = !editMode.value;
      if (!editMode.value) {
        resetForm();
      }
    };

    const triggerFileInput = () => {
      fileInput.value.click();
    };

    const handleAvatarUpload = (event) => {
      const file = event.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = (e) => {
          user.value.avatar = e.target.result;
        };
        reader.readAsDataURL(file);
      }
    };

    const saveProfile = async () => {
      try {
        const token = localStorage.getItem('access_token');
        const response = await fetch('http://127.0.0.1:8000/api/user/profile', {
          method: 'PUT',
          headers: {
            'Authorization': `Bearer ${token}`,
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            ...user.value,
            password: password.value.new ? password.value : null,
            settings: settings.value
          })
        });

        if (response.ok) {
          const data = await response.json();
          user.value = data;
          originalUserData.value = {...data};
          editMode.value = false;
          message.value = 'Profile updated successfully!';
          
          // Clear password fields
          password.value = { current: '', new: '', confirm: '' };
          
          // Hide message after 3 seconds
          setTimeout(() => {
            message.value = '';
          }, 3000);
        } else {
          throw new Error('Failed to update profile');
        }
      } catch (error) {
        message.value = 'Error updating profile: ' + error.message;
      }
    };

    const resetForm = () => {
      user.value = {...originalUserData.value};
      password.value = { current: '', new: '', confirm: '' };
    };

    const confirmDeletion = () => {
      showDeleteModal.value = true;
    };

    const deleteAccount = async () => {
      try {
        const token = localStorage.getItem('access_token');
        const response = await fetch('http://127.0.0.1:8000/api/user/profile', {
          method: 'DELETE',
          headers: {
            'Authorization': `Bearer ${token}`
          }
        });

        if (response.ok) {
          localStorage.removeItem('access_token');
          router.push('/login');
        } else {
          throw new Error('Failed to delete account');
        }
      } catch (error) {
        message.value = 'Error deleting account: ' + error.message;
        showDeleteModal.value = false;
      }
    };

    return {
      user,
      password,
      settings,
      editMode,
      showDeleteModal,
      message,
      fileInput,
      toggleEditMode,
      triggerFileInput,
      handleAvatarUpload,
      saveProfile,
      resetForm,
      confirmDeletion,
      deleteAccount
    };
  }
};
</script>

<style scoped>
/* Overall layout */
.profile-container {
  max-width: 1280px;
  margin: 0 auto;
  padding: 2rem;
}

.profile-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
}

h2, h3, h4 {
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

h4 {
  font-size: 1.2em;
}

.profile-content {
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: 2rem;
}

/* Avatar Section */
.avatar-section {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.avatar-container {
  position: relative;
  margin-bottom: 1.5rem;
}

.avatar {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  object-fit: cover;
  border: 3px solid #4472C4;
}

.avatar-upload-button {
  position: absolute;
  bottom: 10px;
  left: 50%;
  transform: translateX(-50%);
  background-color: #1a1a1a;
  color: rgba(255, 255, 255, 0.87);
  border: 1px solid #4472C4;
  padding: 0.5em 1em;
  border-radius: 8px;
  font-size: 0.9em;
  cursor: pointer;
  transition: border-color 0.25s;
}

.avatar-upload-button:hover {
  border-color: #4472C4;
}

/* Details Section */
.details-section, .settings-section {
  background-color: #1a1a1a;
  padding: 2em;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
}

.settings-section {
  grid-column: span 2;
  margin-top: 1rem;
}

.form-group {
  margin-bottom: 1.5rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.5rem;
  color: rgba(255, 255, 255, 0.87);
}

.form-group input,
.form-group textarea {
  width: 100%;
  padding: 0.6em;
  border-radius: 8px;
  border: 1px solid #4472C4;
  background-color: #242424;
  color: rgba(255, 255, 255, 0.87);
  font-family: inherit;
  transition: border-color 0.25s;
}

.form-group textarea {
  min-height: 100px;
  resize: vertical;
}

.form-group input:focus,
.form-group textarea:focus {
  border-color: #4472C4;
  outline: none;
}

.form-group input:disabled,
.form-group textarea:disabled {
  background-color: #2a2a2a;
  color: rgba(255, 255, 255, 0.6);
  border-color: #3a3a3a;
}

.password-section {
  margin-top: 2rem;
  padding-top: 1.5rem;
  border-top: 1px solid #3a3a3a;
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

.edit-button, .save-button {
  background-color: #4472C4;
  color: white;
}

.edit-button:hover, .save-button:hover {
  background-color: #4472C4;
  border-color: #4472C4;
}

.cancel-button {
  background-color: #3a3a3a;
  color: rgba(255, 255, 255, 0.87);
}

.cancel-button:hover {
  border-color: #4472C4;
}

.delete-account-button {
  background-color: #ff4444;
  color: white;
}

.delete-account-button:hover {
  background-color: #cc0000;
  border-color: #cc0000;
}

.form-actions {
  display: flex;
  gap: 1rem;
  margin-top: 1.5rem;
}

/* Settings Section */
.settings-options {
  margin: 1.5rem 0;
}

.setting-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 0;
  border-bottom: 1px solid #3a3a3a;
}

.danger-zone {
  margin-top: 2rem;
  padding: 1.5rem;
  background-color: #2a1a1a;
  border-radius: 8px;
  border: 1px solid #ff4444;
}

/* Message */
.message {
  margin-top: 1.5rem;
  padding: 0.8em;
  border-radius: 8px;
  text-align: center;
}

.message.success {
  background-color: #1a2a1a;
  color: #4CAF50;
}

.message.error {
  background-color: #2a1a1a;
  color: #ff6b6b;
}

/* Light mode adaptation */
@media (prefers-color-scheme: light) {
  h2, h3, h4 {
    color: #213547;
  }

  .avatar {
    border-color: #4472C4;
  }

  .avatar-upload-button {
    background-color: #f9f9f9;
    color: #213547;
    border-color: #4472C4;
  }

  .details-section, .settings-section {
    background-color: #f9f9f9;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  }

  .form-group label {
    color: #213547;
  }

  .form-group input,
  .form-group textarea {
    background-color: #ffffff;
    color: #213547;
    border-color: #4472C4;
  }

  .form-group input:disabled,
  .form-group textarea:disabled {
    background-color: #f0f0f0;
    color: #666;
    border-color: #ddd;
  }

  .password-section {
    border-top-color: #ddd;
  }

  .edit-button, .save-button {
    background-color: #4472C4;
  }

  .edit-button:hover, .save-button:hover {
    background-color: #4472C4;
  }

  .cancel-button {
    background-color: #e0e0e0;
    color: #333;
  }

  .setting-item {
    border-bottom-color: #ddd;
  }

  .danger-zone {
    background-color: #fff5f5;
    border-color: #ffcccc;
  }

  .message.success {
    background-color: #d4edda;
    color: #155724;
  }

  .message.error {
    background-color: #f8d7da;
    color: #721c24;
  }
}
</style>