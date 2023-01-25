<script setup lang="ts">
import MasterDataItem from './MasterDataItem.vue'
defineProps<{
  itemBadgeColor: string,
  name: string
}>()
</script>
<template>
  <div class="rounded-xl bg-white shadow-xl p-6 my-6">
    <div class="container mt-8 px-5 py-1 mx-auto my-auto">
      <h2 class="mb-8 text-xl text-cyan-900 font-bold">{{ name }}
        <button
          class="text-sm ml-6 px-4 py-2 bg-gray-400  text-white rounded-lg  tracking-wider hover:bg-gray-500 outline-none">Add</button>
      </h2>

      <div class="flex flex-wrap -m-4 text-center">
        <div class="p-1 sm:w-1/3 lg:w-1/4 w-full hover:scale-105 duration-500" v-for="n of 6" :key="n">
          <MasterDataItem :badgeColor=itemBadgeColor />
        </div>

      </div>
    </div>
  </div>

</template>