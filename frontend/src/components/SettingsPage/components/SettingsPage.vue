<template>
  <main class="px-4 py-12 mx-auto max-w-[1116px] text-black">
    <h1 class="mb-12 text-4xl text-center">Settings</h1>

    <section class="mx-auto max-w-[800px]">
      <h2 class="mb-6 text-xl font-bold">Category</h2>

      <div class="flex flex-col space-y-6">
        <div class="flex justify-between items-center gap-24">
          <h3 class="text-xl">Setting Item</h3>
          <ToggleSwitch v-model="settings.item1" />
        </div>

        <div class="flex justify-between items-center gap-24">
          <h3 class="text-xl">Setting Item</h3>
          <ToggleSwitch v-model="settings.item2" />
        </div>

        <div class="flex justify-between items-center gap-24">
          <h3 class="text-xl">Setting Item</h3>
          <ToggleSwitch v-model="settings.item3" />
        </div>

        <div class="flex justify-between items-center gap-24">
          <h3 class="text-xl">Setting Item</h3>
          <SelectDropdown v-model="settings.selectedItem">
            <option value="option1">Option 1</option>
            <option value="option2">Option 2</option>
            <option value="option3">Option 3</option>
          </SelectDropdown>
        </div>
      </div>
    </section>
  </main>
</template>

<script setup>
import { ref } from "vue";
import ToggleSwitch from "./ToggleSwitch.vue";
import SelectDropdown from "./SelectDropdown.vue";

const settings = ref({
  item1: false,
  item2: false,
  item3: true,
  selectedItem: "",
});
</script>

<script>
export default {
  name: "SettingsPage",
};
</script>
