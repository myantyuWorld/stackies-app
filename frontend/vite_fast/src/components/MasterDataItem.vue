<script setup lang="ts">
defineProps<{
  badgeColor: string
}>()
</script>
<template>
  <div class=" flex items-center  justify-between p-4  rounded-lg bg-white shadow-indigo-50 shadow-md">
    <div
      class="bg-gradient-to-tr w-16 h-16  rounded-full shadow-2xl  border-white  border-dashed border-2  flex justify-center items-center"
      :class="`from-${badgeColor}-500 to-${badgeColor}-400 shadow-${badgeColor}-400`">
      <div>
        <h1 class="text-white text-xs">Java</h1>
      </div>
    </div>

    <div>
      <button
        class="text-xs mt-0 px-3 py-3 bg-black-400 text-white rounded-lg  tracking-wider hover:bg-black-300 outline-none">Del</button>
    </div>

  </div>

</template>