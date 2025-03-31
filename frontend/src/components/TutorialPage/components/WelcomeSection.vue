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
    <form @submit.prevent="handleFormSubmit" class="w-full max-w-[482px]">
      <FormInput
        id="name"
        label="Enter your name:"
        v-model="formData.name"
        :showSubmitButton="false"
        :disabled="isSubmitting"
      />
      <FormInput
        id="villageName"
        label="What would you like to name your village?"
        v-model="formData.villageName"
        :showSubmitButton="false"
        :disabled="isSubmitting"
      />
      <button
        type="submit"
        class="mt-4 px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700 disabled:opacity-50"
        :disabled="isSubmitting"
        style="background-color: #4472C4;"
      >
        Submit
      </button>
      <div v-if="error" class="text-red-500 text-sm mt-2">{{ error }}</div>
      <div v-if="success" class="text-green-500 text-sm mt-2">{{ success }}</div>
    </form>
  </section>
</template>

<script>
import FormInput from "./FormInput.vue";
import { initializeVillage } from "../../../services/villageServices.js";

export default {
  name: "WelcomeSection",
  components: {
    FormInput,
  },
  data() {
    return {
      formData: {
        name: "",
        villageName: "",
      },
      isSubmitting: false,
      error: "",
      success: "",
      validationRules: {
        name: (value) => value.length >= 2 || "Name must be at least 2 characters",
        villageName: (value) =>
          value.length >= 3 || "Village name must be at least 3 characters",
      },
    };
  },
  methods: {
    validateField(fieldName, value) {
      const rule = this.validationRules[fieldName];
      if (rule) {
        const result = rule(value);
        if (typeof result === "string") {
          this.error = result;
          return false;
        }
      }
      this.error = "";
      return true;
    },
    async handleFormSubmit() {
      this.isSubmitting = true;
      this.error = "";
      this.success = "";

      const isNameValid = this.validateField("name", this.formData.name);
      const isVillageNameValid = this.validateField("villageName", this.formData.villageName);

      if (!isNameValid || !isVillageNameValid) {
        this.isSubmitting = false;
        return;
      }

      try {
        const response = await initializeVillage(this.formData.villageName);
        console.log("Village created:", response);
        this.success = `Welcome to your village, ${this.formData.name}!`;

        // Clear form
        this.formData.name = "";
        this.formData.villageName = "";
      } catch (err) {
        console.error("Error creating village:", err);
        this.error = "An error occurred while creating your village.";
      } finally {
        this.isSubmitting = false;
      }
    },
  },
};
</script>
