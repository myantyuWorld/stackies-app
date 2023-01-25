<script setup lang="ts">
import ExperienceRating from '../components/ExperienceRating.vue'

import { onMounted } from 'vue'
import { initDropdowns, } from 'flowbite'

// initialize components based on data attribute selectors
onMounted(() => {
  initDropdowns();
})

</script>

<template>
  <div class="py-8 bg-gradient-to-br from-sky-100 to-gray-200">
    <div class="flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
      <div class="relative container m-auto px-0 text-gray-500 md:px-0 xl:px-12">
        <div class="m-auto">
          <div class="rounded-xl bg-white shadow-xl">
            <div class="p-6 sm:p-6">

              <div class="space-y-4">
                <h2 class="mb-0 text-2xl text-cyan-900 font-bold">基本情報登録</h2>
              </div>

              <div class="flex bg-white">
                <div class="w-full px-4 shadow-none">
                  <!-- イニシャル、住所、資格（名前、取得時期）、学歴、生年月日、自己PR） -->
                  <form action="#" class="p-0">
                    <div class="mt-5 w-full">

                      <div>
                        <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
                          for="grid-password">
                          イニシャル
                        </label>
                        <input type="text"
                          class="block w-full p-2 border rounded border-gray-300 focus:outline-none focus:ring-1 focus:ring-gray-400 focus:border-transparent disabled:bg-slate-50 disabled:text-slate-500 disabled:border-slate-200 disabled:shadow-none"
                          placeholder="" disabled value="Y O">
                      </div>

                    </div>
                    <div class="mt-5 w-full">

                      <div>
                        <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
                          for="grid-password">
                          生年月日
                        </label>
                        <input type="date"
                          class="block w-full p-2 border rounded border-gray-300 focus:outline-none focus:ring-1 focus:ring-gray-400 focus:border-transparent disabled:bg-slate-50 disabled:text-slate-500 disabled:border-slate-200 disabled:shadow-none"
                          placeholder="生年月日" disabled>
                      </div>

                    </div>
                    <div class="mt-5">

                      <div>
                        <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
                          for="grid-password">
                          最終学歴
                        </label>
                        <input type="text"
                          class="block w-full p-2 border rounded border-gray-300 focus:outline-none focus:ring-1 focus:ring-gray-400 focus:border-transparent disabled:bg-slate-50 disabled:text-slate-500 disabled:border-slate-200 disabled:shadow-none"
                          placeholder="最終学歴" disabled>
                      </div>

                    </div>
                    <div class="mt-5">

                      <div>
                        <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
                          for="grid-password">
                          住所
                        </label>
                        <input type="text"
                          class="block w-full p-2 border rounded border-gray-300 focus:outline-none focus:ring-1 focus:ring-gray-400 focus:border-transparent disabled:bg-slate-50 disabled:text-slate-500 disabled:border-slate-200 disabled:shadow-none"
                          placeholder="住所" disabled>
                      </div>

                    </div>
                    <div class="mt-5">

                      <div>
                        <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
                          for="grid-password">
                          資格
                        </label>
                        <input type="text"
                          class="block w-full p-2 border rounded border-gray-300 focus:outline-none focus:ring-1 focus:ring-gray-400 focus:border-transparent disabled:bg-slate-50 disabled:text-slate-500 disabled:border-slate-200 disabled:shadow-none"
                          placeholder="資格" disabled>
                      </div>

                    </div>

                    <div class="mt-5">

                      <div>
                        <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
                          for="grid-password">
                          自己PR
                        </label>
                        <textarea type="text"
                          class="block w-full p-2 border rounded border-gray-300 focus:outline-none focus:ring-1 focus:ring-gray-400 focus:border-transparent disabled:bg-slate-50 disabled:text-slate-500 disabled:border-slate-200 disabled:shadow-none"
                          placeholder="Email" disabled></textarea>
                      </div>

                    </div>
                  </form>

                </div>
              </div>

            </div>
            <div class="p-6 sm:p-6">

              <div class="space-y-0">
                <h2 class="mb-0 text-2xl text-cyan-900 font-bold">
                  経験技術
                </h2>
              </div>

              <div class="flex bg-white">
                <div class="w-full px-4 shadow-none">
                  <!-- 　以下の項目が必要
                　　業種、
                　　期間、
                　　業務概要、
                　　言語、
                　　DB・ツール、
                　　動作環境、
                　　作業工程（調査・分析、要件定義、基本設計、詳細設計、製造、評価、運用保守）、
                　　規模、
                　　役割 -->
                  <div class="mt-5">
                    <!-- https://flowbite.com/docs/components/tables/#table-caption -->
                    <div class="w-full mx-auto my-5">
                      <caption
                      class="p-5 text-lg font-semibold text-left text-gray-900 bg-white dark:text-white dark:bg-gray-800">
                      Our products
                      <p class="mt-1 text-sm font-normal text-gray-500 dark:text-gray-400">Browse a list of Flowbite
                        products designed to help you work and play, stay organized, get answers, keep in touch, grow
                        your business, and more.</p>
                      </caption>
                    </div>

                    <!-- https://flowbite.com/docs/components/tables/#table-filter -->
                    <table
                      class="w-full flex flex-row flex-no-wrap sm:bg-white rounded-lg overflow-hidden sm:shadow-lg my-5">

                      <div class="flex items-center justify-between">
                        <div>
                          <button id="dropdownRadioButton" data-dropdown-toggle="dropdownRadio"
                            class="inline-flex items-center text-gray-500 bg-white border border-gray-300 focus:outline-none hover:bg-gray-100 focus:ring-4 focus:ring-gray-200 font-medium rounded-lg text-sm px-3 py-1.5 dark:bg-gray-800 dark:text-white dark:border-gray-600 dark:hover:bg-gray-700 dark:hover:border-gray-600 dark:focus:ring-gray-700"
                            type="button">
                            <svg class="w-4 h-4 mr-2 text-gray-400" aria-hidden="true" fill="currentColor"
                              viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                              <path fill-rule="evenodd"
                                d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-12a1 1 0 10-2 0v4a1 1 0 00.293.707l2.828 2.829a1 1 0 101.415-1.415L11 9.586V6z"
                                clip-rule="evenodd"></path>
                            </svg>
                            Last 30 days
                            <svg class="w-3 h-3 ml-2" aria-hidden="true" fill="none" stroke="currentColor"
                              viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7">
                              </path>
                            </svg>
                          </button>
                          <!-- Dropdown menu -->
                          <div id="dropdownRadio"
                            class="z-10 hidden w-48 bg-white divide-y divide-gray-100 rounded-lg shadow dark:bg-gray-700 dark:divide-gray-600"
                            data-popper-reference-hidden="" data-popper-escaped="" data-popper-placement="top"
                            style="position: absolute; inset: auto auto 0px 0px; margin: 0px; transform: translate3d(522.5px, 3847.5px, 0px);">
                            <ul class="p-3 space-y-1 text-sm text-gray-700 dark:text-gray-200"
                              aria-labelledby="dropdownRadioButton">
                              <li>
                                <div class="flex items-center p-2 rounded hover:bg-gray-100 dark:hover:bg-gray-600">
                                  <input id="filter-radio-example-1" type="radio" value="" name="filter-radio"
                                    class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                                  <label for="filter-radio-example-1"
                                    class="w-full ml-2 text-sm font-medium text-gray-900 rounded dark:text-gray-300">Last
                                    day</label>
                                </div>
                              </li>
                              <li>
                                <div class="flex items-center p-2 rounded hover:bg-gray-100 dark:hover:bg-gray-600">
                                  <input checked="" id="filter-radio-example-2" type="radio" value=""
                                    name="filter-radio"
                                    class="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600">
                                  <label for="filter-radio-example-2"
                                    class="w-full ml-2 text-sm font-medium text-gray-900 rounded dark:text-gray-300">Last
                                    7 days</label>
                                </div>
                              </li>
                            </ul>
                          </div>
                        </div>
                        <label for="table-search" class="sr-only">Search</label>
                        <div class="relative">
                          <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
                            <svg class="w-5 h-5 text-gray-500 dark:text-gray-400" aria-hidden="true" fill="currentColor"
                              viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                              <path fill-rule="evenodd"
                                d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z"
                                clip-rule="evenodd"></path>
                            </svg>
                          </div>
                          <input type="text" id="table-search"
                            class="block p-2 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg w-80 bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                            placeholder="Search for items">
                        </div>
                      </div>

                      <thead class="text-cyan-900">
                        <!-- SP版にした際に、表示する場合、明細件数と同じ数のヘッダーが必要 -->
                        <tr
                          class="bg-gray-100 flex flex-col flex-no wrap sm:table-row rounded-l-lg sm:rounded-none mb-2 sm:mb-0">
                          <th class="p-3 text-left text-xs">業種</th>
                          <th class="p-3 text-left text-xs">期間</th>
                          <th class="p-3 text-left text-xs">業務概要</th>
                          <th class="p-3 text-left text-xs">言語</th>
                          <th class="p-3 text-left text-xs">DB/Tool</th>
                          <th class="p-3 text-left text-xs">動作環境</th>
                          <th class="p-3 text-left text-xs">作業工程</th>
                          <th class="p-3 text-left text-xs">役割</th>
                          <th class="p-3 text-left text-xs">Actions</th>
                        </tr>
                        <tr
                          class="bg-gray-100 flex flex-col flex-no wrap sm:table-row rounded-l-lg sm:rounded-none mb-2 sm:mb-0">
                          <th class="p-3 text-left text-xs">業種</th>
                          <th class="p-3 text-left text-xs">期間</th>
                          <th class="p-3 text-left text-xs">業務概要</th>
                          <th class="p-3 text-left text-xs">言語</th>
                          <th class="p-3 text-left text-xs">DB/Tool</th>
                          <th class="p-3 text-left text-xs">動作環境</th>
                          <th class="p-3 text-left text-xs">作業工程</th>
                          <th class="p-3 text-left text-xs">役割</th>
                          <th class="p-3 text-left text-xs">Actions</th>
                        </tr>
                      </thead>
                      <tbody class="flex-1 sm:flex-none">
                        <tr class="flex flex-col flex-no wrap sm:table-row mb-2 sm:mb-0">
                          <td class="border-grey-light border hover:bg-gray-100 p-3 text-xs">John Covv</td>
                          <td class="border-grey-light border hover:bg-gray-100 p-3 text-xs">あああああああ</td>
                          <td class="border-grey-light border hover:bg-gray-100 p-3 text-xs">あああああああ</td>
                          <td class="border-grey-light border hover:bg-gray-100 p-3 text-xs">あああああああ</td>
                          <td class="border-grey-light border hover:bg-gray-100 p-3 text-xs">あああああああ</td>
                          <td class="border-grey-light border hover:bg-gray-100 p-3 text-xs">あああああああ</td>
                          <td class="border-grey-light border hover:bg-gray-100 p-3 text-xs">あああああああ</td>
                          <td class="border-grey-light border hover:bg-gray-100 p-3 text-xs">あああああああ</td>
                          <td
                            class="border-grey-light border hover:bg-gray-100 p-3 text-red-400 hover:text-red-600 hover:font-medium cursor-pointer text-xs">
                            Del</td>
                        </tr>
                        <tr class="flex flex-col flex-no wrap sm:table-row mb-2 sm:mb-0">
                          <td class="border-grey-light border hover:bg-gray-100 p-3 text-xs">John Covv</td>
                          <td class="border-grey-light border hover:bg-gray-100 p-3 text-xs">あああああああ</td>
                          <td class="border-grey-light border hover:bg-gray-100 p-3 text-xs">あああああああ</td>
                          <td class="border-grey-light border hover:bg-gray-100 p-3 text-xs">あああああああ</td>
                          <td class="border-grey-light border hover:bg-gray-100 p-3 text-xs">あああああああ</td>
                          <td class="border-grey-light border hover:bg-gray-100 p-3 text-xs">あああああああ</td>
                          <td class="border-grey-light border hover:bg-gray-100 p-3 text-xs">あああああああ</td>
                          <td class="border-grey-light border hover:bg-gray-100 p-3 text-xs">あああああああ</td>
                          <td
                            class="border-grey-light border hover:bg-gray-100 p-3 text-red-400 hover:text-red-600 hover:font-medium cursor-pointer text-xs">
                            Del</td>
                        </tr>

                      </tbody>
                    </table>
                  </div>

                </div>
              </div>

            </div>
          </div>
        </div>
      </div>
    </div>
  </div>





</template>

<style>
html,
body {
  height: 100%;
}

@media (min-width: 640px) {
  table {
    display: inline-table !important;
  }

  thead tr:not(:first-child) {
    display: none;
  }
}

td:not(:last-child) {
  border-bottom: 0;
}

th:not(:last-child) {
  border-bottom: 2px solid rgba(0, 0, 0, .1);
}
</style>