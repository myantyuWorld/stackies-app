<script setup lang="ts">
import { ref } from 'vue';
import router from '@/router';
import MasterData from '../components/MasterData.vue'
const click_regist = () => {
  console.log(languageList.value)
  console.log(toolList.value)
  console.log(infraList.value)
  // router.push('menu')
}

const languageList = ref([
  {
    name: "Java",
    value:"1",
    checked : false
  },
  {
    name: "C#",
    value:"2",
    checked : false
  },
  {
    name: "Python",
    value:"3",
    checked : false
  },
  {
    name: "Javascript",
    value:"4",
    checked : false
  },
  {
    name: "aaa",
    value:"5",
    checked : false
  },
  {
    name: "bbb",
    value:"6",
    checked : false
  },
  {
    name: "ccc",
    value:"7",
    checked : false
  },
])
const toolList = ref([
  {
    name: "Docker",
    value:"1",
    checked : false
  },
  {
    name: "AWS CLI",
    value:"2",
    checked : false
  },
  {
    name: "VS Code",
    value:"3",
    checked : false
  },
])
const infraList = ref([
  {
    name: "Windows",
    value:"1",
    checked : false
  },
  {
    name: "Linux",
    value:"2",
    checked : false
  },
  {
    name: "AWS ECS",
    value:"3",
    checked : false
  },
])

// TODO : Vue.js: 子コンポーネントのチェックボックスを双方向にデータバインディングする | https://qiita.com/FumioNonaka/items/709360072e9f645447f8
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
              <button @click="click_regist" class="m-3 p-3 bg-green-500 text-white w-full rounded hover:bg-green-600">更新</button>
          </div>

        </div>
      </div>
    </div>
  </div>





</template>