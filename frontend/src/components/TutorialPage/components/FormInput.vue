<template>
  <div class="flex flex-col gap-2.5 mb-11 w-[482px] max-md:w-full">
    <label :for="id" class="text-xl text-black max-sm:text-base">{{
      label
    }}</label>
    <div class="flex gap-2">
      <input
        :id="id"
        :type="type"
        v-model="inputValue"
        class="flex-1 w-full bg-white border text-black border-solid shadow-sm border-zinc-300 h-[39px]"
      />
      <button
        v-if="showSubmitButton"
        @click="handleSubmit"
        type="button"
        class="px-4 py-2 text-sm text-white bg-blue-500 rounded hover:bg-blue-600 transition-colors h-[39px]"
        style="background-color: #4472C4"
      >
        Submit
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "FormInput",
  props: {
    label: {
      type: String,
      required: true,
    },
    id: {
      type: String,
      required: true,
    },
    type: {
      type: String,
      default: "text",
    },
    modelValue: {
      type: String,
      default: "",
    },
    showSubmitButton: {
      type: Boolean,
      default: false,
    },
  },
  emits: ["update:modelValue", "submit"],
  computed: {
    inputValue: {
      get() {
        return this.modelValue;
      },
      set(value) {
        this.$emit("update:modelValue", value);
      },
    },
  },
  methods: {
    handleSubmit() {
      this.$emit("submit", this.inputValue);
    },
  },
};
</script>
