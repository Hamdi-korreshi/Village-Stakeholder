<template>
  <section class="flex flex-col items-center pt-9 max-md:px-5 max-md:py-9">
    <h1 class="mb-7 text-4xl text-black max-sm:text-3xl max-sm:text-center">
      Welcome to your Village!
    </h1>
    <p
      class="mb-16 text-xl text-center text-black max-w-[661px] max-sm:text-base"
    >
      This is a placeholder paragraph for villagers' tutorial page for when they
      first sign up and log into their village account. This will be replaced by
      the actual body, I'm just stretching it out so it's long and fills up a
      decent portion of the page.
    </p>
    <form @submit.prevent="handleSubmit">
      <FormInput
        id="name"
        label="Enter your name:"
        v-model="name"
        :showSubmitButton="true"
        @submit="handleNameSubmit"
      />
      <FormInput
        id="villageName"
        label="What would you like to name your village?"
        v-model="villageName"
        :showSubmitButton="true"
        @submit="handleVillageNameSubmit"
      />
    </form>
  </section>
</template>

<script>
import FormInput from "./FormInput.vue";

export default {
  name: "WelcomeSection",
  components: {
    FormInput,
  },
  data() {
    return {
      name: "",
      villageName: "",
    };
  },
  methods: {
    handleNameSubmit(value) {
      console.log("Name submitted:", value);
      // Handle name submission
    },
    handleVillageNameSubmit(value) {
      console.log("Village name submitted:", value);
      // Handle village name submission
    },
    handleSubmit() {
      console.log("Form submitted:", {
        name: this.name,
        villageName: this.villageName,
      });
    },
  },
};
</script>
