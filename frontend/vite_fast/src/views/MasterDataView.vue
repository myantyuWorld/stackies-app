<script setup lang="ts">
import MasterData from '../components/MasterData.vue'
</script>

<template>
  <div class="relative py-8 bg-gradient-to-br from-sky-100 to-gray-200">
    <div class="flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
      <div class="relative container m-auto px-0 text-gray-500 md:px-0 xl:px-12">
        <div class="m-auto">

          <div class="rounded-xl bg-white shadow-xl">

            <div class="p-6 sm:p-16">
              <div class="space-y-4">
                <h2 class="mb-8 text-2xl text-cyan-900 font-bold">マスタ管理</h2>
              </div>
              <MasterData name="言語" itemBadgeColor="blue"/>
              <MasterData name="DB・ツール" itemBadgeColor="rose"/>
              <MasterData name="動作環境" itemBadgeColor="lime"/>
            </div>

          </div>

        </div>
      </div>
      <!-- component -->
    </div>
  </div>





</template>