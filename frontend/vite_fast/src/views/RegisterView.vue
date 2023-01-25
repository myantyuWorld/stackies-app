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
                    <div class="mt-5">

                      <div>
                        <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
                          for="grid-password">
                          E-mail
                        </label>
                        <input type="text"
                          class="block w-full p-2 border rounded border-gray-300 focus:outline-none focus:ring-1 focus:ring-gray-400 focus:border-transparent "
                          placeholder="Email">
                      </div>
                      
                    </div>
                    <div class="mt-5">

                      <div>
                        <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
                          for="grid-password">
                          E-mail
                        </label>
                        <input type="text"
                          class="block w-full p-2 border rounded border-gray-300 focus:outline-none focus:ring-1 focus:ring-gray-400 focus:border-transparent "
                          placeholder="Email">
                      </div>

                    </div>
                    <div class="mt-5">

                      <div>
                        <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2"
                          for="grid-password">
                          E-mail
                        </label>
                        <input type="text"
                          class="block w-full p-2 border rounded border-gray-300 focus:outline-none focus:ring-1 focus:ring-gray-400 focus:border-transparent "
                          placeholder="Email">
                      </div>

                    </div>

                    <div class="mt-10">
                      <input type="submit" value="Sign up with email"
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