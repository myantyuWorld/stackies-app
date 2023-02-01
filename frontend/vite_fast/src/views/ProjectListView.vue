<script setup lang="ts">
import { onMounted } from 'vue'
import { initDropdowns, } from 'flowbite'

import ProjectListTable from '../components/ProjectListTable.vue'
import BaseInfo from '../components/BaseInfo.vue'
import ExperienceRating from '../components/ExperienceRating.vue'

// initialize components based on data attribute selectors
onMounted(() => {
  initDropdowns();
})

const baseinfo = {
  initial: "あああ",
  birth_date:"1990-08-20",
  last_educational_background:"ほげほげ専門学校",
  qualification:"応用情報技術者, AWS CLF",
  postcode:"7310102",
  address:"広島県広島市hogehogeのほげ",
  self_pr:"あああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああああ"
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
                <!-- TODO : 入力モード、表示モードをpropで切り替えられるようにする -->
                <BaseInfo :inputMode="true" :initial="baseinfo.initial" :birth_date="baseinfo.birth_date" :last_educational_background="baseinfo.last_educational_background" :qualification="baseinfo.qualification" :postcode="baseinfo.postcode" :address="baseinfo.address" :self_pr="baseinfo.self_pr"/>
              </div>
            </div>
            <div class="p-3 sm:p-3">
              <!-- tabs -->
              <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="grid-password">
                経験
              </label>

              <ExperienceRating :experienceRate="4" itemName="Java" />
              <ExperienceRating :experienceRate="2" itemName="Docker" />
              <ExperienceRating :experienceRate="4" itemName="JavaScript" />
            </div>
            <div class="p-3 sm:p-3">

              <div class="space-y-0">
                <h2 class="mb-0 text-2xl text-cyan-900 font-bold">
                  業務履歴
                </h2>
              </div>
              <div class="flex bg-white">
                <div class="w-full px-4 shadow-none">
                  <ProjectListTable />
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