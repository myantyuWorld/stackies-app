<script setup lang="ts">
import MasterDataItem from './MasterDataItem.vue'

defineProps<{
  itemBadgeColor: string,
  name: string,
  list: object
}>()
</script>
<template>
  <div class="rounded-xl bg-white shadow-xl p-6 my-6">
    <div class="container mt-8 px-5 py-1 mx-auto my-auto">
      <h2 class="mb-8 text-xl text-cyan-900 font-bold">{{ name }}
        <!-- TODO：本画面で、言語など追加できるようにする -->
        <!-- <button
          class="text-sm ml-6 px-4 py-2 bg-gray-400  text-white rounded-lg  tracking-wider hover:bg-gray-500 outline-none">Add</button> -->
      </h2>

    </div>
    <div class="flex flex-wrap w-full">
      <MasterDataItem :name=item.name v-for="item of list" :key="item.name" />
    </div>
  </div>

</template>