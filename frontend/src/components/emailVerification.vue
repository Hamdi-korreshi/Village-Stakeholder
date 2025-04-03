<template>
    <div>
      <h2>Email Verification</h2>
      <!-- <LoadingSpinner v-if="loading" /> -->
      <div class="container">
        <template v-if="!verificationSuccess">
          <p>Please enter the verification code sent to your email address.</p>
          <label for="verificationCode">
            Verification Code:
            <br />
            <input
              id="verificationCode"
              type="text"
              placeholder="Enter 6-digit code"
              v-model="verificationCode"
              required
              maxlength="6"
            />
          </label>
          <br />
          <button @click="handleVerification">Verify Email</button>
          <button @click="resendCode" :disabled="resendDisabled">
            Resend Code {{ resendCountdown > 0 ? `(${resendCountdown})` : '' }}
          </button>
        </template>
        <div v-else class="success-message">
          <p>Your email has been successfully verified!</p>
          <button @click="handleContinue">Continue</button>
        </div>
        <p class="message">{{ message }}</p>
      </div>
    </div>
  </template>
  
  <script>
  import { ref, onMounted } from 'vue';
  import { useRouter } from 'vue-router';
  //import LoadingSpinner from './LoadingSpinner.vue';
  
  export default {
    components: {
      //LoadingSpinner,
    },
    props: {
      onVerificationSuccess: {
        type: Function,
        required: true,
      },
      email: {
        type: String,
        required: true,
      },
    },
    setup(props) {
      const verificationCode = ref('');
      const message = ref('');
      const loading = ref(false);
      const verificationSuccess = ref(false);
      const resendDisabled = ref(false);
      const resendCountdown = ref(0);
      const router = useRouter();
  
      const startResendCountdown = () => {
        resendDisabled.value = true;
        resendCountdown.value = 30; // 30 seconds countdown
        const timer = setInterval(() => {
          resendCountdown.value--;
          if (resendCountdown.value <= 0) {
            clearInterval(timer);
            resendDisabled.value = false;
          }
        }, 1000);
      };
  
      const handleVerification = async () => {
        if (verificationCode.value.length !== 6) {
          message.value = 'Please enter a valid 6-digit code';
          return;
        }
  
        loading.value = true;
        message.value = '';
  
        try {
          const response = await fetch('http://127.0.0.1:8000/api/verify-email', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              'Authorization': `Bearer ${localStorage.getItem('access_token')}`
            },
            body: JSON.stringify({
              email: props.email,
              code: verificationCode.value
            }),
          });
  
          loading.value = false;
  
          if (response.ok) {
            verificationSuccess.value = true;
            message.value = 'Email verification successful!';
          } else {
            const errorData = await response.json();
            message.value = errorData.detail || 'Invalid verification code';
          }
        } catch (error) {
          loading.value = false;
          message.value = 'An error occurred: ' + error.message;
        }
      };
  
      const resendCode = async () => {
        loading.value = true;
        message.value = '';
  
        try {
          const response = await fetch('http://127.0.0.1:8000/api/resend-verification', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
              'Authorization': `Bearer ${localStorage.getItem('access_token')}`
            },
            body: JSON.stringify({
              email: props.email
            }),
          });
  
          loading.value = false;
  
          if (response.ok) {
            message.value = 'Verification code resent successfully';
            startResendCountdown();
          } else {
            const errorData = await response.json();
            message.value = errorData.detail || 'Failed to resend verification code';
          }
        } catch (error) {
          loading.value = false;
          message.value = 'An error occurred: ' + error.message;
        }
      };
  
      const handleContinue = () => {
        props.onVerificationSuccess();
        router.push({ path: '/' });
      };
  
      onMounted(() => {
        startResendCountdown();
      });
  
      return {
        verificationCode,
        message,
        loading,
        verificationSuccess,
        resendDisabled,
        resendCountdown,
        handleVerification,
        resendCode,
        handleContinue,
      };
    },
  };
  </script>
  
  <style scoped>
  /* Overall layout */
  div {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2rem;
  }
  
  h2 {
    font-size: 2em;
    margin-bottom: 1.5rem;
    color: rgba(255, 255, 255, 0.87);
  }
  
  /* Container styling */
  .container {
    width: 100%;
    max-width: 400px;
    padding: 2em;
    border-radius: 8px;
    background-color: #1a1a1a;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
    text-align: center;
  }
  
  p {
    color: rgba(255, 255, 255, 0.87);
    margin-bottom: 1.5rem;
  }
  
  /* Input field styling */
  label {
    display: block;
    margin-bottom: 1rem;
    font-size: 1em;
    color: rgba(255, 255, 255, 0.87);
    text-align: left;
  }
  
  input {
    width: 100%;
    padding: 0.6em;
    margin-top: 0.5rem;
    border-radius: 8px;
    border: 1px solid #4472C4;
    background-color: #242424;
    color: rgba(255, 255, 255, 0.87);
    font-family: inherit;
    font-size: 1em;
    transition: border-color 0.25s;
    text-align: center;
    letter-spacing: 0.5em;
  }
  
  input:focus {
    border-color: #4472C4;
    outline: none;
  }
  
  input::placeholder {
    color: rgba(255, 255, 255, 0.5);
    letter-spacing: normal;
  }
  
  /* Button styling */
  button {
    border-radius: 8px;
    border: 1px solid transparent;
    padding: 0.6em 1.2em;
    font-size: 1em;
    font-weight: 500;
    font-family: inherit;
    cursor: pointer;
    transition: border-color 0.25s, background-color 0.25s;
    margin: 0.5rem;
  }
  
  button:first-of-type {
    background-color: #4472C4;
    color: white;
  }
  
  button:first-of-type:hover:not(:disabled) {
    background-color: #4472C4;
  }
  
  button:disabled {
    background-color: #3a3a3a;
    color: rgba(255, 255, 255, 0.5);
    cursor: not-allowed;
  }
  
  /* Success message */
  .success-message {
    color: #4CAF50;
    margin: 1.5rem 0;
  }
  
  .success-message button {
    background-color: #4CAF50;
    color: white;
    margin-top: 1rem;
  }
  
  .success-message button:hover {
    background-color: #3e8e41;
  }
  
  /* General message styling */
  .message {
    margin-top: 1.5rem;
    padding: 0.8em;
    border-radius: 8px;
    font-size: 0.9em;
  }
  
  .message.error {
    background-color: #2a1a1a;
    color: #ff6b6b;
  }
  
  /* Light mode adaptation */
  @media (prefers-color-scheme: light) {
    h2 {
      color: #213547;
    }
  
    .container {
      background-color: #f9f9f9;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }
  
    p, label {
      color: #213547;
    }
  
    input {
      background-color: #ffffff;
      color: #213547;
      border-color: #4472C4;
    }
  
    input::placeholder {
      color: rgba(0, 0, 0, 0.5);
    }
  
    button:first-of-type {
      background-color: #4472C4;
    }
  
    button:first-of-type:hover:not(:disabled) {
      background-color: #4472C4;
    }
  
    button:disabled {
      background-color: #e0e0e0;
      color: #666;
    }
  
    .success-message {
      color: #2E7D32;
    }
  
    .message.error {
      background-color: #f8d7da;
      color: #721c24;
    }
  }
  </style>