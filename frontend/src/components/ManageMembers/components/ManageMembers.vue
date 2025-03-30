<template>
  <div class="min-w-screen min-h-screen bg-gray-100">
    <Header />
    <main class="px-20 py-8 max-md:p-5">
      <h1 class="mb-6 text-5xl text-center text-black max-sm:text-3xl">
        Manage Members
      </h1>

      <div
        class="flex gap-8 justify-center max-md:flex-col max-md:items-center"
      >
        <MembersList :members="members" />

        <aside
          class="flex flex-col gap-3.5 pt-12 max-md:pt-0 max-md:mt-5 max-sm:gap-2.5 max-md:w-full"
        >
          <ActionButton
            text="Add a Member"
            variant="add"
            @click="handleAddMember"
          />
          <ActionButton
            text="Remove a Member"
            variant="remove"
            @click="showRemoveMemberPopup = true"
          />
        </aside>
      </div>
    </main>

    <AddMemberPopup v-model="showAddMemberPopup" @add="addMember" />
    <RemoveMemberPopup
      v-model="showRemoveMemberPopup"
      :members="members"
      @remove="removeMember"
    />
  </div>
</template>

<script setup>
import { ref } from "vue";
import Header from "./Header.vue";
import MembersList from "./MembersList.vue";
import ActionButton from "./ActionButton.vue";
import AddMemberPopup from "./AddMemberPopup.vue";
import RemoveMemberPopup from "./RemoveMemberPopup.vue";

const showAddMemberPopup = ref(false);
const showRemoveMemberPopup = ref(false);

const members = ref([
  { id: 1, username: "member_1" },
  { id: 2, username: "member_2" },
  { id: 3, username: "member_3" },
  // { id: 4, username: "member_4" },
  // { id: 5, username: "member_5" },
  // { id: 6, username: "member_6" },
  // { id: 7, username: "member_7" },
  // { id: 8, username: "member_8" },
]);

const handleAddMember = () => {
  console.log("Opening add member popup"); // Debug log
  showAddMemberPopup.value = true;
};

const addMember = (memberData) => {
  members.value.push({
    id: members.value.length + 1,
    username: memberData.username,
    role: memberData.role,
  });
};

const removeMember = (memberId) => {
  members.value = members.value.filter((member) => member.id !== memberId);
};
</script>
