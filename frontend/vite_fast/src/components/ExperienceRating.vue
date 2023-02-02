<script setup lang="ts">
import { ref } from 'vue';
import MasterDataItem from '../components/MasterDataItem.vue'
import Rating from '../components/Rating.vue'

defineProps<{
  rate:object
}>()

</script>
<template>

  <div class="justify-between p-2 rounded-lg bg-white shadow-indigo-50 shadow-md my-2">
    <div class="flex flex-wrap h-10 leading-10 m-3">

      <MasterDataItem :name=rate.name />
      <div class="p-1 w-1/4 hover:scale-105 duration-500">
        <select id="countries" v-model="rate.level"
          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
          <option :value="n" v-for="n of 5" :key="n">{{ n }}</option>
        </select>
      </div>
      <div class="p-1 sm:w-1/4 lg:w-2/4 w-full hover:scale-105 duration-500">
        <Rating :rate="rate.level" />
      </div>
    </div>

  </div>
</template>