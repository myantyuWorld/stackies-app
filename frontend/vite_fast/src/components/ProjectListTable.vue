<script setup lang="ts">
// defineProps<{
//   itemBadgeColor: string,
//   name: string
// }>()
import  ProjectListDetail from './ProjectListDetail.vue'
</script>
<template>
  <!-- https://flowbite.com/docs/components/tables/#table-filter -->
  <table class="w-full flex flex-row flex-no-wrap sm:bg-white rounded-lg overflow-hidden sm:shadow-lg my-5 table-auto">
    <thead class="text-cyan-900">

      <!-- SP版にした際に、表示する場合、明細件数と同じ数のヘッダーが必要 -->
      <tr class="bg-gray-100 flex flex-col flex-no wrap sm:table-row rounded-l-lg sm:rounded-none mb-2 sm:mb-0">
        <th rowspan="2" class="p-1 text-center text-xs">業種</th>
        <th rowspan="2" class="p-1 text-center text-xs">期間</th>
        <th rowspan="2" class="p-1 text-center text-xs">業務概要</th>
        <th rowspan="2" class="p-1 text-center text-xs">言語</th>
        <th rowspan="2" class="p-1 text-center text-xs">DB/Tool</th>
        <th rowspan="2" class="p-1 text-center text-xs">動作環境</th>
        <th colspan="7" class="p-1 text-center text-xs">作業工程</th>
        <th rowspan="2" class="p-1 text-center text-xs">役割</th>
        <th rowspan="2" class="p-1 text-center text-xs">Actions</th>
      </tr>
      <tr class="bg-gray-100 flex flex-col flex-no wrap sm:table-row rounded-l-lg sm:rounded-none mb-2 sm:mb-0">
        <th rowspan="" class="p-1 text-center text-xs">分析</th>
        <th rowspan="" class="p-1 text-center text-xs">要件</th>
        <th rowspan="" class="p-1 text-center text-xs">基本</th>
        <th rowspan="" class="p-1 text-center text-xs">詳細</th>
        <th rowspan="" class="p-1 text-center text-xs">製造</th>
        <th rowspan="" class="p-1 text-center text-xs">評価</th>
        <th rowspan="" class="p-1 text-center text-xs">運用</th>
      </tr>
    </thead>
    <tbody class="flex-1 sm:flex-none">
      <ProjectListDetail />
      <ProjectListDetail />
      <ProjectListDetail />
      <ProjectListDetail />
    </tbody>
  </table>
</template>