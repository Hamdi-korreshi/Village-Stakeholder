<template>
  <div
    class="grid gap-14 grid-cols-[1fr_2fr_1fr] max-w-[1200px] mx-auto max-md:gap-5 max-md:grid-cols-[1fr] max-sm:p-2.5"
  >
    <MembersList />
    <MessageBoard />
    <ActionButtons />
  </div>
</template>

<script>
import MembersList from "./MembersList.vue";
import MessageBoard from "./MessageBoard.vue";
import ActionButtons from "./ActionButtons.vue";

export default {
  name: "DashboardGrid",
  components: {
    MembersList,
    MessageBoard,
    ActionButtons,
  },
};
</script>
