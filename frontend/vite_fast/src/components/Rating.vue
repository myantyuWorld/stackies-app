<script setup lang="ts">
// defineProps<{
//   badgeColor: string
// }>()
</script>
<template>
  <!-- <div class="grid w-full grid-cols-4 space-x-2 rounded-xl bg-white my-auto p-2" x-data="app"> -->
  <div class=" flex items-center  justify-between p-4  rounded-lg bg-white shadow-indigo-50 shadow-md" x-data="app">
    <div>
      <input type="radio" name="option" id="1" class="peer hidden" checked />
      <label for="1"
        class="block cursor-pointer select-none rounded-xl p-2 text-center peer-checked:bg-blue-500 peer-checked:font-bold peer-checked:text-white">1</label>
    </div>

    <div>
      <input type="radio" name="option" id="2" class="peer hidden" />
      <label for="2"
        class="block cursor-pointer select-none rounded-xl p-2 text-center peer-checked:bg-blue-500 peer-checked:font-bold peer-checked:text-white">2</label>
    </div>

    <div>
      <input type="radio" name="option" id="3" class="peer hidden" />
      <label for="3"
        class="block cursor-pointer select-none rounded-xl p-2 text-center peer-checked:bg-blue-500 peer-checked:font-bold peer-checked:text-white">3</label>
    </div>

    <div>
      <input type="radio" name="option" id="4" class="peer hidden" />
      <label for="4"
        class="block cursor-pointer select-none rounded-xl p-2 text-center peer-checked:bg-blue-500 peer-checked:font-bold peer-checked:text-white">4</label>
    </div>
  </div>
</template>