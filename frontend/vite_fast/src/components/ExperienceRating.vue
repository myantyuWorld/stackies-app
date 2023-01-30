<script setup lang="ts">
defineProps<{
  itemName: string,
  experienceRate : int
}>()
import MasterDataItem from '../components/MasterDataItem.vue'
import Rating from '../components/Rating.vue'
</script>
<template>

  <div class="justify-between p-2 rounded-lg bg-white shadow-indigo-50 shadow-md my-2">
    <div class="flex flex-wrap -m-4 p-4 justify-center">
      <MasterDataItem :name=itemName />
      <div class="p-1 sm:w-2/3 lg:w-3/4 w-full hover:scale-105 duration-500">
        <Rating :rate=experienceRate />
      </div>
    </div>

  </div>
</template>