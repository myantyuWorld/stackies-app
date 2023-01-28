<script setup lang="ts">
// defineProps<{
//   itemBadgeColor: string,
//   name: string
// }>()
import ProjectListDetail from './ProjectListDetail.vue'
</script>
<template>
  <div class="m-4">
    <!-- https://flowbite.com/docs/components/tables/#table-caption -->
    <div class="w-full flex">
      <caption class="text-lg font-semibold text-left text-gray-900 bg-white dark:text-white dark:bg-gray-800">
        あなたがこれまで経験してきた案件です。
        <p class="mt-1 text-sm font-normal text-gray-500 dark:text-gray-400">
          hogehogeふがふが
        </p>
      </caption>
    </div>
    <!-- https://flowbite.com/docs/components/tables/#table-filter -->
    <table
      class="w-full flex flex-row flex-no-wrap sm:bg-white rounded-lg overflow-hidden sm:shadow-lg my-5 table-auto">
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
        <ProjectListDetail />
        <ProjectListDetail />
        <ProjectListDetail />
        <ProjectListDetail />
        <ProjectListDetail />
      </tbody>
    </table>
    <nav class="flex flex-wrap text-center items-center justify-between" aria-label="Table navigation">

      <div class="sm:w-1/2">
        <span class="text-sm font-normal text-gray-500 dark:text-gray-400">Showing <span
            class="font-semibold text-gray-900 dark:text-white">1-10</span> of <span
            class="font-semibold text-gray-900 dark:text-white">1000</span></span>
      </div>

      <div class="sm:w-1/2">
        <ul class="inline-flex items-center -space-x-px">
          <li>
            <a href="#"
              class="block px-2 py-1 ml-0 leading-tight text-gray-500 bg-white border border-gray-300 rounded-l-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">
              <span class="sr-only">Previous</span>
              <svg class="w-5 h-5" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd"
                  d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z"
                  clip-rule="evenodd"></path>
              </svg>
            </a>
          </li>
          <li>
            <a href="#"
              class="px-2 py-1 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">1</a>
          </li>
          <li>
            <a href="#"
              class="px-2 py-1 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">2</a>
          </li>
          <li>
            <a href="#" aria-current="page"
              class="z-10 px-2 py-1 leading-tight text-blue-600 border border-blue-300 bg-blue-50 hover:bg-blue-100 hover:text-blue-700 dark:border-gray-700 dark:bg-gray-700 dark:text-white">3</a>
          </li>
          <li>
            <a href="#"
              class="px-2 py-1 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">...</a>
          </li>
          <li>
            <a href="#"
              class="px-2 py-1 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">100</a>
          </li>
          <li>
            <a href="#"
              class="block px-2 py-1 leading-tight text-gray-500 bg-white border border-gray-300 rounded-r-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">
              <span class="sr-only">Next</span>
              <svg class="w-5 h-5" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20"
                xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd"
                  d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z"
                  clip-rule="evenodd"></path>
              </svg>
            </a>
          </li>
        </ul>

      </div>

    </nav>
  </div>
</template>