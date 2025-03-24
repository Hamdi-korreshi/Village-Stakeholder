<template>
  <aside class="w-full text-white max-md:mt-8">
    <section
      class="px-0.5 pt-0.5 pb-72 text-black bg-gray-100 border border-solid shadow-sm border-black border-opacity-0 max-md:pb-24"
    >
      <header
        class="px-16 py-1 text-sm bg-gray-100 border border-solid border-black border-opacity-0 shadow-[0px_4px_4px_rgba(0,0,0,0.25)] max-md:px-5"
      >
        March 7
      </header>

      <article
        class="flex flex-col pt-2 pr-10 pb-4 pl-3.5 mt-2.5 mb-0 bg-green-100 rounded-xl border border-solid border-black border-opacity-0 shadow-[0px_4px_4px_rgba(0,0,0,0.25)] max-md:pr-5 max-md:mb-2.5"
      >
        <time class="self-start text-sm">8:30am - 9:00am</time>
        <p class="mt-2 text-xs">
          Doctor's Appointment - 123 Central Ave. Newark, NJ
        </p>
      </article>
    </section>

    <div class="mt-4 space-y-3.5">
      <button
        class="flex gap-5 justify-between items-start px-10 py-0.5 w-full bg-green-500 rounded-xl border border-solid border-black border-opacity-0 shadow-[0px_4px_4px_rgba(0,0,0,0.25)] max-md:px-5 max-md:mr-0.5"
      >
        <span class="mt-4 text-xl font-bold">Add a Schedule Item</span>
        <span class="text-5xl max-md:text-4xl">+</span>
      </button>

      <button
        class="flex flex-col px-7 py-px w-full bg-red-400 rounded-xl border border-solid border-black border-opacity-0 shadow-[0px_4px_4px_rgba(0,0,0,0.25)] max-md:px-5 max-md:mr-0.5"
      >
        <span class="self-end text-5xl max-md:text-4xl">-</span>
        <span class="z-10 mt-3.5 -mb-1.5 text-xl font-bold"
          >Remove a Schedule Item</span
        >
      </button>
    </div>
  </aside>
</template>
