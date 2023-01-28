<template>
  <div class="w-full px-4 shadow-none flex flex-wrap ">
    <!-- イニシャル、住所、資格（名前、取得時期）、学歴、生年月日、自己PR） -->
    <div class="p-1 w-1/12">
      <div>
        <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="grid-password">
          イニシャル
        </label>
        <input type="text"
          class="block w-full p-2 border rounded border-gray-300 focus:outline-none focus:ring-1 focus:ring-gray-400 focus:border-transparent disabled:bg-slate-50 disabled:text-slate-500 disabled:border-slate-200 disabled:shadow-none"
          placeholder="" disabled value="Y O">
      </div>

    </div>
    <div class="p-1 w-2/12">

      <div>
        <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="grid-password">
          生年月日
        </label>
        <input type="date"
          class="block w-full p-2 border rounded border-gray-300 focus:outline-none focus:ring-1 focus:ring-gray-400 focus:border-transparent disabled:bg-slate-50 disabled:text-slate-500 disabled:border-slate-200 disabled:shadow-none"
          placeholder="生年月日" disabled>
      </div>

    </div>
    <div class="p-1 w-4/12">

      <div>
        <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="grid-password">
          最終学歴
        </label>
        <input type="text"
          class="block w-full p-2 border rounded border-gray-300 focus:outline-none focus:ring-1 focus:ring-gray-400 focus:border-transparent disabled:bg-slate-50 disabled:text-slate-500 disabled:border-slate-200 disabled:shadow-none"
          placeholder="最終学歴" disabled>
      </div>

    </div>
    <div class="p-1 w-5/12">
      <div>
        <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="grid-password">
          資格
        </label>
        <input type="text"
          class="block w-full p-2 border rounded border-gray-300 focus:outline-none focus:ring-1 focus:ring-gray-400 focus:border-transparent disabled:bg-slate-50 disabled:text-slate-500 disabled:border-slate-200 disabled:shadow-none"
          placeholder="資格" disabled>
      </div>

    </div>
    <div class="p-1 w-3/12">
      <div>
        <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="grid-password">
          郵便番号
        </label>
        <input type="text"
          class="block w-full p-2 border rounded border-gray-300 focus:outline-none focus:ring-1 focus:ring-gray-400 focus:border-transparent disabled:bg-slate-50 disabled:text-slate-500 disabled:border-slate-200 disabled:shadow-none"
          placeholder="住所" disabled>
      </div>

    </div>
    <div class="p-1 w-9/12">

      <div>
        <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="grid-password">
          住所
        </label>
        <input type="text"
          class="block w-full p-2 border rounded border-gray-300 focus:outline-none focus:ring-1 focus:ring-gray-400 focus:border-transparent disabled:bg-slate-50 disabled:text-slate-500 disabled:border-slate-200 disabled:shadow-none"
          placeholder="住所" disabled>
      </div>

    </div>


    <div class="p-1 w-full">

      <div>
        <label class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2" for="grid-password">
          自己PR
        </label>
        <textarea type="text"
          class="block w-full p-2 border rounded border-gray-300 focus:outline-none focus:ring-1 focus:ring-gray-400 focus:border-transparent disabled:bg-slate-50 disabled:text-slate-500 disabled:border-slate-200 disabled:shadow-none"
          placeholder="Email" disabled></textarea>
      </div>

    </div>

  </div>
</template>