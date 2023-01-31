<script setup lang="ts">
import { expressionStatement } from '@babel/types';
import { ref } from 'vue';
import MasterDataItem from '../components/MasterDataItem.vue'
import Rating from '../components/Rating.vue'

const data = defineProps<{
  itemName: string,
  experienceRate: int
}>()

const selected = ref(0)
selected.value = data.experienceRate

// selected = data.experienceRate

</script>
<template>

  <div class="justify-between p-2 rounded-lg bg-white shadow-indigo-50 shadow-md my-2">
    <div class="flex flex-wrap h-10 leading-10 m-3">

      <MasterDataItem :name=itemName />
      <div class="p-1 w-1/4 hover:scale-105 duration-500">
        <select v-model="selected" id="countries"
          class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
          <option :value="n" v-for="n of 5" :key="n">{{ n }}</option>
        </select>
      </div>
      <div class="p-1 sm:w-1/4 lg:w-2/4 w-full hover:scale-105 duration-500">
        <Rating :rate=selected />
      </div>
    </div>

  </div>
</template>