<script setup lang="ts">
import { ref } from 'vue';
import { onMounted } from 'vue'
import { initDropdowns, } from 'flowbite'

import ProjectListTable from '../components/ProjectListTable.vue'
import BaseInfo from '../components/BaseInfo.vue'
import ExperienceRating from '../components/ExperienceRating.vue'

// initialize components based on data attribute selectors
onMounted(() => {
  initDropdowns();
})

const data = {
  baseinfo: {
    initial: "あああ",
    birth_date: "1990-08-20",
    last_educational_background: "ほげほげ専門学校",
    qualification: "応用情報技術者, AWS CLF",
    postcode: "7310102",
    address: "広島県広島市hogehogeのほげ",
    self_pr: "あああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああ"
  },
  experienceRateInfo: [
    {
      id: "1",
      name: "Java",
      level: "3",
    },
    {
      id: "2",
      name: "C#",
      level: "3",
    },
    {
      id: "3",
      name: "javascript",
      level: "3",
    }
  ],
  businessHistories: [
    {
      industries: "建設",
      systemName: "AAA管理システム",
      period: "2021/01/01(22021/03/30)",
      businessOverview: "AAAの管理システムを作成、BBBというパッケージソフトとデータ連携を行い、hogehogeしたもの",
      language: [
        "Java", "JQuery",
      ],
      tools: [
        "Copilot", "Fargate", "ECS", "Django",
      ],
      infra: [
        "Docker",
      ],
      workProcess: {
        rd: false,
        bd: true,
        dd: true,
        cd: true,
        ut: true,
        it: true,
        op: false,
      },
      role: "member"
    },
    {
      industries: "情報通信",
      systemName: "遠隔監視支援システム",
      period: "2021/01/01(22021/03/30)",
      businessOverview: "AIの解析結果を、フロント（Vue.js）に表示したもの、Vuetifyを使用",
      language: [
        "Vue.js", "Python", "graphql"
      ],
      tools: [
        "Nuxt.js", "Flask",
      ],
      infra: [
        "Linux",
      ],
      workProcess: {
        rd: false,
        bd: true,
        dd: true,
        cd: true,
        ut: true,
        it: true,
        op: false,
      },
      role: "member"
    }
  ]

}
</script>

<template>
  <div class="py-8 bg-gradient-to-br from-sky-100 to-gray-200">
    <div class="flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
      <div class="relative container m-auto px-0 text-gray-500 md:px-0 xl:px-12">
        <div class="m-auto">
          <div class="rounded-xl bg-white shadow-xl">
            <div class="p-3 sm:p-3">
              <div class="space-y-4">
                <h2 class="mb-0 text-2xl text-cyan-900 font-bold">案件対応履歴</h2>
              </div>
              <div class="flex bg-white">
                <BaseInfo :inputMode="true" :base-info="data.baseinfo" />
              </div>
            </div>
            <div class="p-3 sm:p-3">
              <!-- tabs -->
              <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="grid-password">
                経験
              </label>
              <div v-for="item in data.experienceRateInfo" :key="item.id">
                <ExperienceRating :is-show="false" :rate="item" v-model="item.level" />
              </div>
            </div>
            <div class="p-3 sm:p-3">

              <div class="space-y-0">
                <div class="flex">
                  <h2 class="mb-0 text-2xl text-cyan-900 font-bold">
                    業務履歴
                  </h2>
                  <button type="button" class="ml-3 text-white bg-gradient-to-r from-purple-500 via-purple-600 to-purple-700 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-purple-300 dark:focus:ring-purple-800 shadow-lg shadow-purple-500/50 dark:shadow-lg dark:shadow-purple-800/80 font-medium rounded-lg text-sm px-5 py-2.5 text-center mr-2 mb-2">追加</button>
                </div>
              </div>
              <div class="flex bg-white">
                <div class="w-full px-4 shadow-none">
                  <ProjectListTable :business-histories="data.businessHistories" />
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

  /* thead tr:not(:first-child) {
    display: none;
  } */
}

td:not(:last-child) {
  border-bottom: 0;
}

/* th:not(:last-child) {
  border: 1px solid rgba(0, 0, 0, .1);
} */
th {
  border: 1px solid rgba(0, 0, 0, .1);
}
</style>