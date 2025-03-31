<template>
  <div class="profile-container">
    <div class="profile-header">
      <h2>User Profile</h2>
      <button @click="toggleEditMode" class="edit-button">
        {{ editMode ? 'Exit' : 'Edit Profile' }}
      </button>
    </div>

    <div v-if="loading" class="loading-message">Loading profile...</div>
    <div v-if="error" class="error-message">{{ error }}</div>

    <div v-if="!loading && !error" class="profile-content">
      <!-- User Avatar Section -->
      <div class="avatar-section">
        <div class="avatar-container">
          <img 
            :src="user.profile_picture || 'https://via.placeholder.com/150'" 
            alt="Profile Picture" 
            class="avatar"
          />
        </div>
        <div v-if="editMode" class="avatar-url-input">
          <label for="profile_picture">Image URL:</label>
          <input 
            type="url" 
            id="profile_picture" 
            v-model="user.profile_picture" 
            placeholder="Enter image URL"
          />
        </div>
      </div>

      <!-- User Details Section -->
      <div class="details-section">
        <form @submit.prevent="handleUpdate" class="profile-form">
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
            <label for="full_name">Full Name</label>
            <input 
              id="full_name" 
              type="text" 
              v-model="user.full_name" 
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

          <!-- Only show password change button in edit mode -->
          <div v-if="editMode" class="password-section">
            <button type="button" @click="redirectToChangePassword" class="edit-button">
              Change Password
            </button>
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
        
        <div class="danger-zone">
          <h4>Danger Zone</h4>
          <button @click="confirmDeletion" class="delete-account-button">
            Delete Account
          </button>
          <p v-if="deleteMessage" class="message success">{{ deleteMessage }}</p>
          <p v-if="deleteError" class="message error">{{ deleteError }}</p>
        </div>
      </div>
    </div>

    <!-- Confirmation Modal -->
    <modal v-if="showDeleteModal" @close="showDeleteModal = false">
      <h3 slot="header">Confirm Account Deletion</h3>
      <div slot="body">
        <p>Are you sure you want to delete your account? This action cannot be undone.</p>
        <p>All your data will be permanently removed.</p>
        <div class="confirmation-input">
          <label for="confirmDelete">Type "DELETE" to confirm:</label>
          <input 
            id="confirmDelete" 
            type="text" 
            v-model="deleteConfirmation" 
            placeholder="Type DELETE"
          />
        </div>
      </div>
      <div slot="footer">
        <button 
          @click="handleDelete" 
          class="confirm-delete-button"
          :disabled="deleteConfirmation !== 'DELETE'"
        >
          Delete Account
        </button>
        <button @click="showDeleteModal = false" class="cancel-delete-button">Cancel</button>
      </div>
    </modal>

    <p v-if="updateMessage" class="message success">{{ updateMessage }}</p>
    <p v-if="updateError" class="message error">{{ updateError }}</p>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { get_profile, update_profile, delete_profile } from '../services/authServices.js';
import { toast } from "vue3-toastify";
import "vue3-toastify/dist/index.css";

