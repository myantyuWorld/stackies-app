<script setup lang="ts">
import MasterData from '../components/MasterData.vue'
import MasterDataItem from '../components/MasterDataItem.vue'
import Rating from '../components/Rating.vue'
import ExperienceRating from '../components/ExperienceRating.vue'

import { onMounted } from 'vue'
import { initModals } from 'flowbite'

// initialize components based on data attribute selectors
onMounted(() => {
  initModals();
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
                          class="block w-full p-2 border rounded border-gray-300 focus:outline-none focus:ring-1 focus:ring-gray-400 focus:border-transparent "
                          placeholder="イニシャル">
                      </div>

                    </div>
                    <div class="mt-5 w-full">

                      <div>
                        <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
                          for="grid-password">
                          生年月日
                        </label>
                        <input type="date"
                          class="block w-full p-2 border rounded border-gray-300 focus:outline-none focus:ring-1 focus:ring-gray-400 focus:border-transparent "
                          placeholder="生年月日">
                      </div>

                    </div>
                    <div class="mt-5">

                      <div>
                        <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
                          for="grid-password">
                          最終学歴
                        </label>
                        <input type="text"
                          class="block w-full p-2 border rounded border-gray-300 focus:outline-none focus:ring-1 focus:ring-gray-400 focus:border-transparent "
                          placeholder="最終学歴">
                      </div>

                    </div>
                    <div class="mt-5">

                      <div>
                        <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
                          for="grid-password">
                          住所
                        </label>
                        <input type="text"
                          class="block w-full p-2 border rounded border-gray-300 focus:outline-none focus:ring-1 focus:ring-gray-400 focus:border-transparent "
                          placeholder="住所">
                      </div>

                    </div>
                    <div class="mt-5">

                      <div>
                        <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
                          for="grid-password">
                          資格
                        </label>
                        <input type="text"
                          class="block w-full p-2 border rounded border-gray-300 focus:outline-none focus:ring-1 focus:ring-gray-400 focus:border-transparent "
                          placeholder="資格">
                      </div>

                    </div>

                    <div class="mt-5">

                      <div>
                        <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
                          for="grid-password">
                          自己PR
                        </label>
                        <textarea type="text"
                          class="block w-full p-2 border rounded border-gray-300 focus:outline-none focus:ring-1 focus:ring-gray-400 focus:border-transparent "
                          placeholder="Email"></textarea>
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
                  <button data-modal-toggle="defaultModal" data-modal-target="defaultModal"
                    class="text-sm ml-6 px-4 py-2 bg-gray-400  text-white rounded-lg  tracking-wider hover:bg-gray-500 outline-none">ToggleModal</button>
                </h2>

                <!--  -->
                <!--  -->
                <!-- Modal -->
                <!--  -->
                <!--  -->

                <!-- Main modal -->
                <div id="defaultModal" tabindex="-1" aria-hidden="true"
                  class="fixed top-0 left-0 right-0 z-50 hidden w-full p-4 overflow-x-hidden overflow-y-auto md:inset-0 h-modal md:h-full">
                  <div class="relative w-full h-full max-w-2xl md:h-auto">
                    <!-- Modal content -->
                    <div class="relative bg-white rounded-lg shadow-xl dark:bg-gray-700">
                      <!-- Modal header -->
                      <div class="flex items-start justify-between p-4 border-b rounded-t dark:border-gray-600">
                        <h3 class="text-xl font-semibold text-gray-900 dark:text-white">
                          経験技術
                        </h3>
                        <button type="button"
                          class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center dark:hover:bg-gray-600 dark:hover:text-white"
                          data-modal-hide="defaultModal">
                          <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"
                            xmlns="http://www.w3.org/2000/svg">
                            <path fill-rule="evenodd"
                              d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z"
                              clip-rule="evenodd"></path>
                          </svg>
                          <span class="sr-only">Close modal</span>
                        </button>
                      </div>
                      <!-- Modal body -->
                      <div class="p-6 space-y-6">
                        <ExperienceRating/>
                        <ExperienceRating/>
                        <ExperienceRating/>
                        <ExperienceRating/>
                        <ExperienceRating/>
                        <ExperienceRating/>
                      </div>
                      <!-- Modal footer -->
                      <div
                        class="flex items-center p-6 space-x-2 border-t border-gray-200 rounded-b dark:border-gray-600">
                        <button data-modal-hide="defaultModal" type="button"
                          class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">追加</button>
                        <button data-modal-hide="defaultModal" type="button"
                          class="text-gray-500 bg-white hover:bg-gray-100 focus:ring-4 focus:outline-none focus:ring-blue-300 rounded-lg border border-gray-200 text-sm font-medium px-5 py-2.5 hover:text-gray-900 focus:z-10 dark:bg-gray-700 dark:text-gray-300 dark:border-gray-500 dark:hover:text-white dark:hover:bg-gray-600 dark:focus:ring-gray-600">閉じる</button>
                      </div>
                    </div>
                  </div>
                </div>
                <!--  -->
                <!--  -->
                <!-- Modal -->
                <!--  -->
                <!--  -->


              </div>

              <div class="flex bg-white">
                <div class="w-full px-4 shadow-none">
                  <!-- イニシャル、住所、資格（名前、取得時期）、学歴、生年月日、自己PR） -->
                  <form action="#" class="p-0">

                    <div class="mt-5">
                      <!-- tabs -->
                      <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
                        for="grid-password">
                        経験
                      </label>

                      <ExperienceRating/>
                      <ExperienceRating/>
                      <ExperienceRating/>
                    </div>

                    <div class="mt-10">
                      <input type="submit" value="基本情報登録"
                        class="py-3 bg-green-500 text-white w-full rounded hover:bg-green-600">
                    </div>
                  </form>

                </div>
              </div>

            </div>
          </div>
        </div>
      </div>
    </div>
  </div>





</template>