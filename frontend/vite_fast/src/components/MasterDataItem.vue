<script setup lang="ts">
defineProps<{
  name:string,
  value:string
}>()
</script>
<template>
  <div class="w-1/4 items-center mb-4">
    <input :id="name" type="checkbox" :value="value"
      class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
    <label :for="name" class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">{{ name }}</label>
  </div>
</template>