export default {
  name: 'ProfilePage',
  setup() {
    const router = useRouter();
    const editMode = ref(false);
    const showDeleteModal = ref(false);
    const updateMessage = ref('');
    const updateError = ref('');
    const deleteMessage = ref('');
    const deleteError = ref('');
    const deleteConfirmation = ref('');
    const originalUserData = ref({});
    const loading = ref(true);
    const error = ref(null);
    
    const user = ref({
      username: '',
      email: '',
      full_name: '',
      bio: '',
      profile_picture: ''
    });

    const redirectToChangePassword = () => {
      router.push({ name: "PasswordReset" });
    };

    // Fetch user data when component mounts
    const fetchProfile = async () => {
      try {
        const data = await get_profile();
        user.value = data;
        originalUserData.value = {...data};
      } catch (err) {
        error.value = err.response?.data?.error || "Failed to load profile.";
        console.error("Error fetching profile:", err);
      } finally {
        loading.value = false;
      }
    };

    onMounted(fetchProfile);

    const toggleEditMode = () => {
      editMode.value = !editMode.value;
      if (!editMode.value) {
        resetForm();
      }
    };

    const handleUpdate = async () => {
      updateMessage.value = '';
      updateError.value = '';
      
      const payload = {
        full_name: user.value.full_name,
        email: user.value.email,
        username: user.value.username,
        profile_picture: user.value.profile_picture,
        bio: user.value.bio
      };

      try {
        await update_profile(payload);
        updateMessage.value = "Profile updated successfully!";
        originalUserData.value = {...user.value};
        
        toast.success("Profile updated successfully!", {
          autoClose: 5000,
        });
        
        setTimeout(() => {
          updateMessage.value = '';
        }, 3000);

        await fetchProfile();
      } catch (err) {
        updateError.value = err.response?.data?.detail || "An error occurred updating your profile.";
        console.error("Update profile error:", err);
        toast.error("An error occurred updating your profile.", {
          autoClose: 5000,
        });
      }
    };

    const resetForm = () => {
      user.value = {...originalUserData.value};
      updateMessage.value = '';
      updateError.value = '';
    };

    const confirmDeletion = () => {
      showDeleteModal.value = true;
      deleteConfirmation.value = '';
      deleteMessage.value = '';
      deleteError.value = '';
    };

    const handleDelete = async () => {
      deleteMessage.value = '';
      deleteError.value = '';
      
      try {
        const response = await delete_profile();
        deleteMessage.value = response?.message || "Profile deleted successfully.";
        toast.success("Profile deleted successfully. We are sorry to see you go :(", {
          autoClose: 5000,
        });
        
        setTimeout(() => {
          router.push({ name: 'login' });
        }, 2000);
      } catch (err) {
        deleteError.value = err.response?.data?.detail || "An error occurred while deleting your profile.";
        console.error("Delete profile error:", err);
        toast.error("An error occurred while deleting your profile.", {
          autoClose: 5000,
        });
      } finally {
        showDeleteModal.value = false;
      }
    };

    return {
      user,
      editMode,
      showDeleteModal,
      updateMessage,
      updateError,
      deleteMessage,
      deleteError,
      deleteConfirmation,
      loading,
      error,
      toggleEditMode,
      handleUpdate,
      resetForm,
      confirmDeletion,
      handleDelete,
      redirectToChangePassword
    };
  }
};
</script>

<style scoped>
/* Avatar URL Input */
.avatar-url-input {
  margin-top: 1rem;
  width: 100%;
}

.avatar-url-input label {
  display: block;
  margin-bottom: 0.5rem;
  color: rgba(255, 255, 255, 0.87);
}

.avatar-url-input input {
  width: 100%;
  padding: 0.6em;
  border-radius: 8px;
  border: 1px solid #4472C4;
  background-color: #242424;
  color: rgba(255, 255, 255, 0.87);
}

.confirmation-input {
  margin-top: 1rem;
}

.confirmation-input label {
  display: block;
  margin-bottom: 0.5rem;
  color: rgba(255, 255, 255, 0.87);
}

.confirmation-input input {
  width: 100%;
  padding: 0.6em;
  border-radius: 8px;
  border: 1px solid #ff4444;
  background-color: #242424;
  color: rgba(255, 255, 255, 0.87);
}

.confirm-delete-button:disabled {
  background-color: #5a5a5a;
  cursor: not-allowed;
  opacity: 0.7;
}

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

.loading-message {
  text-align: center;
  padding: 2rem;
  color: rgba(255, 255, 255, 0.87);
}

.error-message {
  color: red;
  text-align: center;
  padding: 2rem;
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

.confirm-delete-button {
  background-color: #ff4444;
  color: white;
}

.confirm-delete-button:hover:not(:disabled) {
  background-color: #cc0000;
  border-color: #cc0000;
}

.cancel-delete-button {
  background-color: #3a3a3a;
  color: rgba(255, 255, 255, 0.87);
  margin-left: 1rem;
}

.cancel-delete-button:hover {
  border-color: #4472C4;
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

  .avatar-url-input label {
    color: #213547;
  }

  .avatar-url-input input {
    background-color: #ffffff;
    color: #213547;
    border-color: #4472C4;
  }

  .confirmation-input label {
    color: #213547;
  }

  .confirmation-input input {
    background-color: #ffffff;
    color: #213547;
    border-color: #ff4444;
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