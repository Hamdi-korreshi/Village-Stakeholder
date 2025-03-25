<template>
  <nav class="navbar">
    <div class="logo">
      <!--<img src="@/assets/logo.png" alt="B the Cause Logo" />-->
      <span>B the Cause™</span>
    </div>
    <div class="nav-links">
      <router-link to="/">Home</router-link>
      <router-link to="/login">Login</router-link>
      <router-link to="/registration">Register</router-link>
      <router-link to="/profile">Profile</router-link>
      <router-link to="/passwordReset">Reset Password</router-link>
      <router-link to="/emailVerification">Verify Email</router-link>
    </div>
  </nav>
</template>

<style scoped>
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #eee; /* Light grey background */
  padding: 15px 25px;
  border-bottom: 2px solid #0047ab; /* Blue bottom border */
}

.logo {
  display: flex;
  align-items: center;
  font-size: 18px;
  font-weight: bold;
  color: #4c7fe5;
}

.logo img {
  height: 40px;
  margin-right: 10px;
}

.nav-links {
  display: flex;
  background: #f6f7f8; /* Slightly off-white */
  padding: 12px 20px;
  border-radius: 30px;
  box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
}

.nav-links a {
  text-decoration: none;
  color: #555;
  font-size: 16px;
  margin: 0 15px;
  transition: color 0.3s ease-in-out;
}

.nav-links a:hover {
  color: #000;
  font-weight: bold;
}

.nav-links a.router-link-exact-active {
  color: #0047ab; /* Highlight active link in blue */
  font-weight: bold;
}
</style>
