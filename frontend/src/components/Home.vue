<template>
  <div class="login">
    <div class="overlap-wrapper">
      <div class="overlap">
        <p class="text-wrapper">Back to your digital life</p>
        <p class="div">Choose one of the option to go</p>
        <div class="overlap-group">
          <p class="get-ziontutorial-com">
            <span class="span">Username</span>
            <span class="text-wrapper-2"></span>
            <span class="text-wrapper-3"></span>
          </p>
        </div>
        <div class="div-wrapper">
          <div class="text-wrapper-4">Password</div>
        </div>
        <div class="text-wrapper-5">Or continue with</div>
        <img class="line" alt="Line" src="./line-1.png" />
        <div class="element-wrapper">
          <img class="element" alt="Element" src="./341350527-1184363148892088-4003333439020170582-n-2.png" />
        </div>
        <div class="img-wrapper">
          <img class="img" alt="Element" src="./image.png" />
        </div>
        <div class="overlap-2">
          <img class="element-2" alt="Element" src="./341350527-1184363148892088-4003333439020170582-n-3.png" />
        </div>
        <div class="group">
          <div class="overlap-group-2">
            <div class="text-wrapper-6">Log in</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// Import the Login component
import Login from './login.vue';

export default {
  name: 'Home',
  components: {
    Login, // Register the Login component
  },
  methods: {
    handleLoginSuccess() {
      // Handle login success logic here
      console.log('Login successful!');
      // You can redirect the user or update the state as needed
    },
  },
};
</script>

<style>
.login {
  background-color: #eef2f5;
  display: flex;
  flex-direction: row;
  justify-content: center;
  width: 100%;
}

.login .overlap-wrapper {
  background-color: #eef2f5;
  height: 1024px;
  width: 1440px;
}

.login .overlap {
  background-color: #ffffff;
  border-radius: 4px;
  box-shadow: 0px 1px 3px #0000001a;
  height: 690px;
  left: 427px;
  position: relative;
  top: 167px;
  width: 585px;
}

.login .text-wrapper {
  color: #292929;
  font-family: "Inter-Bold", Helvetica;
  font-size: 30px;
  font-weight: 700;
  left: 80px;
  letter-spacing: 0;
  line-height: normal;
  position: absolute;
  top: 84px;
  white-space: nowrap;
}

.login .div {
  color: #535353;
  font-family: "IBM Plex Serif-Regular", Helvetica;
  font-size: 18px;
  font-weight: 400;
  left: 80px;
  letter-spacing: 0;
  line-height: normal;
  position: absolute;
  top: 132px;
}

.login .overlap-group {
  background-color: #ffffff;
  border: 1px solid;
  border-color: #8abfff;
  border-radius: 10px;
  height: 69px;
  left: 80px;
  position: absolute;
  top: 205px;
  width: 440px;
}

.login .get-ziontutorial-com {
  color: transparent;
  font-family: "Inter-Medium", Helvetica;
  font-size: 16px;
  font-weight: 400;
  left: 35px;
  letter-spacing: 0;
  line-height: normal;
  position: absolute;
  top: 22px;
  white-space: nowrap;
}

.login .span {
  color: #0b0b0b;
  font-weight: 500;
}

.login .text-wrapper-2 {
  color: #4e4e4e;
  font-family: "Inter-Regular", Helvetica;
}

.login .text-wrapper-3 {
  color: #000000;
  font-weight: 500;
}

.login .div-wrapper {
  background-color: #ffffff;
  border: 1px solid;
  border-color: #e6e6e6;
  border-radius: 10px;
  height: 69px;
  left: 80px;
  position: absolute;
  top: 290px;
  width: 440px;
}

.login .text-wrapper-4 {
  color: #4e4e4e;
  font-family: "Inter-Regular", Helvetica;
  font-size: 16px;
  font-weight: 400;
  left: 35px;
  letter-spacing: 0;
  line-height: normal;
  position: absolute;
  top: 22px;
  white-space: nowrap;
}

.login .text-wrapper-5 {
  color: #4e4e4e;
  font-family: "Inter-Regular", Helvetica;
  font-size: 16px;
  font-weight: 400;
  left: 80px;
  letter-spacing: 0;
  line-height: normal;
  position: absolute;
  top: 405px;
  white-space: nowrap;
}

.login .line {
  height: 1px;
  left: 214px;
  position: absolute;
  top: 414px;
  width: 304px;
}

.login .element-wrapper {
  background-color: #f7f7f7;
  border-radius: 4px;
  height: 67px;
  left: 80px;
  position: absolute;
  top: 461px;
  width: 131px;
}

.login .element {
  height: 45px;
  left: 39px;
  position: absolute;
  top: 9px;
  width: 46px;
}

.login .img-wrapper {
  background-color: #f7f7f7;
  border-radius: 4px;
  height: 71px;
  left: 232px;
  position: absolute;
  top: 457px;
  width: 136px;
}

.login .img {
  height: 44px;
  left: 39px;
  position: absolute;
  top: 14px;
  width: 59px;
}

.login .overlap-2 {
  background-color: #f7f7f7;
  border-radius: 4px;
  height: 71px;
  left: 383px;
  position: absolute;
  top: 457px;
  width: 137px;
}

.login .element-2 {
  height: 48px;
  left: 45px;
  position: absolute;
  top: 12px;
  width: 48px;
}

.login .group {
  height: 62px;
  left: 136px;
  position: absolute;
  top: 575px;
  width: 314px;
}

.login .overlap-group-2 {
  background-color: #0366ff;
  border-radius: 8px;
  height: 62px;
  position: relative;
  width: 312px;
}

.login .text-wrapper-6 {
  color: #ffffff;
  font-family: "IBM Plex Serif-Regular", Helvetica;
  font-size: 16px;
  font-weight: 400;
  left: 133px;
  letter-spacing: 0;
  line-height: normal;
  position: absolute;
  top: 21px;
}
</style>