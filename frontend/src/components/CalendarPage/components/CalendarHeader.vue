<template>
  <header class="px-20 py-5 w-full bg-gray-200 max-md:px-5 max-md:max-w-full">
    <div class="flex gap-5 max-md:flex-col items-center justify-center">
      <div class="w-[120px] flex-shrink-0 max-md:w-full">
        <img
          src="../../../assets/logo.png"
          alt="BtheCause"
          class="object-contain w-[90px] max-md:mt-10"
        />
      </div>
      <nav class="flex-1 flex justify-center max-w-screen-xl mx-auto">
        <div
          class="w-[400px] flex justify-center items-center px-16 py-7 bg-gray-100 rounded-[35px] text-stone-500 max-md:px-5 max-md:mt-10 max-md:w-full"
        >
          <div class="flex gap-12 text-xs whitespace-nowrap">
            <a href="#" class="hover:text-stone-700">Home</a>
            <a href="#" class="hover:text-stone-700">About</a>
            <a href="#" class="hover:text-stone-700">Contact</a>
          </div>
        </div>
      </nav>
      <div class="w-[120px] flex-shrink-0 max-md:hidden"></div>
    </div>
  </header>
</template>
