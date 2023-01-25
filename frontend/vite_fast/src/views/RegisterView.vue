<script setup lang="ts">
import MasterData from '../components/MasterData.vue'
</script>

<template>
  <div class="py-8 bg-gradient-to-br from-sky-100 to-gray-200">
    <div class="flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
      <div class="relative container m-auto px-0 text-gray-500 md:px-0 xl:px-12">
        <div class="m-auto">
          <div class="rounded-xl bg-white shadow-xl">
            <div class="p-6 sm:p-16">

              <div class="space-y-4">
                <h2 class="mb-8 text-2xl text-cyan-900 font-bold">基本情報登録</h2>
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
            <div class="p-6 sm:p-16">

              <div class="space-y-0">
                <h2 class="mb-8 text-2xl text-cyan-900 font-bold">経験技術</h2>
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
                      <div class="grid w-full grid-cols-4 space-x-2 rounded-xl bg-gray-200 p-2" x-data="app">
                        <div>
                          <input type="radio" name="option" id="1" class="peer hidden" checked />
                          <label for="1"
                            class="block cursor-pointer select-none rounded-xl p-2 text-center peer-checked:bg-blue-500 peer-checked:font-bold peer-checked:text-white">1</label>
                        </div>

                        <div>
                          <input type="radio" name="option" id="2" class="peer hidden" />
                          <label for="2"
                            class="block cursor-pointer select-none rounded-xl p-2 text-center peer-checked:bg-blue-500 peer-checked:font-bold peer-checked:text-white">2</label>
                        </div>

                        <div>
                          <input type="radio" name="option" id="3" class="peer hidden" />
                          <label for="3"
                            class="block cursor-pointer select-none rounded-xl p-2 text-center peer-checked:bg-blue-500 peer-checked:font-bold peer-checked:text-white">3</label>
                        </div>

                        <div>
                          <input type="radio" name="option" id="4" class="peer hidden" />
                          <label for="4"
                            class="block cursor-pointer select-none rounded-xl p-2 text-center peer-checked:bg-blue-500 peer-checked:font-bold peer-checked:text-white">4</label>
                        </div>
                      </div>
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