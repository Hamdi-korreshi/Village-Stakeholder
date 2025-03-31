<template>
  <section class="shadow-sm bg-zinc-300 h-[431px] w-full min-w-[300px]">
    <header class="p-1.5 text-sm text-center text-black bg-white shadow-sm">
      Messages
    </header>
    <div
      class="pt-48 text-sm text-center text-black h-[calc(100%_-_28px)]"
      role="region"
      aria-label="Message board"
    >
      No Messages
    </div>
  </section>
</template>

<script>
export default {
  name: "MessageBoard",
};
</script>
