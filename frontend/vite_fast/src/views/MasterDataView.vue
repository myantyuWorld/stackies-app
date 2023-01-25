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
<!-- 
              <div class="rounded-xl bg-white shadow-xl">
                <div class="p-5 sm:p-8">
                  <div class="space-y-4">
                    <h2 class="mb-8 text-lg text-cyan-900 font-bold">言語</h2>
                  </div>
                </div>
              </div>

              <div class="rounded-xl bg-white shadow-xl">
                <div class="p-5 sm:p-8">
                  <div class="space-y-4">
                    <h2 class="mb-8 text-lg text-cyan-900 font-bold">言語</h2>
                  </div>
                </div>
              </div>

              <div class="rounded-xl bg-white shadow-xl my-4">
                <div class="p-5 sm:p-8">
                  <div class="space-y-4">
                    <h2 class="mb-8 text-lg text-cyan-900 font-bold">言語</h2>
                  </div>
                </div>
              </div> -->

              <!-- 言語 -->
              <div class="rounded-xl bg-white shadow-xl p-6 my-6">
                <div class="container mt-8 px-5 py-1 mx-auto my-auto">
  
                  <h2 class="mb-8 text-xl text-cyan-900 font-bold">言語
                    <button
                      class="text-sm ml-6 px-4 py-2 bg-gray-400  text-white rounded-lg  tracking-wider hover:bg-gray-500 outline-none">Add</button>
                  </h2>
  
                  <div class="flex flex-wrap -m-4 text-center">
  
                    <div class="p-1 sm:w-1/3 lg:w-1/4 w-full hover:scale-105 duration-500" v-for="n of 6"
                      :key="n">
                      <div
                        class=" flex items-center  justify-between p-4  rounded-lg bg-white shadow-indigo-50 shadow-md">
  
                        <div
                          class="bg-gradient-to-tr from-blue-500 to-blue-400 w-16 h-16  rounded-full shadow-2xl shadow-blue-400 border-white  border-dashed border-2  flex justify-center items-center ">
                          <div>
                            <h1 class="text-white text-xs">Java</h1>
                          </div>
                        </div>
  
                        <div>
                          <button
                            class="text-xs mt-0 px-3 py-3 bg-black-400 text-white rounded-lg  tracking-wider hover:bg-black-300 outline-none">Del</button>
                        </div>
  
                      </div>
                    </div>
  
                    <!-- <div class="p-4 sm:w-1/2 lg:w-1/3 w-full hover:scale-105 duration-500">
                    <div class=" flex items-center  justify-between p-4  rounded-lg bg-white shadow-indigo-50 shadow-md">
                      <div>
                        <h2 class="text-gray-900 text-lg font-bold">Total Ballance</h2>
                        <h3 class="mt-2 text-xl font-bold text-orange-500 text-left">+ 150.000 ₭</h3>
                        <p class="text-sm font-semibold text-gray-400">Last Transaction</p>
                        <button
                          class="text-sm mt-6 px-4 py-2 bg-orange-400  text-white rounded-lg  tracking-wider hover:bg-orange-500 outline-none">Add
                          to cart</button>
                      </div>
                      <div
                        class="bg-gradient-to-tr from-orange-500 to-orange-400 w-32 h-32  rounded-full shadow-2xl shadow-orange-400 border-white  border-dashed border-2  flex justify-center items-center ">
                        <div>
                          <h1 class="text-white text-2xl">C#</h1>
                        </div>
                      </div>
                    </div>
                  </div> -->
  
  
                  </div>
                </div>
              </div>
              
              <!-- DB/tool -->
              <div class="rounded-xl bg-white shadow-xl p-6 my-6">
                <div class="container mt-8 px-5 py-1 mx-auto my-auto">
  
                  <h2 class="mb-8 text-xl text-cyan-900 font-bold">DB・ツール
                    <button
                      class="text-sm ml-6 px-4 py-2 bg-gray-400  text-white rounded-lg  tracking-wider hover:bg-gray-500 outline-none">Add</button>
                  </h2>
  
                  <div class="flex flex-wrap -m-4 text-center">
  
                    <div class="p-1 sm:w-1/3 lg:w-1/4 w-full hover:scale-105 duration-500" v-for="n of 6"
                      :key="n">
                      <div
                        class=" flex items-center  justify-between p-4  rounded-lg bg-white shadow-indigo-50 shadow-md">
  
                        <div
                          class="bg-gradient-to-tr from-rose-500 to-rose-400 w-16 h-16  rounded-full shadow-2xl shadow-green-400 border-white  border-dashed border-2  flex justify-center items-center ">
                          <div>
                            <h1 class="text-white text-xs">Java</h1>
                          </div>
                        </div>
  
                        <div>
                          <button
                            class="text-xs mt-0 px-3 py-3 bg-black-400 text-white rounded-lg  tracking-wider hover:bg-black-300 outline-none">Del</button>
                        </div>
  
                      </div>
                    </div>
  
                    <!-- <div class="p-4 sm:w-1/2 lg:w-1/3 w-full hover:scale-105 duration-500">
                    <div class=" flex items-center  justify-between p-4  rounded-lg bg-white shadow-indigo-50 shadow-md">
                      <div>
                        <h2 class="text-gray-900 text-lg font-bold">Total Ballance</h2>
                        <h3 class="mt-2 text-xl font-bold text-orange-500 text-left">+ 150.000 ₭</h3>
                        <p class="text-sm font-semibold text-gray-400">Last Transaction</p>
                        <button
                          class="text-sm mt-6 px-4 py-2 bg-orange-400  text-white rounded-lg  tracking-wider hover:bg-orange-500 outline-none">Add
                          to cart</button>
                      </div>
                      <div
                        class="bg-gradient-to-tr from-orange-500 to-orange-400 w-32 h-32  rounded-full shadow-2xl shadow-orange-400 border-white  border-dashed border-2  flex justify-center items-center ">
                        <div>
                          <h1 class="text-white text-2xl">C#</h1>
                        </div>
                      </div>
                    </div>
                  </div> -->
  
  
                  </div>
                </div>
              </div>

              <!-- DB/tool -->
              <div class="rounded-xl bg-white shadow-xl p-6 my-6">
                <div class="container mt-8 px-5 py-1 mx-auto my-auto">
  
                  <h2 class="mb-8 text-xl text-cyan-900 font-bold">動作環境
                    <button
                      class="text-sm ml-6 px-4 py-2 bg-gray-400  text-white rounded-lg  tracking-wider hover:bg-gray-500 outline-none">Add</button>
                  </h2>
  
                  <div class="flex flex-wrap -m-4 text-center">
  
                    <div class="p-1 sm:w-1/3 lg:w-1/4 w-full hover:scale-105 duration-500" v-for="n of 6"
                      :key="n">
                      <div
                        class=" flex items-center  justify-between p-4  rounded-lg bg-white shadow-indigo-50 shadow-md">
  
                        <div
                          class="bg-gradient-to-tr from-lime-500 to-lime-400 w-16 h-16  rounded-full shadow-2xl shadow-green-400 border-white  border-dashed border-2  flex justify-center items-center ">
                          <div>
                            <h1 class="text-white text-xs">Java</h1>
                          </div>
                        </div>
  
                        <div>
                          <button
                            class="text-xs mt-0 px-3 py-3 bg-black-400 text-white rounded-lg  tracking-wider hover:bg-black-300 outline-none">Del</button>
                        </div>
  
                      </div>
                    </div>
  
                    <!-- <div class="p-4 sm:w-1/2 lg:w-1/3 w-full hover:scale-105 duration-500">
                    <div class=" flex items-center  justify-between p-4  rounded-lg bg-white shadow-indigo-50 shadow-md">
                      <div>
                        <h2 class="text-gray-900 text-lg font-bold">Total Ballance</h2>
                        <h3 class="mt-2 text-xl font-bold text-orange-500 text-left">+ 150.000 ₭</h3>
                        <p class="text-sm font-semibold text-gray-400">Last Transaction</p>
                        <button
                          class="text-sm mt-6 px-4 py-2 bg-orange-400  text-white rounded-lg  tracking-wider hover:bg-orange-500 outline-none">Add
                          to cart</button>
                      </div>
                      <div
                        class="bg-gradient-to-tr from-orange-500 to-orange-400 w-32 h-32  rounded-full shadow-2xl shadow-orange-400 border-white  border-dashed border-2  flex justify-center items-center ">
                        <div>
                          <h1 class="text-white text-2xl">C#</h1>
                        </div>
                      </div>
                    </div>
                  </div> -->
  
  
                  </div>
                </div>
              </div>
            </div>

          </div>

        </div>
      </div>
      <!-- component -->
    </div>
  </div>





</template>