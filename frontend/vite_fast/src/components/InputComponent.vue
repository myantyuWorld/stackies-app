<script setup lang="ts">
defineProps<{
  inputMode: boolean,
  value: string,
  placeholder: string
}>()
</script>
<template>
  <input type="text"
    class="block w-full p-2 border rounded border-gray-300 focus:outline-none focus:ring-1 focus:ring-gray-400 focus:border-transparent text-black-800"
    :placeholder="placeholder" :value="value"
    :class="{'disabled:bg-slate-50 disabled:text-slate-500 disabled:border-slate-200 disabled:shadow-none' : inputMode}"
    :disabled="inputMode">
</template>