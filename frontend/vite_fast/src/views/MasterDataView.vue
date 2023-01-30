<script setup lang="ts">
import MasterData from '../components/MasterData.vue'
import { ref } from 'vue';

const languageList = ref([
  {
    name: "Java"
  },
  {
    name: "C#"
  },
  {
    name: "Python"
  },
  {
    name: "Javascript"
  },
  {
    name: "aaa"
  },
  {
    name: "bbb"
  },
  {
    name: "ccc"
  },
])
const toolList = ref([
  {
    name: "Docker"
  },
  {
    name: "AWS CLI"
  },
  {
    name: "VS Code"
  },
])
const infraList = ref([
  {
    name: "Windows"
  },
  {
    name: "Linux"
  },
  {
    name: "AWS ECS"
  },
])

</script>

<template>
  <div class="bg-gradient-to-br from-sky-100 to-gray-200">
    <div class="flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
      <div class="relative container m-auto px-0 text-gray-500 md:px-0 xl:px-12">
        <div class="m-auto">

          <div class="rounded-xl bg-white shadow-xl">

            <div class="p-3 sm:p-8">

              <div class="">
                <h2 class="text-2xl text-cyan-900 font-bold">経験技術の登録</h2>
                <p class="text-sm font-normal text-gray-500 dark:text-gray-400">
                  あなたがこれまで経験してきた技術を選択して、登録しましょう。
                </p>
              </div>
              <MasterData :list=languageList name="言語" itemBadgeColor="blue" />
              <MasterData :list=toolList name="DB・ツール" itemBadgeColor="rose" />
              <MasterData :list=infraList name="動作環境" itemBadgeColor="lime" />

            </div>
            <input type="submit" value="更新"
              class="m-3 p-3 bg-green-500 text-white w-full rounded hover:bg-green-600">
          </div>

        </div>
      </div>
    </div>
  </div>





</template>